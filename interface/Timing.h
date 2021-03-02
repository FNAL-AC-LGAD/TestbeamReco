#ifndef TIMING_H
#define TIMING_H

#include "TestbeamReco/interface/Utility.h"

class Timing
{
private:
    void timing(NTupleReader& tr)
    {
        // Add code here: will process this function per event
        // Make variables that you want to run in other parts of the code/Fill into histograms

        // Example of getting variables from the TTree
        // const auto& run = tr.getVar<int>("run");
        // const auto& amp = tr.getVec<float>("amp");

        // Example of adding variables on-the-fly
        // double x = 100;
        // tr.registerDerivedVar("keyName", x);
        // auto& x = tr.createDerivedVec<double>("keyName");
        // x = {100, 100};
    }
public:
    Timing()
    {
        std::cout<<"Running Timing Module"<<std::endl;
    }

    void operator()(NTupleReader& tr)
    {
        timing(tr);
    }
};

#endif
