#ifndef Geometry2023_h
#define Geometry2023_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

//################################## Start Geometry for May - June 2023 HPK Sensors ################################

class HPK_W8_18_2_50T_1P0_500P_100M_C600_StripsGeometry: public DefaultGeometry
// HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W8_18_2_50T_1P0_500P_100M_C600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.59338}, {1,0.48883}, {2,0.62065}, {3,0.46902}, {4,0.50390}, {5,0.45180}, {6,0.55662}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.45; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.50; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.492, 0.998, 0.491, -0.010, -0.506, -1.006, -1.502, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.29;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut = -0.75;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.70; // 0.71;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 3;
    int minStripHits = 8;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -1.152450, 1.628628, -12.547487, 12.409411};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    // int centerGoodStripIndex = 3;
	// double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	// double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	// double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	// double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	// std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};

class HPK_W8_17_2_50T_1P0_500P_50M_C600_StripsGeometry: public DefaultGeometry
// HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W8_17_2_50T_1P0_500P_50M_C600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.59104}, {1,0.50003}, {2,0.62669}, {3,0.47664}, {4,0.50786}, {5,0.45314}, {6,0.55516}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.45; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.25; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.526, 1.028, 0.526, 0.023, -0.478, -0.978, -1.479, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.60; //-0.6;// 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut =-7.35;// 0.00;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.71;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -1.162898, 0.988027, -6.238384, 17.134867, -89.438984};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W4_17_2_50T_1P0_500P_50M_C240_StripsGeometry: public DefaultGeometry
// HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W4_17_2_50T_1P0_500P_50M_C240_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.63532}, {1,0.44980}, {2,0.65943}, {3,0.44812}, {4,0.53530}, {5,0.40674}, {6,0.59020}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.8; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.6; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.513, 1.016, 0.516, 0.013, -0.487, -0.987, -1.486, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.54;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  2.46;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.69;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -1.102187, -2.496727, 25.676521, -97.950055};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W5_17_2_50T_1P0_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W5_17_2_50T_1P0_500P_50M_E600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.55365}, {1,0.41265}, {2,0.58756}, {3,0.41238}, {4,0.46536}, {5,0.37530}, {6,0.51456}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.70; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.25; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.518, 1.019, 0.518, 0.017, -0.484, -0.984, -1.484, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.50; // 0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut = -1.99;
    double xBinSize = 0.050;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.623392, 0.074807, -3.237477, 17.697710, -31.574229};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W2_3_2_50T_1P0_500P_50M_E240_StripsGeometry: public DefaultGeometry
// HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W2_3_2_50T_1P0_500P_50M_E240_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.56401}, {1,0.41657}, {2,0.59696}, {3,0.41189}, {4,0.47175}, {5,0.37958}, {6,0.52220}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.75; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.25; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.507, 1.007, 0.508, 0.008, -0.491, -0.991, -1.492, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.72; //-0.72; // 0.00;
    double beta  =  0.00; // 0.00; // 0.00;
    double gamma =  0.00; // 0.00; // 0.00;
    double z_dut =  2.22; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.84;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.693443, 0.894506, -9.526453, 38.944962, -58.650584};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W9_15_2_20T_1P0_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W9_15_2_20T_1P0_500P_50M_E600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.70976}, {1,0.59048}, {2,0.79824}, {3,0.60060}, {4,0.67771}, {5,0.57228}, {6,0.74993}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.5; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.459, 0.963, 0.460, -0.042, -0.539, -1.042, -1.540, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.49; //0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut = -1.17; //0.00;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.639735, -0.431173, 3.227442, -8.977157, 11.446396};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W9_14_2_20T_1P0_500P_100M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W9_14_2_20T_1P0_500P_100M_E600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.79872}, {1,0.64043}, {2,0.84810}, {3,0.63441}, {4,0.71489}, {5,0.58374}, {6,0.76879}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.75; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.50; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.509, 1.009, 0.506, 0.006, -0.493, -0.994, -1.492, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.75; //-0.755;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  3.00; //6.0;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.556451, -0.373801, 1.428454, 3.830588, -16.306163};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};


