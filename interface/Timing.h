#ifndef TIMING_H
#define TIMING_H

#include "TestbeamReco/interface/Utility.h"

class Timing
{
private:
    void timing([[maybe_unused]] NTupleReader& tr)
    {
        //const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");

        //-------------------------------------------------------
        //Code from https://github.com/cmorgoth/AC_LGAD_Timing 
        //-------------------------------------------------------
        double sum_amp = 0.0;
        for(unsigned int i = 0; i < ampLGAD.size(); i++)
        {
            for(unsigned int j = 0; j < ampLGAD[i].size(); j++)
            {
                const auto& amp = ampLGAD[i][j];
                const auto& time = timeLGAD[i][j];
                if(time != 0.0)
                {
                    sum_amp += amp;
                }
            }
        }
        
        //looping over all ac-strips
        double weighted_time=0.0, total_weight=0.0;
        int rowIndex = 0;
        for(const auto& row : ampLGAD)
        {
            for(unsigned int i = 0; i < row.size(); i++)
            {
                const auto& amp = ampLGAD[rowIndex][i];
                const auto& time = timeLGAD[rowIndex][i];
                if(time != 0.0)
                {
                    auto amp_frac = amp/sum_amp;
                    weighted_time += amp_frac*time;
                    total_weight += amp_frac;
                }                    
            }
        }
        tr.registerDerivedVar("weighted_time", weighted_time);

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
