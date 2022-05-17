#ifndef Geometry2022_h
#define Geometry2022_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"
#include "TestbeamReco/interface/Utility.h"

class EIC1cmStripsGeometry : public DefaultGeometry
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
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  =-1.0; // Lab-Tracker's frame
    double sensorCenterY = 2.8; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.567, 1.064, 0.568, 0.068, -0.432, -0.932, -1.432, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.20; //-0.20; //-0.20; //-0.21; // 0.0;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut =-2.87; //-2.76; //-3.80; // 0.00; // 0.0;
    double xBinSize = 0.05;
    double yBinSize = 0.2;
    double xmin = -3.00; // Sensor's local frame
    double xmax =  3.00; // Sensor's local frame
    double ymin = -5.00; // Sensor's local frame
    double ymax =  5.00; // Sensor's local frame
    double positionRecoMaxPoint = 0.81;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2; // 4;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.250000, -0.440132, -3.524095, 36.376552, -151.080147, 194.344126};
    std::vector<double> positionRecoPar = {0.250000, -0.412552, -4.392779, 46.140779, -195.436380, 264.025921};
    // std::vector<std::vector<double>> sensorEdges = {{-3.0, -2.0}, {1.0, 7.6}};
    std::vector<std::vector<double>> sensorEdges = {{-2.0, -4.8}, {2.0, 4.8}}; // Sensor's local frame
};

class EIC1cmStrips300Geometry : public DefaultGeometry
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
    // double sensorCenter  =-0.50; // Lab-Tracker's frame
    // double sensorCenterY = 2.25; // Lab-Tracker's frame
    double sensorCenter  =-1.125; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.347, 1.052, 0.752, 0.452, 0.182, -0.022, -0.223, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 3;
    double alpha =-0.65; //-0.65; //-0.66; //-0.55; // 0.00; // -0.719;
    double beta  =-0.03; //-0.61; // 0.00; // 0.00; // 0.00;
    double gamma =-0.02; // 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-1.45; // 0.12; // 0.00; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.25;
    double xmin = -1.65; // Sensor's local frame
    double xmax =  1.65; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.72;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.150000, -0.327752, -3.991644, 54.115327, -354.909392, 762.694132};
    std::vector<double> positionRecoPar = {0.150000, -0.264595, -6.515409, 92.129057, -569.612996, 1170.771788};
    // std::vector<std::vector<double>> sensorEdges = {{-1.53, -2.7}, {0.40, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -1.5}, {2.5, 0.5}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -2.5}, {0.5, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-0.375, -4.75}, {1.625, 5.25}}; // Sensor's local frame
};

class EIC1cmStrips200Geometry : public DefaultGeometry
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
    double sensorCenter  =-1.125; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {0.184, -0.024, -0.218, -0.421, -0.615, -0.817, -1.012, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.00; // -0.719;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.25;
    double xmin = -1.65; // Sensor's local frame
    double xmax =  1.65; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    // std::vector<std::vector<double>> sensorEdges = {{-2.32, -2.7}, {-0.82, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -2.25}, {2.5, -0.75}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.25, -2.5}, {-0.75, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.125, -4.75}, {0.375, 5.25}}; // Sensor's local frame
};

class EIC1cmStrips100Geometry : public DefaultGeometry
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
    double sensorCenter  =-1.125; // Lab-Tracker's frame
    double sensorCenterY = 2.250; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {-0.569, -0.841, -0.994, -1.086, -1.201, -1.301, -1.137, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.00; // -0.719;
    double beta  = 0.00;
    double gamma = 0.00;
    double z_dut = 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.25;
    double xmin = -1.65; // Sensor's local frame
    double xmax =  1.65; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    // std::vector<std::vector<double>> sensorEdges = {{-2.9, -2.7}, {-1.85, 8.0}};
    // std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {1.625, 4.75}}; // Sensor's local frame -> WHOLE SENSOR, INCLUDING CHANNELS NOT READ HERE
    // std::vector<std::vector<double>> sensorEdges = {{-7.5, -2.75}, {2.5, -1.75}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-2.75, -2.5}, {-1.75, 7.5}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.625, -4.75}, {-0.625, 5.25}}; // Sensor's local frame
};

class EIC2p5cmStripsUCSCGeometry : public DefaultGeometry
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
    std::vector<utility::ROI> regionsOfIntrest = {{"hot", 0.0,3.5, -4.5,4.0}};
};