class HPK_KOJI_50T_1P0_80P_60M_E240_StripsGeometry: public DefaultGeometry
// HPK_KOJI_50T_1P0_80P_60M_E240_190V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_KOJI_50T_1P0_80P_60M_E240_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.74096}, {1,0.64983}, {2,0.72606}, {3,0.62496}, {4,0.59749}, {5,0.55756}, {6,0.71849}, {7,0.0}};
    double stripWidth = 0.060;
    double pitch = 0.080;
    double sensorCenter  = 0.30; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.50; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {0.212, 0.132, 0.051, -0.028, -0.108, -0.189, -0.269, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.92; //-0.92; // 0.00;
    double beta  =  0.00; // 0.00; // 0.00;
    double gamma =  0.00; // 0.00; // 0.00;
    double z_dut = -3.63; // 0.00; // 0.00;
    double xBinSize = 0.010; // 0.050;
    double yBinSize = 0.100;
    double xBinSize_delay_corr = 0.020;
    double yBinSize_delay_corr = 0.200;
    double xmin = -0.50; // Sensor's local frame
    double xmax =  0.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.62;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.040000, -0.336709, 3.029055, -63.405274, 597.812604, -2488.253914};
    std::vector<std::vector<double>> sensorEdges = {{-0.32, -4.70}, {0.25, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_KOJI_20T_1P0_80P_60M_E240_StripsGeometry: public DefaultGeometry
// HPK_KOJI_20T_1P0_80P_60M_E240_112V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_KOJI_20T_1P0_80P_60M_E240_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.93182}, {1,0.81958}, {2,0.92787}, {3,0.81084}, {4,0.80082}, {5,0.74340}, {6,0.93252}, {7,0.0}};
    double stripWidth = 0.060;
    double pitch = 0.080;
    double sensorCenter  = 0.42; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.00; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {0.239, 0.159, 0.079, 0.001, -0.080, -0.160, -0.242, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.59; //-0.59; // 0.00;
    double beta  =  0.00; // 0.00; // 0.00;
    double gamma =  0.00; // 0.00; // 0.00;
    double z_dut = -2.06; // 0.00; // 0.00;
    double xBinSize = 0.010; // 0.050;
    double yBinSize = 0.100;
    double xBinSize_delay_corr = 0.020;
    double yBinSize_delay_corr = 0.200;
    double xmin = -0.50; // Sensor's local frame
    double xmax =  0.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.62;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.040000, -0.220506, -0.626693, -3.596348, 117.512250, -841.237998};
    std::vector<std::vector<double>> sensorEdges = {{-0.30, -4.70}, {0.30, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};


class HPK_W9_15_4_20T_0P5_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    HPK_W9_15_4_20T_0P5_500P_50M_E600_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.62454}, {1,0.52235}, {2,0.66154}, {3,0.51883}, {4,0.54148}, {5,0.49415}, {6,0.58219}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = -0.7; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = -1.3; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.507, 1.006, 0.506, 0.006, -0.493, -0.994, -1.493, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.11;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut = -2.00;
    double xBinSize = 0.050;
    double yBinSize = 0.100;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.75; // Sensor's local frame
    double ymax =  2.75; // Sensor's local frame
    double positionRecoMaxPoint = 0.93;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool usesMay2023Tracker = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.543402, 0.639837, -6.105570, 22.185985, -27.380118};
    std::vector<std::vector<double>> sensorEdges = {{-1.80, -2.35}, {1.80, 2.45}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
};

class HPK_W9_22_3_20T_500x500_150M_E600_PixelsGeometry : public DefaultGeometry
{
public:
    // HPK_W9_22_3_20T_500x500_150M_E600_112V Mapping set
    // Used lecroy scope channels 0-7
    // -------
    // |  2  |           -----
    // |3 1 0|           |777|
    // |4 5 6|           |777|
    // -------           -----

    HPK_W9_22_3_20T_500x500_150M_E600_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.51724}, {1,0.63723}, {2,0.0}, {3,0.77677}, {4,0.67601}, {5,0.61875}, {6,0.55879}, {7,0.0}};
    double stripWidth = 0.150;
    double pitch = 0.500;
    double sensorCenter = 1.36; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY = -0.96; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.504, 0.003, 0.0, -0.488, -0.487, 0.004, 0.493, 0.0};
    std::vector<double> stripCenterYPosition = {0.246, 0.246, 0.0, 0.234, -0.251, -0.255, -0.255, 0.0};
    double alpha = -1.53;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.90;
    double xmax =  0.90;
    double ymin = -0.60;
    double ymax =  0.60;
    double xBinSize = 0.050;
    double yBinSize = 0.050;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double positionRecoMaxPointCol = 0.83; // 0.84;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 25; // 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParCol = {0.250000, -0.799820, 6.173329, -50.093476, 183.145262, -244.383245};
    std::vector<std::vector<double>> xSlices = {{0.80, 1.00}, {1.25, 1.45}, {1.75, 1.95}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.80, -0.60}, {-1.30, -1.10}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[4], stripCenterYPosition[4]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    // std::vector<utility::ROI> regionsOfIntrest = {{"MetalAndGap", -0.70,0.70, -0.4,-0.1}, {"Half", -0.70,0.70, -0.25, 0.25}};
};

class HPK_W9_23_3_20T_500x500_300M_E600_PixelsGeometry : public DefaultGeometry
// HPK_W9_23_3_20T_500x500_300M_E600_112V
{
public:
    // (!) Missing channel 0 (!) Mapping set
    // Used lecroy scope channels 0-7
    // --------
    // |  2   |           -----
    // |3 1 X0|           |777|
    // |4 5 X6|           |777|
    // -------            -----

    HPK_W9_23_3_20T_500x500_300M_E600_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1}, {4,5}, {7}}; // {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.66496}, {2,0.0}, {3,0.81830}, {4,0.71062}, {5,0.67177}, {6,0.57879}, {7,0.0}};
    double stripWidth = 0.300;
    double pitch = 0.500;
    double sensorCenter = 1.21; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY = -0.46; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.0, 0.251, 0.0, -0.250, -0.250, 0.243, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.0, 0.231, 0.0, 0.232, -0.254, -0.254, 0.0, 0.0};
    double alpha = -1.20;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.70;
    double xmax =  0.70;
    double ymin = -0.50;
    double ymax =  0.50;
    double xBinSize = 0.050;
    double yBinSize = 0.050;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double positionRecoMaxPointCol = 0.87;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParCol = {0.250000, -0.315639, 1.620337, -15.181558, 57.735255, -75.182057};
    // std::vector<double> positionRecoParTop = {-0.494315,  1.28059, 1.92055, -9.89445, 11.8025, -4.01589};
    // std::vector<double> positionRecoParBot = {-0.0849671, -3.72958, 25.6829, -63.7924, 70.3368, -28.3888};
    // std::vector<double> positionRecoParRight = {-0.046495, -3.91451, 24.6937, -57.5006, 59.3214, -22.163};
    // std::vector<double> positionRecoParLeft = {0.0339823, -5.42069, 33.1184, -78.8264, 84.4803, -33.3587};
    std::vector<std::vector<double>> xSlices = {{0.77, 1.13}, {1.27, 1.63}}; // Raw data coordinates // {1.77, 2.13}
    std::vector<std::vector<double>> ySlices = {{-0.40, 0.00}, {-0.90, -0.50}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50,-0.50}, {0.50, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.50,-0.50}, {0.50, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[4], stripCenterYPosition[4]}, {stripCenterXPosition[1], stripCenterYPosition[1]}}; // Sensor's local frame
    // std::vector<utility::ROI> regionsOfIntrest = {{"MetalAndGap", -0.70,0.70, -0.4,-0.1}, {"Half", -0.70,0.70, -0.25, 0.25}};
};

class HPK_W11_22_3_20T_500x500_150M_C600_PixelsGeometry : public DefaultGeometry
{
public:
    // HPK_W11_22_3_20T_500x500_150M_C600_116V Mapping set
    // Used lecroy scope channels 0-7
    // -------
    // |  2  |           -----
    // |3 1 0|           |777|
    // |4 5 6|           |777|
    // -------           -----

