#ifndef NTUPLE_READER_H
#define NTUPLE_READER_H

#include "TestbeamReco/interface/SATException.h"

#include "TLorentzVector.h"
#include "TBranch.h"
#include "TLeaf.h"
#include "TTree.h"

#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <set>
#include <typeinfo>
#include <typeindex>
#include <functional>
#include <cxxabi.h>
#include <iostream>

#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

#pragma link C++ class vector<TLorentzVector>+;
#endif


/* This class is designed to be a simple interface to reading stop NTuples
   
   To use this class simply open the desired Tree as a TTree or TChain and pass it 
   to the constructor.  Then the tuple contents may be accessed as follows

   NTupleReader tr(tree);
   while(tr.getNextEvent())
   {
       const int& run = tr.getVar<unsigned int>("run");
   }

   and so on.  
 */

class NTupleReader;

//"Iterator" to allow use with for loops
class NTupleReaderIterator
{
    friend NTupleReader;

private:
    NTupleReader& tr_;
    mutable int current_;
    NTupleReaderIterator(NTupleReader& tr, int begin);

public:        
    NTupleReaderIterator& operator++();

    const NTupleReaderIterator& operator++() const ;

    bool operator==(const NTupleReaderIterator& itr) const;
    bool operator!=(const NTupleReaderIterator& itr) const;

    NTupleReader& operator*();
};

void baselineUpdate(NTupleReader& tr);

class NTupleReader
{
    friend void baselineUpdate(NTupleReader& tr);

    friend NTupleReaderIterator;

private:

    //Machinery to allow object cleanup
    //Generic deleter base class to obfiscate template type
    class deleter_base
    {
    public:
        virtual void create(void *, TBranch*, TBranch*, const NTupleReader&, int, int = -1,  const std::vector<int>& = {}) {}
        virtual void deletePtr(void *) {}
        virtual void destroy(void *) = 0;
        virtual ~deleter_base() {}
    };

    //Templated class to create/store simple object deleter 
    template<typename T> 
    class deleter : public deleter_base
    {
    public:
        void destroy(void *ptr)
        {
            delete static_cast<T*>(ptr);
        }
    };

    //Templated class to create/store vector object deleter 
    template<typename T> 
    class vec_deleter : public deleter_base
    {
    public:
        virtual void deletePtr(void *ptr)
        {
            //Delete vector
            T& vecptr = *static_cast<T*>(ptr);
            if(vecptr != nullptr) delete vecptr;
            vecptr = nullptr;
        }

        virtual void destroy(void *ptr)
        {
            //Delete vector
            T vecptr = *static_cast<T*>(ptr);
            if(vecptr != nullptr) delete vecptr;            

            //delete pointer to vector
            delete static_cast<T*>(ptr);
        }
    };

    //Templated class to create/store vector object deleter for arrays
    template<typename T, typename N>
    class array_deleter : public vec_deleter<T>
    {
    public:
        void deletePtr(void*) {}

        void create(void * ptr, TBranch* branch, TBranch* branchVec, const NTupleReader& tr, int evt, int,  const std::vector<int>&)
        {
            //Get the array length
            if(branch->GetReadEntry() != evt) branch->GetEntry(evt);
            const N& ArrayLen = tr.getVar<N>(std::string(branch->GetName()));
          
            //Delete vector if one already exists
            T* vecptr = static_cast<T*>(ptr);
            if(*vecptr != nullptr) delete *vecptr;

            //with vector cleaned up, create new vector
            //this typedef seems manditory to unconfuse the compilier 
            typedef typename std::remove_pointer<T>::type vec_type;
            *vecptr = new vec_type(ArrayLen);
            branchVec->SetAddress( (*vecptr)->data() );
        }
    };

    //Templated class to create/store vector object deleter for arrays
    template<typename T>
    class fixedlen_array_deleter : public vec_deleter<T>
    {
    public:
        void deletePtr(void*) {}

        void create(void * ptr, TBranch* branch, TBranch*, const NTupleReader&, int, int len, const std::vector<int>&)
        {
            //Delete vector if one already exists
            T* vecptr = static_cast<T*>(ptr);
            if(*vecptr != nullptr) delete *vecptr;

            //with vector cleaned up, create new vector
            //this typedef seems manditory to unconfuse the compilier 
            typedef typename std::remove_pointer<T>::type vec_type;
            *vecptr = new vec_type(len);
            branch->SetAddress( (*vecptr)->data() );
        }
    };

