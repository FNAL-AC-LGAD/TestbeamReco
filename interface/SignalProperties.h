#ifndef SIGNALPROPERTIES_H
#define SIGNALPROPERTIES_H

#include "TestbeamReco/interface/Utility.h"

class SignalProperties
{
private:
    template<typename T> inline T stayPositive(const T value) const
    {
        return (value > 0.0) ? value : 0.0;
    }

    void signalProperties([[maybe_unused]] NTupleReader& tr)
    {
        const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
        const auto& isPadSensor = tr.getVar<bool>("isPadSensor");
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampRow = tr.getVec<double>("ampRow");
        const auto& ampCol = tr.getVec<double>("ampCol");
        const auto& baselineRMS = tr.getVec<std::vector<float>>("baselineRMS");
        const auto& stripCenterXPosition = tr.getVar<std::vector<double>>("stripCenterXPosition");
        const auto& stripCenterYPosition = tr.getVar<std::vector<double>>("stripCenterYPosition");

        const auto& x = tr.getVar<double>("x");
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");
        const auto& extraChannelIndex = tr.getVar<int>("extraChannelIndex");
        const auto& enablePositionReconstructionPad = tr.getVar<bool>("enablePositionReconstructionPad");

        // Remap to LGAD geometry
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");
        const auto& ampRowLGAD = utility::remapToLGADgeometry(tr, ampRow, "ampRowLGAD");
        const auto& ampColLGAD = utility::remapToLGADgeometry(tr, ampCol, "ampColLGAD");
        const auto& stripCenterXPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterXPosition, "stripCenterXPositionLGAD");
        //const auto& stripCenterYPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterYPosition, "stripCenterYPositionLGAD");
        utility::remapToLGADgeometry(tr, stripCenterYPosition, "stripCenterYPositionLGAD");

        const auto amp1Indexes = utility::findNthRankChannel(ampLGAD, 1, corrAmp[extraChannelIndex]);
        const auto amp2Indexes = utility::findNthRankChannel(ampLGAD, 2, corrAmp[extraChannelIndex]);
        const auto amp3Indexes = utility::findNthRankChannel(ampLGAD, 3, corrAmp[extraChannelIndex]);
        const auto amp4Indexes = utility::findNthRankChannel(ampLGAD, 4, corrAmp[extraChannelIndex]);
        const auto amp5Indexes = utility::findNthRankChannel(ampLGAD, 5, corrAmp[extraChannelIndex]);
        const auto amp6Indexes = utility::findNthRankChannel(ampLGAD, 6, corrAmp[extraChannelIndex]);
        tr.registerDerivedVar("amp1Indexes", amp1Indexes);
        tr.registerDerivedVar("amp2Indexes", amp2Indexes);
        tr.registerDerivedVar("amp3Indexes", amp3Indexes);
        tr.registerDerivedVar("amp4Indexes", amp4Indexes);
        tr.registerDerivedVar("amp5Indexes", amp5Indexes);
        tr.registerDerivedVar("amp6Indexes", amp6Indexes);

        const auto& n_row = tr.getVar<int>("n_row");
        const auto ampCol1Indexes = utility::findNthRankChannel(ampColLGAD, 1, corrAmp[extraChannelIndex]);
        const auto ampCol2Indexes = utility::findNthRankChannel(ampColLGAD, 1+n_row, corrAmp[extraChannelIndex]);
        tr.registerDerivedVar("ampCol1Indexes", ampCol1Indexes);
        tr.registerDerivedVar("ampCol2Indexes", ampCol2Indexes);

        const auto& n_col = tr.getVar<int>("n_col");
        const auto ampRow1Indexes = utility::findNthRankChannel(ampRowLGAD, 1, corrAmp[extraChannelIndex]);
        const auto ampRow2Indexes = utility::findNthRankChannel(ampRowLGAD, 1+n_col, corrAmp[extraChannelIndex]);
        tr.registerDerivedVar("ampRow1Indexes", ampRow1Indexes);
        tr.registerDerivedVar("ampRow2Indexes", ampRow2Indexes);

        // OLD: 2x2 pads variables
        std::pair<int,int> ampIndexesTop;
        if(amp1Indexes.first == 0 && amp1Indexes.second == 0)
        {
            ampIndexesTop = std::make_pair<int,int>(0,1);
        }
        else if(amp1Indexes.first == 0  && amp1Indexes.second == 1)
        {		
            ampIndexesTop = std::make_pair<int,int>(0,0);
        }