    HPK_W11_22_3_20T_500x500_150M_C600_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.57609}, {1,0.70186}, {2,0.0}, {3,0.83347}, {4,0.72950}, {5,0.68663}, {6,0.61618}, {7,0.0}};
    double stripWidth = 0.150;
    double pitch = 0.500;
    double sensorCenter = 1.29; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY = -0.8; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.487, -0.005, 0.0, -0.484, -0.491, -0.003, 0.481, 0.0};
    std::vector<double> stripCenterYPosition = {0.250, 0.248, 0.0, 0.252, -0.248, -0.250, -0.253, 0.0};
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.90;
    double xmax =  0.90;
    double ymin = -0.70;
    double ymax =  0.70;
    double xBinSize = 0.050;
    double yBinSize = 0.050;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double positionRecoMaxPointCol = 0.81; // 0.84;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParCol = {0.250000, -1.063382, 12.004629, -103.303789, 376.826502, -487.471421};
    std::vector<std::vector<double>> xSlices = {{0.70, 0.90}, {1.20, 1.40}, {1.65, 1.85}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.15, -0.95}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[4], stripCenterYPosition[4]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
};

class HPK_W8_1_1_50T_500x500_150M_C600_PixelsGeometry : public DefaultGeometry
{
public:
    // HPK_W8_1_1_50T_500x500_150M_C600_200V Mapping set
    // Used lecroy scope channels 0-7
    // -------
    // |  2  |           -----
    // |3 1 0|           |777|
    // |4 5 6|           |777|
    // -------           -----

    HPK_W8_1_1_50T_500x500_150M_C600_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.38173}, {1,0.52337}, {2,0.0}, {3,0.64922}, {4,0.54185}, {5,0.50666}, {6,0.41963}, {7,0.0}};
    double stripWidth = 0.150;
    double pitch = 0.500;
    double sensorCenter = 1.20; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY = -1.05; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.478, 0.007, 0.0, -0.488, -0.489, 0.007, 0.489, 0.0};
    std::vector<double> stripCenterYPosition = {0.245, 0.234, 0.0, 0.240, -0.260, -0.261, -0.260, 0.0};
    double alpha = -0.92;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.90;
    double xmax =  0.90;
    double ymin = -0.70;
    double ymax =  0.70;
    double xBinSize = 0.050;
    double yBinSize = 0.050;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double positionRecoMaxPointCol = 0.81; // 0.82;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParCol = {0.250000, -0.980465, 8.088825, -60.699625, 199.028843, -248.247343};
    std::vector<std::vector<double>> xSlices = {{0.65, 0.85}, {1.10, 1.30}, {1.55, 1.75}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.90, -0.70}, {-1.40, -1.20}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[4], stripCenterYPosition[4]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    // std::vector<utility::ROI> regionsOfIntrest = {{"MetalAndGap", -0.70,0.70, -0.4,-0.1}, {"Half", -0.70,0.70, -0.25, 0.25}};
};

class HPK_W5_1_1_50T_500x500_150M_E600_PixelsGeometry : public DefaultGeometry
{
public:
    // HPK_W5_1_1_50T_500x500_150M_E600_185V Mapping set
    // Used lecroy scope channels 0-7
    // -------
    // |  2  |           -----
    // |3 1 0|           |777|
    // |4 5 6|           |777|
    // -------           -----

    HPK_W5_1_1_50T_500x500_150M_E600_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.35611}, {1,0.46193}, {2,0.0}, {3,0.61546}, {4,0.49756}, {5,0.44839}, {6,0.38811}, {7,0.0}};
    double stripWidth = 0.150;
    double pitch = 0.500;
    double sensorCenter = 1.75; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY = -0.80; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.491, -0.004, 0.0, -0.498, -0.499, -0.005, 0.490, 0.0};
    std::vector<double> stripCenterYPosition = {0.251, 0.251, 0.0, 0.252, -0.245, -0.246, -0.255, 0.0};
    double alpha = -0.65;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.90;
    double xmax =  0.90;
    double ymin = -0.70;
    double ymax =  0.70;
    double xBinSize = 0.050;
    double yBinSize = 0.050;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double positionRecoMaxPointCol = 0.86; // 0.86;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParCol = {0.250000, -0.654670, 3.097194, -18.156571, 42.335163, -36.740634};
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.70,-0.50}, {0.70, 0.50}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[4], stripCenterYPosition[4]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    // std::vector<utility::ROI> regionsOfIntrest = {{"MetalAndGap", -0.70,0.70, -0.4,-0.1}, {"Half", -0.70,0.70, -0.25, 0.25}};
};

//################################## End Geometry for May - June 2023 HPK Sensors ################################

//###############################################################################################################
//                        2023 April Test Beam
//###############################################################################################################

class BNL_30um_5mm_500um_W3104_StripsGeometry : public DefaultGeometry
// BNL_30um_5mm_500um_W3104
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_30um_5mm_500um_W3104_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,10.44399}, {1,10.58574}, {2,10.50332}, {3,10.53967}, {4,10.38204}, {5,10.57758}, {6,10.38570}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 1.1; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.2; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.500, 1.000, 0.500, 0.0, -0.500, -1.000, -1.500, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -1.80; // Sensor's local frame
    double xmax =  1.80; // Sensor's local frame
    double ymin = -2.25; // Sensor's local frame
    double ymax =  2.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931};
    std::vector<std::vector<double>> sensorEdges = {{-1.70,-2.00}, {1.70,2.00}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -2.0}, {stripCenterXPosition[lowGoodStripIndex], 2.0}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, ymin,ymax},{"lowGain", leftLowGainX,rightLowGainX, ymin,ymax}};
};

