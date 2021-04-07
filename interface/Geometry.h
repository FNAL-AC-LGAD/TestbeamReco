#ifndef Geometry_h
#define Geometry_h

#include "TestbeamReco/interface/NTupleReader.h"

class DefaultGeometry
{
public:
    std::map<int, std::vector<int>> indexToGeometryMap = {{0,{0,0}}};
    std::vector<std::vector<int>> geometry = {{0}};
    std::map<int, bool> acLGADChannelMap = {{0,false}};
    static const int numLGADchannels = 0;
    static const int photekIndex = 0;
    std::map<std::string,double> sensorConfigMap = {
        {"angle", -1},
        {"xmin",  -1},
        {"xmax",  -1},
        {"ymin",  -1},
        {"ymax",  -1}, 
	{"photekSignalThreshold", 50.0}, //in mV
	{"noiseAmpThreshold", 10.0},      //in mV
	{"signalAmpThreshold", 30.0},    //in mV
	
    };   
};

class BNL2020Geometry
{
public:
    // BNL 2020 Mapping
    // Used lecroy scope channels 0-7
    // scope channel 0 was DC ring, scope channel 1-6 was AC strips, and scope channel 7 was the photok
    // -----------------
    // |000000000000000|
    // |0 1 2 3 4 5 6 0|             -----
    // |0 1 2 3 4 5 6 0|             |777|
    // |0 1 2 3 4 5 6 0|             |777|
    // |000000000000000|             -----
    // -----------------
    std::map<int, std::vector<int>> indexToGeometryMap = {
        {0,{0,0}},
        {1,{1,0}},
        {2,{1,1}},
        {3,{1,2}},
        {4,{1,3}},
        {5,{1,4}},
        {6,{1,5}},
        {7,{2,0}},
    };
    
    std::vector<std::vector<int>> geometry = {
        {0},
        {1,2,3,4,5,6},
        {7},
    };

    std::map<int, bool> acLGADChannelMap = {
        {0,false},
        {1,true},
        {2,true},
        {3,true},
        {4,true},
        {5,true},
        {6,true},
        {7,false},        
    };

    static const int numLGADchannels = 6;
    static const int photekIndex = 7;

    std::map<std::string,double> sensorConfigMap = {
        //{"angle", 12.6},
        {"angle", 1.5},
        {"xmin", -0.5},
        {"xmax",  1.5},
        {"ymin",  9.5},
        {"ymax", 12.0}, 
	{"photekSignalThreshold", 50.0},
     	{"noiseAmpThreshold", 10.0},
	{"signalAmpThreshold", 30.0},
    };
};

#endif
