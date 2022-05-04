#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

#include <numeric>
#include "TestbeamReco/interface/Utility.h"
#include <TRandom3.h>
#include <chrono>

class PrepNTupleVars
{
private:
    float xSlope_;
    float ySlope_;
    float xIntercept_;
    float yIntercept_;
    bool doAmpSmearing_;
    mutable int seed;

    void Rotate(NTupleReader& tr, double x0, double y0, double angle) const
    {
        double rad_angle = angle*3.14159/180.;
        double x_rot = x0*cos(rad_angle) + y0*sin(rad_angle);
        double y_rot = y0*cos(rad_angle) - x0*sin(rad_angle);
        tr.registerDerivedVar("x", x_rot);
        tr.registerDerivedVar("y", y_rot);
    }

    void RotateVec(NTupleReader& tr, const std::vector<float>& vx, const std::vector<float>& vy, double angle) const
    {
        auto& vec_x = tr.createDerivedVec<float>("x_var");
        auto& vec_y = tr.createDerivedVec<float>("y_var");
        double rad_angle = angle*3.14159/180.;
        for(unsigned int i=0; i < vx.size() ;i++)
        {
            vec_x.push_back(vx[i]*cos(rad_angle) + vy[i]*sin(rad_angle));
            vec_y.push_back(vy[i]*cos(rad_angle) - vx[i]*sin(rad_angle));
        }
    }

    double getSmear(double mean, double sigma) const
    {
        seed+=1;
        double smear = 1.0;
        if(doAmpSmearing_)
        {
            auto rNG = TRandom3(seed);
            smear = rNG.Gaus(mean, sigma);
            smear = (smear < 0.0) ? -1.0*smear : smear;
        }
        return smear;
    }

    void ApplyAmplitudeCorrection(NTupleReader& tr) const
    {     
        const auto& ampCorrectionFactors = tr.getVar<std::map<int,double>>("amplitudeCorrectionFactor");
        auto& corrAmp = tr.createDerivedVec<double>("corrAmp");
        const auto& amp = tr.getVec<float>("amp");
        
        int counter = 0;
        for(auto thisAmp : amp) 
        {
            corrAmp.emplace_back(getSmear(1.0, 0.2)*thisAmp*ampCorrectionFactors.at(counter));
            counter++;
        }
    }

    void getXYOnSensor(double& xFinal, double& yFinal, const float z=0.0, const float alpha=0.0, const float beta=0.0, const float gamma=0.0)
    {
        //Define intial x, y position based on fit from telescope reco
        double x0 = xSlope_*z + xIntercept_;
        double y0 = ySlope_*z + yIntercept_;

        //Correct for rotation in the plane of the sensor
        double degreesToRad = 3.14159/180.0;
        double gamma_rad = gamma*degreesToRad;
        double x1 = x0*cos(gamma_rad) + y0*sin(gamma_rad);
        double y1 = y0*cos(gamma_rad) - x0*sin(gamma_rad);

        //Correct for z-x plane rotation
        double alpha_rad = alpha*degreesToRad;
        double x2 = x1 + x1*tan(alpha_rad);

        //Correct for z-y plane rotation
        double beta_rad = beta*degreesToRad;
        double y2 = y1 + y1*tan(beta_rad);

        xFinal = x2;
        yFinal = y2;
    }

