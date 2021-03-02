#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Utility.h"

#include "TFile.h"
#include "TChain.h"
#include "TObjArray.h"

NTupleReaderIterator::NTupleReaderIterator(NTupleReader& tr, int begin) : tr_(tr), current_(begin)
{
    //read first event
    if(!tr_.goToEvent(current_))
    {
        current_ = -1;
    }
}

NTupleReaderIterator& NTupleReaderIterator::operator++()
{
    if(tr_.goToEvent(current_ + 1))
    {
        ++current_;
    }
    else
    {
        current_ = -1;
    }
    return *this;
}

const NTupleReaderIterator& NTupleReaderIterator::operator++() const
{
    if(tr_.goToEvent(current_ + 1))
    {
        ++current_;
    }
    else
    {
        current_ = -1;
    }
    return *this;
}

bool NTupleReaderIterator::operator!=(const NTupleReaderIterator& itr) const 
{
    return current_ != itr.current_;
}

bool NTupleReaderIterator::operator==(const NTupleReaderIterator& itr) const 
{
    return !operator!=(itr);
}


NTupleReader& NTupleReaderIterator::operator*()
{
    return tr_;
}

//specialization for bool return value
template<>
class NTupleReader::FuncWrapperImpl<std::function<bool(NTupleReader&)>> : public FuncWrapper
{
private:
    std::function<bool(NTupleReader&)> func_;
    
public:
    bool operator()(NTupleReader& tr)
    {
        return func_(tr);
    }

    FuncWrapperImpl(std::function<bool(NTupleReader&)> f) : func_(f) {}
};

NTupleReader::NTupleReader(TTree * tree, const std::set<std::string>& activeBranches) : activeBranches_(activeBranches)
{
    tree_ = tree;
    if(!tree_) THROW_SATEXCEPTION("NTupleReader(...): TTree " + std::string(tree_->GetName()) + " is invalid!!!!");
    init();
}

NTupleReader::NTupleReader(TTree * tree)
{
    tree_ = tree;
    init();
}

NTupleReader::NTupleReader(NTupleReader&& tr) : tree_(tr.tree_), nevt_(tr.nevt_), evtProcessed_(tr.evtProcessed_), chainCurrentTree_(tr.chainCurrentTree_), isUpdateDisabled_(tr.isUpdateDisabled_), reThrow_(tr.reThrow_), convertHackActive_(tr.convertHackActive_), branchMap_(std::move(tr.branchMap_)), branchVecMap_(std::move(tr.branchVecMap_)), functionVec_(std::move(tr.functionVec_)), typeMap_(std::move(tr.typeMap_)), activeBranches_(std::move(tr.activeBranches_))
{    
}

NTupleReader::NTupleReader()
{
    tree_ = nullptr;
    init();
}

NTupleReader::~NTupleReader()
{
    //Clean up any remaining dynamic memory
    for(auto& branch : branchMap_)    if(branch.second.ptr) branch.second.destroy();
    for(auto& branch : branchVecMap_) if(branch.second.ptr) branch.second.destroy();
    for(auto& funcWrapPtr : functionVec_) if(funcWrapPtr) delete funcWrapPtr;
}

void NTupleReader::init()
{
    nevt_ = evtProcessed_ = 0;
    isUpdateDisabled_ = false;
    reThrow_ = true;
    convertHackActive_ = false;
    chainCurrentTree_ = -999;

    if(tree_)
    {
        if(tree_->InheritsFrom(TChain::Class())) 
        {
            chainCurrentTree_ = reinterpret_cast<TChain*>(tree_)->GetTreeNumber();
        }

        tree_->SetBranchStatus("*", 0);

        // Add desired branches to branchMap_/branchVecMap_
        populateBranchList();
    }
}

void NTupleReader::setTree(TTree * tree)
{
    if(!tree_)
    {
        tree_ = tree;
        tree_->SetBranchStatus("*", 0);
        
        // Add desired branches to branchMap_/branchVecMap_
        populateBranchList();
    }
    else
    {
        THROW_SATEXCEPTION("Tree already loaded into NTupleReader: you can only load one tree!!!"); 
    }
}

std::string NTupleReader::getFileName() const
{
    return std::string( tree_->GetCurrentFile()->GetName() );
}

