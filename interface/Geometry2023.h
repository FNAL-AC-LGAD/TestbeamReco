#ifndef Geometry2023_h
#define Geometry2023_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

//################################## Start Geometry for May - June 2023 HPK Sensors ################################

class HPK_W8_18_2_50T_1P0_500P_100M_C600_StripsGeometry: public DefaultGeometry
// HPK_W8_18_2_50T_1P0_500P_100M_C600
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
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.59239}, {1,0.48878}, {2,0.62067}, {3,0.46903}, {4,0.50387}, {5,0.45182}, {6,0.55730}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.45; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.5; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.493, 0.998, 0.491, -0.010, -0.505, -1.006, -1.503, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.050;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.7;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 3;
    int minStripHits = 8;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -1.055097, -3.113738, 57.919697, -403.222963, 841.444532};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class HPK_W8_17_2_50T_1P0_500P_50M_C600_StripsGeometry: public DefaultGeometry
// HPK_W8_17_2_50T_1P0_500P_50M_C600
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.59175}, {1,0.49570}, {2,0.62982}, {3,0.47298}, {4,0.51059}, {5,0.45010}, {6,0.55854}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.45; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.5; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.526, 1.029, 0.531, 0.027, -0.472, -0.974, -1.476, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.050;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.70;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -1.213789, 3.678867, -54.268217, 382.442724, -1097.795614};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class HPK_W4_17_2_50T_1P0_500P_50M_C240_StripsGeometry: public DefaultGeometry
// HPK_W4_17_2_50T_1P0_500P_50M_C240
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.63438}, {1,0.44968}, {2,0.65954}, {3,0.44812}, {4,0.53521}, {5,0.40685}, {6,0.59025}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.8; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.6; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.527, 1.028, 0.529, 0.025, -0.474, -0.974, -1.474, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.050;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.70;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -1.056368, -4.804256, 60.238713, -287.587925, 281.601725};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};

class HPK_W5_17_2_50T_1P0_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W5_17_2_50T_1P0_500P_50M_E600
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.55468}, {1,0.41259}, {2,0.58763}, {3,0.41236}, {4,0.46534}, {5,0.37535}, {6,0.51170}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.7; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.25; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.528, 1.029, 0.529, 0.027, -0.474, -0.973, -1.473, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
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
	std::vector<double> positionRecoPar = {0.250000, -0.647481, 0.481948, -6.927496, 33.961854, -58.405273};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.56521}, {1,0.41653}, {2,0.59702}, {3,0.41189}, {4,0.47170}, {5,0.37968}, {6,0.51752}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.75; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.25; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {1.525, 1.024, 0.526, 0.027, -0.471, -0.970, -1.470, 0.0};
    // std::vector<double> stripCenterXPosition = {1.522, 1.023, 0.525, 0.025, -0.472, -0.972, -1.471, 0.0};
    std::vector<double> stripCenterXPosition = {1.507, 1.007, 0.508, 0.008, -0.491, -0.991, -1.492, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.72; //-0.72; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut = 2.22; // 0.00; // 0.00;
    double xBinSize = 0.050; // 0.025;
    double yBinSize = 0.1;
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
    // std::vector<double> positionRecoPar = {0.250000, -0.759111, 2.720336, -28.817118, 125.689631, -198.288382};
    // std::vector<double> positionRecoPar = {0.250000, -0.749650, 2.469930, -26.721903, 118.830073, -190.862811};
    std::vector<double> positionRecoPar = {0.250000, -0.693443, 0.894506, -9.526453, 38.944962, -58.650584};
    std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};

