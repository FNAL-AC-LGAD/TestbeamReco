#ifndef Geometry2022_h
#define Geometry2022_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"

class EIC1cmStripsGeometry : public DefaultGeometry
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photok
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
    std::map<int, double> amplitudeCorrectionFactor = {{0,0.9398}, {1,0.9619}, {2,0.9845}, {3,0.9794}, {4,1.0186}, {5,1.0318}, {6,1.1004}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {0.6, 0.1, -0.4, -0.9, -1.4, -1.9, -2.4, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -4.0;
    double xmax =   2.0;
    double ymin =  -3.0;
    double ymax =   9.0;
    double positionRecoMaxPoint = 0.7;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.330948, -6.63994,  53.6787, -134.515};
    std::vector<std::vector<double>> sensorEdges = {{-3.1, -2.5}, {1.1, 8.0}};
};

class EIC1cmStrips300Geometry : public DefaultGeometry
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photok
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
    std::vector<double> stripCenterXPosition = {0.2, -0.1, -0.4, -0.7, -0.95, -1.15, -1.35, 0.00};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = -0.719 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -3.5;
    double xmax =   1.0;
    double ymin =  -3.0;
    double ymax =   7.5;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<std::vector<double>> sensorEdges = {{-1.53, -2.7}, {0.40, 8.0}};
};

class EIC1cmStrips200Geometry : public DefaultGeometry
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photok
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
    std::vector<double> stripCenterXPosition = {-0.95, -1.15, -1.35, -1.55, -1.75, -1.95, -2.15, 0.00};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = -0.719 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -3.5;
    double xmax =   1.0;
    double ymin =  -3.0;
    double ymax =   7.5;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<std::vector<double>> sensorEdges = {{-2.32, -2.7}, {-0.82, 8.0}};
};

class EIC1cmStrips100Geometry : public DefaultGeometry
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photok
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
    std::vector<double> stripCenterXPosition = {-1.95, -2.15, -2.35, -2.45, -2.55, -2.65, -2.75, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = -0.719 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -3.5;
    double xmax =   1.0;
    double ymin =  -3.0;
    double ymax =   7.5;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<std::vector<double>> sensorEdges = {{-2.9, -2.7}, {-1.85, 8.0}};
};

class EIC2p5cmStripsUCSCGeometry : public DefaultGeometry
{
public:
    // EIC W1 1cm long strips 500um pitch 300um gap size
    // Used lecroy scope channels 0-7
    // Scope channel 0-6 was AC channels, and scope channel 7 was the photok
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

    EIC2p5cmStripsUCSCGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.72933369}, {1,0.84711394}, {2,0.77180697}, {3,0.69436211}, {4,0.62754714}, {5,0.68871500}, {6,0.71286921}, {7,0.0}};
    double stripWidth = 0.200;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {-2.33, -2.33, -2.83, -3.33, -3.83, -4.33, -4.83, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xBinSize = 0.05;
    double yBinSize = 0.10;
    double xmin =  -5.5;
    double xmax =  -1.5;
    double ymin = -20.0;
    double ymax =  20.0;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 2.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.589864, 0.930168, -6.40437, 5.39412};
    std::vector<std::vector<double>> sensorEdges = {{-5.5, -20.0}, {0.0, 20.0}};
};

class HPKStripsEbWideMetalGeometry : public DefaultGeometry
{
public:
    // HPK Strips 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0-6 was AC pads, and scope channel 7 was the photok
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
    std::map<int, double> timeCalibrationCorrection = {{0,1.0+0.017836547}, {1,1.0-0.12687069}, {2,1.0-0.029163092}, {3,1.0-0.12144786}, {4,1.0+0.0070835592}, {5,1.0-0.068400721}, {6,1.0-0.098439735}, {7,0.0}};
    double stripWidth = 0.045;
    double pitch = 0.080;
    std::vector<double> stripCenterXPosition = {-2.16, -2.24, -2.32, -2.40, -2.48, -2.56, -2.64, 0.0};
    int numLGADchannels = 7;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = -0.719 + 90.0;
    double z_dut = 28.41878;
    double xBinSize = 0.015;
    double yBinSize = 0.05;
    double xmin =  -2.80;
    double xmax =  -2.05;
    double ymin =  -1.8;
    double ymax =   8.2;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 20.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.04, -0.268695, 0.462989, -12.2277};
    std::vector<std::vector<double>> sensorEdges = {{-2.65, -1.75}, {-2.12, 8.10}};
};

class EIC_W2_1cm_500um_400um_gap_StripsGeometry : public DefaultGeometry
{
public:

