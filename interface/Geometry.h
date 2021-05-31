#ifndef Geometry_h
#define Geometry_h

#include "TestbeamReco/interface/NTupleReader.h"

class DefaultGeometry
{
public:
    DefaultGeometry(const int v=0) : voltage(v){}
    virtual ~DefaultGeometry() = default;
    const int voltage;
    class VoltageDependence
    {
    public:
        double noiseAmpThreshold;
        double signalAmpThreshold;
    };

    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}};
    std::vector<std::vector<int>> geometry = {{0}};
    std::map<int, bool> acLGADChannelMap = {{0,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}};
    std::map<int, double> stripCenterXPosition = {{0,0.0}};
    int numLGADchannels = 0;
    int photekIndex = 7;
    double angle = -1;
    double xmin =  -1;
    double xmax =  -1;
    double ymin =  -1;
    double ymax =  -1; 
    double photekSignalThreshold = 50.0; //in mV
    double noiseAmpThreshold = 10.0;      //in mV
    double signalAmpThreshold = 30.0;    //in mV        
    double enablePositionReconstruction = 0.0;   
    double positionRecoPar0 = -1;
    double positionRecoPar1 = -1;
    double positionRecoPar2 = -1;
    double positionRecoPar3 = -1;
    std::vector<std::vector<double>> sensorEdges = {{-999.9, -999.9}, {999.9, 999.9}};
};

class BNL2020Geometry : public DefaultGeometry
{
public:
    // BNL 2020 Mapping
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC strips, and scope channel 7 was the photek
    // -----------------
    // |000000000000000|
    // |0 1 2 3 4 5 6 0|             -----
    // |0 1 2 3 4 5 6 0|             |777|
    // |0 1 2 3 4 5 6 0|             |777|
    // |000000000000000|             -----
    // -----------------
    BNL2020Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1/1.043}, {2,1/1.000}, {3,1/1.078}, {4,1/1.084}, {5,1/1.067}, {6,1/1.017}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0.635, 0.535, 0.435, 0.335, 0.235, 0.135, 0.0};
    int numLGADchannels = 6;
    std::map<int,VoltageDependence> voltageDependenceMap = {{200,{2.0,8.0}}, {210,{3.5,20.0}}, {220,{10.0,30.0}}, {225,{15.0,45.0}}};
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = voltageDependenceMap[voltage].noiseAmpThreshold;
    double signalAmpThreshold = voltageDependenceMap[voltage].signalAmpThreshold; 
    double enablePositionReconstruction = 1.0;   
    double positionRecoPar0 = 0.8129;
    double positionRecoPar1 = -3.599;
    double positionRecoPar2 = 5.735;
    double positionRecoPar3 = -3.166; 
    std::vector<std::vector<double>> sensorEdges = {{-0.1, 9.8}, { 0.8, 11.6}};
};

class BNL2021Geometry : public BNL2020Geometry
{
public:
    // BNL 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC strips, and scope channel 7 was the photok
    // -----------------
    // |000000000000000|
    // |0 1 2 3 4 5 6 0|             -----
    // |0 1 2 3 4 5 6 0|             |777|
    // |0 1 2 3 4 5 6 0|             |777|
    // |000000000000000|             -----
    // -----------------
    BNL2021Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};    
    std::vector<double> stripCenterXPosition = {0.0, 0.635, 0.535, 0.435, 0.335, 0.235, 0.135, 0.0};
    int numLGADchannels = 6;
    double angle = 1.5;
    double xmin = -8;
    double xmax =  -2;
    double ymin =  8;
    double ymax = 13.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    double enablePositionReconstruction = 0.0;   
    double positionRecoPar0 = 0.8129;
    double positionRecoPar1 = -3.599;
    double positionRecoPar2 = 5.735;
    double positionRecoPar3 = -3.166; 
    std::vector<std::vector<double>> sensorEdges = {{-999.9, -999.9}, {999.9, 999.9}};
};

