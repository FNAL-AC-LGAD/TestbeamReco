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
	my_2d_histos.emplace( ("Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s).c_str(), std::make_shared<TH2D>( ("Amp1OverAmp1and2_vs_deltaXmax"+r+s).c_str(), ("Amp1OverAmp1and2_vs_deltaXmax"+r+s+"; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{2}").c_str(), 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
      }
      rowIndex++;
    }
    
    //Global 2D efficiencies
    my_2d_histos.emplace( "efficiency_vs_xy_highThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_highThreshold_numerator", "efficiency_vs_xy_highThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_lowThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_lowThreshold_numerator", "efficiency_vs_xy_lowThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_denominator", std::make_shared<TH2D>( "efficiency_vs_xy_denominator", "efficiency_vs_xy_denominator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "clusterSize_vs_x", std::make_shared<TH2D>( "clusterSize_vs_x", "clusterSize_vs_x; X [mm]; Cluster Size", (xmax-xmin)/0.02,xmin,xmax, 20,-0.5,19.5 ) );
    my_2d_histos.emplace( "Amp1OverAmp1and2_vs_deltaXmax", std::make_shared<TH2D>( "Amp1OverAmp1and2_vs_deltaXmax", "Amp1OverAmp1and2_vs_deltaXmax; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{2}", 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
    my_2d_histos.emplace( "deltaX_vs_Xtrack", std::make_shared<TH2D>( "deltaX_vs_Xtrack", "deltaX_vs_Xtrack; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/0.01,xmin,xmax, 200,-0.5,0.5 ) );
    my_2d_histos.emplace( "Xreco_vs_Xtrack", std::make_shared<TH2D>( "Xreco_vs_Xtrack", "Xreco_vs_Xtrack; X_{track} [mm]; #X_{reco} [mm]", (xmax-xmin)/0.005,xmin,xmax, (xmax-xmin)/0.005,xmin,xmax ) );

 
  
    //Define 3D histograms
    rowIndex = 0;
    for(const auto& row : geometry) {
      if(row.size()<2) continue;
      for(unsigned int i = 0; i < row.size(); i++) {
   	const auto& r = std::to_string(rowIndex);
   	const auto& s = std::to_string(i);            
   	my_3d_histos.emplace( ("amplitude_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("amplitude_vs_xy_channel"+r+s).c_str(), ("amplitude_vs_xy_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.01,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax, 500,0,500 ) );	
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
    const auto& stripCenterXPosition = tr.getVar<std::vector<double>>("stripCenterXPosition");
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
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");        
	const auto& stripCenterXPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterXPosition, "stripCenterXPositionLGAD");        

        //Get variables that you want to cut on
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        bool pass = ntracks==1 && nplanes>10 && npix>0 && hitSensor;

	//Find max channel and 2nd channel
        auto maxAmpIter = std::max_element(ampLGAD[0].begin(),ampLGAD[0].end());
        int maxAmpIndex = std::distance(ampLGAD[0].begin(), maxAmpIter);
	//find channel with 2nd largest element
	int Amp2Index = -1;
	double tmpAmp2 = -1.0;
	for(unsigned int i = 0; i < ampLGAD[0].size(); i++) {
	  if (i==maxAmpIndex) continue; //skip the max channel
	  if (ampLGAD[0][i] > tmpAmp2) { Amp2Index = i; tmpAmp2 = ampLGAD[0][i]; }
	}

	//Compute position-sensitive variables
	double xCenterMaxStrip = 0;
	double xCenterStrip2 = 0;
	double Amp1OverAmp1and2 = 0;
	double deltaXmax = -999;
	if (maxAmpIndex >= 0 && Amp2Index>=0) {
	  xCenterMaxStrip = stripCenterXPositionLGAD[0][maxAmpIndex];
	  xCenterStrip2 = stripCenterXPositionLGAD[0][Amp2Index];
	  Amp1OverAmp1and2 = ampLGAD[0][maxAmpIndex] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index]);
	  deltaXmax = x - xCenterMaxStrip;
	}

        double totAmp = 0.0;
        for(auto i : ampLGAD[0]) totAmp +=i;

        std::vector<double> relFrac;
        for(auto i : ampLGAD[0]) relFrac.emplace_back(i/totAmp);

        //const auto& channel = tr.getVecVec<float>("channel");
        //std::cout<<"channel: "<<channel.size()<<" "<<channel[0].size()<<" "<<channel[0][0]<<" "<<channel[1][0]<<" "<<channel[0][1]<<std::endl;

   
        //Make cuts and fill histograms here
        if(pass) 
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

		    //reconstruction position
		 
		    
		    if (maxAmpIndex== int(i)) {
		      my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s]->Fill(deltaXmax, Amp1OverAmp1and2);
		    }
                }
                rowIndex++;
            }
	    //only fill the global a1/(a1+a2) if the max amp strip is not one of the edge strips
	    if (maxAmpIndex >= 1 && maxAmpIndex <= 4) {
	      my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax"]->Fill(fabs(deltaXmax), Amp1OverAmp1and2);
	    }
        }

	//******************************************************************
	//X-Position Reconstruction
	//******************************************************************
	double x_reco = 0;
	double positionRecoPar0 = 0;
	double positionRecoPar1 = 0;
	double positionRecoPar2 = 0;
	double positionRecoPar3 = 0;
	double positionRecoCutFitCutOffPoint = 0.735;
	double x1 = 0;
	double x2 = 0;
	if (sensorConfigMap.at("enablePositionReconstruction") >= 1.0) 
        {
	  positionRecoPar0 = sensorConfigMap.at("positionRecoPar0");
	  positionRecoPar1 = sensorConfigMap.at("positionRecoPar1");
	  positionRecoPar2 = sensorConfigMap.at("positionRecoPar2");
	  positionRecoPar3 = sensorConfigMap.at("positionRecoPar3");
	  
	  if (pass) 
	  {
	    if (maxAmpIndex >= 1 && maxAmpIndex <= 4) {
	      assert(Amp1OverAmp1and2 >= 0); //make sure a1/(a1+a2) is a sensible number
	      assert(Amp1OverAmp1and2 <= 1);
	      x1 = stripCenterXPositionLGAD[0][maxAmpIndex];
	      x2 = stripCenterXPositionLGAD[0][Amp2Index];
	    
	      //use the poly fit function
	      double dX = positionRecoPar0 + positionRecoPar1*Amp1OverAmp1and2 + positionRecoPar2*pow(Amp1OverAmp1and2,2) + positionRecoPar3*pow(Amp1OverAmp1and2,3);
	    
	      //After the "cut-off" point of the fit, then linearly 
	      //interpolate to (Amp1OverAmp1and2=0.75,dX=0.0) point
	      if (Amp1OverAmp1and2 > 0.75) {
		dX = 0.0;
	      } else if (Amp1OverAmp1and2 > positionRecoCutFitCutOffPoint) {
		double dX_atCutOffPoint = positionRecoPar0 + positionRecoPar1*positionRecoCutFitCutOffPoint + positionRecoPar2*pow(positionRecoCutFitCutOffPoint,2) + positionRecoPar3*pow(positionRecoCutFitCutOffPoint,3);
		dX = dX_atCutOffPoint + ((0.0 - dX_atCutOffPoint)/(0.75 - positionRecoCutFitCutOffPoint))*(Amp1OverAmp1and2-0.75);
	      }
	    
	      //if dX is larger than 0.5, then just use the midpoint between the strips
	      //not sure why the profile wants to "over-shoot"
	      //if (dX >= 0.5) dX = 0.5;
	    
	      if (x2>x1) {
		x_reco = x1 + dX; 
	      } else {
		x_reco = x1 - dX; 
	      }
	    
	      // if (x < 0.2) {
	      // 	std::cout << "x = " << x << "\n";
	      // 	std::cout << "strip1,2 = " << maxAmpIndex << " , " << Amp2Index
	      // 	     << " at " << x1 << " , " << x2 << "\n";
	      // 	std::cout << "a1/(a1+a2) = " << Amp1OverAmp1and2 << "\n";
	      // 	std::cout << "normal dX = " << positionRecoPar0 + positionRecoPar1*Amp1OverAmp1and2 + positionRecoPar2*pow(Amp1OverAmp1and2,2) + positionRecoPar3*pow(Amp1OverAmp1and2,3) << "\n";
	      // 	std::cout << "positionRecoCutFitCutOffPoint = " << positionRecoCutFitCutOffPoint << "\n";
	      // 	std::cout << "dX_atCutOffPoint = " << positionRecoPar0 + positionRecoPar1*positionRecoCutFitCutOffPoint + positionRecoPar2*pow(positionRecoCutFitCutOffPoint,2) + positionRecoPar3*pow(positionRecoCutFitCutOffPoint,3) << "\n";
	      // 	std::cout << "dX = " << dX << "\n";
	      // 	std::cout << "x_reco = " << x_reco << "\n\n\n";		
	      // }

	      //fill position reco residual
	      my_2d_histos["deltaX_vs_Xtrack"]->Fill(x, x_reco-x);
	      my_2d_histos["Xreco_vs_Xtrack"]->Fill(x, x_reco);
	    
	    } //if max strip is index 1-4
	  } //if passes good event selection
	} //if enabled position reconstruction

	//******************************************************************
	//Time Resolution
	//******************************************************************
	if(pass) 
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
	if(pass) {

	  //Require at least 50 mV signal on Photek
	  const auto& photekIndex = tr.getVar<int>("photekIndex");
	  if (corrAmp[photekIndex] > sensorConfigMap.at("photekSignalThreshold")) {
	    my_2d_histos["efficiency_vs_xy_denominator"]->Fill(x,y);

	    bool hasGlobalSignal_highThreshold = false;
	    bool hasGlobalSignal_lowThreshold = false;
	    int clusterSize = 0;

	    for(const auto& row : ampLGAD)  {
	      int rowIndex = 0;
	      for(unsigned int i = 0; i < row.size(); i++)  {
		const auto& r = std::to_string(rowIndex);
		const auto& s = std::to_string(i);

		if (ampLGAD[rowIndex][i] > sensorConfigMap.at("noiseAmpThreshold")) {
		  hasGlobalSignal_lowThreshold = true; 
		  clusterSize++;
		  my_3d_histos["amplitude_vs_xy_channel"+r+s]->Fill(x,y,ampLGAD[rowIndex][i]);
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
	    if (hasGlobalSignal_highThreshold) {
	      my_2d_histos["efficiency_vs_xy_highThreshold_numerator"]->Fill(x,y);
	      my_2d_histos["clusterSize_vs_x"]->Fill(x,clusterSize);
	    }

	  } //if it passes Photek threshold
	} //if there's a valid track
	//******************************************************************

	// Example Fill event selection efficiencies
	my_efficiencies["event_sel_weight"]->SetUseWeightedEvents();
	my_efficiencies["event_sel_weight"]->FillWeighted(true,1.0,0);

    } //event loop
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
