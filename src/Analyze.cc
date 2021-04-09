#define Analyze_cxx
#include "TestbeamReco/interface/Analyze.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>

Analyze::Analyze()
{
}

//Define all your histograms here. 
void Analyze::InitHistos(const std::vector<std::vector<int>>& geometry, const std::map<std::string,double>& sensorConfigMap)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    //Define 1D histograms
    auto xmin = sensorConfigMap.at("xmin");
    auto xmax = sensorConfigMap.at("xmax");
    auto ymin = sensorConfigMap.at("ymin");
    auto ymax = sensorConfigMap.at("ymax");

    int rowIndex = 0;
    for(const auto& row : geometry)
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

    //Per Channel 2D efficiencies
    rowIndex = 0;
    for(const auto& row : geometry) {
      if(row.size()<2) continue;
      for(unsigned int i = 0; i < row.size(); i++) {
	const auto& r = std::to_string(rowIndex);
	const auto& s = std::to_string(i);            
	my_2d_histos.emplace( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
	my_2d_histos.emplace( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
	my_2d_histos.emplace( ("relFrac_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel"+r+s).c_str(), ("relFrac_vs_x_channel"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
	my_2d_histos.emplace( ("relFrac_vs_y_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_y_channel"+r+s).c_str(), ("relFrac_vs_y_channel"+r+s+"; Y [mm]; relFrac").c_str(), (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0 ) );
      }
      rowIndex++;
    }
    
    //Global 2D efficiencies
    my_2d_histos.emplace( "efficiency_vs_xy_highThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_highThreshold_numerator", "efficiency_vs_xy_highThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_lowThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_lowThreshold_numerator", "efficiency_vs_xy_lowThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_denominator", std::make_shared<TH2D>( "efficiency_vs_xy_denominator", "efficiency_vs_xy_denominator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );

    //Define 3D histograms
    rowIndex = 0;
    for(const auto& row : geometry) {
      if(row.size()<2) continue;
      for(unsigned int i = 0; i < row.size(); i++) {
   	const auto& r = std::to_string(rowIndex);
   	const auto& s = std::to_string(i);            
   	my_3d_histos.emplace( ("amplitude_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("amplitude_vs_xy_channel"+r+s).c_str(), ("amplitude_vs_xy_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax, 500,0,500 ) );	
      }
      rowIndex++;
    }
    
    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    my_efficiencies.emplace("event_sel_weight", std::make_shared<TEfficiency>("event_sel_weight","event_sel_weight",9,0,9));
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& sensorConfigMap = tr.getVar<std::map<std::string,double>>("sensorConfigMap");
    InitHistos(geometry, sensorConfigMap);

    while( tr.getNextEvent() )
    {
        //This is added to count the number of events- do not change the next two lines.
        const auto& eventCounter = tr.getVar<int>("eventCounter");
        my_histos["EventCounter"]->Fill( eventCounter );

        //Print Event Number 
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 100000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );
                       
        //Can add some fun code here....try not to calculate too much in this file: use modules to do the heavy caclulations
        //const auto& run = tr.getVar<int>("run");
        const auto& amp = tr.getVec<float>("amp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, amp, "ampLGAD");        

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
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
                                  
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
                    my_2d_histos["relFrac_vs_x_channel"+r+s]->Fill(x, relFrac[i]);
                    my_2d_histos["relFrac_vs_y_channel"+r+s]->Fill(y, relFrac[i]);
                }
                rowIndex++;
            }
        }

	//******************************************************************
	//Time Resolution
	//******************************************************************
	if( ntracks==1 && nplanes>10 && npix>0 ) 
        {
            const auto& LP2_20 = tr.getVec<float>("LP2_20");
            const auto& photekIndex = tr.getVar<int>("photekIndex");
            for(const auto& row : geometry) 
            {
                if(row.size()<2) continue;
                for(unsigned int i = 0; i < row.size(); i++) 
                {
                    //std::cout<<LP2_20[i]<<" "<<LP2_20[photekIndex]<<std::endl;
                }
            }
            //LP2_20[{0}]-LP2_20[{1}]
        }

	//******************************************************************
	//Efficiency
	//******************************************************************

	//Make cuts and fill histograms here
	if( ntracks==1 && nplanes>10 && npix>0 ) {

	  //Require at least 50 mV signal on Photek
	  if (amp[7] > sensorConfigMap.at("photekSignalThreshold")) {
	    my_2d_histos["efficiency_vs_xy_denominator"]->Fill(x,y);

	    bool hasGlobalSignal_highThreshold = false;
	    bool hasGlobalSignal_lowThreshold = false;
	    for(const auto& row : ampLGAD)  {
	      int rowIndex = 0;
	      for(unsigned int i = 0; i < row.size(); i++)  {
		const auto& r = std::to_string(rowIndex);
		const auto& s = std::to_string(i);
		
		if (ampLGAD[rowIndex][i] > sensorConfigMap.at("noiseAmpThreshold")) {
		  my_3d_histos["amplitude_vs_xy_lowThreshold_channel"+r+s]->Fill(x,y,ampLGAD[rowIndex][i]);
		  hasGlobalSignal_lowThreshold = true; 
		  my_2d_histos["efficiency_vs_xy_lowThreshold_numerator_channel"+r+s]->Fill(x,y);		  
		}
				
		if (ampLGAD[rowIndex][i]  > sensorConfigMap.at("signalAmpThreshold") ) {
		  hasGlobalSignal_highThreshold = true; 
		  my_2d_histos["efficiency_vs_xy_highThreshold_numerator_channel"+r+s]->Fill(x,y);
		}

	      }
	      rowIndex++;
	    }

	    if (hasGlobalSignal_lowThreshold) my_2d_histos["efficiency_vs_xy_lowThreshold_numerator"]->Fill(x,y);
	    if (hasGlobalSignal_highThreshold) my_2d_histos["efficiency_vs_xy_highThreshold_numerator"]->Fill(x,y);

	  }
	}

	//******************************************************************


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
    
    for (const auto &p : my_3d_histos) {
        p.second->Write();
    }
    
    for (const auto &p : my_efficiencies) {
        p.second->Write();
    }    
}