int NTupleReader::getNEntries() const
{
    try
    {
        if(tree_) return tree_->GetEntries();
        else 
        {
            THROW_SATEXCEPTION("NO tree defined yet!!!");
        }
    }
    catch(const SATException& e)
    {
        e.print();
        if(reThrow_) throw;
        return -1;
    }
}

void NTupleReader::populateBranchList()
{
    TObjArray *lob = tree_->GetListOfBranches();
    TIter next(lob);
    TBranch *branch;

    while((branch = (TBranch*)next())) 
    {
        std::string name(branch->GetName());

        if(activeBranches_.size() > 0 && activeBranches_.count(name) == 0)
        {
            //allow typeMap_ to track that the branch exists without filling type
            registerBranch(branch, false);
        }
        else
        {
            registerBranch(branch);
        }
    }
}

void NTupleReader::registerBranch(TBranch * const branch, bool activate) const
{
    std::string type;
    std::string name(branch->GetName());
    std::string title;
    std::string firstdim, seconddim;
    int leafLength = -1;
    TLeaf *countLeaf = nullptr;

    TObjArray *lol = branch->GetListOfLeaves();
    int lolSize = lol->GetEntries();
    std::vector<int> dimVec;

    if (lolSize >= 1) 
    {
        TLeaf *leaf = (TLeaf*)lol->UncheckedAt(0);
        type = leaf->GetTypeName();
        leafLength = leaf->GetLen();
        title = leaf->GetTitle();
        //count leaf is set if the branch holds a variable length array
        countLeaf = leaf->GetLeafCount();
        firstdim  = utility::split("last",utility::split("first", title, "]"),"[");
        seconddim = utility::split("first", utility::split("last", title, "]["),"]");
        if(firstdim == title) firstdim = "";
        if(seconddim != title && seconddim.find(name) != std::string::npos) seconddim = "";
        if(firstdim  != "") dimVec.emplace_back(std::atoi(firstdim.c_str()));
        if(seconddim != "") dimVec.emplace_back(std::atoi(seconddim.c_str()));
    }
    else
    {
        THROW_SATEXCEPTION("Branch \"" + name + "\" has no leaves and therefore no data!!!\?\?\?!!!");
    }

    //Check if this is an array or singleton (vectors count as singleton)
    if(leafLength == 1 && !countLeaf)
    {
        if(type.find("vector<vector") != std::string::npos)
        {
            if     (type.find("double")         != std::string::npos) registerVecBranch<std::vector<double>>(name, activate);
            else if(type.find("unsigned int")   != std::string::npos) registerVecBranch<std::vector<unsigned int>>(name, activate);
            else if(type.find("unsigned long")  != std::string::npos) registerVecBranch<std::vector<unsigned long>>(name, activate);
            else if(type.find("unsigned char")  != std::string::npos) registerVecBranch<std::vector<unsigned char>>(name, activate);
            else if(type.find("unsigned short") != std::string::npos) registerVecBranch<std::vector<unsigned short>>(name, activate);
            else if(type.find("short")          != std::string::npos) registerVecBranch<std::vector<short>>(name, activate);
            else if(type.find("char")           != std::string::npos) registerVecBranch<std::vector<char>>(name, activate);
            else if(type.find("int")            != std::string::npos) registerVecBranch<std::vector<int>>(name, activate);
            else if(type.find("bool")           != std::string::npos) registerVecBranch<std::vector<bool>>(name, activate);
            else if(type.find("string")         != std::string::npos) registerVecBranch<std::vector<std::string>>(name, activate);
            else if(type.find("TLorentzVector") != std::string::npos) registerVecBranch<std::vector<TLorentzVector>>(name, activate);
            else if(type.find("float")          != std::string::npos) registerVecBranch<std::vector<float>>(name, activate);
            else THROW_SATEXCEPTION("No type match for branch \"" + name + "\" with type \"" + type + "\"!!!");
        }
        else if(type.find("vector") != std::string::npos)
        {
            if     (type.find("double")         != std::string::npos) registerVecBranch<double>(name, activate);
            else if(type.find("unsigned int")   != std::string::npos) registerVecBranch<unsigned int>(name, activate);
            else if(type.find("unsigned long")  != std::string::npos) registerVecBranch<unsigned long>(name, activate);
            else if(type.find("unsigned char")  != std::string::npos) registerVecBranch<unsigned char>(name, activate);
            else if(type.find("unsigned short") != std::string::npos) registerVecBranch<unsigned short>(name, activate);
            else if(type.find("short")          != std::string::npos) registerVecBranch<short>(name, activate);
            else if(type.find("char")           != std::string::npos) registerVecBranch<char>(name, activate);
            else if(type.find("int")            != std::string::npos) registerVecBranch<int>(name, activate);
            else if(type.find("bool")           != std::string::npos) registerVecBranch<bool>(name, activate);
            else if(type.find("string")         != std::string::npos) registerVecBranch<std::string>(name, activate);
            else if(type.find("TLorentzVector") != std::string::npos) registerVecBranch<TLorentzVector>(name, activate);
            else if(type.find("float")          != std::string::npos) registerVecBranch<float>(name, activate);
            else if(type.find("UInt_t")    != std::string::npos) registerVecBranch<UInt_t>(name, activate);
            else if(type.find("ULong64_t") != std::string::npos) registerVecBranch<ULong64_t>(name, activate);
            else if(type.find("UChar_t")   != std::string::npos) registerVecBranch<char>(name, activate);
            else if(type.find("Float_t")   != std::string::npos) registerVecBranch<float>(name, activate);
            else if(type.find("Double_t")  != std::string::npos) registerVecBranch<double>(name, activate);
            else if(type.find("Int_t")     != std::string::npos) registerVecBranch<int>(name, activate);
            else if(type.find("Bool_t")    != std::string::npos) registerVecBranch<bool>(name, activate);
            else THROW_SATEXCEPTION("No type match for branch \"" + name + "\" with type \"" + type + "\"!!!");
        }
        else
        {
            if     (type.find("UInt_t")    != std::string::npos) registerBranch<UInt_t>(name, activate);
            else if(type.find("ULong64_t") != std::string::npos) registerBranch<ULong64_t>(name, activate);
            else if(type.find("UChar_t")   != std::string::npos) registerBranch<UChar_t>(name, activate);
            else if(type.find("Float_t")   != std::string::npos) registerBranch<float>(name, activate);
            else if(type.find("Double_t")  != std::string::npos) registerBranch<double>(name, activate);
            else if(type.find("Int_t")     != std::string::npos) registerBranch<int>(name, activate);
            else if(type.find("Long64_t")  != std::string::npos) registerBranch<Long64_t>(name, activate);
            else if(type.find("Bool_t")    != std::string::npos) registerBranch<bool>(name, activate);
            else if(type.find("/D") != std::string::npos) registerBranch<double>(name, activate);
            else if(type.find("/I") != std::string::npos) registerBranch<int>(name, activate);
            else if(type.find("/i") != std::string::npos) registerBranch<unsigned int>(name, activate);
            else if(type.find("/F") != std::string::npos) registerBranch<float>(name, activate);
            else if(type.find("/C") != std::string::npos) registerBranch<char>(name, activate);
            else if(type.find("/c") != std::string::npos) registerBranch<unsigned char>(name, activate);
            else if(type.find("/S") != std::string::npos) registerBranch<short>(name, activate);
            else if(type.find("/s") != std::string::npos) registerBranch<unsigned short>(name, activate);
            else if(type.find("/O") != std::string::npos) registerBranch<bool>(name, activate);
            else if(type.find("/L") != std::string::npos) registerBranch<unsigned long>(name, activate);
            else if(type.find("/l") != std::string::npos) registerBranch<long>(name, activate);
            else if(type.find("/b") != std::string::npos) registerBranch<bool>(name, activate);
            else THROW_SATEXCEPTION("No type match for branch \"" + name + "\" with type \"" + type + "\"!!!");
        }
    }
    else if(countLeaf || leafLength > 1) //if this ptr is non-null then this is a variable length arra
    {
        if     (type.find("double")         != std::string::npos) registerArrayBranch<double>(name, branch, activate, leafLength, dimVec);
        else if(type.find("unsigned int")   != std::string::npos) registerArrayBranch<unsigned int>(name, branch, activate, leafLength, dimVec);
        else if(type.find("unsigned long")  != std::string::npos) registerArrayBranch<unsigned long>(name, branch, activate, leafLength, dimVec);
        else if(type.find("unsigned char")  != std::string::npos) registerArrayBranch<unsigned char>(name, branch, activate, leafLength, dimVec);
        else if(type.find("unsigned short") != std::string::npos) registerArrayBranch<unsigned short>(name, branch, activate, leafLength, dimVec);
        else if(type.find("short")          != std::string::npos) registerArrayBranch<short>(name, branch, activate, leafLength, dimVec);
        else if(type.find("char")           != std::string::npos) registerArrayBranch<char>(name, branch, activate, leafLength, dimVec);
        else if(type.find("int")            != std::string::npos) registerArrayBranch<int>(name, branch, activate, leafLength, dimVec);
        else if(type.find("bool")           != std::string::npos) registerArrayBranch<uint8_t>(name, branch, activate, leafLength, dimVec);
        else if(type.find("string")         != std::string::npos) registerArrayBranch<std::string>(name, branch, activate, leafLength, dimVec);
        else if(type.find("TLorentzVector") != std::string::npos) registerArrayBranch<TLorentzVector>(name, branch, activate, leafLength, dimVec);
        else if(type.find("float")          != std::string::npos) registerArrayBranch<float>(name, branch, activate, leafLength, dimVec);
        else if(type.find("UInt_t")         != std::string::npos) registerArrayBranch<UInt_t>(name, branch, activate, leafLength, dimVec);
        else if(type.find("ULong64_t")      != std::string::npos) registerArrayBranch<ULong64_t>(name, branch, activate, leafLength, dimVec);
        else if(type.find("UChar_t")        != std::string::npos) registerArrayBranch<UChar_t>(name, branch, activate, leafLength, dimVec);
        else if(type.find("Float_t")        != std::string::npos) registerArrayBranch<float>(name, branch, activate, leafLength, dimVec);
        else if(type.find("Double_t")       != std::string::npos) registerArrayBranch<double>(name, branch, activate, leafLength, dimVec);
        else if(type.find("Int_t")          != std::string::npos) registerArrayBranch<int>(name, branch, activate, leafLength, dimVec);
        else if(type.find("Bool_t")         != std::string::npos) registerArrayBranch<uint8_t>(name, branch, activate, leafLength, dimVec);
        else THROW_SATEXCEPTION("No type match for branch \"" + name + "\" with type \"" + type + "\"!!!");
    }
    else
    {
        THROW_SATEXCEPTION("Branch \"" + name + "\" with type \"" + type + "\" has no data!!!");
    }
}