    EIC_W2_1cm_500um_400um_gap_StripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.}, {1,1.}, {2,1.}, {3,1.}, {4,1.}, {5,1.}, {6,1.}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.94679459}, {1,0.82059504}, {2,0.92001622}, {3,0.81254756}, {4,0.88364704}, {5,0.79850545}, {6,0.93318906}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {0.2, -0.3, -0.8, -1.3, -1.8, -2.3, -2.8, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 5;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -5.0;
    double xmax =   2.0;
    double ymin =  -3.0;
    double ymax =   9.0;
    double positionRecoMaxPoint = 0.75;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    //std::vector<double> positionRecoPar = {0.25, -0.323138, -9.25501,  71.6547, -170.496};
    std::vector<double> positionRecoPar = {0.25, -0.691307, 0.170215, -0.0131045, -5.13558};
    //std::vector<std::vector<double>> sensorEdges = {{-3.5, -2}, {0.9, 8.2}};
    std::vector<std::vector<double>> sensorEdges = {{-3.0, -1.6}, {0.4, 7.8}};
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
    double stripWidth = 0.100;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {0.15, -0.35, -0.85, -1.35, -1.85, -2.35, -2.85, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -4;
    double xmax =   0.5;
    double ymin =  0.0;
    double ymax =   5.2;
    double positionRecoMaxPoint = 0.75;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 15.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.323138, -9.25501,  71.6547, -170.496};
    std::vector<std::vector<double>> sensorEdges = {{-3.7, 0.5}, {0, 4.8}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.96398053}, {1,0.84198568}, {2,0.93964217}, {3,0.83790917}, {4,0.88894472}, {5,0.80036949}, {6,0.91889931}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {-0.54, -1.04, -1.54, -2.04, -2.54, -3.04, -3.54, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 6;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -4.2;
    double xmax =   0.5;
    double ymin =  -1.0;
    double ymax =   5.2;
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 10.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.682406,  12.6055, -257.771,   2476.2, -12142.6,  29452.7, -28032.3};
    std::vector<std::vector<double>> sensorEdges = {{-4.0, -1.0}, {0, 4.8}};
};


class BNL_500um_squares_Geometry : public DefaultGeometry
{
public:

    BNL_500um_squares_Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{1,0}}, {3,{1,1}}, {4,{2,0}},{5,{2,1}}, {7,{3,0}}};    
    std::vector<std::vector<int>> geometry = {{0,1}, {2,3}, {4,5}, {6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true},{5,true},{6,false}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.1770}, {1,1.0961}, {2,1.0516}, {3,0.9551}, {4,0.9751}, {5,0.9202}, {6,0.8865}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.96398053}, {1,0.84198568}, {2,0.93964217}, {3,0.83790917}, {4,0.88894472}, {5,0.80036949}, {6,0.91889931}, {7,0.0}};
    double stripWidth = 0.100;
    double pitch = 0.500;
    std::vector<double> stripCenterXPosition = {-0.54, -1.04, -1.54, -2.04, -2.54, -3.04, -3.54, 0.0};
    std::vector<double> stripCenterYPosition = {-0.54, -1.04, -1.54, -2.04, -2.54, -3.04, -3.54, 0.0};
    int numLGADchannels = 6;
    int lowGoodStripIndex = 0;
    int highGoodStripIndex = 5;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = 0.0 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -3;
    double xmax =   -1;
    double ymin =  1.0;
    double ymax =   3.5;
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 10.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.25, -0.682406,  12.6055, -257.771,   2476.2, -12142.6,  29452.7, -28032.3};
    std::vector<std::vector<double>> sensorEdges = {{-2.7, 1.4}, {-1, 2.8}};
};

class BNL2021MediumV2Geometry : public DefaultGeometry
{
public:
    BNL2021MediumV2Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{0,1}}, {2,{0,2}}, {3,{0,3}}, {4,{0,4}}, {5,{0,5}}, {6,{0,6}}, {7,{1,0}}};   
    std::vector<std::vector<int>> geometry = {{0,1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0930}, {1,0.9213}, {2,0.9915}, {3,1.0095}, {4,0.9953}, {5,0.9988}, {6,1.0056}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.95666818}, {1,0.96263358}, {2,0.96177595}, {3,0.95310060}, {4,0.95760225}, {5,0.96902361}, {6,0.96389299}, {7,0.0}};    
    double stripWidth = 0.08;
    double pitch = 0.15;
    std::vector<double> stripCenterXPosition = {-0.68, -0.83, -0.98, -1.13, -1.28, -1.43, -1.58, 0.0};
    int numLGADchannels = 7;
    int lowGoodStripIndex = 1;
    int highGoodStripIndex = 5;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma =  1.3;
    double z_dut = 28.41878;
    double xBinSize = 0.02;
    double yBinSize = 0.05;
    double xmin =  -1.8;
    double xmax =  -0.4;
    double ymin =  -3.7;
    double ymax =  -0.8;
    double positionRecoMaxPoint = 0.82;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 20.0;
    double signalAmpThreshold = 20.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.075, -0.172763, 0.152945, -0.894909, 0.246914};
    //std::vector<double> positionRecoPar = {0.075, -0.140285, -0.774667, 5.65837, -13.5359};
    std::vector<std::vector<double>> sensorEdges = {{-1.62, -3.50}, {-0.64, -1.15}};
};

#endif