class BNL_30um_5mm_700um_W3104_StripsGeometry : public DefaultGeometry
// BNL_30um_5mm_700um_W3104
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_30um_5mm_700um_W3104_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,10.31610}, {1,10.57848}, {2,10.44672}, {3,10.49184}, {4,10.34537}, {5,10.52095}, {6,10.36233}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.700;
    double sensorCenter  = 0.05; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.797, 1.211, 0.610, 0.010, -0.591, -1.192, -1.788, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -2.25; // Sensor's local frame
    double xmax =  2.25; // Sensor's local frame
    double ymin = -2.25; // Sensor's local frame
    double ymax =  2.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931};
    std::vector<std::vector<double>> sensorEdges = {{-2.0,-2.0}, {2.0,2.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -2.0}, {stripCenterXPosition[lowGoodStripIndex], 2.0}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, ymin,ymax},{"lowGain", leftLowGainX,rightLowGainX, ymin,ymax}};
};


class BNL_20um_5mm_700um_W3080_StripsGeometry : public DefaultGeometry
// BNL_20um_5mm_700um_W3080
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_5mm_700um_W3080_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{1,0}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5},{6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,false}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,10.42493}, {1,10.68229}, {2,10.56573}, {3,10.61049}, {4,10.46066}, {5,10.64728}, {6,0.0}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.700;
    double sensorCenter  = 0.45; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.1; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.750, 1.050, 0.350, -0.350, -1.050, -1.750, 0.0, 0.0};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 4;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -2.25; // Sensor's local frame
    double xmax =  2.25; // Sensor's local frame
    double ymin = -2.25; // Sensor's local frame
    double ymax =  2.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931};
    std::vector<std::vector<double>> sensorEdges = {{-2.0,-2.0}, {2.0,2.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -2.0}, {stripCenterXPosition[lowGoodStripIndex], 2.0}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, ymin,ymax},{"lowGain", leftLowGainX,rightLowGainX, ymin,ymax}};
};


class BNL_20um_5mm_500um_W3080_StripsGeometry : public DefaultGeometry
// BNL_20um_5mm_500um_W3080
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_5mm_500um_W3080_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,10.44692}, {1,10.61520}, {2,10.50839}, {3,10.54858}, {4,10.39683}, {5,10.58750}, {6,10.42181}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.4; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.433, 0.938, 0.433, -0.062, -0.563, -1.071, -1.562, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -1.80; // Sensor's local frame
    double xmax =  1.80; // Sensor's local frame
    double ymin = -2.25; // Sensor's local frame
    double ymax =  2.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931};
    std::vector<std::vector<double>> sensorEdges = {{-1.70,-2.00}, {1.70,2.00}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -2.00}, {stripCenterXPosition[lowGoodStripIndex], 2.00}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, ymin,ymax},{"lowGain", leftLowGainX,rightLowGainX, ymin,ymax}};
};


class BNL_30um_500x500_SmallSquare_W3104_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_30um_500x500_SmallSquare_W3104 Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_30um_500x500_SmallSquare_W3104_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.475649}, {1,10.597300}, {2,0.0}, {3,10.725462}, {4,10.604304}, {5,10.572591}, {6,10.525313}, {7,0.0}};
	double stripWidth = 0.50; 
    double pitch = 0.5;
    double sensorCenter =  -1.025;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.475; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
	double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}};
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}};
    std::vector<std::vector<double>> sensorEdges = {{xmin, ymin}, {xmax, ymax}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{xmin, ymin}, {xmax, ymax}};
};


class BNL_20um_500x500_SmallSquare_W3080_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_20um_500x500_SmallSquare_W3080 Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_20um_500x500_SmallSquare_W3080_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.511177}, {1,10.621432}, {2,0.0}, {3,10.752771}, {4,10.651117}, {5,10.613118}, {6,10.549674}, {7,0.0}};
    double stripWidth = 0.50; 
    double pitch = 0.5;
    double sensorCenter = -1.025;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.475; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.25}, {0.50, 0.25}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{-0.50, -0.25}, {0.50, 0.25}};
};

class BNL_30um_500x500_LargeSquare_W3104_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_30um_500x500_LargeSquare_W3104  Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_30um_500x500_LargeSquare_W3104_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.449868}, {1,10.578475}, {2,0.0}, {3,10.697433}, {4,10.591534}, {5,10.563197}, {6,10.488916}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -0.875;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.25; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.20;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{xmin, ymin}, {xmax, ymax}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{xmin, ymin}, {xmax, ymax}};

};

class BNL_20um_500x500_LargeSquare_W3080_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_20um_500x500_LargeSquare_W3080  Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_20um_500x500_LargeSquare_W3080_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.509198}, {1,10.626718}, {2,0.0}, {3,10.750338}, {4,10.653928}, {5,10.615395}, {6,10.550804}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -0.95;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.30; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.25}, {0.50, 0.25}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{-0.50, -0.25}, {0.50, 0.25}};

};

class BNL_30um_500x500_SquaredCircle_W3104_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_30um_500x500_SquaredCircle_W3104 Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_30um_500x500_SquaredCircle_W3104_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.452788}, {1,10.572580}, {2,0.0}, {3,10.697640}, {4,10.578140}, {5,10.553696}, {6,10.437773}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -1.025;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.3; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{xmin, ymin}, {xmax, ymax}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{xmin, ymin}, {xmax, ymax}};

};


class BNL_20um_500x500_SquaredCircle_W3080_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_20um_500x500_SquaredCircle_W3080 Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_20um_500x500_SquaredCircle_W3080_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.496743}, {1,10.615338}, {2,0.0}, {3,10.706889}, {4,10.646108}, {5,10.606342}, {6,10.485968}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -0.85;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.32; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.25}, {0.50, 0.25}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{-0.50, -0.25}, {0.50, 0.25}};

};


class BNL_30um_500x500_Cross_W3104_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_30um_500x500_Cross_W3104_PixelsGeometry Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_30um_500x500_Cross_W3104_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.450841}, {1,10.591952}, {2,0.0}, {3,10.711292}, {4,10.605504}, {5,10.569321}, {6,10.504950}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -1.05;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.12; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{xmin, ymin}, {xmax, ymax}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{xmin, ymin}, {xmax, ymax}};

};


