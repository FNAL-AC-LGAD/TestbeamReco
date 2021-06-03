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
	Rotate(tr, x_dut[0], y_dut[0], angle);
	ApplyAmplitudeCorrection(tr);

        // Cut to get hits that only go through active sensor
	const auto& x = tr.getVar<double>("x");
	const auto& y = tr.getVar<double>("y");
        const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
        bool hitSensor = sensorEdges[0][0] < x && x < sensorEdges[1][0] &&  sensorEdges[0][1] < y && y < sensorEdges[1][1];
        tr.registerDerivedVar<bool>("hitSensor", hitSensor);
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
