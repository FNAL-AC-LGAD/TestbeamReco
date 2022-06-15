#ifndef Geometry2022_h
#define Geometry2022_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

class EIC_W2_1cm_500um_200um_gap_StripsGeometry : public DefaultGeometry
// EIC_W2_1cm_500up_300uw
{
public:
    // EIC W2 1cm 500um pitch 200um gap size
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channels 1-6 were AC channels, and scope channel 7 was the photek
    // 
    // |---------------|             -----
    // | 0 0 0 0 0 0 0 |             |777|
    // | 0 1 1 1 1 1 0 |             |777|
    // | 0 2 2 2 2 2 0 |             -----
    // | 0 3 3 3 3 3 0 |
    // | 0 4 4 4 4 4 0 |
    // | 0 5 5 5 5 5 0 |
    // | 0 6 6 6 6 6 0 |
    // | 0 0 0 0 0 0 0 |
    // |---------------|

    EIC_W2_1cm_500um_200um_gap_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{0},{1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.300;
    double pitch = 0.500;
    double sensorCenter  =-1.15; // Lab-Tracker's frame
    double sensorCenterY = 2.30; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {0.0, 1.271, 0.769, 0.268, -0.233, -0.729, -1.238, 0.0};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 2;
    int highGoodStripIndex = 5;
    double alpha =-0.49; //-0.48; //-0.47; //-0.47; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-1.97; //-1.25; //-1.97; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin =  -2.5;
    double xmax =   2.5;
    double ymin =  -6.0;
    double ymax =   6.0;
    double positionRecoMaxPoint = 0.72; // 0.74;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 20.0; // 20.0; // 10.0;
    double signalAmpThreshold = 25.0; // 25.0; // 30.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.643829, 8.150092, -117.089379, 675.759294, -1385.358876};
    // std::vector<std::vector<double>> sensorEdges = {{-3.1, -2}, {0.4, 8.1}};
    // std::vector<std::vector<double>> sensorEdges = {{-7.4, -2.8}, {2.6, 0.5}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.8, -2.6}, {0.4, 7.4}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.7, -5.0}, {1.7, 5.0}}; // Sensor's local frame
};

class EIC1cmStripsGeometry : public DefaultGeometry
// EIC_W1_1cm_500up_200uw
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
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

    EIC1cmStripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    // std::map<int, double> amplitudeCorrectionFactor = {{0,0.9398}, {1,0.9619}, {2,0.9845}, {3,0.9794}, {4,1.0186}, {5,1.0318}, {6,1.1004}, {7,1.0}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    //std::map<int, double> timeCalibrationCorrection = {{0,0.83550257}, {1,0.72130393}, {2,0.82432096}, {3,0.71540105}, {4,0.78519213}, {5,0.69938706}, {6,0.82695301}, {7,0.0}};
    // std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  =-0.95; // Lab-Tracker's frame
    double sensorCenterY = 2.7; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.518, 1.014, 0.515, 0.016, -0.483, -0.983, -1.483, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.23; //-0.20; //-0.20; //-0.21; // 0.0;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut =-2.37; //-2.76; //-3.80; // 0.00; // 0.0;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.20; // Sensor's local frame
    double ymax =  5.20; // Sensor's local frame
    double positionRecoMaxPoint = 0.77; // 0.81;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 10.0;
    double signalAmpThreshold = 25.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.496276, -1.074230, 5.910960, -3.311599, -44.637909};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.95, -5.0}, {1.95, 5.0}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.95,1.15, -1.6,-0.30},{"cold", 0.95,1.15, 1.2,2.5},{"gap", 0.75,0.85, 0.4,3.00}};
};

