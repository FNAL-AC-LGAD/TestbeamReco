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
    int xbins = 175;
    int ybins = 175;

    int timeDiffNbin = 200;
    double timeDiffLow = -1.0;
    double timeDiffHigh = 1.0;
    int timeDiffYnbin = 10;

    int rowIndex = 0;
    for(const auto& row : geometry)
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++)
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);            
            my_histos.emplace( ("amp"+r+s).c_str(), std::make_shared<TH1D>( ("amp"+r+s).c_str(), ("amp"+r+s).c_str(), 450, -50.0, 400.0 ) ) ;
            my_histos.emplace( ("time"+r+s).c_str(), std::make_shared<TH1D>( ("time"+r+s).c_str(), ("time"+r+s).c_str(), 500, -225.0, -175.0 ) ) ;
            my_histos.emplace( ("ampMax"+r+s).c_str(), std::make_shared<TH1D>( ("ampMax"+r+s).c_str(), ("ampMax"+r+s).c_str(), 450, -50.0, 400.0 ) ) ;
            my_histos.emplace( ("relFrac"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac"+r+s).c_str(), ("relFrac"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
            my_histos.emplace( ("timeDiff_channel"+r+s).c_str(), std::make_shared<TH1D>( ("timeDiff_channel"+r+s).c_str(), ("timeDiff_channel"+r+s).c_str(), timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
            my_histos.emplace( ("weighted_timeDiff_channel"+r+s).c_str(), std::make_shared<TH1D>( ("weighted_timeDiff_channel"+r+s).c_str(), ("weighted_timeDiff_channel"+r+s).c_str(), timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
            my_histos.emplace( ("weighted_time-time_channel"+r+s).c_str(), std::make_shared<TH1D>( ("weighted_time-time_channel"+r+s).c_str(), ("weighted_time-time_channel"+r+s).c_str(), timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
            my_histos.emplace( ("relFrac_top"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_top"+r+s).c_str(), ("relFrac_top"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;
            my_histos.emplace( ("relFrac_bottom"+r+s).c_str(), std::make_shared<TH1D>( ("relFrac_bottom"+r+s).c_str(), ("relFrac_bottom"+r+s).c_str(), 100, 0.0, 1.0 ) ) ;

            my_2d_histos.emplace( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_highThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
            my_2d_prof.emplace( ("efficiency_vs_xy_highThreshold_prof_channel"+r+s).c_str(), std::make_shared<TProfile2D>( ("efficiency_vs_xy_highThreshold_prof_channel"+r+s).c_str(), ("efficiency_vs_xy_highThreshold_prof_channel"+r+s+"; X [mm]; Y [mm]").c_str(), xbins,xmin,xmax, ybins,ymin,ymax ) );
            my_2d_histos.emplace( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), std::make_shared<TH2D>( ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s).c_str(), ("efficiency_vs_xy_lowThreshold_numerator_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
            my_2d_histos.emplace( ("relFrac_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel"+r+s).c_str(), ("relFrac_vs_x_channel"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel_top"+r+s).c_str(), ("relFrac_vs_x_channel_top"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("delay_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("delay_vs_x_channel_top"+r+s).c_str(), ("delay_vs_x_channel_top"+r+s+"; X [mm]; Arrival time [ns]").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,-11,-10 ) );
            my_2d_histos.emplace( ("timeDiff_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("timeDiff_vs_x_channel"+r+s).c_str(), ("timeDiff_vs_x_channel"+r+s).c_str(), (xmax-xmin)/0.02,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
            my_2d_histos.emplace( ("relFrac_vs_x_channel_bottom"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_x_channel_bottom"+r+s).c_str(), ("relFrac_vs_x_channel_bottom"+r+s+"; X [mm]; relFrac").c_str(), (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
            my_2d_histos.emplace( ("relFrac_vs_y_channel"+r+s).c_str(), std::make_shared<TH2D>( ("relFrac_vs_y_channel"+r+s).c_str(), ("relFrac_vs_y_channel"+r+s+"; Y [mm]; relFrac").c_str(), (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0 ) );

            my_2d_histos.emplace( ("Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s).c_str(), std::make_shared<TH2D>( ("Amp1OverAmp1and2_vs_deltaXmax"+r+s).c_str(), ("Amp1OverAmp1and2_vs_deltaXmax"+r+s+"; #X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{2}").c_str(), 0.50/0.002,-0.25,0.25, 100,0.0,1.0 ) );
            
            my_2d_histos.emplace( ("amp_vs_x_channel"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel"+r+s).c_str(), ("amp_vs_x_channel"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_x_channel_top"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel_top"+r+s).c_str(), ("amp_vs_x_channel_top"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("amp_vs_x_channel_bottom"+r+s).c_str(), std::make_shared<TH2D>( ("amp_vs_x_channel_bottom"+r+s).c_str(), ("amp_vs_x_channel_bottom"+r+s+"; X [mm]; amp").c_str(), (xmax-xmin)/0.02,xmin,xmax, 250,0.0,500) );
            my_2d_histos.emplace( ("stripBoxInfo"+r+s).c_str(), std::make_shared<TH2D>( ("stripBoxInfo"+r+s).c_str(), ("stripBoxInfo"+r+s).c_str(), 1,-9999.0,9999.0, 1,-9999.9,9999.9));
            

            //Define 3D histograms
            my_3d_histos.emplace( ("amplitude_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("amplitude_vs_xy_channel"+r+s).c_str(), ("amplitude_vs_xy_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 ) );
            my_3d_histos.emplace( ("timeDiff_vs_xy_channel"+r+s).c_str(), std::make_shared<TH3D>( ("timeDiff_vs_xy_channel"+r+s).c_str(), ("timeDiff_vs_xy_channel"+r+s+"; X [mm]; Y [mm]").c_str(), (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
        }
        rowIndex++;
    }
    my_histos.emplace( "deltaX", std::make_shared<TH1D>( "deltaX", "deltaX; #X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5 ) );
    my_histos.emplace( "timePhotek", std::make_shared<TH1D>( "timePhotek", "timePhotek", 500, -225.0, -175.0 ) ) ;
    my_histos.emplace( "timeDiff", std::make_shared<TH1D>("timeDiff", "timeDiff", timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_histos.emplace( "timeDiff_amp2", std::make_shared<TH1D>("timeDiff_amp2", "timeDiff_amp2", timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_histos.emplace( "timeDiff_amp3", std::make_shared<TH1D>("timeDiff_amp3", "timeDiff_amp3", timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_histos.emplace( "weighted_timeDiff", std::make_shared<TH1D>("weighted_timeDiff", "weighted_timeDiff", timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;

    //Global 2D efficiencies
    my_2d_histos.emplace( "relFracDC_vs_x_channel_top", std::make_shared<TH2D>( "relFracDC_vs_x_channel_top", "relFracDC_vs_x_channel_top; X [mm]; relFrac", (xmax-xmin)/0.02,xmin,xmax, 100,0.0,1.0 ) );
    my_2d_histos.emplace( "weighted_timeDiff_vs_x", std::make_shared<TH2D>( "weighted_timeDiff_vs_x", "weighted_timeDiff_vs_x", (xmax-xmin)/0.02,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;

    //Global 2D efficiencies
    //my_2d_histos.emplace( "efficiency_vs_xy_highThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_highThreshold_numerator", "efficiency_vs_xy_highThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax ) );
    my_2d_histos.emplace( "efficiency_vs_xy_highThreshold_numerator", std::make_shared<TH2D>( "efficiency_vs_xy_highThreshold_numerator", "efficiency_vs_xy_highThreshold_numerator; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax ) );
    my_2d_prof.emplace( "efficiency_vs_xy_highThreshold_prof", std::make_shared<TProfile2D>( "efficiency_vs_xy_highThreshold_prof", "efficiency_vs_xy_highThreshold_prof; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax ) );
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

    my_3d_histos.emplace( "totgoodamplitude_vs_xy", std::make_shared<TH3D>( "totgoodamplitude_vs_xy", "totgoodamplitude_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 ) );	
    my_3d_histos.emplace( "totamplitude_vs_xy", std::make_shared<TH3D>( "totamplitude_vs_xy", "totamplitude_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 ) );
    my_3d_histos.emplace( "amp123_vs_xy", std::make_shared<TH3D>( "amp123_vs_xy", "amp123_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 ) );
    my_3d_histos.emplace( "amp12_vs_xy", std::make_shared<TH3D>( "amp12_vs_xy", "amp12_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 ) );	
    my_3d_histos.emplace( "timeDiff_vs_xy", std::make_shared<TH3D>( "timeDiff_vs_xy", "timeDiff_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_3d_histos.emplace( "timeDiff_vs_xy_amp2", std::make_shared<TH3D>( "timeDiff_vs_xy_amp2", "timeDiff_vs_xy_amp2; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_3d_histos.emplace( "timeDiff_vs_xy_amp3", std::make_shared<TH3D>( "timeDiff_vs_xy_amp3", "timeDiff_vs_xy_amp3; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;
    my_3d_histos.emplace( "weighted_timeDiff_vs_xy", std::make_shared<TH3D>( "weighted_timeDiff_vs_xy", "weighted_timeDiff_vs_xy; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh ) ) ;

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
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    //const auto& xSlices = tr.getVec<std::vector<double>>("xSlices");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
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
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        const auto& corrTime = tr.getVec<double>("corrTime");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& x_reco = tr.getVar<double>("x_reco");
        const auto& weighted_time = tr.getVar<double>("weighted_time");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& relFracDC = tr.getVar<double>("relFracDC");
        const auto& relFrac = tr.getVec<double>("relFrac");
        const auto& totAmpLGAD = tr.getVar<double>("totAmpLGAD");
        const auto& totGoodAmpLGAD = tr.getVar<double>("totGoodAmpLGAD");
        const auto& Amp123 = tr.getVar<double>("Amp123");
        const auto& Amp12 = tr.getVar<double>("Amp12");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& amp2Indexes = tr.getVar<std::pair<int,int>>("amp2Indexes");
        const auto& amp3Indexes = tr.getVar<std::pair<int,int>>("amp3Indexes");
        const auto& deltaXmax = tr.getVar<double>("deltaXmax");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");
        const auto& Amp2OverAmp2and3 = tr.getVar<double>("Amp2OverAmp2and3");
        const auto& Amp1OverAmp123 = tr.getVar<double>("Amp1OverAmp123");
        const auto& Amp2OverAmp123 = tr.getVar<double>("Amp2OverAmp123");
        const auto& Amp3OverAmp123 = tr.getVar<double>("Amp3OverAmp123");
        const auto& hasGlobalSignal_lowThreshold = tr.getVar<bool>("hasGlobalSignal_lowThreshold");
        const auto& hasGlobalSignal_highThreshold = tr.getVar<bool>("hasGlobalSignal_highThreshold");
        const auto& clusterSize = tr.getVar<int>("clusterSize");
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& stripWidth = tr.getVar<double>("stripWidth");

        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold;
        bool passTrigger = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        bool pass = passTrigger && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = maxAmpIndex >= 1 && maxAmpIndex <= 4;
        bool inBottomRow = y>ySlices[0][0] && y<ySlices[0][1];
        bool inTopRow = y>ySlices[1][0] && y<ySlices[1][1];
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;
        bool goodDCAmp = corrAmp[0]>signalAmpThreshold;
        bool highRelAmp1 = Amp1OverAmp1and2>=0.75;
        double photekTime = corrTime[photekIndex];
        double maxAmpTime = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        double amp2Time = timeLGAD[amp2Indexes.first][amp2Indexes.second];
        double amp3Time = timeLGAD[amp3Indexes.first][amp3Indexes.second];
        double firstEvent = tr.isFirstEvent();

	//******************************************************************
        //Make cuts and fill histograms here
	//******************************************************************        
        //Loop over each channel in each sensor
        bool goodHitGlobal2and5 = false;
        int rowIndex = 0;
        for(const auto& row : ampLGAD)
        {
            for(unsigned int i = 0; i < row.size(); i++)
            {
                const auto& r = std::to_string(rowIndex);
                const auto& s = std::to_string(i);
                const auto& ampChannel = ampLGAD[rowIndex][i];
                bool goodNoiseAmp = ampChannel>noiseAmpThreshold;
                bool goodSignalAmp = ampChannel>signalAmpThreshold;
                double time = timeLGAD[rowIndex][i];
                bool isMaxChannel = amp1Indexes.first == rowIndex && amp1Indexes.second == int(i);
                bool goodHit = goodNoiseAmp && goodMaxLGADAmp;
                if(i==1 || i==4) goodHitGlobal2and5 = goodHitGlobal2and5 || (isMaxChannel && goodHit);
                int LGAD_index = rowIndex*row.size()+i;
                utility::fillHisto(pass,                                                    my_histos["amp"+r+s], ampChannel);
                utility::fillHisto(pass && isMaxChannel,                                    my_histos["ampMax"+r+s], ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_histos["relFrac"+r+s], relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit && inBottomRow,                          my_histos["relFrac_bottom"+r+s], relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit && inTopRow,                             my_histos["relFrac_top"+r+s], relFrac[LGAD_index]);
                utility::fillHisto(pass,                                                    my_histos["time"+r+s], time);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["timeDiff_channel"+r+s], time-photekTime);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["weighted_timeDiff_channel"+r+s], weighted_time-photekTime);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["weighted_time-time_channel"+r+s], weighted_time-time);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["amp_vs_x_channel"+r+s], x,ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_x_channel"+r+s], x,relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_y_channel"+r+s], y,relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s], deltaXmax, Amp1OverAmp1and2);
                utility::fillHisto(pass && goodNoiseAmp,                                    my_2d_histos["efficiency_vs_xy_lowThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(pass && goodSignalAmp,                                   my_2d_histos["efficiency_vs_xy_highThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_2d_histos["timeDiff_vs_x_channel"+r+s], x,time-photekTime);
                utility::fillHisto(pass && goodHit && inBottomRow,                          my_2d_histos["relFrac_vs_x_channel_bottom"+r+s], x, relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit && inBottomRow,                          my_2d_histos["amp_vs_x_channel_bottom"+r+s], x, ampChannel);
                utility::fillHisto(pass && goodHit && inTopRow,                             my_2d_histos["relFrac_vs_x_channel_top"+r+s], x, relFrac[LGAD_index]);
                utility::fillHisto(pass && goodHit && inTopRow,                             my_2d_histos["amp_vs_x_channel_top"+r+s], x, ampChannel);
                utility::fillHisto(pass && goodHit && inTopRow && time!=0 && photekTime!=0, my_2d_histos["delay_vs_x_channel_top"+r+s], x, timeLGAD[rowIndex][i] - photekTime);
                utility::fillHisto(firstEvent,                                              my_2d_histos["stripBoxInfo"+r+s], stripCenterXPositionLGAD[rowIndex][i],stripWidth);
                utility::fillHisto(pass && goodHit,                                         my_3d_histos["amplitude_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_3d_histos["timeDiff_vs_xy_channel"+r+s], x,y,time-photekTime);
                utility::fillHisto(passTrigger,                                             my_2d_prof["efficiency_vs_xy_highThreshold_prof_channel"+r+s], x,y,ampChannel > signalAmpThreshold);
                utility::fillHisto(passTrigger && isMaxChannel,                             my_2d_prof["efficiency_vs_xy_highThreshold_prof"], x,y,goodHit);
            }
            rowIndex++;
        }
        utility::fillHisto(pass,                                         my_histos["timePhotek"],photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["deltaX"], x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["timeDiff"], maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["timeDiff_amp2"], amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["timeDiff_amp3"], amp3Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["weighted_timeDiff"], weighted_time-photekTime);
        utility::fillHisto(pass,                                         my_2d_histos["relFracDC_vs_x_channel_top"], x,relFracDC);
        utility::fillHisto(pass,                                         my_2d_histos["efficiency_vs_xy_denominator"], x,y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax"], fabs(deltaXmax),Amp1OverAmp1and2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_2d_histos["Amp1OverAmp123_vs_deltaXmax"], fabs(deltaXmax),Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_2d_histos["Xtrack_vs_Amp1OverAmp123"], x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_2d_histos["Xtrack_vs_Amp2OverAmp123"], x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_2d_histos["Xtrack_vs_Amp3OverAmp123"], x,Amp3OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_2d_histos["deltaX_vs_Xtrack"], x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_2d_histos["weighted_timeDiff_vs_x"], x,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_2d_histos["Xreco_vs_Xtrack"], x,x_reco);
        utility::fillHisto(pass && highRelAmp1,                          my_2d_histos["deltaX_vs_Xtrack_A1OverA12Above0p75"], x,x_reco-x);	    
        utility::fillHisto(pass && highRelAmp1,                          my_2d_histos["Amp2OverAmp2and3_vs_deltaXmax"], deltaXmax,Amp2OverAmp2and3);
        utility::fillHisto(pass && goodDCAmp,                            my_2d_histos["efficiencyDC_vs_xy_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold,         my_2d_histos["efficiency_vs_xy_lowThreshold_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,        my_2d_histos["efficiency_vs_xy_highThreshold_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,        my_2d_histos["clusterSize_vs_x"], x,clusterSize);
        utility::fillHisto(pass && goodMaxLGADAmp,                       my_3d_histos["totgoodamplitude_vs_xy"], x,y,totGoodAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                       my_3d_histos["totamplitude_vs_xy"], x,y,totAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                       my_3d_histos["amp123_vs_xy"], x,y, Amp123);
        utility::fillHisto(pass && goodMaxLGADAmp,                       my_3d_histos["amp12_vs_xy"], x,y, Amp12);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_3d_histos["timeDiff_vs_xy"], x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_3d_histos["timeDiff_vs_xy_amp2"], x,y,amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_3d_histos["timeDiff_vs_xy_amp3"], x,y,amp3Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_3d_histos["weighted_timeDiff_vs_xy"], x,y,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_1d_prof["Xtrack_vs_Amp1OverAmp123_prof"], x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_1d_prof["Xtrack_vs_Amp2OverAmp123_prof"], x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                   my_1d_prof["Xtrack_vs_Amp3OverAmp123_prof"], x,Amp3OverAmp123);
        utility::fillHisto(passTrigger,                                  my_2d_prof["efficiency_vs_xy_Strip2or5"], x,y,goodHitGlobal2and5);
        utility::fillHisto(passTrigger,                                  my_2d_prof["efficiency_vs_xy_DCRing"], x,y,goodDCAmp);

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

    std::cout<<"Made it to the end of writing histos"<<std::endl;
}