void NTupleReader::createVectorsForArrayReads(int evt)
{
    bool updateBranches = false;
    int iEvtLocal = evt;
    //if this tree is defined this is a TChain
    if(chainCurrentTree_ >= -1)
    {
        //Load next file in chain if needed and get local event number for file 
        iEvtLocal = tree_->LoadTree(evt);

        //check if we have moved to a new file in the chain
        int treeNum = tree_->GetTreeNumber();
        if(chainCurrentTree_ != treeNum)
        {
            chainCurrentTree_ = treeNum;
            //update branch references 
            updateBranches = true;
        }
    }

    for(auto& handlePair : branchVecMap_)
    {
        //If the size branch is set, this is an array read
        if(handlePair.second.branch)
        {
            if(updateBranches)
            {
                handlePair.second.branchVec = tree_->GetBranch(handlePair.first.c_str());
                TLeaf *l = (TLeaf*)handlePair.second.branchVec->GetListOfLeaves()->At(0); 
                if(l->GetLeafCount())
                { 
                    handlePair.second.branch = l->GetLeafCount()->GetBranch();
                }
                else if(l->GetLen() > 1)
                {
                    handlePair.second.branch = handlePair.second.branchVec;
                    handlePair.second.branchVec = nullptr;
                }
                else
                {
                    THROW_SATEXCEPTION("Branch \"" + handlePair.first + "\" appears to be an array, but there is no size branch");
                }
            }
            //Prep the vector which will hold the data
            handlePair.second.create(*this, iEvtLocal);
        }
    }
}