class HPK_W9_15_2_20T_1P0_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_15_2_20T_1P0_500P_50M_E600
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	//std::map<int, double> timeCalibrationCorrection = {{0,0.70926}, {1,0.58994}, {2,0.79739}, {3,0.59987}, {4,0.67658}, {5,0.57114}, {6,0.74408}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.70191}, {1,0.59132}, {2,0.78101}, {3,0.60026}, {4,0.67723}, {5,0.57176}, {6,0.74621}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = 0.5; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
	//std::vector<double> stripCenterXPosition = {1.471, 0.971, 0.468, -0.032, -0.528, -1.030, -1.527, 0.0};
	std::vector<double> stripCenterXPosition = {1.459, 0.963, 0.460, -0.042, -0.539, -1.042, -1.540, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =   -0.487;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  -1.171;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 7.0;
    double signalAmpThreshold = 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	//std::vector<double> positionRecoPar = {0.250000, -0.670131, 0.466044, -3.932996, 18.001662, -35.438068};
	std::vector<double> positionRecoPar = {0.250000, -0.629151, -0.330539, 2.348626, -4.694552, -3.942263};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class HPK_W9_14_2_20T_1P0_500P_100M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_14_2_20T_1P0_500P_100M_E600
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
	//std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.79685}, {1,0.63699}, {2,0.84518}, {3,0.63102}, {4,0.71232}, {5,0.58215}, {6,0.75795}, {7,0.0}};
	double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.75; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.5; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.525, 1.024, 0.527, 0.025, -0.472, -0.973, -1.470, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    double xmin = -2.50; // Sensor's local frame
	double xmax =  2.50; // Sensor's local frame
	double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 7.0;
    double signalAmpThreshold = 7.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -0.607455, 0.920900, -10.655371, 50.536797, -94.554720};
	std::vector<std::vector<double>> sensorEdges = {{-1.8, -4.70}, {1.8, 4.70}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
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
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.70583}, {1,0.64872}, {2,0.72512}, {3,0.62405}, {4,0.59587}, {5,0.55577}, {6,0.64927}, {7,0.0}};
    double stripWidth = 0.060;
    double pitch = 0.080;
    double sensorCenter  = 0.30; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.5; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {1.524, 1.027, 0.529, 0.024, -0.474, -0.976, -1.477, 0.0};
    // std::vector<double> stripCenterXPosition = {0.248, 0.169, 0.086, 0.008, -0.071, -0.150, -0.233, 0.0};
    std::vector<double> stripCenterXPosition = {0.212, 0.132, 0.051, -0.028, -0.108, -0.189, -0.269, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.92; //-0.92; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut =-3.63; // 0.00; // 0.00;
    double xBinSize = 0.020; // 0.050;
    double yBinSize = 0.100;
    double xBinSize_delay_corr = 0.020;
    double yBinSize_delay_corr = 0.200;
    double xmin = -0.50; // Sensor's local frame
    double xmax =  0.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.62; // 0.56;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -1.219936, 3.779402, -54.194809, 377.018165, -1084.775117};
    // std::vector<double> positionRecoPar = {0.040000, -2.030627, 57.870271, -633.526041};
    std::vector<double> positionRecoPar = {0.040000, -0.336709, 3.029055, -63.405274, 597.812604, -2488.253914};
    std::vector<std::vector<double>> sensorEdges = {{-0.45, -4.70}, {0.45, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
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
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.85921}, {1,0.80977}, {2,0.92397}, {3,0.80973}, {4,0.79924}, {5,0.73829}, {6,0.87987}, {7,0.0}};
    double stripWidth = 0.060;
    double pitch = 0.080;
    double sensorCenter  = 0.42; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 1.0; // Lab-Tracker's frame -> -x_dut
    // std::vector<double> stripCenterXPosition = {1.524, 1.027, 0.529, 0.024, -0.474, -0.976, -1.477, 0.0};
    // std::vector<double> stripCenterXPosition = {0.262, 0.180, 0.101, 0.018, -0.061, -0.142, -0.221, 0.0};
    std::vector<double> stripCenterXPosition = {0.239, 0.159, 0.079, 0.001, -0.080, -0.160, -0.242, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.59; //-0.59; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut =-2.06; // 0.00; // 0.00;
    double xBinSize = 0.020; // 0.050;
    double yBinSize = 0.100;
    double xBinSize_delay_corr = 0.020;
    double yBinSize_delay_corr = 0.200;
    double xmin = -0.50; // Sensor's local frame
    double xmax =  0.50; // Sensor's local frame
    double ymin = -5.25; // Sensor's local frame
    double ymax =  5.25; // Sensor's local frame
    double positionRecoMaxPoint = 0.62; // 0.59;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -1.219936, 3.779402, -54.194809, 377.018165, -1084.775117};
    // std::vector<double> positionRecoPar = {0.040000, -1.297072, 68.471126, -2036.256046, 25826.743142, -117157.858167};
    std::vector<double> positionRecoPar = {0.040000, -0.220255, -0.639081, -3.339341, 116.405885, -847.047372};
    std::vector<std::vector<double>> sensorEdges = {{-0.45, -4.70}, {0.45, 4.70}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    int centerGoodStripIndex = 3;
    double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
    double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
    double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
    double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
    std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};


class HPK_W9_15_4_20T_0P5_500P_50M_E600_StripsGeometry: public DefaultGeometry
// HPK_W9_15_4_20T_0P5_500P_50M_E600
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
    //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
	std::map<int, double> timeCalibrationCorrection = {{0,0.62441}, {1,0.52250}, {2,0.66163}, {3,0.51899}, {4,0.54160}, {5,0.49432}, {6,0.58235}, {7,0.0}};
	double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  = -0.7; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = -1.3; // Lab-Tracker's frame -> -x_dut
	std::vector<double> stripCenterXPosition = {1.502, 1.005, 0.505, 0.006, -0.494, -0.994, -1.494, 0.0};
	int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =  0.00;
    double beta  =  0.00;
    double gamma =  0.00;
    double z_dut =  0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.1;
    //double xBinSize_delay_corr = 0.05;
	//double yBinSize_delay_corr = 0.1;
	double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.75; // Sensor's local frame
    double ymax =  2.75; // Sensor's local frame
    double positionRecoMaxPoint = 0.90;
    double photekSignalThreshold = 150.0;
    double noiseAmpThreshold  = 15.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
	std::vector<double> positionRecoPar = {0.250000, -0.540399, 0.612133, -5.831108, 20.771927, -25.098450};
	std::vector<std::vector<double>> sensorEdges = {{-1.80, -2.35}, {1.80, 2.45}}; // Sensor's local frame 
	std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
	int centerGoodStripIndex = 3;
	double leftHighGainX = stripCenterXPosition[centerGoodStripIndex] - (stripWidth/2);
	double rightHighGainX = stripCenterXPosition[centerGoodStripIndex] + (stripWidth/2);
	double leftLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) - (stripWidth/2);
	double rightLowGainX = stripCenterXPosition[centerGoodStripIndex] - (pitch/2) + (stripWidth/2);
	std::vector<utility::ROI> regionsOfIntrest = {{"highGain", leftHighGainX,rightHighGainX, -4.6,4.6},{"lowGain", leftLowGainX,rightLowGainX, -4.6,4.6}};
};