class BNL_20um_500x500_Cross_W3080_PixelsGeometry : public DefaultGeometry
{
public:
    // BNL_20um_500x500_Cross_W3080_PixelsGeometry Mapping set
    // Used lecroy scope channels 0-7
    // ----- -----
	// |  2  |
    // |0 1 3|               -----
    // |6 5 4|               |777|
    // ----- -----           |777|
    //                       -----
    //
    BNL_20um_500x500_Cross_W3080_PixelsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,2}}, {1,{0,1}}, {2,{3,0}}, {3,{0,0}}, {4,{1,0}}, {5,{1,1}}, {6,{1,2}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{3,1,0}, {4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,true}, {4,true}, {5, true}, {6, true}, {7,false}};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,10.496731}, {1,10.629129}, {2,0.0}, {3,10.761273}, {4,10.649664}, {5,10.614115}, {6,10.537795}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter = -1.0;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.175; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {0.5, 0.0, 0.0, -0.5, -0.5,  0.0, 0.5, 0.0};
	double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = -0.75 - (0.025/2);
	double xmax = 0.75 + (0.025/2);
	double ymin = -0.50;
    double ymax = 0.50;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool usesMay2023Tracker = false;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<std::vector<double>> xSlices = {{1.15, 1.35}, {1.65, 1.85}, {2.05, 2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-0.65, -0.45}, {-1.10, -0.90}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.25}, {0.50, 0.25}};
	std::vector<std::vector<double>> sensorEdgesExtra = {{-0.50, -0.25}, {0.50, 0.25}};

};

//############################ End of 2023 April Test Beam ############################################
//#####################################################################################################


class BNL_50um_1cm_450um_W3051_2_2_StripsGeometry : public DefaultGeometry
// BNL_50um_1cm_450um_W3051_2_2_170V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_50um_1cm_450um_W3051_2_2_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.5604958}, {1,1.4633604}, {2,1.5785752}, {3,1.4528504}, {4,1.5231632}, {5,1.4348996}, {6,1.5287634}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.2; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.2; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {1.514, 1.015, 0.515, 0.015, -0.481, -0.984, -1.487, 0.0}; // Iter1 (10-Factor in xSlope)
    // std::vector<double> stripCenterXPosition = {1.515, 1.016, 0.517, 0.018, -0.481, -0.980, -1.483, 0.0}; // BeginIter2
    std::vector<double> stripCenterXPosition = {1.515, 1.016, 0.516, 0.017, -0.482, -0.982, -1.485, 0.0}; // Iter3
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.03; //  0.06; // 0.06; // 0.00;
    double beta  =  0.00; //  0.00; // 0.00; // 0.00;
    double gamma =  0.00; //  0.00; // 0.00; // 0.00;
    double z_dut =-11.88; //-11.88; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.60; // Sensor's local frame
    double ymax =  5.60; // Sensor's local frame
    double positionRecoMaxPoint = 0.79; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 10.0; // 7.0;
    double signalAmpThreshold = 15.0; // 10.0; // 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -0.778279, 1.003278, -13.493687, 67.667341, -125.846727};
    // std::vector<double> positionRecoPar = {0.250000, -0.759465, 0.416867, -7.052692, 37.772359, -75.441845};
    // std::vector<double> positionRecoPar = {0.250000, -0.767546, 0.725612, -10.787760, 55.640142, -104.849358}; // Iter1
    // std::vector<double> positionRecoPar = {0.250000, -0.786692, 1.097448, -13.641628, 65.104157, -115.965746}; // BeginIter2
    std::vector<double> positionRecoPar = {0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931}; // Iter3
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-2.4, -5.5}, {2.4, 5.5}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};