bool NTupleReader::goToEvent(int evt)
{
    return goToEventInternal(evt, false);
}

bool NTupleReader::goToEventInternal(int evt, const bool filter)
{
    int status = 0;
    bool passFilters = false;
    do
    {
        clearDerivedVectors();
        //Create vectors for array reads 
        createVectorsForArrayReads(evt);
        //Load data from TTree
        status = tree_->GetEntry(evt);
        if (status <= 0) //0 means event not found, -1 means IO error
        {
            nevt_ = -1;
            return false;
        }
        nevt_ = evt + 1;
        ++evtProcessed_;
        //Calculate extra derived variables 
        passFilters = calculateDerivedVariables();
    }
    while(filter && (status > 0 && !passFilters && ++evt));
    return status > 0;
}

bool NTupleReader::getNextEvent()
{
    return goToEventInternal(nevt_, true);
}

void NTupleReader::disableUpdate()
{
    isUpdateDisabled_ = true;
    printf("NTupleReader::disableUpdate(): You have disabled tuple updates.  You may therefore be using old variablre definitions.  Be sure you are ok with this!!!\n");
}

void NTupleReader::clearDerivedVectors()
{
    for(auto& branchPair : branchVecMap_)
    {
        auto& deleterPtr = branchPair.second.deleter;
        if(deleterPtr)
        {
            deleterPtr->deletePtr(branchPair.second.ptr);
        }
    }
}

