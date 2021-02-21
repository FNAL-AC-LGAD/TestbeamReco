#define Analyze_cxx
#include "TestbeamReco/interface/Analyze.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TEfficiency.h>
#include <TRandom3.h>
#include <iostream>
#include <TFile.h>

Analyze::Analyze()
{
    InitHistos();
}

//Define all your histograms here. 
void Analyze::InitHistos()
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    //Define 1D histograms
    my_histos.emplace( "h_njets", std::make_shared<TH1D>( "h_njets", "h_njets", 8, 7, 15 ) ) ;

    //Define 2D histograms
    my_2d_histos.emplace( "h_njets_HT", std::make_shared<TH2D>( "h_njets_HT", "h_njets_HT", 8, 7, 15, 100, 0, 5000.0 ) );

    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    my_efficiencies.emplace("event_sel_weight", std::make_shared<TEfficiency>("event_sel_weight","event_sel_weight",9,0,9));
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    while( tr.getNextEvent() )
    {
        //This is added to count the number of events- do not change the next two lines.
        const auto& eventCounter        = tr.getVar<int>("eventCounter");
        my_histos["EventCounter"]->Fill( eventCounter );

        //Print Event Number 
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 1000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );
        
        //const auto& passBaseline  = tr.getVar<bool>("passBaseline1l_Good");
       
        //Define weight
        double weight = 1.0;
        
        //Make cuts and fill histograms here
        //if( passBaseline ) 
        if( true ) 
        {
            my_histos["h_njets"]->Fill( 1.0, weight ); 
            my_2d_histos["h_njets_HT"]->Fill( 1.0, 2.0, weight );
        }

        // Example Fill event selection efficiencies
        my_efficiencies["event_sel_weight"]->SetUseWeightedEvents();
        my_efficiencies["event_sel_weight"]->FillWeighted(true,weight,0);
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
