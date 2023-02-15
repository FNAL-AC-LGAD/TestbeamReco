#ifndef Geometry2023_h
#define Geometry2023_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
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
    double xBinSize = 0.025;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.60; // Sensor's local frame
    double ymax =  5.60; // Sensor's local frame
    double positionRecoMaxPoint = 0.79; // 0.79;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 10.0; // 7.0;
    double signalAmpThreshold = 10.0; // 7.0;
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
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -5.5}, {stripCenterXPosition[lowGoodStripIndex], 5.5}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.7; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {1.516, 1.013, 0.514, 0.015, -0.484, -0.985, -1.485, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
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
    std::vector<double> positionRecoPar = {0.250000, -0.592554, 1.695367, -24.201246, 132.757266, -259.853428};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.5, -7.0}, {3.0, 5.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -4.6}, {stripCenterXPosition[lowGoodStripIndex], 4.6}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
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
    double xBinSize = 0.025;
    double yBinSize = 0.2;
    double xmin = -2.70; // Sensor's local frame
    double xmax =  2.70; // Sensor's local frame
    double ymin = -13.20; // Sensor's local frame
    double ymax =  13.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.71; // 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 7.0; // 15.0;
    double signalAmpThreshold = 7.0; // 15.0;
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
    std::vector<std::vector<double>> sensorEdges = {{-2.6, -13.0}, {2.6, 13.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -13.0}, {stripCenterXPosition[lowGoodStripIndex], 13.0}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
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
    double xBinSize = 0.025;
    double yBinSize = 0.2;
    double xmin = -2.70; // Sensor's local frame
    double xmax =  2.70; // Sensor's local frame
    double ymin = -13.20; // Sensor's local frame
    double ymax =  13.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.71; // 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 7.0; // 15.0;
    double signalAmpThreshold = 7.0; // 15.0;
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
    std::vector<std::vector<double>> sensorEdges = {{-2.6, -13.0}, {2.6, 13.0}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdgesTight = {{stripCenterXPosition[highGoodStripIndex], -13.0}, {stripCenterXPosition[lowGoodStripIndex], 13.0}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.90,1.10, -1.5,-0.5},{"cold", 0.90,1.10, -3.5,-2.5}};
};

class HPK_20um_500x500um_E600_2x2PadGeometry : public DefaultGeometry
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,1}}, {1,{0,0}}, {2,{1,0}}, {3,{1,1}}, {4,{2,0}}, {7,{3,0}}};
    std::vector<std::vector<int>> geometry = {{1,0},{2,3}, {4}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5, false}, {6, false}, {7,false}};
    
    int numLGADchannels = 5;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 2;

    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.0},{1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,0.0}}; //{1,10.4797103988649}, {2,10.5140246761814}, {3,10.4517123511449}, {4,10.4652081424981}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.5; 
    double pitch = 0.5;
    double sensorCenter =-2.0;// Lab-Tracker's frame ->  y_dut
    double sensorCenterY = 2.0; // Lab-Tracker's frame -> -x_dut
    std::vector<double> stripCenterXPosition = {-1.5,-2.5, -2.5, -1.5, -1.4, 0.0, 0.0, -2.0};
    //std::vector<double> stripCenterYPosition = {0.0, 10.641, 10.641, 10.141, 10.141, 0.0};
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xmin = 0.0;
    double xmax = 2.0;
    double ymin =  -5.0;
    double ymax = -3.0; 
    double xBinSize = 0.025;
    double yBinSize = 0.2;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 15.0;
    double signalAmpThreshold = 15.0; 
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    bool isPadSensor = true; 
    bool enablePositionReconstruction = false;
    bool enablePositionReconstructionPad = true;
    std::vector<double> positionRecoParTop = {-0.494315,  1.28059, 1.92055, -9.89445, 11.8025, -4.01589};
    std::vector<double> positionRecoParBot = {-0.0849671, -3.72958, 25.6829, -63.7924, 70.3368, -28.3888};
    std::vector<double> positionRecoParRight = {-0.046495, -3.91451, 24.6937, -57.5006, 59.3214, -22.163};
    std::vector<double> positionRecoParLeft = {0.0339823, -5.42069, 33.1184, -78.8264, 84.4803, -33.3587};
    //std::vector<std::vector<double>> sensorEdges = {{-3.5 , -4.0}, { 0.5, 0.0}}; //square interior of pads
    std::vector<std::vector<double>> sensorEdges = {{0.0 , -5.0}, { 2.0, -3.0}}; //square interior of pads
    //std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    //std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    //std::vector<std::vector<double>> boxes_XY ={{-6.1, -5.8,10.05, 10.35}}; 
};

#endif
