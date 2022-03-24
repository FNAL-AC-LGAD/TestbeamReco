#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

#include <numeric>
#include "TestbeamReco/interface/Utility.h"

class PrepNTupleVars
{
private:
    float xSlope_;
    float ySlope_;
    float xIntercept_;
    float yIntercept_;

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

    void ApplyAmplitudeCorrection(NTupleReader& tr) const
    {     
        const auto& ampCorrectionFactors = tr.getVar<std::map<int,double>>("amplitudeCorrectionFactor");
        auto& corrAmp = tr.createDerivedVec<double>("corrAmp");
        const auto& amp = tr.getVec<float>("amp");
        int counter = 0;
        for(auto thisAmp : amp) 
        {
            corrAmp.emplace_back(thisAmp*ampCorrectionFactors.at(counter));
            counter++;
        }      
    }

    void getXYOnSensor(double& xFinal, double& yFinal, const float z_C=0.0, const float theta=0.0, const float phi=0.0, const float x_C=0.0, const float y_C=0.0)
    {
        double degreesToRad = 3.14159/180.0;
        double theta_rad = theta*degreesToRad;
        double phi_rad = phi*degreesToRad;

        double z_lab = (z_C - tan(theta_rad)*(cos(xIntercept_ - x_C) + sin(yIntercept_ - y_C))) / (1 + tan(theta_rad)*(cos(phi_rad)*xSlope_ + sin(phi_rad)*ySlope_));

        double lx = xIntercept_ + z_lab*xSlope_ - x_C;
        double ly = yIntercept_ + z_lab*ySlope_ - y_C;
        double lz = z_lab - z_C;

        xFinal = lx*(cos(phi_rad)*cos(theta_rad)) + ly*(sin(phi_rad)*cos(theta_rad)) + lz*(-sin(theta_rad));
        yFinal = lx*(-sin(phi_rad)) + ly*(cos(phi_rad));

        // //Define intial x, y position based on fit from telescope reco
        // double x0 = xSlope_*z + xIntercept_;
        // double y0 = ySlope_*z + yIntercept_;

        // //Correct for rotation in the plane of the sensor
        // double degreesToRad = 3.14159/180.0;
        // double gamma_rad = gamma*degreesToRad;
        // double x1 = x0*cos(gamma_rad) + y0*sin(gamma_rad);
        // double y1 = y0*cos(gamma_rad) - x0*sin(gamma_rad);

        // //Correct for z-x plane rotation
        // double alpha_rad = alpha*degreesToRad;
        // double x2 = x1 + x1*tan(alpha_rad);

        // //Correct for z-y plane rotation
        // double beta_rad = beta*degreesToRad;
        // double y2 = y1 + y1*tan(beta_rad);

        // xFinal = x2;
        // yFinal = y2;
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
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");
        const auto& sensorCenterY = tr.getVar<double>("sensorCenterY");
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
        getXYOnSensor(x, y, z_dut, alpha, beta, sensorCenter, sensorCenterY);

        // Create vectors of possible x,y locations by varying hard coded parameters
        const auto& zScan = tr.getVar<std::vector<double>>("zScan");
        const auto& alphaScan = tr.getVar<std::vector<double>>("alphaScan");
        const auto& betaScan = tr.getVar<std::vector<double>>("betaScan");
        auto& x_var = tr.createDerivedVec<double>("x_var",zScan.size()*alphaScan.size()*betaScan.size());
        auto& y_var = tr.createDerivedVec<double>("y_var",zScan.size()*alphaScan.size()*betaScan.size());
        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            for(unsigned int j = 0; j < alphaScan.size(); j++)
            {
                for(unsigned int k = 0; k < betaScan.size(); k++)
                {
                    unsigned int i_var = k + j*betaScan.size() + i*betaScan.size()*alphaScan.size();
                    getXYOnSensor(x_var[i_var], y_var[i_var], zScan[i], alphaScan[j], betaScan[k], sensorCenter, sensorCenterY);
                    //std::cout<<"z_dut = "<<z_dut<<" zHypothesis = "<<zScan[i]<<std::endl;
                }
            }
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
    }

public:
    PrepNTupleVars() : xSlope_(0), ySlope_(0), xIntercept_(0), yIntercept_(0)
    {
    }

    void operator()(NTupleReader& tr)
    {
        prepNTupleVars(tr);
    }
};

#endif