    //Handle class to hold pointer and deleter
    class Handle
    {
    public:
        void* ptr;
        mutable deleter_base* deleter;
        std::type_index type;
        mutable TBranch *branch;
        mutable TBranch *branchVec;
        mutable bool activeFromNTuple;
        mutable int len;

        Handle() : ptr(nullptr), deleter(nullptr), type(typeid(nullptr)), branch(nullptr), branchVec(nullptr), activeFromNTuple(false), len(-1) {}

        Handle(const Handle& h) : ptr(h.ptr), deleter(h.deleter), type(h.type), branch(h.branch), branchVec(h.branchVec), activeFromNTuple(h.activeFromNTuple), len(h.len) {}

        Handle(void* ptr, deleter_base* deleter = nullptr, const std::type_index& type = typeid(nullptr), TBranch* branch = nullptr, TBranch* branchVec = nullptr, const bool activeFromNTuple = false, int len = -1) :  ptr(ptr), deleter(deleter), type(type), branch(branch), branchVec(branchVec), activeFromNTuple(activeFromNTuple), len(len) {}

        void create(const NTupleReader& tr, int evt) const
        {
            if(deleter)
            {
                deleter->create(ptr, branch, branchVec, tr, evt, len);
            }
        }

        void destroy()
        {
            if(deleter)
            {
                deleter->destroy(ptr);
                delete deleter;
            }
        }
    };

    //Helper to make simple Handle
    template<typename T>
    static inline Handle createHandle(T* ptr, const bool activeFromNTuple = false)
    {
        return Handle(ptr, new deleter<T>, typeid(typename std::remove_pointer<T>::type), nullptr, nullptr, activeFromNTuple);
    }

    //Helper to make vector Handle
    template<typename T>
    static inline Handle createVecHandle(T* ptr, const bool activeFromNTuple = false)
    {
        return Handle(ptr, new vec_deleter<T>, typeid(typename std::remove_pointer<T>::type), nullptr, nullptr, activeFromNTuple);
    }

    //Helper to make array Handle
    template<typename T>
    static inline Handle createArrayHandle(T* ptr, TBranch* branch, TBranch* branchVec, const bool activeFromNTuple = false)
    {
        std::string type;
        TObjArray *lol = branch->GetListOfLeaves();
        int lolSize = lol->GetEntries();
        
        if (lolSize >= 1) 
        {
            TLeaf *leaf = (TLeaf*)lol->UncheckedAt(0);
            type = leaf->GetTypeName();
        }

        if(type.compare("int") == 0 || type.compare("Int_t") == 0)
        {
            return Handle(ptr, new array_deleter<T, int>, typeid(typename std::remove_pointer<T>::type), branch, branchVec, activeFromNTuple);
        }
        else if(type.compare("unsigned int") == 0 || type.compare("UInt_t") == 0)
        {
            return Handle(ptr, new array_deleter<T, unsigned int>, typeid(typename std::remove_pointer<T>::type), branch, branchVec, activeFromNTuple);
        }
        else
        {
            THROW_SATEXCEPTION("ERROR: Unknown array length type: " + type);
        }
    }
    
    //Helper to make fixed length array Handle
    template<typename T>
    static inline Handle createFixedlenArrayHandle(T* ptr, TBranch* branch, const bool activeFromNTuple = false, int len = -1)
    {
        return Handle(ptr, new fixedlen_array_deleter<T>, typeid(typename std::remove_pointer<T>::type), branch, nullptr, activeFromNTuple, len);
    }

    //function wrapper 
    //base class
    class FuncWrapper
    {
    public:
        virtual bool operator()(NTupleReader& tr) = 0;

        virtual ~FuncWrapper() {}
    };

    //class for arbitrary return value
    template<typename T>
    class FuncWrapperImpl : public FuncWrapper
    {
    private:
        T func_;
    public:
        bool operator()(NTupleReader& tr)
        {
            func_(tr);
            return true;
        }

        inline T& getFunc()
        { 
            return func_; 
        }

        FuncWrapperImpl(T& f) : func_(std::move(f)) {}
        FuncWrapperImpl(T&& f) : func_(std::move(f)) {}
        template <typename ...Args> FuncWrapperImpl(Args&&... args) : func_(args...) {}
    };

