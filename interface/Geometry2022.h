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
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
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
    double xmin =  -5.5;
    double xmax =  -1.5;
    double ymin =  -5.0;
    double ymax =  15.0;
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
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double stripWidth = 0.045;
    double pitch = 0.080;
    std::vector<double> stripCenterXPosition = {-2.16, -2.24, -2.32, -2.40, -2.48, -2.56, -2.64, 0.0};
    int numLGADchannels = 7;
    double alpha = 0.0;
    double beta  = 0.0;
    double gamma = -0.719 + 90.0;
    double z_dut = 28.41878;
    double xmin =  -3.1;
    double xmax =  -2.0;
    double ymin =  -2.5;
    double ymax =   8.5;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 40.0;
    bool isHPKStrips = true;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.04, -0.258847, -1.18947};
    std::vector<std::vector<double>> sensorEdges = {{-2.7, -1.75}, {-2.1, 8.1}};
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


#endif