class HPKPadC2Geometry : public DefaultGeometry
{
public:
    // HPK 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-4 was AC pads, 5-6 was the other sensor, and scope channel 7 was the photok
    // ----------
    // |0000000|             -----
    // |0 1 2 0|             |777|
    // |0 4 3 0|             |777|
    // |0000000|             -----
    // ----------
    HPKPadC2Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{2,0}}, {4,{2,1}}, {7,{3,0}}};    
    std::vector<std::vector<int>> geometry = {{0}, {1,2}, {4,3}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0.635, 0.535, 0.435, 0.335, 0.0};
    std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    int numLGADchannels = 4;
    double angle = 0;
    double xmin = -7;
    double xmax =  -4;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 20.0;
    double signalAmpThreshold = 90.0;
    double enablePositionReconstruction = 0.0;   
    double positionRecoPar0 = 0.8129; //hack from BNL for now
    double positionRecoPar1 = -3.599;
    double positionRecoPar2 = 5.735;
    double positionRecoPar3 = -3.166;
};

class HPKPadB2Geometry : public HPKPadC2Geometry
{
public:
    // HPK 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-4 was AC pads, 5-6 was the other sensor, and scope channel 7 was the photok
    // ----------
    // |0000000|             -----
    // |0 1 2 0|             |777|
    // |0 4 3 0|             |777|
    // |0000000|             -----
    // ----------
    HPKPadB2Geometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {7,0.0}};
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
};

class HPKStripsC2WideMetalGeometry : public BNL2020Geometry
{
public:
    // HPK Strips 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC pads, and scope channel 7 was the photok
    // ----------
    // |0000000000000|             -----
    // |0 1 1 1 1 1 0|             |777|
    // |0 2 2 2 2 2 0|             |777|
    // |0 3 3 3 3 3 0|             -----
    // |0 4 4 4 4 4 0|
    // |0 5 5 5 5 5 0|
    // |0 6 6 6 6 6 0|
    // |0000000000000|
    // ----------
    HPKStripsC2WideMetalGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
};

class HPKStripsC2NarrowMetalGeometry : public DefaultGeometry
{
public:
    // HPK Strips 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC pads, and scope channel 7 was the photok
    // ----------
    // |0000000000000|             -----
    // |0 6 6 6 6 6 0|             |777|
    // |0 5 5 5 5 5 0|             |777|
    // |0 4 4 4 4 4 0|             -----
    // |0 3 3 3 3 3 0|
    // |0 2 2 2 2 2 0|
    // |0 1 1 1 1 1 0|
    // |0000000000000|
    // ----------
    HPKStripsC2NarrowMetalGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,5}}, {2,{1,4}}, {3,{1,3}}, {4,{1,2}}, {5,{1,1}}, {6,{1,0}}, {7,{2,0}}};    
    std::vector<std::vector<int>> geometry = {{0}, {6,5,4,3,2,1}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1/1.043}, {2,1/1.000}, {3,1/1.078}, {4,1/1.084}, {5,1/1.067}, {6,1/1.017}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    int numLGADchannels = 6;
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
};

class RonStripsGeometry : public BNL2020Geometry
{
public:
    // Ron Strips 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC strips, and scope channel 7 was the photok
    // -----------------
    // |000000000000000|
    // |0 1 2 3 4 5 6 0|             -----
    // |0 1 2 3 4 5 6 0|             |777|
    // |0 1 2 3 4 5 6 0|             |777|
    // |000000000000000|             -----
    // -----------------
    RonStripsGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
};

class BNLPixelHexGeometry : public DefaultGeometry
{
public:
    // BNL Pixel 2021 Mapping set
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-4 was AC pads, 5-6 was the other sensor, and scope channel 7 was the photok
    // ----------
    // |  1  2 |             -----
    // |0  6  3|             |777|
    // |  5  4 |             |777|
    // ----------            -----
    BNLPixelHexGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{1,{0,0}}, {2,{0,1}}, {0,{1,0}}, {6,{1,1}}, {3,{1,2}}, {5,{2,0}}, {4,{2,1}}, {7,{2,0}}};    
    std::vector<std::vector<int>> geometry = {{1,2}, {0,6,3}, {5,4}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1/1.043}, {2,1/1.000}, {3,1/1.078}, {4,1/1.084}, {5,1/1.067}, {6,1/1.017}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    int numLGADchannels = 6;
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    double strip1AmpCorr = 1.0;
};

#endif
