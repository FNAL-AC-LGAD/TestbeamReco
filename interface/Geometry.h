#ifndef Geometry_h
#define Geometry_h

#include "TestbeamReco/interface/NTupleReader.h"

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

    int numLGADchannels = 6;

    template<typename T> std::vector<std::vector<T>>& remapToLGADgeometry(NTupleReader& tr, std::vector<T> vec, const std::string& name) const
    {
        auto& vecvec = tr.createDerivedVec<std::vector<T>>(name);
    
        for(const auto& row : geometry)
        {
            if(row.size()<2) continue;
    
            vecvec.emplace_back(row.size());
            for(unsigned int i = 0; i < vec.size(); i++)
            {            
                if(std::find(row.begin(), row.end(), i) != row.end())
                {
                    const int index = indexToGeometryMap.at(i)[1];
                    vecvec.back()[index] = vec[i];
                }
            }
        }        
        return vecvec;
    }
};

#endif