    void prepNTupleVars(NTupleReader& tr)
    {
        // Create the eventCounter variable to keep track of processed events
        int w = 1;
        tr.registerDerivedVar<int>("eventCounter",w);        

        // Correct the rotation angle for the x and y measurment
        xSlope_     = tr.getVar<float>("xSlope");
        ySlope_     = tr.getVar<float>("ySlope");
        xIntercept_ = tr.getVar<float>("xIntercept");
        yIntercept_ = tr.getVar<float>("yIntercept");
        const auto& alpha = tr.getVar<double>("alpha");
        const auto& beta  = tr.getVar<double>("beta");
        const auto& gamma = tr.getVar<double>("gamma");
        const auto& z_dut = tr.getVar<double>("z_dut");
    	//const auto& x_dut = tr.getVec<float>("x_dut");
    	//const auto& y_dut = tr.getVec<float>("y_dut");
        //
    	//Rotate(tr, x_dut[7], y_dut[7], gamma);
        //RotateVec(tr, x_dut, y_dut, gamma);

        // Define final telescope hit location on DUT based on track lines and hard coded parameters
        auto& x = tr.createDerivedVar<double>("x");
        auto& y = tr.createDerivedVar<double>("y");
        getXYOnSensor(x, y, z_dut, alpha, beta, gamma);

        // Create vectors of possible x,y locations by varying hard coded parameters
        const auto& zScan = tr.getVar<std::vector<double>>("zScan");
        auto& x_var = tr.createDerivedVec<double>("x_var",zScan.size());
        auto& y_var = tr.createDerivedVec<double>("y_var",zScan.size());
        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            getXYOnSensor(x_var[i], y_var[i], zScan[i], alpha, beta, gamma);
            //std::cout<<"z_dut = "<<z_dut<<" zHypothesis = "<<zScan[i]<<std::endl;
        }
        
        // Correct amp and map raw amplitude
	ApplyAmplitudeCorrection(tr);
        const auto& amp = tr.getVec<float>("amp");
        const auto& rawAmpLGAD = utility::remapToLGADgeometry(tr, amp, "rawAmpLGAD");
        double totRawAmpLGAD = 0.0;
        for(auto row : rawAmpLGAD){totRawAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);}
        tr.registerDerivedVar("totRawAmpLGAD", totRawAmpLGAD);

        // Cut to get hits that only go through active sensor
        const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
        bool hitSensor = sensorEdges[0][0] < x && x < sensorEdges[1][0] &&  sensorEdges[0][1] < y && y < sensorEdges[1][1];
        tr.registerDerivedVar("hitSensor", hitSensor);

        // Correct the time variable
        const auto& LP2_20 = tr.getVec<float>("LP2_20");
        const auto& timeCalibrationCorrection = tr.getVar<std::map<int,double>>("timeCalibrationCorrection");
        auto& corrTime = tr.createDerivedVec<double>("corrTime");
        int counter = 0;
        for(auto thisTime : LP2_20)
        {
            double corr = timeCalibrationCorrection.at(counter);
            if(thisTime == 0.0) corr = 0.0;
            corrTime.emplace_back(1e9*thisTime + corr);
            counter++;
        }
        utility::remapToLGADgeometry(tr, corrTime, "timeLGAD");

        // Baseline RMS
        const auto& baselineRMS = tr.getVec<float>("baseline_RMS");
        utility::remapToLGADgeometry(tr, baselineRMS, "baselineRMS");

        // Redefine Risetime
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& risetime = tr.getVec<float>("risetime");
        auto& corrRisetime = tr.createDerivedVec<double>("corrRisetime",risetime.size());
        for(unsigned int i = 0; i < risetime.size(); i++)
        {
            corrRisetime[i] = 1e12*abs(0.8*corrAmp[i] / risetime[i]);
        }
        utility::remapToLGADgeometry(tr, corrRisetime, "risetimeLGAD");

        //Charge, amp/charge ratio
        const auto& integral = tr.getVec<float>("integral");
        auto& charge = tr.createDerivedVec<double>("charge",integral.size());
        auto& AmpChargeRatio = tr.createDerivedVec<double>("AmpChargeRatio",integral.size());
        for(unsigned int i = 0; i < integral.size(); i++)
        {
            charge[i] = -1000*integral[i]*1e9*50/4700;
            AmpChargeRatio[i] = corrAmp[i]/charge[i];
        }
        utility::remapToLGADgeometry(tr, charge, "chargeLGAD");
        utility::remapToLGADgeometry(tr, AmpChargeRatio, "ampChargeRatioLGAD");
    }

public:
    PrepNTupleVars(bool doAmpSmearing = false) : xSlope_(0), ySlope_(0), xIntercept_(0), yIntercept_(0), doAmpSmearing_(doAmpSmearing)
    {
        seed = std::chrono::duration_cast<std::chrono::seconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    }

    void operator()(NTupleReader& tr)
    {
        prepNTupleVars(tr);
    }
};

#endif