class BNL_50um_1cm_400um_W3051_1_4_StripsGeometry : public DefaultGeometry
// BNL_50um_1cm_400um_W3051_1_4_160V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_50um_1cm_400um_W3051_1_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,1.5571204}, {1,1.4723113}, {2,1.5837402}, {3,1.4558382}, {4,1.5302476}, {5,1.4469072}, {6,1.5334498}, {7,0.0}};
	// std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = -0.2; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.5; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.531, 1.034, 0.530, 0.032, -0.468, -0.967, -1.469, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.24;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = -18.30;
    double xBinSize = 0.050;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.60; // Sensor's local frame
    double ymax =  5.60; // Sensor's local frame
    double positionRecoMaxPoint = 0.78; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 15.0;
    double signalAmpThreshold = 15.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -0.718665, -0.139214, 1.987639, -8.425333, -2.053463};
	// std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
	std::vector<std::vector<double>> sensorEdges = {{-2.4, -5.5}, {2.4, 5.5}}; // Sensor's local frame
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_50um_1cm_450um_W3052_2_4_StripsGeometry : public DefaultGeometry
// BNL_50um_1cm_450um_W3052_2_4_185V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_50um_1cm_450um_W3052_2_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,1.5689530}, {1,1.4867041}, {2,1.5966171}, {3,1.4800527}, {4,1.5412827}, {5,1.4494462}, {6,1.5337527}, {7,0.0}};
	// std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.1; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.5; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.504, 1.005, 0.498, -0.000, -0.490, -0.995, -1.493, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.48;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = -19.0;
    double xBinSize = 0.050;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.76; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 15.0;
    double signalAmpThreshold = 15.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -0.810944, 1.960402, -28.122023, 158.066782, -313.770118};
	// std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.80}, {1.8, 4.80}}; // Sensor's local frame
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_20um_1cm_400um_W3074_1_4_StripsGeometry : public DefaultGeometry
// BNL_20um_1cm_400um_W3074_1_4_95V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_1cm_400um_W3074_1_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.789}, {1,1.694}, {2,1.753}, {3,1.648}, {4,1.714}, {5,1.643}, {6,1.732}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // -0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.0; // 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.509, 0.994, 0.514, 0.006, -0.492, -0.988, -1.495, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.067;
    double beta  = 2.00;
    double gamma = -0.21;
    double z_dut = -52.14;
    double xBinSize = 0.025;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.20; // Sensor's local frame
    double ymax =  5.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.77; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 7.0; // 15.0;
    double signalAmpThreshold = 7.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.804706, 1.067913, -5.469697, 11.408790};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.95, -5.0}, {1.95, 5.0}};
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_20um_1cm_400um_W3075_1_2_StripsGeometry : public DefaultGeometry
// BNL_20um_1cm_400um_W3075_1_2_80V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_1cm_400um_W3075_1_2_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0, 1.799}, {1, 1.739}, {2, 1.799}, {3, 1.727}, {4, 1.754}, {5, 1.704}, {6, 1.794}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // -0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.0; // 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -1.04;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 160.0;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.20; // Sensor's local frame
    double ymax =  5.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.77; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.916517, 4.915604, -31.770297, 65.944321};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.95, -5.0}, {1.95, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_20um_1cm_450um_W3074_2_1_StripsGeometry : public DefaultGeometry
// BNL_20um_1cm_450um_W3074_2_1_95V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_1cm_450um_W3074_2_1_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.821}, {1,1.751}, {2,1.820}, {3,1.737}, {4,1.769}, {5,1.710}, {6,1.798}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // -0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.0; // 2.7; // Lab-Tracker's frame -> -x_dut

    std::vector<double> stripCenterXPosition = {1.553, 1.053, 0.505, 0.032, -0.452, -0.960, -1.449, 0.0};

    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = -0.51;
    double beta  = 2.09;
    double gamma = 1.43;
    double z_dut = -96.46;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.20; // Sensor's local frame
    double ymax =  5.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.77; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.698585, -0.194331, 4.207988, -10.699505};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.95, -5.0}, {1.95, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_20um_1cm_450um_W3075_2_4_StripsGeometry : public DefaultGeometry
// BNL_20um_1cm_450um_W3075_2_4_80V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|             -----
    // | 0 0 0 0 0 |             |777|
    // | 1 1 1 1 1 |             |777|
    // | 2 2 2 2 2 |             -----
    // | 3 3 3 3 3 |
    // | 4 4 4 4 4 |
    // | 5 5 5 5 5 |
    // | 6 6 6 6 6 |
    // |-----------|

    BNL_20um_1cm_450um_W3075_2_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.7733575}, {1,1.7179600}, {2,1.7824067}, {3,1.6949863}, {4,1.7409882}, {5,1.6785454}, {6,1.7660326}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.2; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 0.7; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {1.478, 1.030, 0.490, 0.018, -0.473, -1.019, -1.479, 0.0};
    // std::vector<double> stripCenterXPosition = {1.511, 1.024, 0.509, -0.001, -0.469, -1.001, -1.471, 0.0};
    std::vector<double> stripCenterXPosition = {1.509, 1.025, 0.504, -0.001, -0.467, -1.000, -1.472, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.30; //-0.30; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-6.00; //-6.00; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.20; // Sensor's local frame
    double ymax =  5.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.83; // 0.84;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 7.0;
    double signalAmpThreshold = 15.0; // 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -0.936464, 1.897516, -15.593843, 32.081749};
    // std::vector<double> positionRecoPar = {0.250000, -0.989627, 3.870174, -40.279305, 160.215629, -229.438954};
    // std::vector<double> positionRecoPar = {0.250000, -0.997329, 4.084599, -42.707886, 171.844257, -249.440159};
    // std::vector<double> positionRecoPar = {0.250000, -0.980770, 3.669108, -39.123618, 159.022355, -231.519371};
    std::vector<double> positionRecoPar = {0.250000, -0.806497, 1.475103, -4.704219, 5.096062, -0.764719};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-2.4, -5.5}, {2.4, 5.5}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class BNL_50um_2p5cm_mixConfig1_W3051_1_4_StripsGeometry : public DefaultGeometry
// BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|              -----
    // | 0 0 0 0 0 | <- Config 1  |777|
    // | 1 1 1 1 1 | <- Config 1  |777|
    // | 2 2 2 2 2 | <- Config 1  -----
    // | 3 3 3 3 3 | <- Config 1
    // | 4 4 4 4 4 | <- Config 1
    // | 5 5 5 5 5 | <- Config 2
    // | 6 6 6 6 6 | <- Config 2
    // |-----------|

    BNL_50um_2p5cm_mixConfig1_W3051_1_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.1705073}, {1,1.4564536}, {2,1.2600368}, {3,1.4158836}, {4,1.2403504}, {5,1.4185924}, {6,1.1507471}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100; // Config1 has strips of 100 micron width
    double pitch = 0.500;
    // Center of Config1 + Config2
    double sensorCenter  =-0.4; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    // Only Config1
    // double sensorCenter  = 0.2; // Lab-Tracker's frame ->  y_dut
    // double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {2.181, 1.732, 1.228, 0.726, 0.225, -0.270, -0.770, 0.0}; // Iter1
    std::vector<double> stripCenterXPosition = {2.181, 1.730, 1.236, 0.735, 0.232, -0.264, -0.766, 0.0}; // Iter2
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 3;
    double alpha = -0.25; // -0.21; //-0.21; // 0.00;
    double beta  =  0.00; //  0.00; // 0.00; // 0.00;
    double gamma =  0.00; //  0.00; // 0.00; // 0.00;
    double z_dut =-10.41; //-10.41; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.2;
    double xmin = -2.70; // Sensor's local frame
    double xmax =  2.70; // Sensor's local frame
    double ymin = -13.20; // Sensor's local frame
    double ymax =  13.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.71; // 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 12.0; // 7.0;
    double signalAmpThreshold = 15.0; // 12.0; // 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -0.667970, -9.010738, 112.238851, -643.639801, 1280.390139}; // Iter1
    std::vector<double> positionRecoPar = {0.250000, -0.668684, -8.909631, 109.086460, -614.727996, 1204.484787}; // Iter2
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    // std::vector<std::vector<double>> sensorEdges = {{-2.6, -13.0}, {2.6, 13.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.3, -13.0}, {2.5, 13.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -11.5}, {stripCenterXPosition[lowGoodStripIndex], 11.5}}; // Sensor's local frame
    int centerGoodStripIndex = 2;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -11.5,11.5},{"lowGain", leftLowGainX,rightLowGainX, -11.5,11.5}};
};


