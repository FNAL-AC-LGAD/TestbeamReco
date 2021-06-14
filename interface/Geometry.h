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
    std::map<int, double> stripCenterYPosition = {{0,0.0}};
    int numLGADchannels = 0;
    int photekIndex = 7;
    double angle =  0.0;
    double xmin =  -1;
    double xmax =  -1;
    double ymin =  -1;
    double ymax =  -1; 
    double positionRecoMaxPoint = 1.0;
    double photekSignalThreshold = 50.0; //in mV
    double noiseAmpThreshold = 10.0;      //in mV
    double signalAmpThreshold = 30.0;    //in mV        
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {-1};
    std::vector<std::vector<double>> sensorEdges = {{-999.9, 999.9}, {-999.9, 999.9}};
    std::vector<std::vector<double>> ySlices = {{-999.9, 999.9}, {-999.9, 999.9}};
    std::vector<std::vector<double>> xSlices = {{-999.9, 999.9}, {-999.9, 999.9}};
    std::vector<std::vector<double>> boxes_XY = {{-999.9, -999.9,-999.9, -999.9}};
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
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.555185226}, {2,10.659094357}, {3,10.647274798}, {4,10.607507832}, {5,10.643264564}, {6,10.662114527}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0.635, 0.535, 0.435, 0.335, 0.235, 0.135, 0.0};
    int numLGADchannels = 6;
    std::map<int,VoltageDependence> voltageDependenceMap = {{200,{2.0,8.0}}, {210,{3.5,20.0}}, {220,{10.0,30.0}}, {225,{15.0,45.0}}};
    double angle = 1.5;
    double xmin = -0.5;
    double xmax =  1.5;
    double ymin =  9.5;
    double ymax = 12.0; 
    double positionRecoMaxPoint = 0.75;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = voltageDependenceMap[voltage].noiseAmpThreshold;
    double signalAmpThreshold = voltageDependenceMap[voltage].signalAmpThreshold; 
    bool enablePositionReconstruction = true;   
    std::vector<double> positionRecoPar = {51.8472, -484.776, 1878.16, -3849.65, 4395.84, -2647.04,  655.29};
    std::vector<std::vector<double>> sensorEdges = {{-0.1, 9.8}, { 0.8, 11.6}};
};

class BNL2021WideGeometry : public DefaultGeometry
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
    BNL2021WideGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0/0.968607463}, {2,1/1.0}, {3,1/0.999778063}, {4,1/1.083394557}, {5,1/1.077968592}, {6,1/1.05618820}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.570712}, {2,10.601730}, {3,10.589803}, {4,10.526534}, {5,10.596760}, {6,10.578494}, {7,0.0}};    
    std::vector<double> stripCenterXPosition = {0.0, -4.68, 4.85, -5.02, -5.20, -5.40, -5.72, 0.0};
    int numLGADchannels = 6;
    double angle = 1.3;
    double xmin = -6.2;
    double xmax = -4.4;
    double ymin =  9.0;
    double ymax =  12.5; 
    double positionRecoMaxPoint = 0.85;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {-10.1932, 82.0107, -254.384, 386.131, -288.176, 84.6899};
    std::vector<std::vector<double>> sensorEdges = {{-6.39, 9.14}, {-3.21, 12.20}};
};

class BNL2021MediumGeometry : public DefaultGeometry
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
    BNL2021MediumGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0/0.844395944}, {2,1.0/1.0}, {3,1.0/0.97974079}, {4,1.0/0.945585703}, {5,1.0/0.93672097}, {6,1.0/0.9387476}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.102707}, {2,10.026717}, {3,10.232438}, {4,10.357673}, {5,10.544784}, {6,10.526426}, {7,0.0}};    
    std::vector<double> stripCenterXPosition = {0.0, -4.60, -4.74, -4.91, -5.06, -5.20, -5.38, 0.0};
    int numLGADchannels = 6;
    double angle =  1.3;
    double xmin =  -5.7;
    double xmax =  -4.3;
    double ymin =   9.0;
    double ymax =  12.5;
    double positionRecoMaxPoint = 0.8;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = { 7.35671, -59.0054, 191.994, -312.627, 254.084, -82.4947};
    std::vector<std::vector<double>> sensorEdges = {{-6.89, 9.14}, {-3.73, 12.20}};
};

