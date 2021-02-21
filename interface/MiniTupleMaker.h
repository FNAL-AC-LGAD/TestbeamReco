#ifndef MinTupleMaker_h
#define MinTupleMaker_h

#include "TestbeamReco/interface/NTupleReader.h"

#include "TTree.h"
#include "TFile.h"

#include <vector>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <functional>

#include <iostream>

class MiniTupleMaker
{
public:
    MiniTupleMaker(TTree *);

    MiniTupleMaker(std::string, std::string = "tree");

    ~MiniTupleMaker();

    void setTupleVars(const std::set<std::string>);

    //To use derived variables initBranches must be called after the first tuple event is read
    void initBranches(const NTupleReader&);

    void fill();

private:
    TFile* const file_;
    TTree* const tree_;
    std::set<std::string> tupleVars_;

    template<typename T> void prepVar(const NTupleReader& tr, const std::string& name)
    {
        TBranch *tb = tree_->GetBranch(name.c_str());
        if(!tb) tree_->Branch(name.c_str(), static_cast<T*>(const_cast<void*>(tr.getPtr<T>(name))));
        else       tb->SetAddress(const_cast<void*>(tr.getPtr<T>(name)));
    }

    template<typename T> void prepVec(const NTupleReader& tr, const std::string& name)
    {
        TBranch *tb = tree_->GetBranch(name.c_str());
        if(!tb) tree_->Branch(name.c_str(), static_cast<std::vector<T>**>(const_cast<void*>(tr.getVecPtr<T>(name))));
        else       tb->SetAddress(const_cast<void*>(tr.getVecPtr<T>(name)));
    }
};

#endif