        std::pair<int,int> ampIndexesBot;
        if(amp1Indexes.first == 1 && amp1Indexes.second == 0)
        {
            ampIndexesBot = std::make_pair<int,int>(1,1);
        }
        else if(amp1Indexes.first == 1  && amp1Indexes.second == 1)
        {		
            ampIndexesBot = std::make_pair<int,int>(1,0);
        }

        std::pair<int,int> ampIndexesAdjPad;
        if (amp1Indexes.first == 0)
        {
            ampIndexesAdjPad = ampIndexesTop;
        }
        else if (amp1Indexes.first == 1)
        {
            ampIndexesAdjPad = ampIndexesBot;
        }

        tr.registerDerivedVar("ampIndexesAdjPad", ampIndexesAdjPad);

        // Find max LGAD amp
        double maxAmpLGAD = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        double maxAmpColLGAD = ampColLGAD[ampCol1Indexes.first][ampCol1Indexes.second];
        double maxAmpRowLGAD = ampRowLGAD[ampRow1Indexes.first][ampRow1Indexes.second];

        double ampLGAD1st = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        double ampLGAD2nd = ampLGAD[amp2Indexes.first][amp2Indexes.second];
        double ampColLGAD1st = ampColLGAD[ampCol1Indexes.first][ampCol1Indexes.second];
        double ampColLGAD2nd = ampColLGAD[ampCol2Indexes.first][ampCol2Indexes.second];
        tr.registerDerivedVar("maxAmpLGAD", maxAmpLGAD);
        tr.registerDerivedVar("maxAmpColLGAD", maxAmpColLGAD);
        tr.registerDerivedVar("maxAmpRowLGAD", maxAmpRowLGAD);
        tr.registerDerivedVar("ampLGAD1st", ampLGAD1st);
        tr.registerDerivedVar("ampLGAD2nd", ampLGAD2nd);
        tr.registerDerivedVar("ampColLGAD1st", ampColLGAD1st);
        tr.registerDerivedVar("ampColLGAD2nd", ampColLGAD2nd);