class BNL_50um_2p5cm_mixConfig2_W3051_1_4_StripsGeometry : public DefaultGeometry
// BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // 
    // |-----------|              -----
    // | 0 0 0 0 0 | <- Config 1  |777|
    // | 1 1 1 1 1 | <- Config 1  |777|
    // | 2 2 2 2 2 | <- Config 2  -----
    // | 3 3 3 3 3 | <- Config 2
    // | 4 4 4 4 4 | <- Config 2
    // | 5 5 5 5 5 | <- Config 2
    // | 6 6 6 6 6 | <- Config 2
    // |-----------|

    BNL_50um_2p5cm_mixConfig2_W3051_1_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.3716686}, {1,1.2568552}, {2,1.4215433}, {3,1.2103310}, {4,1.3574690}, {5,1.1304036}, {6,1.4516399}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050; // Config2 has strips of 50 micron width
    double pitch = 0.500;
    // Center of Config1 + Config2
    double sensorCenter  =-0.4; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    // Only Config2
    // double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    // double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {0.739, 0.237, -0.259, -0.758, -1.255, -1.748, -2.196, 0.0}; // Iter1
    std::vector<double> stripCenterXPosition = {0.746, 0.245, -0.250, -0.753, -1.244, -1.746, -2.181, 0.0}; // Iter2
    int numLGADchannels = 7;
    int lowGoodStripIndex = 3;
    int highGoodStripIndex = 5;
    double alpha = -0.21; // -0.15; //-0.15; // 0.00;
    double beta  =  0.00; //  0.00; // 0.00; // 0.00;
    double gamma =  0.00; //  0.00; // 0.00; // 0.00;
    double z_dut =-21.33; //-21.33; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.2;
    double xmin = -2.70; // Sensor's local frame
    double xmax =  2.70; // Sensor's local frame
    double ymin = -13.20; // Sensor's local frame
    double ymax =  13.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.71; // 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 12.0; // 7.0;
    double signalAmpThreshold = 15.0; // 12.0; // 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -0.706613, -5.565170, 36.746184, -97.191069}; // Iter1
    std::vector<double> positionRecoPar = {0.250000, -0.709684, -5.430126, 34.929432, -88.611179}; // Iter2
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-2.5, -13.0}, {1.3, 13.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -11.5}, {stripCenterXPosition[lowGoodStripIndex], 11.5}}; // Sensor's local frame
    int centerGoodStripIndex = 4;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -11.5,11.5},{"lowGain", leftLowGainX,rightLowGainX, -11.5,11.5}};
};


class CFD : public DefaultGeometry
{
public:
    // 
    // Used lecroy scope channels 0-7
    // Channel one is spy, channel two is CFD output, and channel 8 is photek

    CFD(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};
    std::vector<std::vector<int>> geometry = {{0,1}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,false}, {3,false}, {4,false}, {5,false}, {6,false}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.62594}, {1,0.038095}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    //double stripWidth = 0.100;
    //double pitch = 0.500;
    double sensorCenter  = 0.0; // Lab-Tracker's frame
    double sensorCenterY = 0.0; // Lab-Tracker's frame
    //std::vector<double> stripCenterXPosition = {2.332, 1.849, 1.339, 0.843, 0.335, -0.195, -0.681, 0.0};
    int numLGADchannels = 2;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 1;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = -2.00;
    double xBinSize = 0.015;
    double yBinSize = 0.015;
    double xmin = -0.2; // Sensor's local frame
    double xmax =  1.5; // Sensor's local frame
    double ymin = -0.2; // Sensor's local frame
    double ymax =  1.5; // Sensor's local frame
    //double positionRecoMaxPoint = 0.77;
    double photekSignalThreshold = 100.0;
    double photekSignalMax = 280.0; //in mV
    double noiseAmpThreshold  = 5.0;
    double signalAmpThreshold = 5.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = false;
    int minPixHits = 4;
    int minStripHits = 12;
    int CFD_threshold = 20;
    std::vector<double> positionRecoPar = {0.250000, -0.610460, -2.619740, 23.242264, -92.980050, 106.189949};
    //std::vector<std::vector<double>> sensorEdges = {{-2.48, 1.15}, {-1.18, 2.45}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-2.35, 0.15}, {-1.05, 1.45}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    //std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5},{"gap", 0.70,0.80, 0.5,2.5},
    //                                              {"hot_ySlice", -1.95,1.95, -1.5,-0.25}, {"cold_ySlice", -1.95,1.95, -4.15,-2.90},
    //                                              {"hotspot", -1.95,1.95, -1.50,-0.50}};
};


class HPK_20um_500x500um_E600_2x2PadGeometry : public DefaultGeometry
// HPK_20um_500x500um_2x2pad_E600_FNAL_105V
{
public:
    // HPK 2022 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0-3 was AC pads on FNAL board, 4 was the same sensor type AC channel on UCSC board, 5-6 were 50D and scope channel 7 was the photek
    // ----- -----
    // |1 0| |4 x|           -----
    // |2 3| |x x|           |777|
    // ----- -----           |777|
    //                       -----
    // 
    HPK_20um_500x500um_E600_2x2PadGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {4, {2,0}}, {5, {2, 1}}, {7,{3,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3}, {4,5},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.9320245},{1,1.9407506}, {2,1.8931535}, {3,1.907246289}, {4,1.7342231}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.450;
    double pitch = 0.500;
    double sensorCenter =-1.05; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-1.875; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha =  0.7;
    double beta  =  0.0;
    double gamma =  0.0;
    double z_dut =-10.0;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 4;
    int minStripHits = 12;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParTop = {-0.494315,  1.28059, 1.92055, -9.89445, 11.8025, -4.01589};
    std::vector<double> positionRecoParBot = {-0.0849671, -3.72958, 25.6829, -63.7924, 70.3368, -28.3888};
    std::vector<double> positionRecoParRight = {-0.046495, -3.91451, 24.6937, -57.5006, 59.3214, -22.163};
    std::vector<double> positionRecoParLeft = {0.0339823, -5.42069, 33.1184, -78.8264, 84.4803, -33.3587};
    std::vector<std::vector<double>> xSlices = {{-1.60, -1.00}, {-1.05, -0.45}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-1.95, -1.35}, {-2.45, -1.85}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.55}, {0.50, 0.50}};
    // std::vector<std::vector<double>> sensorEdgesTight = {{-0.47, -0.48}, {0.47, 0.43}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[2], stripCenterYPosition[2]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesExtra = {{0.57, -0.16}, {0.92, 0.23}}; // {{-0.576, -2.130}, {-0.030, -1.547}};
    // std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.47,-0.05, 0.03, 0.43},{"top_right", 0.07,0.47, 0.03, 0.43},
    //                                                 {"bot_left", -0.47,-0.05, -0.48,-0.09},{"bot_right", 0.07,0.47, -0.48,-0.09}};
};

