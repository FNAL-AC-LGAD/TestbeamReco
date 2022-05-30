#ifndef SPATIALRECONSTRUCTION_H
#define SPATIALRECONSTRUCTION_H

#include "TestbeamReco/interface/Utility.h"

class SpatialReconstruction
{
private:
    double getDX(const std::vector<double>& coeffs, const double x, const double shift = 0.0)
    {
        double dX = 0.0;
        int index = 0;
        for(const auto& coeff : coeffs)
        {
            dX += coeff*pow(x - shift,index);
            index++;
        }
        return (dX >= 0.0) ? dX : 0.0;
    }

    double getDXDerivative(const std::vector<double>& coeffs, const double x, const double shift = 0.0)
    {
        double dXD = 0.0;
        int index = 0;
        for(const auto& coeff : coeffs)
        {
            dXD += index*coeff*pow(x - shift,index-1);
            index++;
        }
        return dXD;
    }

    void spatialReconstruction([[maybe_unused]] NTupleReader& tr)
    {

	//******************************************************************
	//Position Reconstruction
	//******************************************************************
        const auto& enablePositionReconstruction = tr.getVar<bool>("enablePositionReconstruction");
        const auto& positionRecoPar = tr.getVar<std::vector<double>>("positionRecoPar");
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& Amp2Index = tr.getVar<int>("Amp2Index");
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");
        const auto& positionRecoMaxPoint = tr.getVar<double>("positionRecoMaxPoint");
        const auto& pitch = tr.getVar<double>("pitch");
        const auto& timeLGADTracker = tr.getVec<std::vector<double>>("timeLGADTracker");
        const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");

        auto& goodNeighbour = tr.createDerivedVar<bool>("goodNeighbour");
        goodNeighbour = abs(maxAmpIndex - Amp2Index)==1 && ampLGAD[0][Amp2Index]>noiseAmpThreshold;

        double y_reco=0.0, x_reco = 0.0, x1 = 0.0, y1 = 0.0, x2 = 0.0;
        double x_reco_basic = 0.0, y_reco_basic = 0.0;
        double dXdFrac = 0.0;
        if(enablePositionReconstruction)
        {	  
            assert(Amp1OverAmp1and2 >= 0); //make sure a1/(a1+a2) is a sensible number
            assert(Amp1OverAmp1and2 <= 1);
            x1 = stripCenterXPositionLGAD[0][maxAmpIndex];
            x2 = stripCenterXPositionLGAD[0][Amp2Index];

            //use the poly fit function
            auto dX = getDX(positionRecoPar, Amp1OverAmp1and2, 0.5);
            dX = (goodNeighbour && (Amp1OverAmp1and2 < positionRecoMaxPoint)) ? dX : 0.0;

            x_reco = (x2>x1) ? x1+dX : x1-dX;

            //Define basic x reco
            double xBasic = (1.0 - Amp1OverAmp1and2)*pitch;
            x_reco_basic = (x2>x1) ? x1 + xBasic : x1 - xBasic;

            //Define slope of poly fit function
            dXdFrac = getDXDerivative(positionRecoPar, Amp1OverAmp1and2, 0.5);

            //Define basic y reco
            double t1 = timeLGADTracker[0][maxAmpIndex];
            double t2 = timeLGADTracker[0][Amp2Index];
            double vX =  2.0;
            double vY = 50.0;
            double vR = vY/vX;
            double dXSign = (x2>x1) ? dX : -dX;
            double dT = t1 - t2;
            double yBasic = vR*(pitch - 2*dXSign) + vY*dT;
            //double yBasic = vR*(pitch - 2*x_reco_basic) + vY*dT;
            //double yBasic = vR*pitch*(2*Amp1OverAmp1and2 - 1.0) + vY*dT;
            y_reco_basic = 0.5*yBasic;

	    } //if enabled position reconstruction
        
        const auto& positionRecoParRight = tr.getVar<std::vector<double>>("positionRecoParRight");
        const auto& positionRecoParLeft = tr.getVar<std::vector<double>>("positionRecoParLeft");
        const auto& positionRecoParTop = tr.getVar<std::vector<double>>("positionRecoParTop");
        const auto& positionRecoParBot = tr.getVar<std::vector<double>>("positionRecoParBot");
        const auto& enablePositionReconstructionPad = tr.getVar<bool>("enablePositionReconstructionPad");
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");
        const auto& sensorCenterY = tr.getVar<double>("sensorCenterY");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& AmpTopOverAmpTopandBotRight = tr.getVar<double>("AmpTopOverAmpTopandBotRight");
        const auto& AmpTopOverAmpTopandBotLeft = tr.getVar<double>("AmpTopOverAmpTopandBotLeft");
        const auto& AmpLeftOverAmpLeftandRightTop = tr.getVar<double>("AmpLeftOverAmpLeftandRightTop");
        const auto& AmpLeftOverAmpLeftandRightBot = tr.getVar<double>("AmpLeftOverAmpLeftandRightBot");
          	
        if(enablePositionReconstructionPad)
        {	  
            x1 = sensorCenter;
            
            //use the poly fit function
            auto dXTop = getDX(positionRecoParTop, AmpLeftOverAmpLeftandRightTop);
            auto dXBot = getDX(positionRecoParBot, AmpLeftOverAmpLeftandRightBot);
            auto dX = (amp1Indexes.first ==0) ? dXTop : dXBot;
            
            x_reco = x1 + dX;
           
            y1 = sensorCenterY;
            auto dYRight = getDX(positionRecoParRight, AmpTopOverAmpTopandBotRight);
            auto dYLeft = getDX(positionRecoParLeft, AmpTopOverAmpTopandBotLeft);
            auto dY = (amp1Indexes.second == 0) ? dYLeft : dYRight;
            
            y_reco = dY + y1;
                                
             
	    } //if enabled position reconstruction

        tr.registerDerivedVar("x_reco", x_reco);
        tr.registerDerivedVar("x_reco_basic", x_reco_basic);
        tr.registerDerivedVar("dXdFrac", dXdFrac);
        tr.registerDerivedVar("y_reco", y_reco);
        tr.registerDerivedVar("y_reco_basic", y_reco_basic);
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
