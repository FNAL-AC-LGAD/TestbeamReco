#include "TestbeamReco/interface/MiniTupleMaker.h"

#include "TLorentzVector.h"
#include <iostream>

MiniTupleMaker::MiniTupleMaker(TTree * const t) : file_(nullptr), tree_(t)
{
}

MiniTupleMaker::MiniTupleMaker(std::string fname, std::string treeName) : file_(new TFile(fname.c_str(), "RECREATE")), tree_(new TTree(treeName.c_str(), (fname + treeName).c_str()))
{
}

MiniTupleMaker::~MiniTupleMaker()
{
    if(file_)
    {
        file_->cd();
        tree_->Write();
        file_->Close();
    }
}

void MiniTupleMaker::setTupleVars(const std::set<std::string> tv)
{
    for(auto& var : tv) tupleVars_.insert(var);
}

void MiniTupleMaker::initBranches(const NTupleReader& tr)
{
    for(auto& var : tupleVars_)
    {
        std::string type;
        tr.getType(var, type);

        if(type.find("vector") != std::string::npos)
        {
            if(type.find("*") != std::string::npos)
            {
                throw "MiniTupleMaker::initBranches(...): Vectors of pointers are not allowed in MiniTuples!!!";
            }
            else
            {
                //Anyone reading this please forgive me, but root made me do it
                if     (type.find("TLorentzVector") != std::string::npos) prepVec<TLorentzVector>(tr, var);
                else if(type.find("double")         != std::string::npos) prepVec<double>(tr, var);
                else if(type.find("float")          != std::string::npos) prepVec<float>(tr, var);
                else if(type.find("int")            != std::string::npos) prepVec<int>(tr, var);
                else
                {
                    throw "MiniTupleMaker::initBranches(...): Variable type unknown!!! var: " + var + ", type: " + type;           
                }
            }
        }
        else
        {
            if     (type.find("unsigned int")   != std::string::npos) prepVar<unsigned int>(tr, var);
            else if(type.find("int")            != std::string::npos) prepVar<int>(tr, var);
            else if(type.find("double")         != std::string::npos) prepVar<double>(tr, var);
            else if(type.find("float")          != std::string::npos) prepVar<float>(tr, var);
            else if(type.find("unsigned short") != std::string::npos) prepVar<unsigned short>(tr, var);
            else if(type.find("short")          != std::string::npos) prepVar<short>(tr, var);
            else if(type.find("unsigned char")  != std::string::npos) prepVar<unsigned char>(tr, var);
            else if(type.find("string")         != std::string::npos) prepVar<std::string>(tr, var);
            else if(type.find("char")           != std::string::npos) prepVar<char>(tr, var);
            else if(type.find("bool")           != std::string::npos) prepVar<bool>(tr, var);
            else if(type.find("unsigned long")  != std::string::npos) prepVar<unsigned long>(tr, var);
            else if(type.find("long")           != std::string::npos) prepVar<long>(tr, var);
            else if(type.find("TLorentzVector") != std::string::npos) prepVar<TLorentzVector>(tr, var);
            else
            {
                throw "MiniTupleMaker::initBranches(...): Variable type unknown!!! var: " + var + ", type: " + type;
            }
        }
    }
}

void MiniTupleMaker::fill()
{
    tree_->Fill();
}