        // Find  amplitude related variables
        double totAmpLGAD = 0.0, totGoodAmpLGAD = 0.0;
        bool hasGlobalSignal_highThreshold = false, hasGlobalSignal_lowThreshold = false;
        int clusterSize = 0;
        for(auto row : ampLGAD)
        {
            totAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);
            for(auto amp : row)
            {
                if(amp > signalAmpThreshold)
                {
                    hasGlobalSignal_highThreshold = true;
                    totGoodAmpLGAD += amp;
                }

                if(amp > noiseAmpThreshold) 
                {
                    hasGlobalSignal_lowThreshold = true;
                    //clusterSize++;
                }

                if(amp > 50.0) clusterSize++; // 50.0 mV == 10 fC
            }
        }
        tr.registerDerivedVar("totAmpLGAD", totAmpLGAD);
        tr.registerDerivedVar("totGoodAmpLGAD", totGoodAmpLGAD);
        tr.registerDerivedVar("hasGlobalSignal_highThreshold", hasGlobalSignal_highThreshold);
        tr.registerDerivedVar("hasGlobalSignal_lowThreshold", hasGlobalSignal_lowThreshold);
        tr.registerDerivedVar("clusterSize", clusterSize);

        // Find rel fraction of all LGADS
        auto& relFrac = tr.createDerivedVec<std::vector<double>>("relFrac", ampLGAD);
        auto& relFracCol = tr.createDerivedVec<std::vector<double>>("relFracCol", ampLGAD);
        auto& relFracRow = tr.createDerivedVec<std::vector<double>>("relFracRow", ampLGAD);
        for(auto& row : relFrac){ for(auto& amp : row) amp /= totAmpLGAD; }
        for(auto& row : relFracCol){ for(auto& amp : row) amp /= totAmpLGAD; }
        for(auto& row : relFracRow){ for(auto& amp : row) amp /= totAmpLGAD; }

        // Find signal in channel over MaxAmp
        auto& fracMax = tr.createDerivedVec<std::vector<double>>("fracMax", ampLGAD);
        for(auto& row : fracMax){ for(auto& amp : row) amp /= maxAmpLGAD; }

        // Find rel fraction of DC amp vs. LGAD amp
        tr.registerDerivedVar("relFracDC", corrAmp[0]/totAmpLGAD);

        // Amp ratios
        int maxAmpIndex = amp1Indexes.second;
        int Amp2Index = amp2Indexes.second;

        double Amp1 = stayPositive(ampLGAD[amp1Indexes.first][amp1Indexes.second]);
        double Amp2 = stayPositive(ampLGAD[amp2Indexes.first][amp2Indexes.second]);
        double Amp3 = stayPositive(ampLGAD[amp3Indexes.first][amp3Indexes.second]);
        double Noise1 = stayPositive(baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        double Noise2 = stayPositive(baselineRMS[amp2Indexes.first][amp2Indexes.second]);

        // NOTE: Using ampColLGAD for x reconstruction. An ampRowLGAD version should be added for y reconstruction!
        if (enablePositionReconstructionPad)
        {
            Amp1 = stayPositive(ampColLGAD[ampCol1Indexes.first][ampCol1Indexes.second]);
            Amp2 = stayPositive(ampColLGAD[ampCol2Indexes.first][ampCol2Indexes.second]);
            Amp3 = 0.0;
        }

        double Amp12 = stayPositive(Amp1 + Amp2);
        double Noise12 = stayPositive(Noise1 + Noise2);
        double Amp123 = stayPositive(Amp1 + Amp2 + Amp3);
        double Amp1OverAmp1and2 = stayPositive(Amp1 / Amp12);
        double Amp2OverAmp2and3 = stayPositive(Amp2 / Amp12);
        double Amp1OverAmp123 = stayPositive(Amp1 / Amp123);
        double Amp2OverAmp123 = stayPositive(Amp2 / Amp123);
        double Amp3OverAmp123 = stayPositive(Amp3 / Amp123);

        double xCenterMaxStrip = stripCenterXPositionLGAD[amp1Indexes.first][amp1Indexes.second];
        double deltaXmax = x - xCenterMaxStrip;
        double deltaXmaxpos = -999, deltaXmaxneg = -999;

        if (deltaXmax >= 0){ deltaXmaxpos = deltaXmax; }
        else { deltaXmaxneg = deltaXmax; }

        tr.registerDerivedVar("maxAmpIndex", maxAmpIndex);
        tr.registerDerivedVar("Amp2Index", Amp2Index);
        tr.registerDerivedVar("Amp12", Amp12);
        tr.registerDerivedVar("Noise12", Noise12);
        tr.registerDerivedVar("Amp123", Amp123);
        tr.registerDerivedVar("Amp1OverAmp1and2", Amp1OverAmp1and2);
        tr.registerDerivedVar("Amp2OverAmp2and3", Amp2OverAmp2and3);
        tr.registerDerivedVar("Amp1OverAmp123", Amp1OverAmp123);
        tr.registerDerivedVar("Amp2OverAmp123", Amp2OverAmp123);
        tr.registerDerivedVar("Amp3OverAmp123", Amp3OverAmp123);
        tr.registerDerivedVar("xCenterMaxStrip", xCenterMaxStrip);
        tr.registerDerivedVar("deltaXmax", deltaXmax);
        tr.registerDerivedVar("deltaXmaxpos", deltaXmaxpos);
        tr.registerDerivedVar("deltaXmaxneg", deltaXmaxneg);


        // OLD: Compute position-sensitive variablei in 2x2 pads
        double padx = 0;
        double padxAdj = 0;

        if (amp1Indexes.first == 0 && amp1Indexes.second == 0)
        {
            padx = x-sensorCenter;
            padxAdj =  -(x-sensorCenter);
        }
        else if (amp1Indexes.first == 0 && amp1Indexes.second == 1)
        {
            padx = -(x-sensorCenter);
            padxAdj = x-sensorCenter;
        }
        else if (amp1Indexes.first == 1 && amp1Indexes.second == 1)
        {
            padx = -(x-sensorCenter);
            padxAdj = x-sensorCenter;
        }
        else if (amp1Indexes.first == 1 && amp1Indexes.second == 0)
        {
            padx = x-sensorCenter;
            padxAdj = -(x-sensorCenter);
        }

        // OLD: Amp ratios pads
        double AmpTop = stayPositive(ampLGAD[ampIndexesTop.first][ampIndexesTop.second]);
        double AmpBot = stayPositive(ampLGAD[ampIndexesBot.first][ampIndexesBot.second]);
        double AmpAdjPad =  stayPositive(ampLGAD[ampIndexesAdjPad.first][ampIndexesAdjPad.second]);
        double AmpLeftTop = 0, AmpLeftBot = 0, AmpRightTop = 0, AmpRightBot = 0;
        if (isPadSensor)
        {
            AmpLeftTop = stayPositive(ampLGAD[0][0]);
            AmpLeftBot = stayPositive(ampLGAD[1][0]);
            AmpRightTop = stayPositive(ampLGAD[0][1]);
            AmpRightBot = stayPositive(ampLGAD[1][1]);
        }   
        double AmpLeftOverAmpLeftandRightTop = stayPositive(AmpLeftTop / (AmpLeftTop + AmpRightTop));
        double AmpLeftOverAmpLeftandRightBot = stayPositive(AmpLeftBot / (AmpLeftBot + AmpRightBot));
        double AmpTopOverAmpTopandBotLeft = stayPositive(AmpLeftTop/ (AmpLeftTop + AmpLeftBot));
        double AmpTopOverAmpTopandBotRight = stayPositive(AmpRightTop/ (AmpRightTop + AmpRightBot));

        double Amp1Top = stayPositive(Amp1 + AmpTop);
        double Amp1Bot = stayPositive(Amp1 + AmpBot);
        double Amp1AdjPad = stayPositive(Amp1 +AmpAdjPad);
        double Amp1OverAmp1andTop = stayPositive(Amp1 / Amp1Top);
        double Amp1OverAmp1andBot = stayPositive(Amp1 / Amp1Bot);
        double Amp1OverAmp1andAdjPad = stayPositive(Amp1 / Amp1AdjPad);

        double deltaXmaxTopPad = 0, deltaXmaxBotPad = 0, deltaXmaxAdjPad = 0;

        if (amp1Indexes.first==0 && amp1Indexes.second==0){ deltaXmaxTopPad = deltaXmaxneg; }
        else if (amp1Indexes.first==0 && amp1Indexes.second==1){ deltaXmaxTopPad = deltaXmaxpos; }

        if (amp1Indexes.first==1 && amp1Indexes.second==0){ deltaXmaxBotPad = deltaXmaxneg; }
        else if (amp1Indexes.first==1 && amp1Indexes.second==1){ deltaXmaxBotPad = deltaXmaxpos; }

        if (amp1Indexes.first==0){ deltaXmaxAdjPad = deltaXmaxTopPad; }
        else if (amp1Indexes.first==1){ deltaXmaxAdjPad = deltaXmaxBotPad; }

        tr.registerDerivedVar("padx", padx);
        tr.registerDerivedVar("padxAdj", padxAdj);
        tr.registerDerivedVar("deltaXmaxTopPad", deltaXmaxTopPad);
        tr.registerDerivedVar("deltaXmaxBotPad", deltaXmaxBotPad);
        tr.registerDerivedVar("deltaXmaxAdjPad", deltaXmaxAdjPad);
        tr.registerDerivedVar("AmpLeftOverAmpLeftandRightTop", AmpLeftOverAmpLeftandRightTop);
        tr.registerDerivedVar("AmpLeftOverAmpLeftandRightBot", AmpLeftOverAmpLeftandRightBot);
        tr.registerDerivedVar("AmpTopOverAmpTopandBotRight", AmpTopOverAmpTopandBotRight);
        tr.registerDerivedVar("AmpTopOverAmpTopandBotLeft", AmpTopOverAmpTopandBotLeft);
        tr.registerDerivedVar("Amp1OverAmp1andTop", Amp1OverAmp1andTop);
        tr.registerDerivedVar("Amp1OverAmp1andBot", Amp1OverAmp1andBot);
        tr.registerDerivedVar("Amp1OverAmp1andAdjPad", Amp1OverAmp1andAdjPad);

        // Add deltaT
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        auto time1 = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        auto time2 = timeLGAD[amp2Indexes.first][amp2Indexes.second];
        auto deltaT = time1 - time2;
        tr.registerDerivedVar("deltaT",deltaT);
    }
public:
    SignalProperties()
    {
        std::cout<<"Running Signal Properties Module"<<std::endl;
    }

    void operator()(NTupleReader& tr)
    {
        signalProperties(tr);
    }
};

#endif
