#ifndef Utility_h
#define Utility_h

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
}

#endif