bool NTupleReader::calculateDerivedVariables()
{
    for(auto& func : functionVec_)
    {
        if(!(*func)(*this))
        {
            return false;
        }
    }

    return true;
}

void NTupleReader::registerFunction(void (*f)(NTupleReader&))
{
    if(isFirstEvent()) functionVec_.emplace_back(new FuncWrapperImpl<std::function<void(NTupleReader&)>>(std::function<void(NTupleReader&)>(f)));
    else THROW_SATEXCEPTION("new functions cannot be registered after tuple reading begins!");
}

void NTupleReader::registerFunction(bool (*f)(NTupleReader&))
{
    if(isFirstEvent()) functionVec_.emplace_back(new FuncWrapperImpl<std::function<bool(NTupleReader&)>>(std::function<bool(NTupleReader&)>(f)));
    else THROW_SATEXCEPTION("new functions cannot be registered after tuple reading begins!");
}

void NTupleReader::getType(const std::string& name, std::string& type) const
{
    auto typeIter = typeMap_.find(name);
    if(typeIter != typeMap_.end())
    {
        type = typeIter->second;
    }
}

void NTupleReader::setReThrow(const bool reThrow)
{
    reThrow_ = reThrow;
}

bool NTupleReader::getReThrow() const
{
    return reThrow_;
}

void NTupleReader::addAlias(const std::string& name, const std::string& alias)
{
    //Check that alias i not already used
    if(typeMap_.find(alias) == typeMap_.end())
    {
        //set type for alias
        typeMap_[alias] = typeMap_[name];

        auto branch_iter = branchMap_.find(name);
        auto branchVec_iter = branchVecMap_.find(name);
        
        //Check if this variable is already registered and register it if not 
        if(branch_iter == branchMap_.end() && branchVec_iter == branchVecMap_.end())
        {
            //If found in typeMap_, it can be added on the fly
            TBranch *branch = tree_->FindBranch(name.c_str());
        
            //If branch not found continue on to throw exception
            if(branch != nullptr)
            {
                registerBranch(branch);
        
                //force read just this branch if necessary
                if(evtProcessed_ >= 1) branch->GetEvent(nevt_ - 1);
            }
        }

        branch_iter = branchMap_.find(name);
        branchVec_iter = branchVecMap_.find(name);

        //Set the "fake" handle for the alias 
        //Check branchMap for "name"
        if(branch_iter != branchMap_.end())
        {
            branchMap_[alias] = Handle(branch_iter->second.ptr, nullptr, branch_iter->second.type);
        }
        //If the variable name is not in branchMap, check branchVecMap
        else if(branchVec_iter != branchVecMap_.end())
        {
            branchVecMap_[alias] = Handle(branchVec_iter->second.ptr, nullptr, branchVec_iter->second.type);
        }
    }
    else
    {
        THROW_SATEXCEPTION("Variable name \"" + alias + "\" already exists!!!");
    }
}

