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
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");
        const auto& stripCenterXPosition = tr.getVar<std::vector<double>>("stripCenterXPosition");
        const auto& stripCenterXPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterXPosition, "stripCenterXPositionLGAD");
        const auto& x = tr.getVar<double>("x");

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

        //Find max LGAD amp
        double maxAmpLGAD = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        tr.registerDerivedVar("maxAmpLGAD", maxAmpLGAD);
        
        //Find  amplatude related variables
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
        auto& relFrac = tr.createDerivedVec<double>("relFrac");
        for(auto row : ampLGAD){ for(auto i : row) relFrac.emplace_back(i/totAmpLGAD);}

        //Find rel fraction of DC amp vs. LGAD amp
        tr.registerDerivedVar("relFracDC", corrAmp[0]/totAmpLGAD);

        //Compute position-sensitive variables
        int maxAmpIndex = amp1Indexes.second;
        int Amp2Index = amp2Indexes.second;
        double Amp1 = stayPositive(ampLGAD[amp1Indexes.first][amp1Indexes.second]);
        double Amp2 = stayPositive(ampLGAD[amp2Indexes.first][amp2Indexes.second]);
        double Amp3 = stayPositive(ampLGAD[amp3Indexes.first][amp3Indexes.second]);
        double AmpTop = stayPositive(ampLGAD[ampIndexesTop.first][ampIndexesTop.second]);
        double AmpBot = stayPositive(ampLGAD[ampIndexesBot.first][ampIndexesBot.second]); 
        double Amp12 = stayPositive(Amp1 + Amp2);
        double Amp123 = stayPositive(Amp1 + Amp2 + Amp3);
        double Amp1Top = stayPositive(Amp1 + AmpTop);
        double Amp1Bot = stayPositive(Amp1 + AmpBot);
        double Amp1OverAmp1and2 = stayPositive(Amp1 / Amp12);
        double Amp1OverAmp1andTop = stayPositive(Amp1 / Amp1Top);
        double Amp1OverAmp1andBot = stayPositive(Amp1 / Amp1Bot);
        double Amp2OverAmp2and3 = stayPositive(Amp2 / Amp12);
        double Amp1OverAmp123 = stayPositive(Amp1 / Amp123);
        double Amp2OverAmp123 = stayPositive(Amp2 / Amp123);
        double Amp3OverAmp123 = stayPositive(Amp3 / Amp123);
        double xCenterMaxStrip = stripCenterXPositionLGAD[amp1Indexes.first][amp1Indexes.second];
        double deltaXmax = x - xCenterMaxStrip;
        tr.registerDerivedVar("maxAmpIndex", maxAmpIndex);
        tr.registerDerivedVar("Amp2Index", Amp2Index);
        tr.registerDerivedVar("deltaXmax", deltaXmax);
        tr.registerDerivedVar("Amp1OverAmp1and2", Amp1OverAmp1and2);
        tr.registerDerivedVar("Amp2OverAmp2and3", Amp2OverAmp2and3);
        tr.registerDerivedVar("Amp1OverAmp123", Amp1OverAmp123);
        tr.registerDerivedVar("Amp2OverAmp123", Amp2OverAmp123);
        tr.registerDerivedVar("Amp3OverAmp123", Amp3OverAmp123);
        tr.registerDerivedVar("Amp1OverAmp1andTop", Amp1OverAmp1andTop);
        tr.registerDerivedVar("Amp1OverAmp1andBot", Amp1OverAmp1andBot);
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
