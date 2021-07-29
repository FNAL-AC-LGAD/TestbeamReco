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
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");
        const auto& stripCenterXPosition = tr.getVar<std::vector<double>>("stripCenterXPosition");
        const auto& stripCenterYPosition = tr.getVar<std::vector<double>>("stripCenterYPosition");
        const auto& stripCenterXPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterXPosition, "stripCenterXPositionLGAD");
        const auto& stripCenterYPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterYPosition, "stripCenterYPositionLGAD");
        const auto& x = tr.getVar<double>("x");
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");

	//Find max channel and 2nd,3rd channels
        const auto amp1Indexes = utility::findNthRankChannel(ampLGAD, 1);
        const auto amp2Indexes = utility::findNthRankChannel(ampLGAD, 2);
        const auto amp3Indexes = utility::findNthRankChannel(ampLGAD, 3);
        tr.registerDerivedVar("amp1Indexes", amp1Indexes);
        tr.registerDerivedVar("amp2Indexes", amp2Indexes);
        tr.registerDerivedVar("amp3Indexes", amp3Indexes);

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
        //Find max LGAD amp
        double maxAmpLGAD = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        tr.registerDerivedVar("maxAmpLGAD", maxAmpLGAD);
        
        //Find  amplitude related variables
        double totAmpLGAD = 0.0;
        double totGoodAmpLGAD = 0.0;
        bool hasGlobalSignal_highThreshold = false;
        bool hasGlobalSignal_lowThreshold = false;
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
                    clusterSize++;
                }
            }
        }
        tr.registerDerivedVar("totAmpLGAD", totAmpLGAD);
        tr.registerDerivedVar("totGoodAmpLGAD", totGoodAmpLGAD);
        tr.registerDerivedVar("hasGlobalSignal_highThreshold", hasGlobalSignal_highThreshold);
        tr.registerDerivedVar("hasGlobalSignal_lowThreshold", hasGlobalSignal_lowThreshold);
        tr.registerDerivedVar("clusterSize", clusterSize);

        //Find rel fraction of all LGADS
        auto& relFrac = tr.createDerivedVec<std::vector<double>>("relFrac", ampLGAD);
        for(auto& row : relFrac){ for(auto& amp : row) amp /= totAmpLGAD;}

   
        //Find rel fraction of DC amp vs. LGAD amp
        tr.registerDerivedVar("relFracDC", corrAmp[0]/totAmpLGAD);

        //Compute position-sensitive variablei
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
    
        int maxAmpIndex = amp1Indexes.second;
        int Amp2Index = amp2Indexes.second;
        double Amp1 = stayPositive(ampLGAD[amp1Indexes.first][amp1Indexes.second]);
        double Amp2 = stayPositive(ampLGAD[amp2Indexes.first][amp2Indexes.second]);
        double Amp3 = stayPositive(ampLGAD[amp3Indexes.first][amp3Indexes.second]);
        double AmpTop = stayPositive(ampLGAD[ampIndexesTop.first][ampIndexesTop.second]);
        double AmpBot = stayPositive(ampLGAD[ampIndexesBot.first][ampIndexesBot.second]); 
        double AmpAdjPad =  stayPositive(ampLGAD[ampIndexesAdjPad.first][ampIndexesAdjPad.second]);
        double AmpLeftTop = 0;         
        double AmpLeftBot = 0; 
        double AmpRightTop = 0;
        double AmpRightBot = 0;
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
        double Amp12 = stayPositive(Amp1 + Amp2);
        double Amp123 = stayPositive(Amp1 + Amp2 + Amp3);
        double Amp1Top = stayPositive(Amp1 + AmpTop);
        double Amp1Bot = stayPositive(Amp1 + AmpBot);
        double Amp1AdjPad = stayPositive(Amp1 +AmpAdjPad);
        double Amp1OverAmp1and2 = stayPositive(Amp1 / Amp12);
        double Amp1OverAmp1andTop = stayPositive(Amp1 / Amp1Top);
        double Amp1OverAmp1andBot = stayPositive(Amp1 / Amp1Bot);
        double Amp1OverAmp1andAdjPad = stayPositive(Amp1 / Amp1AdjPad);
        double Amp2OverAmp2and3 = stayPositive(Amp2 / Amp12);
        double Amp1OverAmp123 = stayPositive(Amp1 / Amp123);
        double Amp2OverAmp123 = stayPositive(Amp2 / Amp123);
        double Amp3OverAmp123 = stayPositive(Amp3 / Amp123);
        double xCenterMaxStrip = stripCenterXPositionLGAD[amp1Indexes.first][amp1Indexes.second];
        double deltaXmax = x - xCenterMaxStrip;
        double deltaXmaxpos = -999;
        double deltaXmaxneg = -999;
        double deltaXmaxTopPad = 0;
        double deltaXmaxBotPad = 0;
        double deltaXmaxAdjPad = 0; 

        if (deltaXmax >= 0)
        {   
            deltaXmaxpos = deltaXmax;
        }
        else
        {
            deltaXmaxneg = deltaXmax;
        }   
      
 
        if (amp1Indexes.first==0 && amp1Indexes.second==0)
        {
            deltaXmaxTopPad = deltaXmaxneg;
        }
        else if (amp1Indexes.first==0 && amp1Indexes.second==1)
        {
            deltaXmaxTopPad = deltaXmaxpos;
        }
        
         if (amp1Indexes.first==1 && amp1Indexes.second==0)
        {
            deltaXmaxBotPad = deltaXmaxneg;
        }
        else if (amp1Indexes.first==1 && amp1Indexes.second==1)
        {
            deltaXmaxBotPad = deltaXmaxpos;
        } 

        if (amp1Indexes.first==0)
        {
            deltaXmaxAdjPad = deltaXmaxTopPad; 
        } 
        else if (amp1Indexes.first==1)
        { 
            deltaXmaxAdjPad = deltaXmaxBotPad;
        }
       
        tr.registerDerivedVar("maxAmpIndex", maxAmpIndex);
        tr.registerDerivedVar("padx", padx);
        tr.registerDerivedVar("padxAdj", padxAdj);
        tr.registerDerivedVar("Amp2Index", Amp2Index);
        tr.registerDerivedVar("deltaXmax", deltaXmax);
        tr.registerDerivedVar("deltaXmaxpos", deltaXmaxpos);
        tr.registerDerivedVar("deltaXmaxneg", deltaXmaxneg);
        tr.registerDerivedVar("deltaXmaxTopPad", deltaXmaxTopPad);
        tr.registerDerivedVar("deltaXmaxBotPad", deltaXmaxBotPad);
        tr.registerDerivedVar("deltaXmaxAdjPad", deltaXmaxAdjPad);
        tr.registerDerivedVar("xCenterMaxStrip", xCenterMaxStrip);
        tr.registerDerivedVar("AmpLeftOverAmpLeftandRightTop", AmpLeftOverAmpLeftandRightTop);
        tr.registerDerivedVar("AmpLeftOverAmpLeftandRightBot", AmpLeftOverAmpLeftandRightBot);
        tr.registerDerivedVar("AmpTopOverAmpTopandBotRight", AmpTopOverAmpTopandBotRight);
        tr.registerDerivedVar("AmpTopOverAmpTopandBotLeft", AmpTopOverAmpTopandBotLeft);
        tr.registerDerivedVar("Amp1OverAmp1and2", Amp1OverAmp1and2);
        tr.registerDerivedVar("Amp2OverAmp2and3", Amp2OverAmp2and3);
        tr.registerDerivedVar("Amp1OverAmp123", Amp1OverAmp123);
        tr.registerDerivedVar("Amp2OverAmp123", Amp2OverAmp123);
        tr.registerDerivedVar("Amp3OverAmp123", Amp3OverAmp123);
        tr.registerDerivedVar("Amp1OverAmp1andTop", Amp1OverAmp1andTop);
        tr.registerDerivedVar("Amp1OverAmp1andBot", Amp1OverAmp1andBot);
        tr.registerDerivedVar("Amp1OverAmp1andAdjPad", Amp1OverAmp1andAdjPad);
        tr.registerDerivedVar("Amp12", Amp12);
        tr.registerDerivedVar("Amp123", Amp123);
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
