#ifndef Geometry2025_h
#define Geometry2025_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

//################################## Start Geometry for July 2025 CFD Sensor ################################


class CFD_HPK_W2_3_2_50T_1P0_500P_50M_E240_StripsGeometry: public DefaultGeometry
// CFD_HPK_W2_3_2_50T_1P0_500P_50M_E240_187V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-5 was AC-lgad channels [CFD analog & discriminator], 6 was DC LGAD and scope channel 7 was the photek
    // 
    // |-----------|     -----        -----
    // | 2 2 2 2 2 |     |666|        |777|
    // | 1 1 1 1 1 |     |666|        |777|
    // | 0 0 0 0 0 |     -----        -----
    // |-----------|

    CFD_HPK_W2_3_2_50T_1P0_500P_50M_E240_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,0}}, {2,{0,1}}, {3,{0,1}}, {4,{0,2}}, {5,{0,2}}, {6,{1,0}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2},{6},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,false}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.56401}, {1,0.41657}, {2,0.59696}, {3,0.41189}, {4,0.47175}, {5,0.37958}, {6,0.52220}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // Lab-Tracker's frame ->  y_dut   
    double sensorCenterY = 0.5 ; // Lab-Tracker's frame -> x_dut
    std::vector<double> stripCenterXPosition = {2.25, 2.25, 1.75, 1.75, 1.25, 1.25, 0.0, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.72; //-0.72; // 0.00;
    double beta  =  0.00; // 0.00; // 0.00;
    double gamma =  0.00; // 0.00; // 0.00;
    double z_dut =  2.22; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.100;
    double xmin = -9.0; // Sensor's local frame
    double xmax =  10.0; // Sensor's local frame
    double ymin = -5.0; // Sensor's local frame
    double ymax =  5.0; // Sensor's local frame
    double positionRecoMaxPoint = 0.84;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool usesDESYorCERNTracker = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    ///MODIFY ME!!!!???
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.693443, 0.894506, -9.526453, 38.944962, -58.650584};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};
#endif