class EIC_W2_1cm_500um_400um_gap_StripsGeometry : public DefaultGeometry
// EIC_W2_1cm_500up_100uw
{
public:
    // EIC W2 1cm 500um pitch 400um gap size
    // Used lecroy scope channels 0-7
    // scope channels 0-6 were AC channels, and scope channel 7 was the photek
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

    EIC_W2_1cm_500um_400um_gap_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  =-1.3; // Lab-Tracker's frame
    double sensorCenterY = 3.1; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.467, 0.971, 0.470, -0.028, -0.524, -1.028, -1.527, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.51; //-0.50; //-0.50; //-0.49; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-2.89; //-1.32; //-0.81; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.80; // 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 10.0;
    double signalAmpThreshold = 25.0; // 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.250000, -0.625186, -0.634565, 4.385245, -11.638048};
    // std::vector<std::vector<double>> sensorEdges = {{-3.1, -2}, {0.4, 8.1}};
    // std::vector<std::vector<double>> sensorEdges = {{-8.0, -3.4}, {2.0, 0.6}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-3.4, -2.0}, {0.6, 8.0}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.9, -5.0}, {1.9, 5.0}}; // Sensor's local frame
};

class EIC1cmStrips100Geometry : public DefaultGeometry
// EIC_W1_1cm_100up_50uw
{
public:
    // EIC W1 1cm long strips 100um pitch
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

    EIC1cmStrips100Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.050;
    double pitch = 0.100;
    double sensorCenter  =-1.150; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {-0.798, -0.996, -1.174, -1.259, -1.377, -1.456, -1.565, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 2;
    int highGoodStripIndex = 5;
    double alpha = 0.00; // -0.719;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
    double xBinSize = 0.01;
    double yBinSize = 0.25;
    double xmin = -1.80; // Sensor's local frame
    double xmax =  1.80; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.82; // ????
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 5.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    // std::vector<std::vector<double>> sensorEdges = {{-2.9, -2.7}, {-1.85, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -2.75}, {2.5, -1.75}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.75, -2.5}, {-1.75, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.60, -4.75}, {-0.60, 5.25}}; // Sensor's local frame
};

class EIC1cmStrips200Geometry : public DefaultGeometry
// EIC_W1_1cm_200up_100uw
{
public:
    // EIC W1 1cm long strips 200um pitch
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

    EIC1cmStrips200Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.200;
    double sensorCenter  =-1.150; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {0.206, 0.003, -0.194, -0.399, -0.594, -0.794, -0.990, 0.0};
    std::vector<double> stripCenterXPosition = {0.202, 0.002, -0.197, -0.398, -0.598, -0.797, -0.996, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.65; //-0.63; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut =-2.75; // 0.00; // 0.00;
    double xBinSize = 0.01;
    double yBinSize = 0.25;
    double xmin = -1.80; // Sensor's local frame
    double xmax =  1.80; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.62; // 0.65;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 5.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<double> positionRecoPar = {0.100000, -0.424306, -2.681402, 92.750123, -1224.286594, 4527.987949};
    // std::vector<std::vector<double>> sensorEdges = {{-2.32, -2.7}, {-0.82, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -2.25}, {2.5, -0.75}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.25, -2.5}, {-0.75, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.10, -4.75}, {0.40, 5.25}}; // Sensor's local frame
};

class EIC1cmStrips300Geometry : public DefaultGeometry
// EIC_W1_1cm_300up_150uw
{
public:
    // EIC W1 1cm long strips 300um pitch
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

    EIC1cmStrips300Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.150;
    double pitch = 0.300;
    double sensorCenter  =-1.150; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {1.347, 1.052, 0.752, 0.452, 0.182, -0.022, -0.223, 0.0};
    std::vector<double> stripCenterXPosition = {1.372, 1.075, 0.776, 0.477, 0.205, 0.003, -0.199, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 3;
    double alpha =-0.65; //-0.65; //-0.66; //-0.55; // 0.00; // -0.719;
    double beta  =-0.03; //-0.61; // 0.00; // 0.00; // 0.00;
    double gamma =-0.02; // 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-1.45; // 0.12; // 0.00; // 0.00; // 0.00;
    double xBinSize = 0.01;
    double yBinSize = 0.25;
    double xmin = -1.80; // Sensor's local frame
    double xmax =  1.80; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.68; // 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 5.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.150000, -0.264595, -6.515409, 92.129057, -569.612996, 1170.771788};
    std::vector<double> positionRecoPar = {0.150000, -0.220915, -8.023320, 111.756525, -672.460155, 1355.795904};
    // std::vector<std::vector<double>> sensorEdges = {{-1.53, -2.7}, {0.40, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -1.5}, {2.5, 0.5}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -2.5}, {0.5, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-0.35, -4.75}, {1.65, 5.25}}; // Sensor's local frame
};

class EIC2p5cmStripsUCSCGeometry : public DefaultGeometry
// EIC_UCSC_2p5cm_500up_200uw
{
public:
    // EIC UCSC 2p5cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photek
    // Note that the first strip is read by two channels, one in each end
    // 
    // |-------------|             -----
    // | 0 0 0 1 1 1 |             |777|
    // | 2 2 2 2 2 2 |             |777|
    // | 3 3 3 3 3 3 |             -----
    // | 4 4 4 4 4 4 |
    // | 5 5 5 5 5 5 |
    // | 6 6 6 6 6 6 |
    // |-------------|

    EIC2p5cmStripsUCSCGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.72933369}, {1,0.84711394}, {2,0.77180697}, {3,0.69436211}, {4,0.62754714}, {5,0.68871500}, {6,0.71286921}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  =-3.65; // Lab-Tracker's frame
    double sensorCenterY = 4.50; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.309, 1.322, 0.819, 0.320, -0.181, -0.683, -1.183, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 2;
    int highGoodStripIndex = 5;
    double alpha = 0.03; // 0.00;
    double beta  = 0.00; // 0.00;
    double gamma = 0.00; // 0.00;
    double z_dut = 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin =-14.00; // Sensor's local frame
    double ymax = 14.00; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 5.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<double> positionRecoPar = {0.250000, -3.064970, 44.030625, -373.430406, 1413.816981, -1939.591395};
    // std::vector<std::vector<double>> sensorEdges = {{-5.5, -15.0}, {0.0, 15.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-17.0, -5.3}, {8.0, -2.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-5.3, -8.0}, {-2.0, 17.0}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.7, -12.5}, {1.7, 12.5}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", -0.35,0.0, -4.0,-1.5},{"cold", -0.35,0.0, -8.0,-5.5},{"gap", -0.5,-0.3, -1.5,2.875}};
};

class EIC2p5cmStripsGeometry : public DefaultGeometry
// EIC_2p5cm_500up_200uw
{
public:
    // EIC 2p5cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0 was DC ring, scope channels 1-6 were AC channels, and scope channel 7 was the photek
    // 
    // |---------------|
    // | 0 0 0 0 0 0 0 |             -----
    // | 0 1 1 1 1 1 0 |             |777|
    // | 0 2 2 2 2 2 0 |             |777|
    // | 0 3 3 3 3 3 0 |             -----
    // | 0 4 4 4 4 4 0 |
    // | 0 5 5 5 5 5 0 |
    // | 0 6 6 6 6 6 0 |
    // | 0 0 0 0 0 0 0 |
    // |---------------|

    EIC2p5cmStripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0},{1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.64464175}, {1,0.64148521}, {2,0.75787912}, {3,0.64381268}, {4,0.74011157}, {5,0.63451148}, {6,0.75850835}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  = 0.05; // Lab-Tracker's frame
    double sensorCenterY = 0.50; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {0.0, 1.202, 0.726, 0.219, -0.272, -0.769, -1.272, 0.0};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 2;
    int highGoodStripIndex = 5;
    double alpha =-0.56; //-0.56; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut=-10.00; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin =-15.00; // Sensor's local frame
    double ymax = 15.00; // Sensor's local frame
    double positionRecoMaxPoint = 0.73;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; //// 10.0; // 7.0; // 10.0; // 7.0; //  5.0; // 5.0;
    double signalAmpThreshold = 25.0; //// 15.0; //15.0; // 15.0; //12.0; // 10.0; // 5.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -1.220763, 9.797696, -75.459288, 151.303936};
    // std::vector<double> positionRecoPar = {0.250000, -0.941941, 5.241489, -45.243161, 101.427658};
    std::vector<double> positionRecoPar = {0.250000, -0.760107, 0.755445, -0.842242, -9.046702};
    // std::vector<std::vector<double>> sensorEdges = {{-2.35, -12.4}, {2.9, 13.5}};
    // std::vector<std::vector<double>> sensorEdges = {{-13.0, -1.5}, {12.0, 2.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -12.0}, {2.0, 13.0}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.75, -12.5}, {1.75, 12.5}}; // Sensor's local frame // THIS IS NOT CONSIDERING GUARD RING
};

class HPKStripsEbWideMetalGeometry : public DefaultGeometry
// HPK_1cm_80up_45uw
{
public:
    // HPK Strips 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0-6 was AC strips, and scope channel 7 was the photek
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

    HPKStripsEbWideMetalGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0964}, {1,1.0696}, {2,0.9857}, {3,1.0522}, {4,1.0450}, {5,0.9765}, {6,0.8284}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,1.0071012}, {1,0.87209195}, {2,0.97262569}, {3,0.87731328}, {4,1.0050380}, {5,0.92962715}, {6,0.90332001}, {7,0.0}};
    double stripWidth = 0.045;
    double pitch = 0.080;
    double sensorCenter  =-2.4; // Lab-Tracker's frame
    double sensorCenterY = 3.2; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {0.271, 0.197, 0.118, 0.037, -0.043, -0.125, -0.216, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex  = 1;
    int highGoodStripIndex = 4;
    double alpha =-0.68; ////-0.66; //-0.66; //-0.66; // -0.70; //-0.80;
    double beta  = 0.00; //// 0.00; // 0.00; // 0.00; //  0.00; // 0.00;
    double gamma = 0.00; //// 0.00; // 0.00; // 0.00; //  0.00; // 0.00;
    double z_dut = 2.39; //// 2.30; // 1.00; //-2.00; //-10.00; // 0.00;
    double xBinSize = 0.01;
    double yBinSize = 0.20;
    double xmin =-0.60; // Sensor's local frame
    double xmax = 0.60; // Sensor's local frame
    double ymin =-5.50; // Sensor's local frame
    double ymax = 5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.60; // 0.63
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 10.0; // 15.0; // 10.0;
    double signalAmpThreshold = 25.0; // 25.0; // 25.0; // 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.04, -0.268695, 0.462989, -12.2277};
    // std::vector<double> positionRecoPar = {0.040000, -0.291368, 0.526470, -5.120203, -62.435080};
    std::vector<double> positionRecoPar = {0.040000, -0.300401, 1.285693, -21.691921, 42.924177};
    // std::vector<std::vector<double>> sensorEdges = {{-0.5, -5.0}, {0.5, 5.0}}; // Sensor's local frame
    // std::vector<std::vector<double>> sensorEdges = {{-8.5, -2.8}, {2.1, -2.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.8, -2.1}, {-2.0, 8.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-0.4, -5.3}, {0.4, 5.3}}; // Sensor's local frame
};

