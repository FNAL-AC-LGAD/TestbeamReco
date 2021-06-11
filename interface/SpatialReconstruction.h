#ifndef SPATIALRECONSTRUCTION_H
#define SPATIALRECONSTRUCTION_H

#include "TestbeamReco/interface/Utility.h"

class SpatialReconstruction
{
private:
    double getDX(const std::vector<double>& coeffs, const double x)
    {
        double dX = 0.0;
        int index = 0;
        for(const auto& coeff : coeffs)
        {
            dX += coeff*pow(x,index);
            index++;
        }
        return dX;
    }

    void spatialReconstruction([[maybe_unused]] NTupleReader& tr)
    {

	//******************************************************************
	//X-Position Reconstruction
	//******************************************************************
        const auto& enablePositionReconstruction = tr.getVar<double>("enablePositionReconstruction");
        const auto& positionRecoPar = tr.getVar<std::vector<double>>("positionRecoPar");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& Amp2Index = tr.getVar<int>("Amp2Index");        
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");

	double x_reco = 0;
        double positionRecoMaxPoint = 0.75;
	double x1 = 0;
	double x2 = 0;
	if (enablePositionReconstruction >= 1.0)
        {	  
            assert(Amp1OverAmp1and2 >= 0); //make sure a1/(a1+a2) is a sensible number
            assert(Amp1OverAmp1and2 <= 1);
            x1 = stripCenterXPositionLGAD[0][maxAmpIndex];
            x2 = stripCenterXPositionLGAD[0][Amp2Index];
            
            //use the poly fit function
            auto dX = getDX(positionRecoPar, Amp1OverAmp1and2);
            dX = (Amp1OverAmp1and2 > positionRecoMaxPoint) ? 0.0 : dX;

            x_reco = (x2>x1) ? x1+dX : x1-dX;
	} //if enabled position reconstruction

        tr.registerDerivedVar("x_reco", x_reco);
    }
public:
    SpatialReconstruction()
    {
        std::cout<<"Running Spatial Reconstruction Module"<<std::endl;
    }

    void operator()(NTupleReader& tr)
    {
        spatialReconstruction(tr);
    }
};

#endif
