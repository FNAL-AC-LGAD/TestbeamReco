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
        const auto& timeTrackerX = tr.getVec<std::vector<double>>("timeTrackerX");
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
        const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& amp2Indexes = tr.getVar<std::pair<int,int>>("amp2Indexes");
        const auto& baselineRMSSlewRateRatioLGAD = tr.getVec<std::vector<double>>("baselineRMSSlewRateRatioLGAD");

        auto amp1 = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        auto amp2 = ampLGAD[amp2Indexes.first][amp2Indexes.second];
        auto time1 = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        auto time2 = timeLGAD[amp2Indexes.first][amp2Indexes.second];
        auto timeTracker1 = timeLGADTracker[amp1Indexes.first][amp1Indexes.second];
        auto timeTracker2 = timeLGADTracker[amp2Indexes.first][amp2Indexes.second];
        auto timeLGADXY1 = timeLGADXY[amp1Indexes.first][amp1Indexes.second];
        auto timeLGADXY2 = timeLGADXY[amp2Indexes.first][amp2Indexes.second];
        auto timeLGADX1 = timeLGADX[amp1Indexes.first][amp1Indexes.second];
        auto timeLGADX2 = timeLGADX[amp2Indexes.first][amp2Indexes.second];
        auto timeTrackerX1 = timeTrackerX[amp1Indexes.first][amp1Indexes.second];
        auto timeTrackerX2 = timeTrackerX[amp2Indexes.first][amp2Indexes.second];
        auto jitter1 = baselineRMSSlewRateRatioLGAD[amp1Indexes.first][amp1Indexes.second];
        auto jitter2 = baselineRMSSlewRateRatioLGAD[amp2Indexes.first][amp2Indexes.second];

        //-------------------------------------------------------
        //Code from https://github.com/cmorgoth/AC_LGAD_Timing 
        //-------------------------------------------------------
        double sum_amp=0.0, sum_amp_goodSig=0.0, sum_amp2=0.0, sum_amp2_goodSig=0.0;
        double weighted_time=0.0, weighted_time_goodSig=0.0, weighted2_time=0.0, weighted2_time_goodSig=0.0;
        double weighted_time_tracker=0.0, weighted2_time_tracker=0.0;
        double average_time_LGADXY=0.0, average_time_LGADX=0.0, weighted_time_LGADXY=0.0, weighted2_time_LGADXY=0.0, weighted_time_LGADX=0.0, weighted2_time_LGADX=0.0;
        double weighted_time_trackerX = 0.0, weighted2_time_trackerX = 0.0;
        double weighted2_jitter = 0.0;
        double weighted2_jitter_NewDef = 0.0;

        bool similarTime12 = abs(time2 - time1) < 1.0;
        bool twoGoodChannel = amp1 > noiseAmpThreshold  &&  amp2 > noiseAmpThreshold && similarTime12 && time1 != 0.0 && time2 != 0.0;
        if (!twoGoodChannel)
        {
            weighted_time = time1;
            weighted2_time = time1;

            weighted_time_tracker = timeTracker1;
            weighted2_time_tracker = timeTracker1;

            weighted_time_LGADXY = timeLGADXY1;
            weighted2_time_LGADXY = timeLGADXY1;

            weighted_time_LGADX = timeLGADX1;
            weighted2_time_LGADX = timeLGADX1;

            weighted_time_trackerX = timeTrackerX1;
            weighted2_time_trackerX = timeTrackerX1;

            average_time_LGADXY = timeLGADXY1;
            average_time_LGADX = timeLGADX1;

            weighted2_jitter = jitter1;
            weighted2_jitter_NewDef = jitter1;
        }
        else
        {
            sum_amp = amp1 + amp2;
            weighted_time = (amp1*time1 + amp2*time2)/sum_amp;
            weighted_time_tracker = (amp1*timeTracker1 + amp2*timeTracker2)/sum_amp;
            weighted_time_LGADXY = (amp1*timeLGADXY1 + amp2*timeLGADXY2)/sum_amp;
            weighted_time_LGADX = (amp1*timeLGADX1 + amp2*timeLGADX2)/sum_amp;
            weighted_time_trackerX = (amp1*timeTrackerX1 + amp2*timeTrackerX2)/sum_amp;

            sum_amp2 = (amp1*amp1) + (amp2*amp2);
            weighted2_time = (amp1*amp1*time1 + amp2*amp2*time2)/sum_amp2;
            weighted2_time_tracker = (amp1*amp1*timeTracker1 + amp2*amp2*timeTracker2)/sum_amp2;
            weighted2_time_LGADXY = (amp1*amp1*timeLGADXY1 + amp2*amp2*timeLGADXY2)/sum_amp2;
            weighted2_time_LGADX = (amp1*amp1*timeLGADX1 + amp2*amp2*timeLGADX2)/sum_amp2;
            weighted2_time_trackerX = (amp1*amp1*timeTrackerX1 + amp2*amp2*timeTrackerX2)/sum_amp2;

            average_time_LGADXY = (timeLGADXY1 + timeLGADXY2)*0.5;
            average_time_LGADX = (timeLGADX1 + timeLGADX2)*0.5;

            weighted2_jitter = std::sqrt((amp1*amp1*jitter1*jitter1 + amp2*amp2*jitter2*jitter2)/sum_amp2);
            weighted2_jitter_NewDef = std::sqrt((amp1*amp1*amp1*amp1*jitter1*jitter1 + amp2*amp2*amp2*amp2*jitter2*jitter2)/(sum_amp2*sum_amp2));
        }
   
        bool twoGoodChannelSignalThres = amp1 > signalAmpThreshold  &&  amp2 > signalAmpThreshold && similarTime12 && time1 != 0.0 && time2 != 0.0;
        if (!twoGoodChannelSignalThres)
        {
            weighted_time_goodSig = time1;
            weighted2_time_goodSig = time1;
        }
        else
        {
            sum_amp_goodSig = amp1 + amp2;
            weighted_time_goodSig = (amp1*time1 + amp2*time2)/sum_amp_goodSig;

            sum_amp2_goodSig = (amp1*amp1) + (amp2*amp2);
            weighted2_time_goodSig = (amp1*amp1*time1 + amp2*amp2*time2)/sum_amp2_goodSig;
        }
    

        tr.registerDerivedVar("weighted_time", weighted_time);
        tr.registerDerivedVar("weighted_time_tracker", weighted_time_tracker);
        tr.registerDerivedVar("weighted2_time", weighted2_time);
        tr.registerDerivedVar("weighted2_time_tracker", weighted2_time_tracker);
        tr.registerDerivedVar("average_time_LGADXY", average_time_LGADXY); 
        tr.registerDerivedVar("average_time_LGADX", average_time_LGADX); 
        tr.registerDerivedVar("weighted_time_LGADXY", weighted_time_LGADXY);
        tr.registerDerivedVar("weighted2_time_LGADXY", weighted2_time_LGADXY);
        tr.registerDerivedVar("weighted_time_LGADX", weighted_time_LGADX);
        tr.registerDerivedVar("weighted2_time_LGADX", weighted2_time_LGADX);
        tr.registerDerivedVar("weighted_time_trackerX", weighted_time_trackerX);
        tr.registerDerivedVar("weighted2_time_trackerX", weighted2_time_trackerX);
        tr.registerDerivedVar("weighted_time_goodSig", weighted_time_goodSig);
        tr.registerDerivedVar("weighted2_time_goodSig", weighted2_time_goodSig);
        tr.registerDerivedVar("weighted2_jitter", weighted2_jitter);
        tr.registerDerivedVar("weighted2_jitter_NewDef", weighted2_jitter_NewDef);
        tr.registerDerivedVar("twoGoodChannel", twoGoodChannel);


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
