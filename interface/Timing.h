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
        const auto& timeLGADTracker = tr.getVec<std::vector<double>>("timeLGADTracker");
        const auto& timeLGADXY = tr.getVec<std::vector<double>>("timeLGADXY");
        const auto& timeLGADX = tr.getVec<std::vector<double>>("timeLGADX");
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& amp2Indexes = tr.getVar<std::pair<int,int>>("amp2Indexes");
        //auto amp1 = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        auto time1 = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        //auto time2 = timeLGAD[amp2Indexes.first][amp2Indexes.second];
       
        //-------------------------------------------------------
        //Code from https://github.com/cmorgoth/AC_LGAD_Timing 
        //-------------------------------------------------------
        double sum_amp=0.0, sum_amp_goodSig=0.0, sum_amp2=0.0, sum_amp2_goodSig=0.0;
        double weighted_time=0.0, weighted_time_goodSig=0.0, weighted2_time=0.0, weighted2_time_goodSig=0.0;
        double weighted_time_tracker=0.0, weighted2_time_tracker=0.0;
        double average_time_LGADXY=0.0, average_time_LGADX=0.0, weighted_time_LGADXY=0.0, weighted2_time_LGADXY=0.0, weighted_time_LGADX=0.0, weighted2_time_LGADX=0.0;
        for(unsigned int i = 0; i < ampLGAD.size(); i++)
        {
            for(unsigned int j = 0; j < ampLGAD[i].size(); j++)
            {
                const auto& amp = ampLGAD[i][j];
                const auto& time = timeLGAD[i][j];
                const auto& timeTracker = timeLGADTracker[i][j];
                const auto& timeLGADxy = timeLGADXY[i][j];
                const auto& timeLGADx = timeLGADX[i][j];
                auto similarTime = abs(time - time1) < 1.0;

                sum_amp       += getValue(similarTime && time!=0.0, amp);
                weighted_time += getValue(similarTime && time!=0.0, amp*time);
                weighted_time_tracker += getValue(similarTime && time!=0.0, amp*timeTracker);
                weighted_time_LGADXY += getValue(similarTime && time!=0.0, amp*timeLGADxy);            
                weighted_time_LGADX += getValue(similarTime && time!=0.0, amp*timeLGADx);
                
                sum_amp_goodSig       += getValue(similarTime && time!=0.0 && amp > signalAmpThreshold, amp);
                weighted_time_goodSig += getValue(similarTime && time!=0.0 && amp > signalAmpThreshold, amp*time);
                
                sum_amp2       += getValue(similarTime && time!=0.0, amp*amp);
                weighted2_time += getValue(similarTime && time!=0.0, amp*amp*time);
                weighted2_time_tracker += getValue(similarTime && time!=0.0, amp*amp*timeTracker);
                weighted2_time_LGADXY += getValue(similarTime && time!=0.0, amp*amp*timeLGADxy);
                weighted2_time_LGADX += getValue(similarTime && time!=0.0, amp*amp*timeLGADx);

                sum_amp2_goodSig       += getValue(similarTime && time!=0.0 && amp > signalAmpThreshold, amp*amp);
                weighted2_time_goodSig += getValue(similarTime && time!=0.0 && amp > signalAmpThreshold, amp*amp*time);
            }
        }
 
        average_time_LGADXY = (timeLGADXY[amp1Indexes.first][amp1Indexes.second] + timeLGADXY[amp2Indexes.first][amp2Indexes.second])*0.5;
        average_time_LGADX = (timeLGADX[amp1Indexes.first][amp1Indexes.second] + timeLGADX[amp2Indexes.first][amp2Indexes.second])*0.5;
        tr.registerDerivedVar("weighted_time", weighted_time/sum_amp);
        tr.registerDerivedVar("weighted_time_tracker", weighted_time_tracker/sum_amp);
        tr.registerDerivedVar("weighted_time_goodSig", weighted_time_goodSig/sum_amp_goodSig);
        tr.registerDerivedVar("weighted2_time", weighted2_time/sum_amp2);
        tr.registerDerivedVar("weighted2_time_tracker", weighted2_time_tracker/sum_amp2);
        tr.registerDerivedVar("weighted2_time_goodSig", weighted2_time_goodSig/sum_amp2_goodSig);

        tr.registerDerivedVar("average_time_LGADXY", average_time_LGADXY); 
        tr.registerDerivedVar("average_time_LGADX", average_time_LGADX); 
        tr.registerDerivedVar("weighted_time_LGADXY", weighted_time_LGADXY/sum_amp);
        tr.registerDerivedVar("weighted2_time_LGADXY", weighted2_time_LGADXY/sum_amp2);
        tr.registerDerivedVar("weighted_time_LGADX", weighted_time_LGADX/sum_amp); // LGADXY, LGADX
        tr.registerDerivedVar("weighted2_time_LGADX", weighted2_time_LGADX/sum_amp2);

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
