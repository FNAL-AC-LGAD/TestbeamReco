#ifndef SIGNALPROPERTIES_H
#define SIGNALPROPERTIES_H

#include "TestbeamReco/interface/Utility.h"

class SignalProperties
{
private:
    void signalProperties([[maybe_unused]] NTupleReader& tr)
    {
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");        
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
        double totGoodAmpLGAD = 0.0;
        for(auto row : ampLGAD)
        {
            totAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);
            for(auto amp : row)
            {
                if(amp > signalAmpThreshold) totGoodAmpLGAD += amp;
            }
        }
        tr.registerDerivedVar("totAmpLGAD", totAmpLGAD);
        tr.registerDerivedVar("totGoodAmpLGAD", totGoodAmpLGAD);

        //Find rel fraction of all LGADS
        auto& relFrac = tr.createDerivedVec<double>("relFrac");
        for(auto row : ampLGAD){ for(auto i : row) relFrac.emplace_back(i/totAmpLGAD);}

        //Find rel fraction of DC amp vs. LGAD amp
        tr.registerDerivedVar("relFracDC", corrAmp[0]/totAmpLGAD);

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
