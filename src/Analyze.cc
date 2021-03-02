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

std::map<std::string, double> Analyze::GetSensorConfigMap(std::string sensorName) {

  std::map<std::string,double> myMap;
  myMap["angle"] = 0;
  myMap["xmin"] = 0;
  myMap["xmax"] = 0;
  myMap["ymin"] = 0;
  myMap["ymax"] = 0;

  if (sensorName == "BNL2020") {
    //myMap["angle"] = 12.6;
    myMap["angle"] = 1.5;
    myMap["xmin"] = -0.5;
    myMap["xmax"] = 1.5;
    myMap["ymin"] = 9.5;
    myMap["ymax"] = 12;
  }

  return myMap;

}


std::pair<double,double> Analyze::Rotate(double x0, double y0, double angle) {
  double rad_angle = angle*3.14159/180.;
  double x_rot = x0*cos(rad_angle) + y0*sin(rad_angle);
  double y_rot = y0*cos(rad_angle) - x0*sin(rad_angle);
  return std::pair<double,double>(x_rot,y_rot);
}


//Define all your histograms here. 
void Analyze::InitHistos(const BNL2020Geometry& g)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //Get the config settings for the sensor you want to use
    std::map<std::string,double> sensorConfigMap = GetSensorConfigMap("BNL2020");


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

    //Per Channel 2D efficiencies
    rowIndex = 0;
    for(const auto& row : g.geometry) {
      if(row.size()<2) continue;
      for(unsigned int i = 0; i < row.size(); i++) {
	const auto& r = std::to_string(rowIndex);
	const auto& s = std::to_string(i);            
	my_histos.emplace( ("efficiency_vs_xy_numerator_channel"+r+s).c_str(), std::make_shared<TH1D>( ("amp"+r+s).c_str(), ("amp"+r+s).c_str(), 450, -50.0, 400.0 ) ) ;
	
	my_2d_histos.emplace( ("efficiency_vs_xy_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (sensorConfigMap["xmax"]-sensorConfigMap["xmin"]) / 0.02 ,sensorConfigMap["xmin"],sensorConfigMap["xmax"],(sensorConfigMap["ymax"]-sensorConfigMap["ymin"]) / 0.1 ,sensorConfigMap["ymin"],sensorConfigMap["ymax"] ) );
      }
      rowIndex++;
    }
    
    //Global 2D efficiencies
    my_2d_histos.emplace( "efficiency_vs_xy_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_numerator", "efficiency_vs_xy_numerator; X [mm]; Y [mm]", (sensorConfigMap["xmax"]-sensorConfigMap["xmin"]) / 0.02 ,sensorConfigMap["xmin"],sensorConfigMap["xmax"],(sensorConfigMap["ymax"]-sensorConfigMap["ymin"]) / 0.1,sensorConfigMap["ymin"],sensorConfigMap["ymax"] ) );
    my_2d_histos.emplace( "efficiency_vs_xy_denominator", std::make_shared<TH2D>( "efficiency_vs_xy_denominator", "efficiency_vs_xy_denominator; X [mm]; Y [mm]", (sensorConfigMap["xmax"]-sensorConfigMap["xmin"]) / 0.02 ,sensorConfigMap["xmin"],sensorConfigMap["xmax"],(sensorConfigMap["ymax"]-sensorConfigMap["ymin"]) / 0.1,sensorConfigMap["ymin"],sensorConfigMap["ymax"] ) );


    //Define 3D histograms
    rowIndex = 0;
    for(const auto& row : g.geometry) {
      if(row.size()<2) continue;
      for(unsigned int i = 0; i < row.size(); i++) {
   	const auto& r = std::to_string(rowIndex);
   	const auto& s = std::to_string(i);            
   	my_3d_histos.emplace( ("amplitude_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("amplitude_vs_xy_channel"+r+s).c_str(), ("efficiency_vs_xy_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (sensorConfigMap["xmax"]-sensorConfigMap["xmin"]) / 0.02 ,sensorConfigMap["xmin"],sensorConfigMap["xmax"],(sensorConfigMap["ymax"]-sensorConfigMap["ymin"]) / 0.1,sensorConfigMap["ymin"],sensorConfigMap["ymax"],500,0,500 ) );	
      }
      rowIndex++;
    }
    
  


    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    my_efficiencies.emplace("event_sel_weight", std::make_shared<TEfficiency>("event_sel_weight","event_sel_weight",9,0,9));
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    BNL2020Geometry g;
    std::map<std::string,double> sensorConfigMap = GetSensorConfigMap("BNL2020");
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
        const auto& chi2 = tr.getVar<float>("chi2");
                                   
        //Make cuts and fill histograms here
        if( ntracks==1 && nplanes>10 && npix>0 
	    //&& chi2 < 6
	    ) 
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

        }



	//******************************************************************
	//Efficiency
	//******************************************************************
	const double angle = sensorConfigMap["angle"];
	const auto& x_dut = tr.getVec<float>("x_dut");
	const auto& y_dut = tr.getVec<float>("y_dut");
	double x = x_dut[0];
	double y = y_dut[0];
	std::pair<double,double> tmp_pair = Rotate(x_dut[0], y_dut[0], angle);
	x = tmp_pair.first;
	y = tmp_pair.second;

	//Make cuts and fill histograms here
	if( ntracks==1 && nplanes>10 && npix>0 ) {
      
	  if (amp[7] > 50) {
	    my_2d_histos["efficiency_vs_xy_denominator"]->Fill(x,y);

	    bool hasGlobalSignal = false;
	    for(const auto& row : ampLGAD)  {
	      int rowIndex = 0;
	      for(unsigned int i = 0; i < row.size(); i++)  {
		const auto& r = std::to_string(rowIndex);
		const auto& s = std::to_string(i);
		my_3d_histos["amplitude_vs_xy_channel"+r+s]->Fill(x,y,ampLGAD[rowIndex][i]);
		
		if (ampLGAD[rowIndex][i]  > 30 ) {
		  hasGlobalSignal = true; 
		  my_2d_histos["efficiency_vs_xy_numerator_channel"+r+s]->Fill(x,y);
		}
	      }
	      rowIndex++;
	    }
	    if (hasGlobalSignal) my_2d_histos["efficiency_vs_xy_numerator"]->Fill(x,y);

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