    template <class Tfrom, class Tto> 
    static void castVector(NTupleReader& tr, const std::string& var, const char typen);

public:

    NTupleReader(TTree * tree, const std::set<std::string>& activeBranches_);
    NTupleReader(TTree * tree);
    NTupleReader();
    NTupleReader(NTupleReader&& tr);
    ~NTupleReader();

    NTupleReader(NTupleReader&) = delete;

    std::string getFileName() const;

    int getEvtNum() const
    {
        return nevt_;
    }

    inline bool isFirstEvent() const
    {
        return evtProcessed_ <= 1;
    }

    int getNEntries() const;

    NTupleReaderIterator begin()
    {
        return NTupleReaderIterator(*this, 0);
    }

    NTupleReaderIterator end()
    {
        return NTupleReaderIterator(*this, -1);
    }

    inline bool checkBranch(const std::string& name) const
    {
        return (typeMap_.find(name) != typeMap_.end());
    }

    inline bool checkBranchInTree(const std::string& name) const
    {
        TBranch* br = static_cast<TBranch*>(tree_->FindBranch(name.c_str()));
        return (br != nullptr);
    }

    inline bool hasVar(const std::string& name) const {return checkBranch(name); }

    bool goToEvent(int evt);
    bool getNextEvent();
    void disableUpdate();
    void printTupleMembers(FILE *f = stdout) const;
    void printUsedTupleVar(FILE *f = stdout) const;

    void setConvertFloatingPointVectors(const bool doubleToFloat = true, const bool floatToDouble = false);

    std::vector<std::string> getTupleMembers() const;
    std::vector<std::string> getTupleSpecs(const std::string& varName) const;

    template<typename T> void registerFunction(T& f)
    {
        if(isFirstEvent()) functionVec_.emplace_back(new FuncWrapperImpl<T>(f));
        else THROW_SATEXCEPTION("New functions cannot be registered after tuple reading begins!\n");
    }

    template<typename T> void registerFunction(T&& f)
    {
        if(isFirstEvent()) functionVec_.emplace_back(new FuncWrapperImpl<T>(f));
        else THROW_SATEXCEPTION("New functions cannot be registered after tuple reading begins!\n");
    }

    template<typename T, typename ...Args> T& emplaceModule(Args&&... args)
    {
        if(isFirstEvent()) functionVec_.emplace_back(new FuncWrapperImpl<T>(args...));
        else THROW_SATEXCEPTION("New module cannot be registered after tuple reading begins!\n");        
        return static_cast<FuncWrapperImpl<T>*>(functionVec_.back())->getFunc();
    }

    //Specialization for basic functions
    void registerFunction(void (*f)(NTupleReader&));
    void registerFunction(bool (*f)(NTupleReader&));

    void getType(const std::string& name, std::string& type) const;

    void setReThrow(const bool);
    bool getReThrow() const;

    template<typename T> void registerDerivedVar(const std::string& name, T var) const
    {
        try
        {
            auto handleItr = branchMap_.find(name);
            if(handleItr == branchMap_.end())
            {
                auto typeItr = typeMap_.find(name);
                if(typeItr != typeMap_.end())
                {
                    THROW_SATEXCEPTION("You are trying to redefine a tuple var: \"" + name + "\".  This is not allowed!  Please choose a unique name.");
                }
                handleItr = branchMap_.insert(std::make_pair(name, createHandle(new T()))).first;

                typeMap_[name] = demangle<T>();
            }
            setDerived(var, handleItr->second.ptr);
        }
        catch(const SATException& e)
        {
            e.print();
            if(reThrow_) throw;
        }
    }

    template<typename T> void registerDerivedVec(const std::string& name, T* var) const
    {
        try
        {
            auto handleItr = branchVecMap_.find(name);
            if(handleItr == branchVecMap_.end())
            {
                auto typeItr = typeMap_.find(name);
                if(typeItr != typeMap_.end())
                {
                    THROW_SATEXCEPTION("You are trying to redefine a tuple var: \"" + name + "\".  This is not allowed!  Please choose a unique name.");
                }
                handleItr = branchVecMap_.insert(std::make_pair(name, createVecHandle(new T*()))).first;
            
                typeMap_[name] = demangle<T>();
            }
            T *vecptr = *static_cast<T**>(handleItr->second.ptr);
            if(vecptr != nullptr)
            {
                delete vecptr;
            }
            setDerived(var, handleItr->second.ptr);
        }
        catch(const SATException& e)
        {
            e.print();
            if(reThrow_) throw;
        }
    }

