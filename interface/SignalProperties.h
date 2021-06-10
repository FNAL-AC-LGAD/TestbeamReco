#ifndef SIGNALPROPERTIES_H
#define SIGNALPROPERTIES_H

#include "TestbeamReco/interface/Utility.h"

class SignalProperties
{
private:
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
	double xCenterMaxStrip = 0;
        double Amp1 = 0.0, Amp2 = 0.0, Amp3 = 0.0;
	double Amp1OverAmp1and2 = 0;
	double Amp1OverAmp123 = 0, Amp2OverAmp123 = 0, Amp3OverAmp123 = 0;
	double Amp2OverAmp2and3 = 0;
        double Amp12=0;
        double Amp123 = 0;
	double deltaXmax = -999;
        int maxAmpIndex = amp1Indexes.second;
        int Amp2Index = amp2Indexes.second;
        int Amp3Index = amp3Indexes.second;
	if (maxAmpIndex >= 0 && Amp2Index>=0) 
        {
            Amp1 = ampLGAD[amp1Indexes.first][amp1Indexes.second];
            Amp2 = ampLGAD[amp2Indexes.first][amp2Indexes.second];
            Amp1 = (Amp1 > 0.0) ? Amp1 : 0.0;
            Amp2 = (Amp2 > 0.0) ? Amp2 : 0.0;
            Amp1OverAmp1and2 = Amp1 / (Amp1 + Amp2);
            Amp1OverAmp1and2 = (Amp1OverAmp1and2 > 0.0) ? Amp1OverAmp1and2 : 0.0;
            xCenterMaxStrip = stripCenterXPositionLGAD[amp1Indexes.first][amp1Indexes.second];
            deltaXmax = x - xCenterMaxStrip;
            if (Amp3Index >= 0) 
            {
                Amp3 = ampLGAD[amp3Indexes.first][amp3Indexes.second];
                Amp12 = Amp1 + Amp2;
                Amp123 = Amp1 + Amp2 + Amp3;
                Amp2OverAmp2and3 = Amp2 / Amp12;
                Amp1OverAmp123 = Amp1 / Amp123;
                Amp2OverAmp123 = Amp2 / Amp123;
                Amp3OverAmp123 = Amp3 / Amp123;
            }
	}
        tr.registerDerivedVar("maxAmpIndex", maxAmpIndex);
        tr.registerDerivedVar("Amp2Index", Amp2Index);
        tr.registerDerivedVar("deltaXmax", deltaXmax);
        tr.registerDerivedVar("Amp1OverAmp1and2", Amp1OverAmp1and2);
        tr.registerDerivedVar("Amp2OverAmp2and3", Amp2OverAmp2and3);
        tr.registerDerivedVar("Amp1OverAmp123", Amp1OverAmp123);
        tr.registerDerivedVar("Amp2OverAmp123", Amp2OverAmp123);
        tr.registerDerivedVar("Amp3OverAmp123", Amp3OverAmp123);
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
