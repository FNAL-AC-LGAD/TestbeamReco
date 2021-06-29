#ifndef TIMING_H
#define TIMING_H

#include "TestbeamReco/interface/Utility.h"

class Timing
{
private:
    template<typename T> inline T getValue(bool cut, T value) const
    {
        return (cut) ? value : 0.0;
    }

    void timing([[maybe_unused]] NTupleReader& tr)
    {
        //const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");

        //-------------------------------------------------------
        //Code from https://github.com/cmorgoth/AC_LGAD_Timing 
        //-------------------------------------------------------
        double sum_amp=0.0, sum_amp_goodSig=0.0, sum_amp2=0.0, sum_amp2_goodSig=0.0;
        double weighted_time=0.0, weighted_time_goodSig=0.0, weighted2_time=0.0, weighted2_time_goodSig=0.0;
        for(unsigned int i = 0; i < ampLGAD.size(); i++)
        {
            for(unsigned int j = 0; j < ampLGAD[i].size(); j++)
            {
                const auto& amp = ampLGAD[i][j];
                const auto& time = timeLGAD[i][j];
                sum_amp       += getValue(time!=0.0, amp);
                weighted_time += getValue(time!=0.0, amp*time);

                sum_amp_goodSig       += getValue(time!=0.0 && amp > signalAmpThreshold, amp);
                weighted_time_goodSig += getValue(time!=0.0 && amp > signalAmpThreshold, amp*time);
                
                sum_amp2       += getValue(time!=0.0, amp*amp);
                weighted2_time += getValue(time!=0.0, amp*amp*time);

                sum_amp2_goodSig       += getValue(time!=0.0 && amp > signalAmpThreshold, amp*amp);
                weighted2_time_goodSig += getValue(time!=0.0 && amp > signalAmpThreshold, amp*amp*time);
            }
        }
        tr.registerDerivedVar("weighted_time", weighted_time/sum_amp);
        tr.registerDerivedVar("weighted_time_goodSig", weighted_time_goodSig/sum_amp_goodSig);
        tr.registerDerivedVar("weighted2_time", weighted2_time/sum_amp2);
        tr.registerDerivedVar("weighted2_time_goodSig", weighted2_time_goodSig/sum_amp2_goodSig);
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