    template<typename T, typename ...Args> T& createDerivedVar(const std::string& name, Args&&... args) const 
    {
        T varTemp(args...);
        registerDerivedVar(name, varTemp);
        auto* var = static_cast<T*>(getVarPtr(name));
        return (*var);
    }

    template<typename T, typename ...Args> std::vector<T>& createDerivedVec(const std::string& name, Args&&... args) const 
    {
        std::vector<T>* vec = new std::vector<T>(args...);
        registerDerivedVec(name, vec);
        return (*vec);
    }

    void addAlias(const std::string& name, const std::string& alias);

    template<typename T = void> const void* getPtr(const std::string& var) const
    {
        try
        {
            return &getTupleObj<T>(var, branchMap_);
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return static_cast<T*>(nullptr);
        }
    }

    template<typename T = void> const void* getVecPtr(const std::string& var) const
    {
        try
        {
            return &getTupleObj<std::vector<T>*>(var, branchVecMap_);
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return static_cast<std::vector<T>*>(nullptr);
        }
    }

    template<typename T> const T& getVar(const std::string& var) const
    {
        //This function can be used to return single variables
        try
        {
            return getTupleObj<T>(var, branchMap_);
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return *static_cast<T*>(nullptr);
        }
    }

    template<typename T> const std::vector<T>& getVec(const std::string& var) const
    {
        //This function can be used to return vectors
        try
        {            
            return *getTupleObj<std::vector<T>*>(var, branchVecMap_);                
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return *static_cast<std::vector<T>*>(nullptr);
        }
    }

    template<typename T> const std::vector<std::vector<T>>& getVecVec(const std::string& var) const
    {
        //This function can be used to return vectors
        try
        {            
            const auto& dimIter = branchDimMap_.find(var);
            if( dimIter == branchDimMap_.end() )
            {
                return *getTupleObj<std::vector<std::vector<T>>*>(var, branchVecMap_);                
            }
            else 
            {
                std::string dimName = "_array";
                auto& dimVec = dimIter->second;
                for(const auto d : dimVec) dimName += "_" + std::to_string(d);
                std::string name = var+dimName;

                //check if name has already been created
                auto iter = branchVecMap_.find(name);
                if(iter != branchVecMap_.end() && *(static_cast<void**>(iter->second.ptr)) != nullptr)
                {
                    return getVec<std::vector<T>>(name);
                }

                const auto& vec1D = *getTupleObj<std::vector<T>*>(var, branchVecMap_);
                auto& vec2D = createDerivedVec<std::vector<T>>(name);
                for(int i = 0; i < dimVec[0]; i++)
                {
                    vec2D.emplace_back(vec1D.begin()+dimVec[1]*i, vec1D.begin()+dimVec[1]*(i+1));
                }
                return vec2D;
            }
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return *static_cast<std::vector<std::vector<T>>*>(nullptr);
        }
    }

    template<typename T> const std::vector<TLorentzVector>& getVec_LVFromPtEtaPhiM(const std::string& ptVar, const std::string& etaVar, const std::string& phiVar, const std::string& massVar) const
    {
        //This function can be used to return vectors of TLorentzVectors if pt,eta,phi,mass are stored in independent vectors 
        try
        {
            //compose (hopefully) unique name for the TLV in the map
            std::string tlvName = "TLorentzVector_" + ptVar + etaVar + phiVar + massVar;

            //check if tlvName has already been created
            auto iter = branchVecMap_.find(tlvName);
            if(iter != branchVecMap_.end() && *(static_cast<void**>(iter->second.ptr)) != nullptr)
            {
                //vector TLorentzVector has already been calcualted, simply return it 
                return getVec<TLorentzVector>(tlvName);
            }

            //The vector has not been made for this event yet 
            //get components
            auto& pt   = getVec<T>(ptVar);
            auto& eta  = getVec<T>(etaVar);
            auto& phi  = getVec<T>(phiVar);
            auto& mass = getVec<T>(massVar);

            //check vector lengths
            if(pt.size() != eta.size() || pt.size() != phi.size() || pt.size() != mass.size())
            {
                THROW_SATEXCEPTION("TLorentzVector component input vectors have unequal length!!! (" + ptVar + ":" + std::to_string(pt.size()) + " "  + etaVar + ":" + std::to_string(eta.size()) + " "  + phiVar + ":" + std::to_string(phi.size()) + " "  + massVar + ":" + std::to_string(mass.size()) + ")");
            }

            //create vector<TLorentzVector> with number of elements necessary
            auto& tlv = createDerivedVec<TLorentzVector>(tlvName, pt.size());

            for(unsigned int i = 0; i < pt.size(); ++i)
            {
                tlv[i].SetPtEtaPhiM(pt[i], eta[i], phi[i], mass[i]);
            }

            //return resultant vector
            return tlv;
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return *static_cast<std::vector<TLorentzVector>*>(nullptr);
        }
    }