class EIC_W1_0p5cm_500um_300um_gap_1_7_StripsGeometry : public DefaultGeometry
// EIC_W1_0p5cm_500up_200uw_1_7
{
public:
    EIC_W1_0p5cm_500um_300um_gap_1_7_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  =-1.8; //-2.0; // Lab-Tracker's frame
    double sensorCenterY = 2.8; // 2.4; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {1.453, 0.952, 0.446, -0.056, -0.557, -1.048, -1.546, 0.0};
    // std::vector<double> stripCenterXPosition = {1.461, 0.958, 0.453, -0.047, -0.549, -1.042, -1.539, 0.0};
    std::vector<double> stripCenterXPosition = {1.461, 0.958, 0.454, -0.047, -0.546, -1.041, -1.538, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-1.22; ////-1.18; //-1.18; //-1.18; //-1.19; //-1.22; // 0.0;
    double beta  =-1.25; ////-1.83; //-1.44; //-1.78; // 0.00; // 0.00; // 0.0;
    double gamma =-0.32; //// 0.34; //-0.02; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut = 1.91; //// 4.69; // 4.32; // 4.37; // 4.73; // 0.00; // 0.0;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.80; // Sensor's local frame
    double ymax =  2.80; // Sensor's local frame
    double positionRecoMaxPoint = 0.84; // 0.87;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 10.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.25, -0.323138, -9.25501,  71.6547, -170.496};
    // std::vector<double> positionRecoPar = {0.250000, -0.358384, -2.161280, 13.418143, -25.561459};
    std::vector<double> positionRecoPar = {0.250000, -0.356983, -1.978058, 12.067930, -22.871344};
    // std::vector<std::vector<double>> sensorEdges = {{-3.7, 0.5}, {0, 4.8}};
    // std::vector<std::vector<double>> sensorEdges = {{-4.4, -4.0}, {-0.4, 0.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, 0.4}, {0.0, 4.4}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-2.0, -2.4}, {2.0, 2.4}}; // Sensor's local frame
};

class EIC_W1_0p5cm_500um_300um_gap_1_4_StripsGeometry : public DefaultGeometry
// EIC_W1_0p5cm_500up_200uw_1_4
{
public:

    EIC_W1_0p5cm_500um_300um_gap_1_4_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.1770}, {1,1.0961}, {2,1.0516}, {3,0.9551}, {4,0.9751}, {5,0.9202}, {6,0.8865}, {7,1.0}};
    // std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.96398053}, {1,0.84198568}, {2,0.93964217}, {3,0.83790917}, {4,0.88894472}, {5,0.80036949}, {6,0.91889931}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  =-2.0; // Lab-Tracker's frame
    double sensorCenterY = 2.0; // Lab-Tracker's frame
    double xBinSize_delay_corr = 0.05;
    double yBinSize_delay_corr = 0.2;
    // std::vector<double> stripCenterXPosition = {1.475, 0.977, 0.482, -0.018, -0.515, -1.015, -1.513, 0.0};
    // std::vector<double> stripCenterXPosition = {1.480, 0.981, 0.482, -0.017, -0.516, -1.017, -1.517, 0.0};
    std::vector<double> stripCenterXPosition = {1.482, 0.981, 0.482, -0.017, -0.516, -1.018, -1.519, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-1.30; //-1.30; ////-1.30; //-1.30; //-1.30; ////-1.30; //-1.30; //-1.35; // 0.00; // -1.0;
    double beta  = 0.0; ///-2.88; //-2.88; ////-2.36; //-2.25; //-2.20; //// 0.00; // 0.00; // 0.00; // 0.00; // -1.30;
    double gamma = 0.0; ///-0.03; //-0.03; ////-0.03; //-0.03; // 0.00; //// 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut = 2.76; // 3.17; //// 4.50; // 4.62; // 3.64; //// 4.35; // 5.46; // 0.00; // 0.00; // 28.41878;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.50; // Sensor's local frame
    double ymax =  2.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.84; // 0.88;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 15.0; // 10.0;
    double signalAmpThreshold = 25.0; // 15.0; // 10.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.250000, -0.378305, -1.713719, 11.056169, -21.852821};
    // std::vector<double> positionRecoPar = {0.250000, -0.370630, -1.650882, 10.307877, -20.045539};
    // std::vector<double> positionRecoPar = {0.250000, -0.486276, 1.440258, -15.619359, 66.190079, -99.022406}; // 15A 10N
    std::vector<double> positionRecoPar = {0.250000, -0.493802, 1.651379, -17.180369, 69.983728, -100.858147}; // 25A 15N
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, -1.0}, {0, 4.8}};
    // std::vector<std::vector<double>> sensorEdges = {{-4.2, -4.0}, {0.2, 0.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, -0.2}, {0.0, 4.2}}; // Lab-Tracker's frame after rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.0, -2.2}, {2.0, 2.2}}; // Sensor's local frame
    std::vector<std::vector<double>> sensorEdges = {{-1.9, -2.2}, {1.9, 2.2}}; // Sensor's local frame
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", -0.20,0.1, 0.5,1.5},{"cold", -0.20,0.1, -1.7,-0.7},{"gap", -0.35,-0.2, -1.5,0.5}};

};