//################################## End Geometry for May - June 2023 HPK Sensors ################################

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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,false}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.9320245},{1,1.9407506}, {2,1.8931535}, {3,1.907246289}, {4,1.7342231}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter =-1.05; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-1.875; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha =  0.7; // 0.0;
    double beta  =  0.0; // 0.0;
    double gamma =  0.0; // 0.0;
    double z_dut =-10.0; // 0.0;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.05;
    double yBinSize = 0.05;
    double photekSignalThreshold = 50.0;
  double noiseAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
    double signalAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
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
    // std::vector<std::vector<double>> sensorEdges = {{0.45 , -4.4}, { 1.45, -3.4}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdges = {{-0.55 , -0.6}, {0.55, 0.55}};
    std::vector<std::vector<double>> sensorEdgesTight = {{-0.47, -0.48}, {0.47, 0.43}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.47,-0.05, 0.03, 0.43},{"top_right", 0.07,0.47, 0.03, 0.43},
                                                    {"bot_left", -0.47,-0.05, -0.48,-0.09},{"bot_right", 0.07,0.47, -0.48,-0.09}};
    // std::vector<std::vector<double>> sensorEdgesExtra = {{1.6 , -4.0}, { 1.9, -3.7}}; //square interior of pads
    // std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    // std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    // std::vector<std::vector<double>> boxes_XY ={{-6.1, -5.8,10.05, 10.35}};
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,false}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.8435231}, {1,1.8658946}, {2,1.8200936}, {3,1.8310432}, {4,1.6554349}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.5;
    double pitch = 0.5;
    double sensorCenter =-1.0; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-2.0; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha = -0.70; // 0.0;
    double beta  =  0.00; // 0.0;
    double gamma =  0.00; // 0.0;
    double z_dut =-10.00; // 0.0;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.05;
    double yBinSize = 0.05;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
    double signalAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
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
    std::vector<std::vector<double>> sensorEdges = {{-0.55 , -0.6}, {0.55, 0.55}};
    std::vector<std::vector<double>> sensorEdgesTight = {{-0.49, -0.48}, {0.46, 0.44}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.49,-0.06, 0.06, 0.44},{"top_right", 0.05,0.46, 0.06, 0.44},
                                                    {"bot_left", -0.49,-0.06, -0.48,-0.11},{"bot_right", 0.05,0.46, -0.48,-0.11}};
    // std::vector<std::vector<double>> sensorEdgesTight = {{-999.9, -999.9}, {999.9, 999.9}};
    // std::vector<std::vector<double>> sensorEdgesExtra = {{-0.1 , -4.14}, { 0.45, -3.65}}; //square interior of pads
    //std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    //std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    //std::vector<std::vector<double>> boxes_XY ={{-6.1, -5.8,10.05, 10.35}};
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3},{7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,false}, {5, false}, {6, false}, {7,false}};
    int numLGADchannels = 4;
    int extraChannelIndex = 4;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 3;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,0.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.7194699}, {1,1.7460299}, {2,1.7017298}, {3,1.7091336}, {4,1.5604737}, {5,2.0}, {6,2.0}, {7,0.0}};
    double stripWidth = 0.5; 
    double pitch = 0.5;
    double sensorCenter =-2.15; // Lab-Tracker's frame ->  x_dut
    double sensorCenterY =-2.25; // Lab-Tracker's frame -> y_dut
    std::vector<double> stripCenterXPosition = {0.255,-0.255, -0.255, 0.255, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.25, 0.25, -0.25, -0.25, 0.0, 0.0, 0.0, 0.0};
    double alpha = -0.5; // 0.0;
    double beta  =  0.0; // 0.0;
    double gamma =  0.0; // 0.0;
    double z_dut =-10.0; // 0.0;
    double xmin = -0.7;
    double xmax =  0.7;
    double ymin = -0.7;
    double ymax =  0.7;
    double xBinSize = 0.05;
    double yBinSize = 0.05;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
    double signalAmpThreshold = 15.0; // 80.0; // 60.0; // 50.0; // 40.0; // 30.0; // 20.0; // 15.0;
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
    std::vector<std::vector<double>> sensorEdges = {{-0.55 , -0.6}, {0.55, 0.55}};
    std::vector<std::vector<double>> sensorEdgesTight = {{-0.48, -0.48}, {0.48, 0.43}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {  {"top_left", -0.48,-0.04, 0.07, 0.43},{"top_right", 0.07,0.48, 0.07, 0.43},
                                                    {"bot_left", -0.48,-0.04, -0.48,-0.10},{"bot_right", 0.07,0.48, -0.48,-0.10}};
    // std::vector<std::vector<double>> sensorEdgesExtra = {{1.0 , -3.95}, { 1.4, -3.65}}; //square interior of pads
    //std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    //std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    //std::vector<std::vector<double>> boxes_XY ={{-6.1, -5.8,10.05, 10.35}}; 
};

#endif