class HPK_30um_500x500um_E600_2x2PadGeometry : public DefaultGeometry
// HPK_30um_500x500um_2x2pad_E600_FNAL_140V
{
public:
    // HPK 2022 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0-3 was AC pads on FNAL board, 4 was the same sensor type AC channel on UCSC board, 5-6 were 50D and scope channel 7 was the photek
    // ----- -----
    // |1 0| |4 x|           -----
    // |2 3| |x x|           |777|
    // ----- -----           |777|
    //                       -----
    //
    HPK_30um_500x500um_E600_2x2PadGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {4, {2,0}}, {5, {2,1}}, {7,{3,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3}, {4,5},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.8435231}, {1,1.8658946}, {2,1.8200936}, {3,1.8310432}, {4,1.6554349}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.450;
    double pitch = 0.500;
    double sensorCenter =-1.00; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-2.00; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha = -0.70;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =-10.00;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 4;
    int minStripHits = 12;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParTop = {-0.494315,  1.28059, 1.92055, -9.89445, 11.8025, -4.01589};
    std::vector<double> positionRecoParBot = {-0.0849671, -3.72958, 25.6829, -63.7924, 70.3368, -28.3888};
    std::vector<double> positionRecoParRight = {-0.046495, -3.91451, 24.6937, -57.5006, 59.3214, -22.163};
    std::vector<double> positionRecoParLeft = {0.0339823, -5.42069, 33.1184, -78.8264, 84.4803, -33.3587};
    std::vector<std::vector<double>> xSlices = {{-1.55, -0.95}, {-1.05, -0.45}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-2.05, -1.45}, {-2.55, -1.95}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.50, -0.55}, {0.50, 0.50}};
    // std::vector<std::vector<double>> sensorEdgesTight = {{-0.49, -0.48}, {0.46, 0.44}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[2], stripCenterYPosition[2]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesExtra = {{-0.98, -0.03}, {-0.66, 0.29}}; // {{-2.084, -2.130}, {-1.564, -1.610}};
    // std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.49,-0.06, 0.06, 0.44},{"top_right", 0.05,0.46, 0.06, 0.44},
    //                                                 {"bot_left", -0.49,-0.06, -0.48,-0.11},{"bot_right", 0.05,0.46, -0.48,-0.11}};
};

class HPK_50um_500x500um_E600_2x2PadGeometry : public DefaultGeometry
// HPK_50um_500x500um_2x2pad_E600_FNAL_190V
{
public:
    // HPK 2022 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0-3 was AC pads on FNAL board, 4 was the same sensor type AC channel on UCSC board, 5-6 were 50D and scope channel 7 was the photek
    // ----- -----
    // |1 0| |4 x|           -----
    // |2 3| |x x|           |777|
    // ----- -----           |777|
    //                       -----
    //
    HPK_50um_500x500um_E600_2x2PadGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {4,{2,0}}, {5,{2,1}}, {7,{3,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3}, {4,5},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.7194699}, {1,1.7460299}, {2,1.7017298}, {3,1.7091336}, {4,1.5604737}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.450;
    double pitch = 0.500;
    double sensorCenter =-2.15; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-2.25; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha = -0.5;
    double beta  =  0.0;
    double gamma =  0.0;
    double z_dut =-10.0;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.025;
    double yBinSize = 0.025;
    double xBinSize_delay_corr = 0.050;
    double yBinSize_delay_corr = 0.050;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0;
    int minPixHits = 4;
    int minStripHits = 12;
    int CFD_threshold = 50;
    bool isPadSensor = true;
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParTop = {-0.494315,  1.28059, 1.92055, -9.89445, 11.8025, -4.01589};
    std::vector<double> positionRecoParBot = {-0.0849671, -3.72958, 25.6829, -63.7924, 70.3368, -28.3888};
    std::vector<double> positionRecoParRight = {-0.046495, -3.91451, 24.6937, -57.5006, 59.3214, -22.163};
    std::vector<double> positionRecoParLeft = {0.0339823, -5.42069, 33.1184, -78.8264, 84.4803, -33.3587};
    //std::vector<std::vector<double>> sensorEdges = {{-3.5 , -4.0}, { 0.5, 0.0}}; //square interior of pads
    // std::vector<std::vector<double>> sensorEdges = {{-0.6 , -4.75}, { 0.35, -3.8}}; //square interior of pads
    std::vector<std::vector<double>> xSlices = {{-2.70, -2.10}, {-2.20, -1.60}}; // Raw data coordinates
    std::vector<std::vector<double>> ySlices = {{-2.30, -1.70}, {-2.85, -2.25}}; // Raw data coordinates
    std::vector<std::vector<double>> sensorEdges = {{-0.45, -0.50}, {0.45, 0.45}};
    // std::vector<std::vector<double>> sensorEdgesTight = {{-0.48, -0.48}, {0.48, 0.43}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[2], stripCenterYPosition[2]}, {stripCenterXPosition[0], stripCenterYPosition[0]}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesExtra = {{1.17, 0.32}, {1.54, 0.68}}; // {{-1.082, -2.03}, {-0.467, -1.421}};
    // std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.48,-0.04, 0.07, 0.43},{"top_right", 0.07,0.48, 0.07, 0.43},
    //                                                 {"bot_left", -0.48,-0.04, -0.48,-0.10},{"bot_right", 0.07,0.48, -0.48,-0.10}};
};

#endif