class BNL_500um_squares_Geometry : public DefaultGeometry
// BNL_?cm_500up_100uw
{
public:

    BNL_500um_squares_Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{1,0}}, {3,{1,1}}, {4,{2,0}},{5,{2,1}}, {7,{3,0}}};    
    std::vector<std::vector<int>> geometry = {{0,1}, {2,3}, {4,5}, {6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true},{5,true},{6,false}, {7,false}};
    // std::map<int, double> amplitudeCorrectionFactor = {{0,1.1770}, {1,1.0961}, {2,1.0516}, {3,0.9551}, {4,0.9751}, {5,0.9202}, {6,0.8865}, {7,1.0}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.96398053}, {1,0.84198568}, {2,0.93964217}, {3,0.83790917}, {4,0.88894472}, {5,0.80036949}, {6,0.91889931}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    double sensorCenter  = 0.0; // Lab-Tracker's frame
    double sensorCenterY = 0.0; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {-0.54, -1.04, -1.54, -2.04, -2.54, -3.04, -3.54, 0.0};
    std::vector<double> stripCenterYPosition = {-0.54, -1.04, -1.54, -2.04, -2.54, -3.04, -3.54, 0.0};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 5;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 28.41878;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -3.00; // Sensor's local frame
    double xmax = -1.00; // Sensor's local frame
    double ymin =  1.00; // Sensor's local frame
    double ymax =  3.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 10.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    std::vector<double> positionRecoPar = {0.25, -0.682406,  12.6055, -257.771,   2476.2, -12142.6,  29452.7, -28032.3};
    std::vector<std::vector<double>> sensorEdges = {{-2.7, 1.4}, {-1, 2.8}}; // Sensor's local frame
};

