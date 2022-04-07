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

    void getXYOnSensor(double& xFinal, double& yFinal, const float z_C=0.0, const float alpha=0.0, const float beta=0.0, const float gamma=0.0, const float x_C=0.0, const float y_C=0.0)
    {

        // Maybe add a new element related to the strips direction: IsHorizontal = true (default: false)
        double x_temp = x_C;
        double xc = (gamma < -45 || 45 < gamma) ? -y_C : x_C;
        double yc = (gamma < -45 || 45 < gamma) ? x_temp : y_C;
        
        double degreesToRad = 3.14159/180.0;
        double alpha_rad = alpha*degreesToRad;
        double beta_rad = beta*degreesToRad;
        double gamma_rad = gamma*degreesToRad;

        double z_lab = (z_C - tan(alpha_rad)*(cos(beta_rad)*(xIntercept_ - xc) + sin(beta_rad)*(yIntercept_ - yc))) / (1 + tan(alpha_rad)*(cos(beta_rad)*xSlope_ + sin(beta_rad)*ySlope_));

        double lx = xIntercept_ + z_lab*xSlope_ - xc;
        double ly = yIntercept_ + z_lab*ySlope_ - yc;
        double lz = z_lab - z_C;

        double x_sensor = lx*(cos(beta_rad)*cos(alpha_rad)) + ly*(sin(beta_rad)*cos(alpha_rad)) + lz*(-sin(alpha_rad));
        double y_sensor = lx*(-sin(beta_rad)) + ly*(cos(beta_rad));

        xFinal = (xIntercept_!=0 && xSlope_!=0) ? x_sensor*cos(gamma_rad) + y_sensor*sin(gamma_rad) : -9999;
        yFinal = (yIntercept_!=0 && ySlope_!=0) ? y_sensor*cos(gamma_rad) - x_sensor*sin(gamma_rad) : -9999;

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
        const auto& z_dut = tr.getVar<double>("z_dut");
        const auto& alpha = tr.getVar<double>("alpha");
        const auto& beta  = tr.getVar<double>("beta");
        const auto& gamma = tr.getVar<double>("gamma");
    	//const auto& x_dut = tr.getVec<float>("x_dut");
    	//const auto& y_dut = tr.getVec<float>("y_dut");
        //
    	//Rotate(tr, x_dut[7], y_dut[7], gamma);
        //RotateVec(tr, x_dut, y_dut, gamma);

        // Define final telescope hit location on DUT based on track lines and hard coded parameters
        auto& x = tr.createDerivedVar<double>("x");
        auto& y = tr.createDerivedVar<double>("y");
        getXYOnSensor(x, y, z_dut, alpha, beta, gamma, sensorCenter, sensorCenterY);

        // Create vectors of possible x,y locations by varying hard coded parameters
        const auto& zScan = tr.getVar<std::vector<double>>("zScan");
        const auto& alphaScan = tr.getVar<std::vector<double>>("alphaScan");
        const auto& betaScan = tr.getVar<std::vector<double>>("betaScan");
        const auto& gammaScan = tr.getVar<std::vector<double>>("gammaScan");

        auto& x_var = tr.createDerivedVec<double>("x_var",zScan.size());
        auto& y_var = tr.createDerivedVec<double>("y_var",zScan.size());
        auto& x_varA = tr.createDerivedVec<double>("x_varA",alphaScan.size());
        auto& y_varA = tr.createDerivedVec<double>("y_varA",alphaScan.size());
        auto& x_varB = tr.createDerivedVec<double>("x_varB",betaScan.size());
        auto& y_varB = tr.createDerivedVec<double>("y_varB",betaScan.size());
        auto& x_varC = tr.createDerivedVec<double>("x_varC",gammaScan.size());
        auto& y_varC = tr.createDerivedVec<double>("y_varC",gammaScan.size());
        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            getXYOnSensor(x_var[i], y_var[i], zScan[i], alpha, beta, gamma, sensorCenter, sensorCenterY);
        }
        for(unsigned int i = 0; i < alphaScan.size(); i++)
        {
            getXYOnSensor(x_varA[i], y_varA[i], z_dut, alphaScan[i], beta, gamma, sensorCenter, sensorCenterY);
        }
        for(unsigned int i = 0; i < betaScan.size(); i++)
        {
            getXYOnSensor(x_varB[i], y_varB[i], z_dut, alpha, betaScan[i], gamma, sensorCenter, sensorCenterY);
        }
        for(unsigned int i = 0; i < gammaScan.size(); i++)
        {
            getXYOnSensor(x_varC[i], y_varC[i], z_dut, alpha, beta, gammaScan[i], sensorCenter, sensorCenterY);
        }

        //     for(unsigned int j = 0; j < alphaScan.size(); j++)
        //     {
        //         for(unsigned int k = 0; k < betaScan.size(); k++)
        //         {
        //             for(unsigned int l = 0; l < gammaScan.size(); l++)
        //             {
        //                 unsigned int i_var = l + k*gammaScan.size() + j*betaScan.size()*gammaScan.size() + i*betaScan.size()*alphaScan.size()*gammaScan.size();
        //                 getXYOnSensor(x_var[i_var], y_var[i_var], zScan[i], alphaScan[j], betaScan[k], gammaScan[l], sensorCenter, sensorCenterY);
        //                 //std::cout<<"z_dut = "<<z_dut<<" zHypothesis = "<<zScan[i]<<std::endl;
        //             }
        //         }
        //     }
        
        // Correct amp and map raw amplitude
	    ApplyAmplitudeCorrection(tr);
        const auto& amp = tr.getVec<float>("amp");
        const auto& rawAmpLGAD = utility::remapToLGADgeometry(tr, amp, "rawAmpLGAD");
        double totRawAmpLGAD = 0.0;
        for(auto row : rawAmpLGAD){totRawAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);}
        tr.registerDerivedVar("totRawAmpLGAD", totRawAmpLGAD);

        // Cut to get hits that only go through active sensor
        const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
        bool hitSensor = sensorEdges[0][0]-sensorCenter < x && x < sensorEdges[1][0]-sensorCenter &&  sensorEdges[0][1]-sensorCenterY < y && y < sensorEdges[1][1]-sensorCenterY;
        tr.registerDerivedVar("hitSensor", hitSensor);

        // Hit through active sensor for scan vars
        auto& hitSensorZ = tr.createDerivedVec<bool>("hitSensorZ",zScan.size());
        auto& hitSensorA = tr.createDerivedVec<bool>("hitSensorA",alphaScan.size());
        auto& hitSensorB = tr.createDerivedVec<bool>("hitSensorB",betaScan.size());
        auto& hitSensorC = tr.createDerivedVec<bool>("hitSensorC",gammaScan.size());

        for(unsigned int i = 0; i < zScan.size(); i++)
        {
            hitSensorZ[i] = sensorEdges[0][0]-sensorCenter < x_var[i] && x_var[i] < sensorEdges[1][0]-sensorCenter &&  sensorEdges[0][1]-sensorCenterY < y_var[i] && y_var[i] < sensorEdges[1][1]-sensorCenterY;
        }
        for(unsigned int i = 0; i < alphaScan.size(); i++)
        {
            hitSensorA[i] = sensorEdges[0][0]-sensorCenter < x_varA[i] && x_varA[i] < sensorEdges[1][0]-sensorCenter &&  sensorEdges[0][1]-sensorCenterY < y_varA[i] && y_varA[i] < sensorEdges[1][1]-sensorCenterY;
        }
        for(unsigned int i = 0; i < betaScan.size(); i++)
        {
            hitSensorB[i] = sensorEdges[0][0]-sensorCenter < x_varB[i] && x_varB[i] < sensorEdges[1][0]-sensorCenter &&  sensorEdges[0][1]-sensorCenterY < y_varB[i] && y_varB[i] < sensorEdges[1][1]-sensorCenterY;
        }
        for(unsigned int i = 0; i < gammaScan.size(); i++)
        {
            hitSensorC[i] = sensorEdges[0][0]-sensorCenter < x_varC[i] && x_varC[i] < sensorEdges[1][0]-sensorCenter &&  sensorEdges[0][1]-sensorCenterY < y_varC[i] && y_varC[i] < sensorEdges[1][1]-sensorCenterY;
        }

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
