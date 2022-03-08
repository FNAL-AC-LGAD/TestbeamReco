#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

#include <numeric>
#include "TestbeamReco/interface/Utility.h"

class PrepNTupleVars
{
private:
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

    void prepNTupleVars(NTupleReader& tr)
    {
        // Create the eventCounter variable to keep track of processed events
        int w = 1;
        tr.registerDerivedVar<int>("eventCounter",w);        

        // Correct the rotation angle for the x and y measurment
        const auto& angle = tr.getVar<double>("angle");
    	const auto& x_dut = tr.getVec<float>("x_dut");
    	const auto& y_dut = tr.getVec<float>("y_dut");
    	Rotate(tr, x_dut[21], y_dut[21], angle);
        RotateVec(tr, x_dut, y_dut, angle);

        // Correct amp and map raw amplitude
	ApplyAmplitudeCorrection(tr);
        const auto& amp = tr.getVec<float>("amp");
        const auto& rawAmpLGAD = utility::remapToLGADgeometry(tr, amp, "rawAmpLGAD");
        double totRawAmpLGAD = 0.0;
        for(auto row : rawAmpLGAD){totRawAmpLGAD += std::accumulate(row.begin(), row.end(), 0.0);}
        tr.registerDerivedVar("totRawAmpLGAD", totRawAmpLGAD);

        // Cut to get hits that only go through active sensor
	const auto& x = tr.getVar<double>("x");
	const auto& y = tr.getVar<double>("y");
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
    PrepNTupleVars()
    {
    }

    void operator()(NTupleReader& tr)
    {
        prepNTupleVars(tr);
    }
};

#endif