class EIC2p5cmStripsGeometry : public DefaultGeometry
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.64464175}, {1,0.64148521}, {2,0.75787912}, {3,0.64381268}, {4,0.74011157}, {5,0.63451148}, {6,0.75850835}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    double sensorCenter  = 0.05; // Lab-Tracker's frame
    double sensorCenterY = 0.50; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {-2.575, 1.294, 0.745, 0.265, -0.247, -0.739, -1.249, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 2;
    int highGoodStripIndex = 5;
    double alpha =-0.56; //-0.56; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00;
    double z_dut = 0.00; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin =-15.00; // Sensor's local frame
    double ymax = 15.00; // Sensor's local frame
    double positionRecoMaxPoint = 0.73;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 5.0;
    double signalAmpThreshold = 5.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 0;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.25, 0.0262564, -8.09758,  12.3003, -11.0584};
    std::vector<double> positionRecoPar = {0.250000, -1.220763, 9.797696, -75.459288, 151.303936};
    // std::vector<std::vector<double>> sensorEdges = {{-2.35, -12.4}, {2.9, 13.5}};
    // std::vector<std::vector<double>> sensorEdges = {{-13.0, -1.5}, {12.0, 2.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-1.5, -12.0}, {2.0, 13.0}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-1.75, -12.5}, {1.75, 12.5}}; // Sensor's local frame // THIS IS NOT CONSIDERING GUARD RING
};

class HPKStripsEbWideMetalGeometry : public DefaultGeometry
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
    double sensorCenter  =-2.5; // Lab-Tracker's frame
    double sensorCenterY = 3.0; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {0.383, 0.295, 0.217, 0.133, 0.054, -0.026, -0.124, 0.0};
    std::vector<double> stripCenterXPosition = {0.368, 0.294, 0.215, 0.134, 0.055, -0.028, -0.119, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex  = 1;
    int highGoodStripIndex = 4;
    double alpha =-0.8;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 0.0;
    double xBinSize = 0.01;
    double yBinSize = 0.20;
    double xmin =-1.00; // Sensor's local frame
    double xmax = 1.00; // Sensor's local frame
    double ymin =-5.50; // Sensor's local frame
    double ymax = 5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.61;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.04, -0.268695, 0.462989, -12.2277};
    std::vector<double> positionRecoPar = {0.040000, -0.291368, 0.526470, -5.120203, -62.435080};
    std::vector<std::vector<double>> sensorEdges = {{-0.5, -5.0}, {0.5, 5.0}}; // Sensor's local frame
};

class EIC_W2_1cm_500um_400um_gap_StripsGeometry : public DefaultGeometry
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
    double sensorCenter  =-1.4; // Lab-Tracker's frame
    double sensorCenterY = 3.0; // Lab-Tracker's frame
    // std::vector<double> stripCenterXPosition = {0.2, -0.3, -0.8, -1.3, -1.8, -2.3, -2.8, 0.0};
    std::vector<double> stripCenterXPosition = {1.569, 1.074, 0.576, 0.077, -0.422, -0.926, -1.428, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-0.50; //-0.50; //-0.49; // 0.00;
    double beta  = 0.00; // 0.00; // 0.00; // 0.00;
    double gamma = 0.00; // 0.00; // 0.00; // 0.00;
    double z_dut =-1.32; //-0.81; // 0.00; // 0.00;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -5.50; // Sensor's local frame
    double ymax =  5.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 2;
    int minStripHits = 6;
    int CFD_threshold = 50;
    // std::vector<double> positionRecoPar = {0.25, -0.691307, 0.170215, -0.0131045, -5.13558};
    std::vector<double> positionRecoPar = {0.250000, -0.628293, -0.713219, 4.955132, -13.761265};
    // std::vector<std::vector<double>> sensorEdges = {{-3.1, -2}, {0.4, 8.1}};
    // std::vector<std::vector<double>> sensorEdges = {{-8.0, -3.4}, {2.0, 0.6}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-3.4, -2.0}, {0.6, 8.0}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-2.0, -5.0}, {2.0, 5.0}}; // Sensor's local frame
};

class EIC_W2_1cm_500um_200um_gap_StripsGeometry : public DefaultGeometry
{
public:

