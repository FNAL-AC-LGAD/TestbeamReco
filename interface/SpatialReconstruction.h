#ifndef SPATIALRECONSTRUCTION_H
#define SPATIALRECONSTRUCTION_H

#include "TestbeamReco/interface/Utility.h"

class SpatialReconstruction
{
private:
    void spatialReconstruction([[maybe_unused]] NTupleReader& tr)
    {

	//******************************************************************
	//X-Position Reconstruction
	//******************************************************************
        const auto& enablePositionReconstruction = tr.getVar<double>("enablePositionReconstruction");
        const auto& positionRecoPar0 = tr.getVar<double>("positionRecoPar0");
        const auto& positionRecoPar1 = tr.getVar<double>("positionRecoPar1");
        const auto& positionRecoPar2 = tr.getVar<double>("positionRecoPar2");
        const auto& positionRecoPar3 = tr.getVar<double>("positionRecoPar3");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& Amp2Index = tr.getVar<int>("Amp2Index");        
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");

	double x_reco = 0;
	double positionRecoCutFitCutOffPoint = 0.735;
	double x1 = 0;
	double x2 = 0;
	if (enablePositionReconstruction >= 1.0)
        {	  
            assert(Amp1OverAmp1and2 >= 0); //make sure a1/(a1+a2) is a sensible number
            assert(Amp1OverAmp1and2 <= 1);
            x1 = stripCenterXPositionLGAD[0][maxAmpIndex];
            x2 = stripCenterXPositionLGAD[0][Amp2Index];
            
            //double xSin = 1/62.0*(asin((Amp1OverAmp123 - 0.55)/0.059) + 0.124);
            
            //use the poly fit function
            double dX = positionRecoPar0 + positionRecoPar1*Amp1OverAmp1and2 + positionRecoPar2*pow(Amp1OverAmp1and2,2) + positionRecoPar3*pow(Amp1OverAmp1and2,3);
            
            //After the "cut-off" point of the fit, then linearly 
            //interpolate to (Amp1OverAmp1and2=0.75,dX=0.0) point
            if (Amp1OverAmp1and2 > 0.75) 
            {
                dX = 0.0;                
            }
            else if (Amp1OverAmp1and2 > positionRecoCutFitCutOffPoint) {
                double dX_atCutOffPoint = positionRecoPar0 + positionRecoPar1*positionRecoCutFitCutOffPoint + positionRecoPar2*pow(positionRecoCutFitCutOffPoint,2) + positionRecoPar3*pow(positionRecoCutFitCutOffPoint,3);
                dX = dX_atCutOffPoint + ((0.0 - dX_atCutOffPoint)/(0.75 - positionRecoCutFitCutOffPoint))*(Amp1OverAmp1and2-0.75);
            }

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