class BNL2021MediumV2Geometry : public DefaultGeometry
// BNL2021_V2_?cm_150up_80uw
{
public:
    BNL2021MediumV2Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}}; // ???
    std::map<int, double> timeCalibrationCorrection = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,0.0}}; // ???
    double stripWidth = 0.08;
    double pitch = 0.15;
    double sensorCenter  =-1.075; // Lab-Tracker's frame
    double sensorCenterY =-2.325; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {0.461, 0.313, 0.163, 0.011, -0.140, -0.294, -0.448, 0.0};
    std::vector<double> stripCenterXPosition = {0.463, 0.317, 0.165, 0.014, -0.138, -0.290, -0.445, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex  = 1;
    int highGoodStripIndex = 5;
    double alpha = 1.16; //// 1.16; // 1.16; // 1.17; // 1.21; // 0.00;
    double beta  = 0.03; //// 0.03; // 0.03; // 0.00; // 0.00; // 0.00;
    double gamma = 0.00; //// 0.00; // 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-4.15; ////-4.20; //-4.13; //-3.90; // 0.00; // 0.00;
    double xBinSize = 0.02;
    double yBinSize = 0.05;
    double xmin = -0.80; // Sensor's local frame
    double xmax =  0.80; // Sensor's local frame
    double ymin = -1.50; // Sensor's local frame
    double ymax =  1.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold  = 20.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool enablePositionReconstruction = true;
    int minPixHits   = 4;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.075000, -0.126820, -0.546862, 2.919943, -6.478527}; // 2
    std::vector<double> positionRecoPar = {0.075000, -0.119339, -0.663221, 3.508144, -7.475893};
    std::vector<std::vector<double>> sensorEdges = {{-0.575, -1.175}, {0.575, 1.175}}; // 1 // Sensor's local frame
};

class IHEPGeometry : public DefaultGeometry
// IHEP_?cm_150up_80uw
{
public:
    IHEPGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};    
    double stripWidth = 0.08;
    double pitch = 0.15;
    double sensorCenter  =-1.075; // Lab-Tracker's frame
    double sensorCenterY =-2.325; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {-0.68, -0.83, -0.98, -1.13, -1.28, -1.43, -1.58, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.00;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 28.41878;
    double xBinSize = 1.0;
    double yBinSize = 1.0;
    double xmin =-10.00; // Sensor's local frame
    double xmax = 10.00; // Sensor's local frame
    double ymin =-10.00; // Sensor's local frame
    double ymax = 10.00; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 20.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    int minPixHits = 4;
    int minStripHits = 6;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.075, -0.172763, 0.152945, -0.894909, 0.246914};
    std::vector<std::vector<double>> sensorEdges = {{-10.0, 10.0}, {-10., 10.0}}; // Sensor's local frame
};

#endif