void* NTupleReader::getVarPtr(const std::string& var) const
{
    //This function can be used to return the variable pointer
    try
    {
        auto tuple_iter = branchMap_.find(var);
        if(tuple_iter != branchMap_.end())
        {
            return tuple_iter->second.ptr;
        }
            
        THROW_SATEXCEPTION("NTupleReader::getPtr(...): Variable not found: " + var);
    }
    catch(const SATException& e)
    {
        e.print();
        if(reThrow_) throw;
        return nullptr;
    }
}

template<> const void* NTupleReader::getPtr<void>(const std::string& var) const
{
    return getVarPtr(var);
}

template<> const void* NTupleReader::getVecPtr<void>(const std::string& var) const
{
    //This function can be used to return the variable pointer
    try
    {
        auto tuple_iter = branchVecMap_.find(var);
        if(tuple_iter != branchVecMap_.end())
        {
            return tuple_iter->second.ptr;
        }

        THROW_SATEXCEPTION("NTupleReader::getVecPtr(...): Variable not found: " + var);
    }
    catch(const SATException& e)
    {
        e.print();
        if(reThrow_) throw;
        return nullptr;
    }
}

void NTupleReader::printTupleMembers(FILE *f) const
{
    for(auto& iVar : typeMap_)
    {
        fprintf(f, "%60s %s\n", iVar.second.c_str(), iVar.first.c_str());
    }
}

void NTupleReader::printUsedTupleVar(FILE *f) const
{
    for(auto& iVar : branchMap_)
    {
        if(iVar.second.activeFromNTuple) fprintf(f, "%60s %s\n", typeMap_[iVar.first].c_str(), iVar.first.c_str());
    }
    for(auto& iVar : branchVecMap_)
    {
        if(iVar.second.activeFromNTuple) fprintf(f, "%60s %s\n", typeMap_[iVar.first].c_str(), iVar.first.c_str());
    }
}

std::vector<std::string> NTupleReader::getTupleMembers() const
{
    std::vector<std::string> members;
    for(auto& iVar : typeMap_)
    {
        members.push_back(iVar.first);
    }
    return members;
}

std::vector<std::string> NTupleReader::getTupleSpecs(const std::string& varName) const
{
    std::vector<std::string> members = getTupleMembers();
    std::vector<std::string> specs;
    for(auto &member : members)
    {
        std::string::size_type t= member.find(varName);
        if (t != std::string::npos)
        {
            specs.push_back(member.erase(t, varName.length()));
        }
    }
  
    return specs;
}

void NTupleReader::setConvertFloatingPointVectors(const bool doubleToFloat, const bool floatToDouble)
{
    if(doubleToFloat) 
    {
        convertHackActive_ = true;
        for(const auto& i : branchVecMap_)
        {
            if (i.second.type == typeid(std::vector<double>))
            {
                registerFunction(std::bind(&NTupleReader::castVector<double, float>, std::placeholders::_1, i.first, 'f'));
            }
        }
    }

    if(floatToDouble) 
    {
        convertHackActive_ = true;
        for(const auto& i : branchVecMap_)
        {
            if (i.second.type == typeid(std::vector<float>))
            {
                registerFunction(std::bind(&NTupleReader::castVector<float, double>, std::placeholders::_1, i.first, 'd'));
            }
        }
    }
}



// ===  FUNCTION  ============================================================
//         Name:  NTupleReader::CastVector
//  Description:  /* cursor */
// ===========================================================================
template <class Tfrom, class Tto>
void NTupleReader::castVector(NTupleReader& tr, const std::string& var, const char typen)
{
    const std::vector<Tfrom> &obj = tr.getVec<Tfrom>(var);

    std::vector<Tto> *objs = new std::vector<Tto>();
    objs->reserve(obj.size());

    std::string newname = var+"___" + typen;

    for(auto& i : obj)
    {
        objs->push_back(static_cast<Tto>(i));
    }

    tr.registerDerivedVec(newname, objs);
}       // -----  end of function NTupleReader::CastVector  -----

