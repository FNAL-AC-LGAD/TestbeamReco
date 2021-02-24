#include "TestbeamReco/interface/Utility.h"
#include <math.h>
#include "TSystem.h"

namespace utility
{
    double calcDPhi(const double phi1, const double phi2)
    {
        double dphi = phi1 - phi2 ;
        if ( dphi >  M_PI ) dphi -= 2*M_PI ;
        if ( dphi < -M_PI ) dphi += 2*M_PI ;
        return dphi;
    }
    
    double calcDR(const double eta1, const double eta2, const double phi1, const double phi2)
    {
        const double deta = fabs( eta1 - eta2 ) ;
        double dphi = phi1 - phi2 ;
        if ( dphi > M_PI ) dphi -= 2*M_PI ;
        if ( dphi <-M_PI ) dphi += 2*M_PI ;        
        return sqrt( dphi*dphi + deta*deta ) ;
    }

    double calcMT(const TLorentzVector& lepton, const TLorentzVector& met)
    {
        // Assuming that both lepton and met are massless
        const double mt_sq = 2 * lepton.Pt() * met.Pt() * ( 1-cos(met.Phi()-lepton.Phi()) );
        return sqrt(mt_sq);
    }    

    const std::string color(const std::string& text, const std::string& color)
    {
        std::string c;
        if(color=="red") c = "31";
        else if(color=="green") c = "32";
        else if(color=="yellow") c = "33";
        else if(color=="blue") c = "34";
        else if(color=="white") c = "37";       
        return "\033[1;"+c+"m"+ text +"\033[0m";
    }    

    std::string split(const std::string& half, const std::string& s, const std::string& h)
    {
        if(s.find(h) != std::string::npos)
        {
            std::string token;
            if      ("first"==half) token = s.substr(0, s.find(h));
            else if ("last" ==half) token = s.substr(s.find(h) + h.length(), std::string::npos);            
            return token;
        }
        else
        {
            return s;
        }
    } 

    bool compare_pt_TLV( const TLorentzVector& v1, const TLorentzVector& v2 )
    {
        return ( v1.Pt() > v2.Pt() );
    }
}
