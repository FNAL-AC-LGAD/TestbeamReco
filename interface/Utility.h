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

    template<typename T> std::pair<int,int> findNthRankChannel(const std::vector<std::vector<T>>& channels, unsigned int rank)
    {
        typedef std::tuple<T,int,int> TPL;
        std::vector<TPL> vecInfo;
        for(unsigned int i = 0; i < channels.size(); i++)
        {
            for(unsigned int j = 0; j < channels[i].size(); j++)
            {
                vecInfo.emplace_back(channels[i][j], i, j);
            }
        }
        std::sort(vecInfo.begin(), vecInfo.end(), [](TPL v1, TPL v2){return std::get<0>(v1) > std::get<0>(v2);} );
        rank = (rank > vecInfo.size()) ? 1 : rank;
        return std::make_pair<int,int>( int(std::get<1>(vecInfo[rank-1])), int(std::get<2>(vecInfo[rank-1])) );
    }

    template<typename T, typename... Args> void fillHisto(const bool pass, T& histo, Args... args) { if(pass) histo->Fill(args...); }
    template<typename T, typename... Args> void makeHisto(std::map<std::string, std::shared_ptr<T>>& map, const std::string& name, const std::string& hName, Args... args)
    {
        map.emplace(name.c_str(), std::make_shared<T>(name.c_str(), (name+hName).c_str(), args...) ) ;
    }

    template<typename Th, typename Tb> int findBin(const std::shared_ptr<Th>& h, const Tb v, const std::string& axis)
    {
        //Converts overflow to underflow
        int bin = -1;
        if(h)
        {
            if(axis=="X")
            {
                bin = h->GetXaxis()->FindBin(v);
                if( v >= h->GetXaxis()->GetBinUpEdge(h->GetNbinsX()) ) bin = 0;//h->GetNbinsX();
            }
            else if(axis=="Y")
            {
                bin = h->GetYaxis()->FindBin(v);
                if( v >= h->GetYaxis()->GetBinUpEdge(h->GetNbinsY()) ) bin = 0;// h->GetNbinsY();           
            }
        }
        return bin;
    }

    class ROI
    {
    private:
        std::string name_;
        double xmin_;
        double xmax_;
        double ymin_;
        double ymax_;
        
    public:
        ROI(const std::string& name, const double xmin, const double xmax, const double ymin, const double ymax) 
            : name_(name), xmin_(xmin), xmax_(xmax), ymin_(ymin), ymax_(ymax)
        {
        }
        
        bool passROI(const double x, const double y) const { return xmin_ < x && x < xmax_ && ymin_ < y && y < ymax_; }
        const std::string getName() const { return name_; }
    };

}

#endif
