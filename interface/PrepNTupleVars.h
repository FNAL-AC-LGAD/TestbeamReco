#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

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

    void prepNTupleVars(NTupleReader& tr)
    {
        // Create the eventCounter variable to keep track of processed events
        int w = 1;
        tr.registerDerivedVar<int>("eventCounter",w);        

        // Correct the rotation angle for the x and y measurment
        const auto& sensorConfigMap = tr.getVar<std::map<std::string,double>>("sensorConfigMap");
        const auto  angle = sensorConfigMap.at("angle");
	const auto& x_dut = tr.getVec<float>("x_dut");
	const auto& y_dut = tr.getVec<float>("y_dut");
	Rotate(tr, x_dut[0], y_dut[0], angle);
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
