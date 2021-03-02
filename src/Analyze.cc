#define Analyze_cxx
#include "TestbeamReco/interface/Analyze.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/Geometry.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>

Analyze::Analyze()
{
}

//Define all your histograms here. 
void Analyze::InitHistos(const BNL2020Geometry& g)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    //Define 1D histograms
    int rowIndex = 0;
    for(const auto& row : g.geometry)
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++)
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);            
            my_histos.emplace( ("amp"+r+s).c_str(), std::make_shared<TH1D>( ("amp"+r+s).c_str(), ("amp"+r+s).c_str(), 450, -50.0, 400.0 ) ) ;
            my_histos.emplace( ("ampMax"+r+s).c_str(), std::make_shared<TH1D>( ("ampMax"+r+s).c_str(), ("ampMax"+r+s).c_str(), 450, -50.0, 400.0 ) ) ;
            my_histos.emplace( ("relFrac"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac"+r+s).c_str(), ("relFrac"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
        }
        rowIndex++;
    }

    //Define 2D histograms
    my_2d_histos.emplace( "h_njets_HT", std::make_shared<TH2D>( "h_njets_HT", "h_njets_HT", 8, 7, 15, 100, 0, 5000.0 ) );

    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    my_efficiencies.emplace("event_sel_weight", std::make_shared<TEfficiency>("event_sel_weight","event_sel_weight",9,0,9));
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    BNL2020Geometry g;
    InitHistos(g);
    while( tr.getNextEvent() )
    {
        //This is added to count the number of events- do not change the next two lines.
        const auto& eventCounter        = tr.getVar<int>("eventCounter");
        my_histos["EventCounter"]->Fill( eventCounter );

        //Print Event Number 
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 100000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );
                       
        //Can add some fun code here....try not to calculate too much in this file: use modules to do the heavy caclulations
        const auto& run = tr.getVar<int>("run");
        const auto& amp = tr.getVec<float>("amp");
        const auto& ampLGAD = g.remapToLGADgeometry(tr,amp,"ampLGAD");        

        auto maxAmpIter = std::max_element(ampLGAD[0].begin(),ampLGAD[0].end());
        int maxAmpIndex = std::distance(ampLGAD[0].begin(), maxAmpIter);

        double totAmp = 0.0;
        for(auto i : ampLGAD[0]) totAmp +=i;

        std::vector<double> relFrac;
        for(auto i : ampLGAD[0]) relFrac.emplace_back(i/totAmp);

        //const auto& channel = tr.getVecVec<float>("channel");
        //std::cout<<"channel: "<<channel.size()<<" "<<channel[0].size()<<" "<<channel[0][0]<<" "<<channel[1][0]<<" "<<channel[0][1]<<std::endl;

        //Get variables that you want to cut on
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
                                   
        //Make cuts and fill histograms here
        if( ntracks==1 && nplanes>10 && npix>0 ) 
        {
            int rowIndex = 0;
            for(const auto& row : ampLGAD)
            {
                for(unsigned int i = 0; i < row.size(); i++)
                {
                    const auto& r = std::to_string(rowIndex);
                    const auto& s = std::to_string(i);
                    my_histos["amp"+r+s]->Fill(ampLGAD[rowIndex][i], 1.0);
                    if(maxAmpIndex == int(i)) my_histos["ampMax"+r+s]->Fill(ampLGAD[rowIndex][i], 1.0);
                    my_histos["relFrac"+r+s]->Fill(relFrac[i], 1.0);
                }
                rowIndex++;
            }

            my_2d_histos["h_njets_HT"]->Fill( 1.0, 2.0, 1.0 );
        }

        // Example Fill event selection efficiencies
        my_efficiencies["event_sel_weight"]->SetUseWeightedEvents();
        my_efficiencies["event_sel_weight"]->FillWeighted(true,1.0,0);
    } 
}

void Analyze::WriteHistos(TFile* outfile)
{
    outfile->cd();

    for (const auto &p : my_histos) {
        p.second->Write();
    }
    
    for (const auto &p : my_2d_histos) {
        p.second->Write();
    }
    
    for (const auto &p : my_efficiencies) {
        p.second->Write();
    }    
}