    template<typename T> const std::vector<TLorentzVector>& getVec_LVFromNano(const std::string& Collection) const
    {
        return getVec_LVFromPtEtaPhiM<T>(Collection + "_pt", Collection + "_eta", Collection + "_phi", Collection + "_mass");
    }

    template<typename T, typename V> const std::map<T, V>& getMap(const std::string& var) const
    {
        //This function can be used to return maps

        try
        {
            return *getTupleObj<std::map<T, V>*>(var, branchVecMap_);
        }
        catch(const SATException& e)
        {
            if(isFirstEvent()) e.print();
            if(reThrow_) throw;
            return *static_cast<std::map<T, V>*>(nullptr);
        }
    }
 
 
private:
    // private variables for internal use
    TTree *tree_;
    int nevt_, evtProcessed_, chainCurrentTree_;
    bool isUpdateDisabled_, reThrow_, convertHackActive_;
    
    // stl collections to hold branch list and associated info
    mutable std::unordered_map<std::string, Handle> branchMap_;
    mutable std::unordered_map<std::string, Handle> branchVecMap_;
    mutable std::unordered_map<std::string, std::vector<int>> branchDimMap_;
    std::vector<FuncWrapper*> functionVec_;
    mutable std::unordered_map<std::string, std::string> typeMap_;
    std::set<std::string> activeBranches_;

    void init();

    void setTree(TTree * tree);

    void populateBranchList();
    
    void registerBranch(TBranch * const branch, bool activate = true) const;

    void* getVarPtr(const std::string& var) const;

    void clearDerivedVectors();

    bool calculateDerivedVariables();
    
    void createVectorsForArrayReads(int evt);

    bool goToEventInternal(int evt, const bool filter);

    template<typename T> void registerBranch(const std::string& name, bool activate = true) const
    {
        typeMap_[name] = demangle<T>();

        if(activate)
        {
            branchMap_[name] = createHandle(new T(), true);

            tree_->SetBranchStatus(name.c_str(), 1);
            tree_->SetBranchAddress(name.c_str(), branchMap_[name].ptr);
        }
    }
    
    template<typename T> void registerVecBranch(const std::string& name, bool activate = true) const
    {
        typeMap_[name] = demangle<std::vector<T>>();

        if(activate)
        {
            branchVecMap_[name] = createVecHandle(new std::vector<T>*(), true);

            tree_->SetBranchStatus(name.c_str(), 1);
            tree_->SetBranchAddress(name.c_str(), branchVecMap_[name].ptr);
        }
    }

    template<typename T> void registerArrayBranch(const std::string& name, TBranch * branch, bool activate = true, int len = -1, const std::vector<int>& dimVec = {}) const
    {        
        if(dimVec.size() > 1) branchDimMap_[name] = dimVec;
        typeMap_[name] = demangle<std::vector<T>>();

        if(activate)
        {
            //get the event count branch
            TLeaf *l = (TLeaf*)branch->GetListOfLeaves()->At(0); 
            TBranch* countBranch = nullptr;
            if(l->GetLeafCount())
            { 
                countBranch = l->GetLeafCount()->GetBranch();
                branchVecMap_[name] = createArrayHandle(new std::vector<T>*(), countBranch, branch, true);
            }
            else if(l->GetLen() > 1)
            {
                branchVecMap_[name] = createFixedlenArrayHandle(new std::vector<T>*(), branch, true, len);
            }
            else
            {
                THROW_SATEXCEPTION("Branch \"" + name + "\" appears to be an array, but there is no size branch");
            }
        
            tree_->SetBranchStatus(name.c_str(), 1);
        }
    }

