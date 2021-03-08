#ifndef Utility_h
#define Utility_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TLorentzVector.h"
#include <cmath>

namespace utility
{
    double calcDPhi(const double phi1, const double phi2);
    double calcDR(const double eta1, const double eta2, const double phi1, const double phi2);
    double calcMT(const TLorentzVector& lepton, const TLorentzVector& met);
    const std::string color(const std::string& text, const std::string& color);
    std::string split(const std::string& half, const std::string& s, const std::string& h);
    bool compare_pt_TLV(const TLorentzVector& v1, const TLorentzVector& v2);

    template<typename T> T sum2(T v) { return v*v; }
    template<typename T, typename... Args> T sum2(T v, Args... args) { return v*v + sum2(args...); }
    template<typename T, typename... Args> T addInQuad(T v, Args... args) { return sqrt(sum2(v, args...)); }
    
    template<typename T> std::vector<std::vector<T>>& remapToLGADgeometry(NTupleReader& tr, std::vector<T> vec, const std::string& name)
    {
        const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
        const auto& indexToGeometryMap = tr.getVar<std::map<int, std::vector<int>>>("indexToGeometryMap");
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
}

#endif