class BNL2021NarrowGeometry : public DefaultGeometry
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
    BNL2021NarrowGeometry(const int v=0) : voltage(v){}
    const int voltage;
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0/1.021296378}, {2,1.0/1.0}, {3,1.0/0.990261996}, {4,1.0/1.013760435}, {5,1.0/1.055697466}, {6,1.0/1.127465085}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.007110}, {2,10.348299}, {3,10.365704}, {4,10.390483}, {5,10.374036}, {6,10.417291}, {7,0.0}};    
    std::vector<double> stripCenterXPosition = {0.0, -4.58, -4.72, -4.80, -4.89, -5.00, -5.14, 0.0};
    int numLGADchannels = 6;
    double angle = 1.3;
    double xmin = -5.4;
    double xmax = -4.3;
    double ymin =  9.0;
    double ymax =  12.5;
    double positionRecoMaxPoint = 0.73;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {0.475097, -2.10666, 3.63713, -2.24911};
    std::vector<std::vector<double>> sensorEdges = {{-7.29, 9.18}, {-4.24, 12.25}};
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{2,1}}, {4,{2,0}}, {7,{3,0}}};    
    std::vector<std::vector<int>> geometry = {{0}, {1,2}, {4,3}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.421985}, {2,10.454729}, {3,10.396641}, {4,10.386091}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, -5.50, -6.00, -6.00, -5.50,  0.0};
    std::vector<double> stripCenterYPosition = {0.0, 10.57, 10.57, 10.11, 10.11, 0.0};
    int numLGADchannels = 4;
    double angle = -0.5; 
    double xmin = -6.6;
    double xmax = -5.0;
    double ymin =  9.6;
    double ymax = 11.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 90.0;
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {0.8129, -3.599, 5.735, -3.166};
    std::vector<std::vector<double>> sensorEdges = {{-6.25 , 9.85}, { -5.10, 11.}};
    std::vector<std::vector<double>> ySlices = {{10.05, 10.35}, {10.55, 10.85}};
    std::vector<std::vector<double>> xSlices = {{-6.1, -5.8}, {-5.6, -5.3}};
    std::vector<std::vector<double>> boxes_XY ={{-6.1, -5.8,10.05, 10.35}}; 
};

class HPKPadB2Geometry : public DefaultGeometry
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{2,1}}, {4,{2,0}}, {7,{3,0}}};    
    std::vector<std::vector<int>> geometry = {{0}, {1,2}, {4,3}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.354758}, {2,10.415612}, {3,10.323457}, {4,10.325366}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0}; //will fix this later but code for pad efficiency plots is not fully working
    int numLGADchannels = 4;
    double angle = -1.2;
    double xmin = -6.0;
    double xmax =  -4.8;
    double ymin =  9.55;
    double ymax = 10.8; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 20.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {0.8129, -3.599, 5.735, -3.166};
    std::vector<std::vector<double>> sensorEdges = {{-5.7 , 9.7}, { -4.65, 10.85}};
    std::vector<std::vector<double>> ySlices = {{9.85, 10.15}, {10.35, 10.65}};
    std::vector<std::vector<double>> xSlices = {{-5.55, -5.25}, {-5.05, -4.75}};
    std::vector<std::vector<double>> boxes_XY = { {-6.1, -5.8,10.05, 10.35}}; 
};