    template<typename T> void updateTupleVar(const std::string& name, const T& var)
    {
        if(isFirstEvent())
        {
            if(branchMap_.find(name) == branchMap_.end())
            {
                branchMap_[name] = createVecHandle(new T());
                
                typeMap_[name] = demangle<T>();
            }
        }

        auto tuple_iter = branchMap_.find(name);
        if(tuple_iter != branchMap_.end())
        {
            *static_cast<T*>(tuple_iter->second.ptr) = var;
        }
        else THROW_SATEXCEPTION("Variable not found: \"" + name + "\"!!!\n");
    }

    template<typename T, typename V> T& getTupleObj(const std::string& var, const V& v_tuple) const
    {
        //Find variable in the main tuple map 
        auto tuple_iter = v_tuple.find(var);
        bool intuple = tuple_iter != v_tuple.end() ;

        //Check that the variable exists and the requested type matches the true variable type
        if(intuple && (tuple_iter->second.type == typeid(typename std::remove_pointer<T>::type)))
        {
            return *static_cast<T*>(tuple_iter->second.ptr);
        }
        else if(convertHackActive_ && intuple) //else check if it is a vector<float> or vector<double>
        {
            //hack to get vector<double> as vector<float>, requires DuplicateFDVector() to be run
            char typen = '\0';
            if( typeid(typename std::remove_pointer<T>::type) == typeid(std::vector<float>) && tuple_iter->second.type == typeid(std::vector<double>))
                typen='f';
            if( typeid(typename std::remove_pointer<T>::type) == typeid(std::vector<double>) && tuple_iter->second.type == typeid(std::vector<float>))
                typen='d';
            std::string newname = var + "___" + typen;
            auto tuple_iter = branchVecMap_.find(newname);
            if (tuple_iter != branchVecMap_.end())
                return *static_cast<T*>(tuple_iter->second.ptr);
        }
        else if( !intuple && (typeMap_.find(var) != typeMap_.end())) //If it is not loaded, but is a branch in tuple
        {
            //If found in typeMap_, it can be added on the fly
            TBranch *branch = tree_->FindBranch(var.c_str());
        
            //If branch not found continue on to throw exception
            if(branch != nullptr)
            {
                registerBranch(branch);
        
                //get iterator
                tuple_iter = v_tuple.find(var);
        
                //if this is an array, force read length
                if (tuple_iter == v_tuple.end()) THROW_SATEXCEPTION("ERROR: The variable "+var+" of type "+typeMap_[var]+" was not registered");

                if(tuple_iter->second.branch)
                {
                    //Prep the vector which will hold the data
                    tuple_iter->second.create(*this, nevt_ - 1);
                }

                //force read just this branch
                branch->GetEvent(nevt_ - 1);
        
                intuple = true;

                //If it is the same type as requested, we can simply return the result
                if(tuple_iter->second.type == typeid(typename std::remove_pointer<T>::type))
                {
                    //return value
                    return *static_cast<T*>(tuple_iter->second.ptr);
                }
            }
        } 

        //It really does not exist, throw exception 
        auto typeIter = typeMap_.find(var);
        if(typeIter != typeMap_.end())
        {
            THROW_SATEXCEPTION("Variable not found: \"" + var + "\" with type \"" + demangle<typename std::remove_pointer<T>::type>() +"\", but is found with type \"" + typeIter->second + "\"!!!");
        }
        else
        {
            THROW_SATEXCEPTION("Variable not found: \"" + var + "\" with type \"" + demangle<typename std::remove_pointer<T>::type>() +"\"!!!");
        }
    }

    template<typename T> inline static void setDerived(const T& retval, void* const loc)
    {
        *static_cast<T*>(loc) = retval;
    }

    template<typename T> std::string demangle() const
    {
        // unmangled
        int status = 0;
        char* demangled = abi::__cxa_demangle(typeid(T).name(), 0, 0, &status);
        std::string s = demangled;
        free(demangled);
        return s;
    }
};

//template specializations
template<> const void* NTupleReader::getPtr<void>(const std::string& var) const;
template<> const void* NTupleReader::getVecPtr<void>(const std::string& var) const;


#endif