    EIC_W2_1cm_500um_200um_gap_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.300;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {0.2, -0.3, -0.8, -1.3, -1.8, -2.3, -2.8, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 5;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0;
    double z_dut = 28.41878;
    double xmin =  -4.0;
    double xmax =   2.0;
    double ymin =  -3.0;
    double ymax =   9.0;
    double positionRecoMaxPoint = 0.75;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    int CFD_threshold = 50;
    std::vector<double> positionRecoPar = {0.25, -0.691307, 0.170215, -0.0131045, -5.13558};
    std::vector<std::vector<double>> sensorEdges = {{-3.1, -2}, {0.4, 8.1}};
};


class EIC_W1_0p5cm_500um_300um_gap_1_7_StripsGeometry : public DefaultGeometry
{
public:
    EIC_W1_0p5cm_500um_300um_gap_1_7_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.200; // 0.200?
    double pitch = 0.500;
    double sensorCenter  =-1.8; //-2.0; // Lab-Tracker's frame
    double sensorCenterY = 2.8; // 2.4; // Lab-Tracker's frame
    std::vector<double> stripCenterXPosition = {1.453, 0.952, 0.446, -0.056, -0.557, -1.048, -1.546, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-1.18; //-1.18; //-1.18; //-1.19; //-1.22; // 0.0;
    double beta  =-1.83; //-1.44; //-1.78; // 0.00; // 0.00; // 0.0;
    double gamma = 0.34; //-0.02; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut = 4.69; // 4.32; // 4.37; // 4.73; // 0.00; // 0.0;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.80; // Sensor's local frame
    double ymax =  2.80; // Sensor's local frame
    double positionRecoMaxPoint = 0.87;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.25, -0.323138, -9.25501,  71.6547, -170.496};
    std::vector<double> positionRecoPar = {0.250000, -0.358384, -2.161280, 13.418143, -25.561459};
    // std::vector<std::vector<double>> sensorEdges = {{-3.7, 0.5}, {0, 4.8}};
    // std::vector<std::vector<double>> sensorEdges = {{-4.4, -4.0}, {-0.4, 0.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, 0.4}, {0.0, 4.4}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-2.0, -2.4}, {2.0, 2.4}}; // Sensor's local frame
};


class EIC_W1_0p5cm_500um_300um_gap_1_4_StripsGeometry : public DefaultGeometry
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
    std::vector<double> stripCenterXPosition = {1.480, 0.981, 0.482, -0.017, -0.516, -1.017, -1.517, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha =-1.30; //-1.30; //-1.30; ////-1.30; //-1.30; //-1.35; // 0.00; // -1.0;
    double beta  =-2.36; //-2.25; //-2.20; //// 0.00; // 0.00; // 0.00; // 0.00; // -1.30;
    double gamma =-0.03; //-0.03; // 0.00; //// 0.00; // 0.00; // 0.00; // 0.00; // 0.0;
    double z_dut = 4.50; // 4.62; // 3.64; //// 4.35; // 5.46; // 0.00; // 0.00; // 28.41878;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin = -2.50; // Sensor's local frame
    double xmax =  2.50; // Sensor's local frame
    double ymin = -2.50; // Sensor's local frame
    double ymax =  2.50; // Sensor's local frame
    double positionRecoMaxPoint = 0.88;
    double photekSignalThreshold = 200.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 10.0;
    bool uses2022Pix = true;
    bool isHorizontal = true;
    bool enablePositionReconstruction = true;
    int minPixHits = 4;
    int minStripHits = 6;
    // std::vector<double> positionRecoPar = {0.250000, -0.378305, -1.713719, 11.056169, -21.852821};
    std::vector<double> positionRecoPar = {0.250000, -0.370630, -1.650882, 10.307877, -20.045539};
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, -1.0}, {0, 4.8}};
    // std::vector<std::vector<double>> sensorEdges = {{-4.2, -4.0}, {0.2, 0.0}}; // Lab-Tracker's frame before rotation
    // std::vector<std::vector<double>> sensorEdges = {{-4.0, -0.2}, {0.0, 4.2}}; // Lab-Tracker's frame after rotation
    std::vector<std::vector<double>> sensorEdges = {{-2.0, -2.2}, {2.0, 2.2}}; // Sensor's local frame
};


class BNL_500um_squares_Geometry : public DefaultGeometry
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
