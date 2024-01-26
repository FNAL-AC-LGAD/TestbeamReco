#ifndef Utility_h
#define Utility_h

#include "TestbeamReco/interface/NTupleReader.h"
#include "TLorentzVector.h"
#include "TFile.h"
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

        const auto& acLGADChannelMap = tr.getVar<std::map<int, bool>>("acLGADChannelMap");
        const auto& extraChannelIndex  = tr.getVar<int>("extraChannelIndex");

        for(const auto& row : geometry)
        {
            if(row.size()<2) continue;

            int vecSize = (std::find(row.begin(), row.end(), extraChannelIndex) != row.end()) ? 1 : row.size();
            vecvec.emplace_back(vecSize);
            for(unsigned int i = 0; i < vec.size(); i++)
            {
                // Make sure the extra channel is alone
                if(!acLGADChannelMap.at(i)) continue;
                if(std::find(row.begin(), row.end(), i) != row.end())
                {
                    const int index = indexToGeometryMap.at(i)[1];
                    vecvec.back()[index] = vec[i];
                }
            }
        }        
        return vecvec;
    }

    template<typename T> std::pair<int,int> findNthRankChannel(const std::vector<std::vector<T>>& channels, unsigned int rank, T extraChannel)
    {
        typedef std::tuple<T,int,int> TPL;
        std::vector<TPL> vecInfo;
        for(unsigned int i = 0; i < channels.size(); i++)
        {
            for(unsigned int j = 0; j < channels[i].size(); j++)
            {
                if(channels[i][j] == extraChannel) continue;
                vecInfo.emplace_back(channels[i][j], i, j);
            }
        }
        std::sort(vecInfo.begin(), vecInfo.end(), [](TPL v1, TPL v2){return std::get<0>(v1) > std::get<0>(v2);} );
        rank = (rank > vecInfo.size()) ? 1 : rank;
        return std::make_pair<int,int>( int(std::get<1>(vecInfo[rank-1])), int(std::get<2>(vecInfo[rank-1])) );
    }

    template<typename T, typename... Args> void makeHisto(std::map<std::string, std::shared_ptr<T>>& map, const std::string& name, const std::string& hName, Args... args)
    {
        map.emplace(name.c_str(), std::make_shared<T>(name.c_str(), (name+hName).c_str(), args...) ) ;
    }

    template<typename T, typename... Args> void fillHisto(const bool pass, std::map<std::string, std::shared_ptr<T>>& map, const std::string& name, Args... args) 
    { 
        try
        {
            if(pass) map.at(name)->Fill(args...);
        }
        catch(std::out_of_range& e)
        {
            throw std::out_of_range(color("Error: Histogram named: \"" + name + "\" not defined", "red"));
        }
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

    template<typename T> std::vector<std::shared_ptr<T>> getHistoFromROOT(const std::string& filename, const std::vector<std::string>& histos)
    {
        TFile* file = TFile::Open(filename.c_str(),"READ");
        std::vector<std::shared_ptr<T>> outVec; 
   
        if(file)
        {
            for (const auto& name : histos)
            {
                T* hist = (T*)file->Get(name.c_str());
                outVec.emplace_back(hist);
            }
        }
        else 
        {
            std::cout<<"ROOT File:\""+filename+"\" not found"<<std::endl;
        }
    
        return outVec; 
    }

    template<typename T> std::shared_ptr<T> getHistoFromROOT(const std::string& filename, const std::string& name)
    {
        TFile* file = TFile::Open(filename.c_str(),"READ");
        std::shared_ptr<T> out; 
   
        if(file)
        {
            out.reset((T*)file->Get(name.c_str()));
        }
        else 
        {
            std::cout<<"ROOT File:\""+filename+"\" not found"<<std::endl;
        }
    
        return out; 
    }

    template<typename T> double getTrackerTimeCorr(double x, double y, double time, uint channel, const std::vector<std::shared_ptr<T>>& histVec)
    {
        double tracker_corr=0;
        //Must check that time !=0, because 0 indicates there was no timestamp assigned by TimingDAQ
        if(time != 0.0 && histVec.size() > 0 && channel < histVec.size())
        {
            auto hist = histVec[channel];
            int ibin = hist->FindBin(x,y);
            int xbin = utility::findBin(hist, x, "X");
            int ybin = utility::findBin(hist, y, "Y");
            tracker_corr = hist->GetBinContent(ibin);
            
            if(tracker_corr==0.0 && xbin >0 && ybin>0)
            {
                tracker_corr = hist->Interpolate(x,y);
            }
        }
        return tracker_corr;    
    }

    template<typename T> double getTrackerTimeCorr(double x, double time, uint channel, const std::vector<std::shared_ptr<T>>& histVec)
    {
        double tracker_corr=0;
        //Must check that time !=0, because 0 indicates there was no timestamp assigned by TimingDAQ
        if(time != 0.0 && histVec.size() > 0 && channel < histVec.size())
        {
            auto hist = histVec[channel];
            int ibin = hist->FindBin(x);
            tracker_corr = hist->GetBinContent(ibin); 
        }
        return tracker_corr;    
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