class HPKStripsC2WideMetalGeometry : public DefaultGeometry
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};   
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.476853}, {2,10.328344}, {3,10.477243}, {4,10.328026}, {5,10.494593}, {6,10.401719}, {7,0.0}};    
    std::vector<double> stripCenterXPosition = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.0, 0.941, 0.890, 0.822, 0.722, 0.621, 0.544, 0.0};
    int numLGADchannels = 6;
    double angle = -0.2 + 90.0;
    double xmin =   0.2;
    double xmax =   1.2;
    double ymin =   0.0;
    double ymax =   4.3;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;//17.0;
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {0.8129, -3.599, 5.735, -3.166};
    std::vector<std::vector<double>> sensorEdges = {{0.4, 0.5}, {1.0, 4.0}};
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
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.363155}, {2,10.446376}, {3,10.280995}, {4,10.397997}, {5,10.286721}, {6,10.419460}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    std::vector<double> stripCenterYPosition = {0.0, 0.701, 0.599, 0.524, 0.434, 0.351, 0.290, 0.0};
    int numLGADchannels = 6;
    double angle = -0.2 - 90.0;
    double xmin =  -4.5;
    double xmax =   0.0;
    double ymin =  -3.0;
    double ymax =   3.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {0.8129, -3.599, 5.735, -3.166};
    std::vector<std::vector<double>> sensorEdges = {{-4.45, 0.16}, {-0.01, 1.58}};

};

class RonStripsGeometry : public DefaultGeometry
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
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}, {1,{1,0}}, {2,{1,1}}, {3,{1,2}}, {4,{1,3}}, {5,{1,4}}, {6,{1,5}}, {7,{2,0}}};
    std::vector<std::vector<int>> geometry = {{0}, {1,2,3,4,5,6}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,false}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0/1.014141505}, {2,1.0/1.0}, {3,1.0/0.98719996}, {4,1.0/1.018744019}, {5,1.0/0.947666048}, {6,1.0/0.991277675}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.575768}, {2,10.483311}, {3,10.550070}, {4,10.571403}, {5,10.565505}, {6,10.531885}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, -4.785, -4.985, -5.192, -5.412, -5.586, -5.787, 0.0};
    int numLGADchannels = 6;
    double angle = 0.2;
    double xmin = -6.0;
    double xmax = -4.5;
    double ymin =  9.4;
    double ymax =  11.4;
    double positionRecoMaxPoint = 0.79;
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 8.0;
    double signalAmpThreshold = 10.0;
    bool enablePositionReconstruction = true;
    std::vector<double> positionRecoPar = {-0.0254199, 1.50893, -3.51021, 2.08929};
    std::vector<std::vector<double>> sensorEdges = {{-6.60, 9.40}, {-4.44, 11.51}};
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
    std::vector<std::vector<int>> geometry = {{1,2}, {0,6,3}, {5,4}, {7}};
    std::map<int, bool> acLGADChannelMap = {{0,true}, {1,true}, {2,true}, {3,true}, {4,true}, {5,true}, {6,true}, {7,false}};     
    std::map<int, double> amplitudeCorrectionFactor = {{0,1.0}, {1,1.0}, {2,1.0}, {3,1.0}, {4,1.0}, {5,1.0}, {6,1.0}, {7,1.0}};
    std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,0.0}, {2,0.0}, {3,0.0}, {4,0.0}, {5,0.0}, {6,0.0}, {7,0.0}};
    std::vector<double> stripCenterXPosition = {0.0, 0, 0, 0, 0, 0, 0, 0.0};
    std::vector<double> stripCenterYPosition = {0.0, 0, 0, 0, 0, 0, 0, 0.0}; 
    int numLGADchannels = 6;
    double angle = 0.0;
    double xmin = -5.0;
    double xmax =  5.0;
    double ymin = -5.0;
    double ymax =  5.0; 
    double photekSignalThreshold = 50.0;
    double noiseAmpThreshold = 10.0;
    double signalAmpThreshold = 30.0;
    bool enablePositionReconstruction = false;
    std::vector<double> positionRecoPar = {0.8129, -3.599, 5.735, -3.166};
    std::vector<std::vector<double>> sensorEdges = {{-999.9, -999.9}, {999.9, 999.9}};    
};

#endif
