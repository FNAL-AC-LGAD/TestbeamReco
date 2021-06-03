#ifndef SIGNALPROPERTIES_H
#define SIGNALPROPERTIES_H

#include "TestbeamReco/interface/Utility.h"

class SignalProperties
{
private:
    void signalProperties([[maybe_unused]] NTupleReader& tr)
    {
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");

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
        
        //Find total amplatude
        double totAmpLGAD = 0.0;
        for(auto row : ampLGAD) totAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);
        tr.registerDerivedVar("totAmpLGAD", totAmpLGAD);

        //Find rel fraction of all LGADS
        auto& relFrac = tr.createDerivedVec<double>("relFrac");
        for(auto row : ampLGAD){ for(auto i : row) relFrac.emplace_back(i/totAmpLGAD);}

        //Find rel fraction of DC amp vs. LGAD amp
        tr.registerDerivedVar("relFracDC", corrAmp[0]/totAmpLGAD);

	////Compute position-sensitive variables
        ////Only good for strip sensors currently
	//double xCenterMaxStrip = 0;
	//double xCenterStrip2 = 0;
	//double xCenterStrip3 = 0;
        //double Amp1 = 0.0, Amp2 = 0.0, Amp3 = 0.0;
	//double Amp1OverAmp1and2 = 0;
	//double Amp1OverAmp123 = 0, Amp2OverAmp123 = 0, Amp3OverAmp123 = 0;
	//double Amp2OverAmp2and3 = 0;
	//double deltaXmax = -999;
        //int maxAmpIndex = amp1Indexes.second;
        //int Amp2Index = amp2Indexes.second;
        //int Amp3Index = amp3Indexes.second;
	//if (maxAmpIndex >= 0 && Amp2Index>=0) 
        //{
        //    Amp1 = ampLGAD[0][maxAmpIndex];
        //    Amp2 = ampLGAD[0][Amp2Index];
        //    xCenterMaxStrip = stripCenterXPositionLGAD[0][maxAmpIndex];
        //    xCenterStrip2 = stripCenterXPositionLGAD[0][Amp2Index];
        //    Amp1OverAmp1and2 = ampLGAD[0][maxAmpIndex] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index]);
        //    if (Amp3Index >= 0) 
        //    {
        //        Amp3 = ampLGAD[0][Amp3Index];
        //        xCenterStrip3 = stripCenterXPositionLGAD[0][Amp3Index];
        //        Amp2OverAmp2and3= ampLGAD[0][Amp2Index] / (ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
        //        Amp1OverAmp123 = ampLGAD[0][maxAmpIndex] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
        //        Amp2OverAmp123 = ampLGAD[0][Amp2Index] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
        //        Amp3OverAmp123 = ampLGAD[0][Amp3Index] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
        //    }
        //    deltaXmax = x - xCenterMaxStrip;
	//}
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
