#define Analyze_cxx
#include "TestbeamReco/interface/Analyze.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>
#include <numeric>

Analyze::Analyze()
{
}

//Define all your histograms here. 
void Analyze::InitHistos(NTupleReader& tr, const std::vector<std::vector<int>>& geometry)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    //Define 1D histograms
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");
    const auto& boxes_XY = tr.getVar<std::vector<std::vector<double>>>("boxes_XY");
    int xbins = 175;
    int ybins = 175;

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
            my_histos.emplace( ("timeDiff_channel"+r+s).c_str(), std::make_shared<TH1D>( ("timeDiff_channel"+r+s).c_str(), ("timeDiff_channel"+r+s).c_str(), 100, -110.0, -100.0 ) ) ;
            my_histos.emplace( ("relFrac_top"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_top"+r+s).c_str(), ("relFrac_top"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
            my_histos.emplace( ("relFrac_bottom"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_bottom"+r+s).c_str(), ("relFrac_bottom"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
            my_histos.emplace( ("relFrac_left"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_left"+r+s).c_str(), ("relFrac_left"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
            my_histos.emplace( ("relFrac_right"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_right"+r+s).c_str(), ("relFrac_right"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
        }
        rowIndex++;
    }
    my_histos.emplace( "deltaX", std::make_shared<TH1D>( "deltaX", "deltaX; #X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5 ) );

    //Per Channel 2D efficiencies
    my_2d_histos.emplace( "relFracDC_vs_x_channel_top", std::make_shared<TH2D>( "relFracDC_vs_x_channel_top", "relFracDC_vs_x_channel_top; X [mm]; relFrac", (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );

    rowIndex = 0;
    for(const auto& row : geometry) 
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++) 
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);            
            my_2d_histos.emplace( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
            my_2d_prof.emplace( ("efficiency_vs_xy_highThreshold_prof_channel"+r+s).c_str(), std::make_shared<TProfile2D>( ("efficiency_vs_xy_highThreshold_prof_channel"+r+s).c_str(), ("efficiency_vs_xy_highThreshold_prof_channel"+r+s+"; X [mm]; Y [mm]").c_str(), xbins,xmin,xmax, ybins,ymin,ymax ) );
            my_2d_histos.emplace( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
            my_2d_histos.emplace( ("relFrac_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel"+r+s).c_str(), ("relFrac_vs_x_channel"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel_top"+r+s).c_str(), ("relFrac_vs_x_channel_top"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("delay_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("delay_vs_x_channel_top"+r+s).c_str(), ("delay_vs_x_channel_top"+r+s+"; X [mm]; Arrival time [ns]").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,-11,-10 ) );
            my_2d_histos.emplace( ("relFrac_vs_x_channel_bottom"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel_bottom"+r+s).c_str(), ("relFrac_vs_x_channel_bottom"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_y_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_y_channel"+r+s).c_str(), ("relFrac_vs_y_channel"+r+s+"; Y [mm]; relFrac").c_str(), (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_y_channel_left"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_y_channel_left"+r+s).c_str(), ("relFrac_vs_y_channel_left"+r+s+"; Y [mm]; relFrac").c_str(), (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_y_channel_right"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_y_channel_right"+r+s).c_str(), ("relFrac_vs_y_channel_right"+r+s+"; Y [mm]; relFrac").c_str(), (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s).c_str(), std::make_shared<TH2D>( ("Amp1OverAmp1and2_vs_deltaXmax"+r+s).c_str(), ("Amp1OverAmp1and2_vs_deltaXmax"+r+s+"; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{2}").c_str(), 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
            
            my_2d_histos.emplace( ("amp_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel"+r+s).c_str(), ("amp_vs_x_channel"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel_top"+r+s).c_str(), ("amp_vs_x_channel_top"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_x_channel_bottom"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel_bottom"+r+s).c_str(), ("amp_vs_x_channel_bottom"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_y_channel"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_y_channel"+r+s).c_str(), ("amp_vs_y_channel"+r+s+"; Y [mm]; amp").c_str(), (ymax-ymin)/0.1,ymin,ymax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_y_channel_left"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_y_channel_left"+r+s).c_str(), ("amp_vs_y_channel_left"+r+s+"; Y [mm]; amp").c_str(), (ymax-ymin)/0.1,ymin,ymax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_y_channel_right"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_y_channel_right"+r+s).c_str(), ("amp_vs_y_channel_right"+r+s+"; Y [mm]; amp").c_str(), (ymax-ymin)/0.1,ymin,ymax, 250,0.0,500) );            
        }
        rowIndex++;
    }
    
    //Global 2D efficiencies
    my_2d_histos.emplace( "efficiency_vs_xy_highThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_highThreshold_numerator", "efficiency_vs_xy_highThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_prof.emplace( "efficiency_vs_xy_highThreshold_prof", std::make_shared<TProfile2D>( "efficiency_vs_xy_highThreshold_prof_channel", "efficiency_vs_xy_highThreshold_prof_channel; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_lowThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_lowThreshold_numerator", "efficiency_vs_xy_lowThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_denominator", std::make_shared<TH2D>( "efficiency_vs_xy_denominator", "efficiency_vs_xy_denominator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiencyDC_vs_xy_denominator", std::make_shared<TH2D>( "efficiencyDC_vs_xy_denominator", "efficiencyDC_vs_xy_denominator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "efficiencyDC_vs_xy_numerator", std::make_shared<TH2D>( "efficiencyDC_vs_xy_numerator", "efficiencyDC_vs_xy_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_histos.emplace( "clusterSize_vs_x", std::make_shared<TH2D>( "clusterSize_vs_x", "clusterSize_vs_x; X [mm]; Cluster Size", (xmax-xmin)/0.02,xmin,xmax, 20,-0.5,19.5 ) );
    my_2d_histos.emplace( "Amp1OverAmp1and2_vs_deltaXmax", std::make_shared<TH2D>( "Amp1OverAmp1and2_vs_deltaXmax", "Amp1OverAmp1and2_vs_deltaXmax; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2})", 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
    my_2d_histos.emplace( "Amp1OverAmp123_vs_deltaXmax", std::make_shared<TH2D>( "Amp1OverAmp123_vs_deltaXmax", "Amp1OverAmp123_vs_deltaXmax; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
    my_2d_histos.emplace( "Amp2OverAmp2and3_vs_deltaXmax", std::make_shared<TH2D>( "Amp2OverAmp2and3_vs_deltaXmax", "Amp2OverAmp2and3_vs_deltaXmax; #X_{track} - X_{Max Strip} [mm]; Amp_{2} / (Amp_{2} + Amp{3})", 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );

    my_2d_histos.emplace( "deltaX_vs_Xtrack", std::make_shared<TH2D>( "deltaX_vs_Xtrack", "deltaX_vs_Xtrack; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/0.01,xmin,xmax, 200,-0.5,0.5 ) );
    my_2d_histos.emplace( "deltaX_vs_Xtrack_A1OverA12Above0p75", std::make_shared<TH2D>( "deltaX_vs_Xtrack_A1OverA12Above0p75", "deltaX_vs_Xtrack; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/0.01,xmin,xmax, 200,-0.5,0.5 ) );
    my_2d_histos.emplace( "Xreco_vs_Xtrack", std::make_shared<TH2D>( "Xreco_vs_Xtrack", "Xreco_vs_Xtrack; X_{track} [mm]; #X_{reco} [mm]", (xmax-xmin)/0.005,xmin,xmax, (xmax-xmin)/0.005,xmin,xmax ) );
    my_2d_histos.emplace( "Xtrack_vs_Amp1OverAmp123", std::make_shared<TH2D>( "Xtrack_vs_Amp1OverAmp123", "Xtrack_vs_Amp1OverAmp123; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax, 100,0.0,1.0) );
    my_2d_histos.emplace( "Xtrack_vs_Amp2OverAmp123", std::make_shared<TH2D>( "Xtrack_vs_Amp2OverAmp123", "Xtrack_vs_Amp2OverAmp123; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax, 100,0.0,1.0) );
    my_2d_histos.emplace( "Xtrack_vs_Amp3OverAmp123", std::make_shared<TH2D>( "Xtrack_vs_Amp3OverAmp123", "Xtrack_vs_Amp3OverAmp123; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax, 100,0.0,1.0) );

    ///average waveforms  
    for(unsigned int iw = 0; iw < boxes_XY.size(); iw++)
    {
        rowIndex = 0;
    	for(const auto& row : geometry) 
        {
            if(row.size()<2) continue;
            for(unsigned int i = 0; i < row.size(); i++) 
            {
    		const auto& r = std::to_string(rowIndex);
    		const auto& s = std::to_string(i);   
    		my_2d_histos.emplace( ("avg_wave"+r+s).c_str(), std::make_shared<TH2D>( ("avg_wave"+r+s).c_str(), ("avg_wave"+r+s+"; t[ns]; V[mV]").c_str(), 2000,-230,-180, 100,50,-450 ) );
            }
            rowIndex++;
        }
    }
  
    //Define 3D histograms
    rowIndex = 0;
    for(const auto& row : geometry) 
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++) 
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);            
            my_3d_histos.emplace( ("amplitude_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("amplitude_vs_xy_channel"+r+s).c_str(), ("amplitude_vs_xy_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.03,xmin,xmax, (ymax-ymin)/0.03,ymin,ymax, 500,0,500 ) );	
        }
        rowIndex++;
    }

    //Define 2d prof
    my_2d_prof.emplace("efficiency_vs_xy_DCRing", std::make_shared<TProfile2D>("efficiency_vs_xy_DCRing", "efficiency_vs_xy_DCRing; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax ) );	
    my_2d_prof.emplace("efficiency_vs_xy_Strip2or5", std::make_shared<TProfile2D>("efficiency_vs_xy_Strip2or5", "efficiency_vs_xy_Strip2or5; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax ) );	

    //Define 1d prof
    my_1d_prof.emplace("Xtrack_vs_Amp1OverAmp123_prof", std::make_shared<TProfile>( "Xtrack_vs_Amp1OverAmp123_prof", "Xtrack_vs_Amp1OverAmp123_prof; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax));
    my_1d_prof.emplace("Xtrack_vs_Amp2OverAmp123_prof", std::make_shared<TProfile>( "Xtrack_vs_Amp2OverAmp123_prof", "Xtrack_vs_Amp2OverAmp123_prof; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax));
    my_1d_prof.emplace("Xtrack_vs_Amp3OverAmp123_prof", std::make_shared<TProfile>( "Xtrack_vs_Amp3OverAmp123_prof", "Xtrack_vs_Amp3OverAmp123_prof; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/0.01,xmin,xmax));
    
    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    my_efficiencies.emplace("event_sel_weight", std::make_shared<TEfficiency>("event_sel_weight","event_sel_weight",9,0,9));
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& stripCenterXPosition = tr.getVar<std::vector<double>>("stripCenterXPosition");
    const auto& enablePositionReconstruction = tr.getVar<double>("enablePositionReconstruction");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& positionRecoPar0 = tr.getVar<double>("positionRecoPar0");
    const auto& positionRecoPar1 = tr.getVar<double>("positionRecoPar1");
    const auto& positionRecoPar2 = tr.getVar<double>("positionRecoPar2");
    const auto& positionRecoPar3 = tr.getVar<double>("positionRecoPar3");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    //const auto& xSlices = tr.getVec<std::vector<double>>("xSlices");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
    const auto& doSlices = true;
    InitHistos(tr, geometry);

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
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");
        const auto& stripCenterXPositionLGAD = utility::remapToLGADgeometry(tr, stripCenterXPosition, "stripCenterXPositionLGAD");
        const auto& LP2_20 = tr.getVec<float>("LP2_20");
        const auto& timeLGAD = utility::remapToLGADgeometry(tr, LP2_20, "timeLGAD");
        const auto& photekIndex = tr.getVar<int>("photekIndex");

        //Get variables that you want to cut on
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        //const auto& channel = tr.getVecVec<float>("channel");
        //const auto& time = tr.getVecVec<float>("time");
        bool passTrigger = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        bool pass = passTrigger && hitSensor;

	//Find max channel and 2nd,3rd channels
        const auto amp1Indexes = utility::findNthRankChannel(ampLGAD, 1);
        const auto amp2Indexes = utility::findNthRankChannel(ampLGAD, 2);
        const auto amp3Indexes = utility::findNthRankChannel(ampLGAD, 3);
        double maxAmpLGAD = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        double totAmp = 0.0;
        for(auto row : ampLGAD) totAmp += std::accumulate(row.begin(), row.end(), 0.0);
        double relFracDC = corrAmp[0]/totAmp;
        std::vector<double> relFrac;
        for(auto row : ampLGAD){ for(auto i : row) relFrac.emplace_back(i/totAmp);}

	//Compute position-sensitive variables
        //Only good for strip sensors currently
	double xCenterMaxStrip = 0;
	double xCenterStrip2 = 0;
	double xCenterStrip3 = 0;
        double Amp1 = 0.0, Amp2 = 0.0, Amp3 = 0.0;
	double Amp1OverAmp1and2 = 0;
	double Amp1OverAmp123 = 0, Amp2OverAmp123 = 0, Amp3OverAmp123 = 0;
	double Amp2OverAmp2and3 = 0;
	double deltaXmax = -999;
        int maxAmpIndex = amp1Indexes.second;
        int Amp2Index = amp2Indexes.second;
        int Amp3Index = amp3Indexes.second;
	if (maxAmpIndex >= 0 && Amp2Index>=0) 
        {
            Amp1 = ampLGAD[0][maxAmpIndex];
            Amp2 = ampLGAD[0][Amp2Index];
            xCenterMaxStrip = stripCenterXPositionLGAD[0][maxAmpIndex];
            xCenterStrip2 = stripCenterXPositionLGAD[0][Amp2Index];
            Amp1OverAmp1and2 = ampLGAD[0][maxAmpIndex] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index]);
            if (Amp3Index >= 0) 
            {
                Amp3 = ampLGAD[0][Amp3Index];
                xCenterStrip3 = stripCenterXPositionLGAD[0][Amp3Index];
                Amp2OverAmp2and3= ampLGAD[0][Amp2Index] / (ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
                Amp1OverAmp123 = ampLGAD[0][maxAmpIndex] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
                Amp2OverAmp123 = ampLGAD[0][Amp2Index] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
                Amp3OverAmp123 = ampLGAD[0][Amp3Index] / (ampLGAD[0][maxAmpIndex] + ampLGAD[0][Amp2Index] + ampLGAD[0][Amp3Index]);
            }
            deltaXmax = x - xCenterMaxStrip;
	}

	//******************************************************************
	//X-Position Reconstruction
	//******************************************************************
	double x_reco = 0;
	double positionRecoCutFitCutOffPoint = 0.735;
	double x1 = 0;
	double x2 = 0;
	if (enablePositionReconstruction >= 1.0 && ampLGAD[0][maxAmpIndex] > signalAmpThreshold)
        {	  
	  if (pass) 
	  {
	    if (maxAmpIndex >= 1 && maxAmpIndex <= 4) 
            {
	      assert(Amp1OverAmp1and2 >= 0); //make sure a1/(a1+a2) is a sensible number
	      assert(Amp1OverAmp1and2 <= 1);
	      x1 = stripCenterXPositionLGAD[0][maxAmpIndex];
	      x2 = stripCenterXPositionLGAD[0][Amp2Index];

              //double xSin = 1/62.0*(asin((Amp1OverAmp123 - 0.55)/0.059) + 0.124);
	    
	      //use the poly fit function
	      double dX = positionRecoPar0 + positionRecoPar1*Amp1OverAmp1and2 + positionRecoPar2*pow(Amp1OverAmp1and2,2) + positionRecoPar3*pow(Amp1OverAmp1and2,3);
	    
	      //After the "cut-off" point of the fit, then linearly 
	      //interpolate to (Amp1OverAmp1and2=0.75,dX=0.0) point
	      if (Amp1OverAmp1and2 > 0.75) 
              {
	        dX = 0.0;                
                //std::cout<<"Amp1: "<<Amp1<<" Amp2: "<<Amp2<<" Amp3: "<<Amp3<<" Amp1OverAmp1and2:"<<Amp1OverAmp1and2<<std::endl;              
	        my_2d_histos["Amp2OverAmp2and3_vs_deltaXmax"]->Fill(deltaXmax, Amp2OverAmp2and3);
              
	      }
              else if (Amp1OverAmp1and2 > positionRecoCutFitCutOffPoint) {
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

	      //fill position reco residual
              my_histos["deltaX"]->Fill(x_reco-x);
	      my_2d_histos["deltaX_vs_Xtrack"]->Fill(x, x_reco-x);
	      my_2d_histos["Xreco_vs_Xtrack"]->Fill(x, x_reco);
	      if (Amp1OverAmp1and2>=0.75) { my_2d_histos["deltaX_vs_Xtrack_A1OverA12Above0p75"]->Fill(x, x_reco-x);}
	    
	    } //if max strip is index 1-4
	  } //if passes good event selection
	} //if enabled position reconstruction
   
	//******************************************************************
        //Make cuts and fill histograms here
	//******************************************************************
        if(pass && maxAmpLGAD > 50) 
        {
            my_2d_histos["relFracDC_vs_x_channel_top"]->Fill(x, relFracDC);

            int rowIndex = 0;
            for(const auto& row : ampLGAD)
            {
                for(unsigned int i = 0; i < row.size(); i++)
                {
                    const auto& r = std::to_string(rowIndex);
                    const auto& s = std::to_string(i);
                    int LGAD_index = rowIndex*row.size()+i; //geometry[rowIndex][i]-1;

                    my_histos["amp"+r+s]->Fill(ampLGAD[rowIndex][i], 1.0);
                    if(maxAmpIndex == int(i)) my_histos["ampMax"+r+s]->Fill(ampLGAD[rowIndex][i], 1.0); /// This only works for single row sensors...
                    my_histos["relFrac"+r+s]->Fill(relFrac[LGAD_index], 1.0);
                    my_2d_histos["relFrac_vs_x_channel"+r+s]->Fill(x, relFrac[LGAD_index]);
                    my_2d_histos["relFrac_vs_y_channel"+r+s]->Fill(y, relFrac[LGAD_index]);
                    if(doSlices)
                    {
                    	//in bottom row
                    	if(y > ySlices[0][0] && y<ySlices[0][1])
                        {
                            my_histos["relFrac_bottom"+r+s]->Fill(relFrac[LGAD_index], 1.0);
                            my_2d_histos["relFrac_vs_x_channel_bottom"+r+s]->Fill(x, relFrac[LGAD_index]);
                            my_2d_histos["amp_vs_x_channel_bottom"+r+s]->Fill(x, ampLGAD[rowIndex][i]);
                        }
                    	//in top row
                    	if(y > ySlices[1][0] && y<ySlices[1][1])
                        {
                            my_histos["relFrac_top"+r+s]->Fill(relFrac[LGAD_index], 1.0);
                            my_2d_histos["relFrac_vs_x_channel_top"+r+s]->Fill(x, relFrac[LGAD_index]);
                            my_2d_histos["amp_vs_x_channel_top"+r+s]->Fill(x, ampLGAD[rowIndex][i]);
                            const auto& LP2_20 = tr.getVec<float>("LP2_20");
                            if(timeLGAD[rowIndex][i]!=0 && LP2_20[photekIndex]!=0) my_2d_histos["delay_vs_x_channel_top"+r+s]->Fill(x, 1e9*(timeLGAD[rowIndex][i] - LP2_20[photekIndex]));                            
                    	}
                    }

		    //reconstruction position		 
		    
		    if (maxAmpIndex== int(i)) 
                    {
                        my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s]->Fill(deltaXmax, Amp1OverAmp1and2);
		    }
                }
                rowIndex++;
            }
	    //only fill the global a1/(a1+a2) if the max amp strip is not one of the edge strips
	    if (maxAmpIndex >= 1 && maxAmpIndex <= 4) 
            {
                my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax"]->Fill(fabs(deltaXmax), Amp1OverAmp1and2);
                my_2d_histos["Amp1OverAmp123_vs_deltaXmax"]->Fill(fabs(deltaXmax), Amp1OverAmp123);
                my_2d_histos["Xtrack_vs_Amp1OverAmp123"]->Fill(x, Amp1OverAmp123);
                my_2d_histos["Xtrack_vs_Amp2OverAmp123"]->Fill(x, Amp2OverAmp123);
                my_2d_histos["Xtrack_vs_Amp3OverAmp123"]->Fill(x, Amp3OverAmp123);
                my_1d_prof["Xtrack_vs_Amp1OverAmp123_prof"]->Fill(x, Amp1OverAmp123);
                my_1d_prof["Xtrack_vs_Amp2OverAmp123_prof"]->Fill(x, Amp2OverAmp123);
                my_1d_prof["Xtrack_vs_Amp3OverAmp123_prof"]->Fill(x, Amp3OverAmp123);
	    }
        }

	//******************************************************************
	//Efficiency
	//******************************************************************

        if(passTrigger) 
        {
            my_2d_prof["efficiency_vs_xy_DCRing"]->Fill(x,y,amp[0]>30);

	    for(const auto& row : ampLGAD)  
            {
                int rowIndex = 0;
                auto maxAmpRowIter = std::max_element(ampLGAD[rowIndex].begin(),ampLGAD[rowIndex].end());
                int maxAmpRowIndex = std::distance(ampLGAD[rowIndex].begin(), maxAmpRowIter);
                bool goodHitGlobal = false;
                for(unsigned int i = 0; i < row.size(); i++)  
                {
                    const auto& r = std::to_string(rowIndex);
                    const auto& s = std::to_string(i);

                    auto ampLeft = (i != 0) ? ampLGAD[rowIndex][i-1] : 0.0;
                    auto ampRight = (i != row.size()-1) ? ampLGAD[rowIndex][i+1] : 0.0;

                    bool goodHit = ampLGAD[rowIndex][i] > 50.0 && ampLGAD[rowIndex][i] > ampLeft && ampLGAD[rowIndex][i] > ampRight;
                    my_2d_prof["efficiency_vs_xy_highThreshold_prof_channel"+r+s]->Fill(x,y,goodHit);

                    double time = timeLGAD[rowIndex][i]*10e9;
                    double photekTime = LP2_20[photekIndex]*10e9;

                    if(i==1 || i==4) goodHitGlobal = goodHitGlobal || goodHit;
                    if(int(i)==maxAmpRowIndex)
                    {
                        my_2d_prof["efficiency_vs_xy_highThreshold_prof"]->Fill(x,y,goodHit);
                        if(ampLGAD[rowIndex][i] > 30.0) my_histos["timeDiff_channel"+r+s]->Fill(time-photekTime);
                    }
                }
                my_2d_prof["efficiency_vs_xy_Strip2or5"]->Fill(x,y,goodHitGlobal);
                rowIndex++;
            }
        }

	//******************************************************************
	//Make cuts and fill histograms here
	//******************************************************************
	if(pass) 
        {
            //Require at least 50 mV signal on Photek
            if (corrAmp[photekIndex] > photekSignalThreshold) 
            {
                my_2d_histos["efficiency_vs_xy_denominator"]->Fill(x,y);

                bool hasGlobalSignal_highThreshold = false;
                bool hasGlobalSignal_lowThreshold = false;
                int clusterSize = 0;
                int rowIndex = 0;

                if(corrAmp[0] > signalAmpThreshold)
                {
                    my_2d_histos["efficiencyDC_vs_xy_numerator"]->Fill(x,y);
		}
                for(const auto& row : ampLGAD)  
                {	      
                    for(unsigned int i = 0; i < row.size(); i++)
                    {
                        const auto& r = std::to_string(rowIndex);
                        const auto& s = std::to_string(i);

                        if (ampLGAD[rowIndex][i] > noiseAmpThreshold) 
                        {
                            hasGlobalSignal_lowThreshold = true; 
                            clusterSize++;
                            if (maxAmpLGAD > 50) my_3d_histos["amplitude_vs_xy_channel"+r+s]->Fill(x,y,ampLGAD[rowIndex][i]);
                            my_2d_histos["efficiency_vs_xy_lowThreshold_numerator_channel"+r+s]->Fill(x,y);		  
                        }
				
                        if (ampLGAD[rowIndex][i] > signalAmpThreshold) 
                        {
                            hasGlobalSignal_highThreshold = true; 
                            my_2d_histos["efficiency_vs_xy_highThreshold_numerator_channel"+r+s]->Fill(x,y);
                            my_2d_prof["efficiency_vs_xy_highThreshold_prof_channel"+r+s]->Fill(x,y,ampLGAD[rowIndex][i] > signalAmpThreshold);
                        }
                    }
                    rowIndex++;
                }

                if (hasGlobalSignal_lowThreshold) my_2d_histos["efficiency_vs_xy_lowThreshold_numerator"]->Fill(x,y);
                if (hasGlobalSignal_highThreshold) 
                {
                    my_2d_histos["efficiency_vs_xy_highThreshold_numerator"]->Fill(x,y);
                    my_2d_histos["clusterSize_vs_x"]->Fill(x,clusterSize);
                }

                // for(const auto box : boxes_XY){
                // 	if(box.size()==4){
                // 	if(x > box[0] && x < box[1] && y>box[2] && y<box[3]){
                // 		for(uint isam=0; isam < channel[0].size();isam++){
                // 			// printf("%0.2f %0.2f \n",channel[1][isam],time[0][isam]);
                // 			my_2d_histos["avg_wave00"]->Fill(1e9*time[0][isam],channel[1][isam]);
                // 			my_2d_histos["avg_wave01"]->Fill(1e9*time[0][isam],channel[2][isam]);
                // 			my_2d_histos["avg_wave10"]->Fill(1e9*time[0][isam],channel[3][isam]);
                // 			my_2d_histos["avg_wave11"]->Fill(1e9*time[0][isam],channel[4][isam]);
                // 		}
                // 	}
                // 	}
                // }

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
    
    for (const auto &p : my_2d_prof) {
        p.second->Write();
    }

    for (const auto &p : my_1d_prof) {
        p.second->Write();
    }

    for (const auto &p : my_efficiencies) {
        p.second->Write();
    }    
}
