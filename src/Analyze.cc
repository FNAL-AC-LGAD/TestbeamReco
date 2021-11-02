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
    const auto& pitch = tr.getVar<double>("pitch");
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    double xBinSize = 0.016;
    double xBinSizePad = 0.025;
    double yBinSizePad = 0.025;
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");
    int xbins = 175;
    int ybins = 175;


    int timeDiffNbin = 200;
    double timeDiffLow = -1.0;
    double timeDiffHigh = 1.0;
    int timeDiffYnbin = 50;
    int nvar=35;

    int rowIndex = 0;
    for(const auto& row : geometry)
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++)
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);

            //Define 1D histograms
            utility::makeHisto(my_histos,"amp"+r+s,"", 450,-50.0,400.0);
            utility::makeHisto(my_histos,"time"+r+s, "", 500, -225.0, -175.0);
            utility::makeHisto(my_histos,"ampMax"+r+s, "", 450, -50.0, 400.0);
            utility::makeHisto(my_histos,"relFrac"+r+s, "", 100, 0.0, 1.0);
            utility::makeHisto(my_histos,"timeDiff_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"weighted_timeDiff_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"weighted_time-time_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"relFrac_top"+r+s, "", 100, 0.0, 1.0 );
            utility::makeHisto(my_histos,"relFrac_bottom"+r+s, "", 100, 0.0, 1.0);
            utility::makeHisto(my_histos,"baselineRMS"+r+s,"", 200,-10.0,10.0);
            
            //Define 2D histograms
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_numerator_channel"+r+s,"; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
            utility::makeHisto(my_2d_prof,  "efficiency_vs_xy_highThreshold_prof_channel"+r+s, "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_numerator_channel"+r+s, "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel_top"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"delay_vs_x_channel_top"+r+s, "; X [mm]; Arrival time [ns]", (xmax-xmin)/xBinSize,xmin,xmax, 100,-11,-10);
            utility::makeHisto(my_2d_histos,"timeDiff_vs_x_channel"+r+s, "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel_bottom"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"relFrac_vs_y_channel"+r+s, "; Y [mm]; relFrac", (ymax-ymin)/0.1,ymin,ymax, 100,0.0,1.0);            
            utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s, "; X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{Max} + Amp_{2}", 0.50/0.002,-0.25,0.25, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"baselineRMS_vs_x_channel"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel_top"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel_bottom"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"stripBoxInfo"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);            
            utility::makeHisto(my_2d_histos,"stripBoxInfoY"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);            


            //Define 3D histograms
            utility::makeHisto(my_3d_histos,"baselineRMS_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"amplitude_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeTop_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeBot_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeLeft_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeRight_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"raw_amp_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500 );
            utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_channel"+r+s, "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
        }
        rowIndex++;
    }
    //Global 1D histograms
    utility::makeHisto(my_histos,"ntracks_alt", "; ntracks_alt; Events", 10,0,10);
    utility::makeHisto(my_histos,"chi2", "; Track chi2/ndf; Events", 60,0,30);
    utility::makeHisto(my_histos,"nplanes", "; nplanes; Events", 20,0,20);
    utility::makeHisto(my_histos,"npix", "; npix; Events", 4,0,4);
    utility::makeHisto(my_histos,"monicelli_err", "; Track expected error; Events", 100,0,15);
    utility::makeHisto(my_histos,"slopeX", "; Track X slope [mm per mm]; Events", 100,-0.001,0.001);
    utility::makeHisto(my_histos,"ampRank1", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank2", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank3", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank4", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank5", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank6", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"wave1", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"wave2", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"wave3", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"wave4", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"wave5", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"wave6", "; Time [ns]; Voltage [mV]", 101, 0.0, 10.05); //502,0.0,50.1);
    utility::makeHisto(my_histos,"deltaX", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    for(int ivar=0;ivar<nvar;ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_var"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    }
    utility::makeHisto(my_histos,"deltaX_TopRow", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_BotRow", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaY", "; Y_{reco} - Y_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaY_RightCol", "; Y_{reco} - Y_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaY_LeftCol", "; Y_{reco} - Y_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"timePhotek", "", 500, -225.0, -175.0);
    utility::makeHisto(my_histos,"timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiff_amp2", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiff_amp3", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_goodSig", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_goodSig", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    
    //Global 2D histograms
    utility::makeHisto(my_2d_histos,"relFracTot_vs_x", "; X [mm]; relFracTot", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"relFracMaxAmp_vs_x", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"relFracDC_vs_x_channel_top", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"weighted_timeDiff_vs_x", "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_highThreshold_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator", "; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_denominator", "; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/0.02,xmin,xmax, (ymax-ymin)/0.1,ymin,ymax);
    utility::makeHisto(my_2d_histos,"clusterSize_vs_x", "; X [mm]; Cluster Size", (xmax-xmin)/0.02,xmin,xmax, 20,-0.5,19.5);
    utility::makeHisto(my_2d_histos,"AmpLeftOverAmpLeftandRightTop_vs_x", "; X [mm]; AmpLeftoverAmpLeftandRightTop", (xmax-xmin)/0.03,-0.4,0.4, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpLeftOverAmpLeftandRightBot_vs_x", "; X [mm]; AmpLeftoverAmpLeftandRightBot", (xmax-xmin)/0.03,-0.4,0.4, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpTopOverAmpTopandBotRight_vs_y", "; Y [mm]; AmpTopOverAmpTopandBotRight", (ymax-ymin)/0.03,-0.5,0.5, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpTopOverAmpTopandBotLeft_vs_y", "; Y [mm]; AmpTopOverAmpTopandBotLeft", (ymax-ymin)/0.03,-0.5,0.5, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax", "",           (5*pitch)/0.002,-2.5*pitch,2.5*pitch, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTopPad1_vs_deltaXmaxneg","",   pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTopPad2_vs_deltaXmaxpos","",   pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBotPad3_vs_deltaXmaxpos","",   pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBotPad4_vs_deltaXmaxneg","",   pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTop_vs_deltaXmaxTopPad","",    pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBot_vs_deltaXmaxBotPad","",    pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andAdjPad_vs_deltaXmaxAdjPad","", pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andAdjPad_vs_x","",               pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp123_vs_deltaXmax",          "",    pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp2OverAmp2and3_vs_deltaXmax",        "",    pitch/0.002,-pitch/2.0,pitch/2.0, 100,0.0,1.0);    
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Ytrack", "; Y_{track} [mm]; #Y_{reco} - Y_{track} [mm]", (ymax-ymin)/0.05,ymin,ymax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xreco", "; X_{reco} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Yreco", "; Y_{reco} [mm]; #Y_{reco} - Y_{track} [mm]", (ymax-ymin)/0.05,ymin,ymax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xtrack", "; X_{track} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xreco", "; X_{reco} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_A1OverA12Above0p75", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"Xreco_vs_Xtrack", "; X_{track} [mm]; #X_{reco} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_2d_histos,"Yreco_vs_Ytrack", "; Y_{track} [mm]; #Y_{reco} [mm]", (ymax-ymin)/0.005,ymin,ymax, (ymax-ymin)/0.005,ymin,ymax);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp1OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + A_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp2OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + A_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp3OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + m_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);

    //Define 3D histograms
    utility::makeHisto(my_3d_histos,"totgoodamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500);	
    utility::makeHisto(my_3d_histos,"totamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500);
    utility::makeHisto(my_3d_histos,"totamplitudePad_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 500,0,500);
    utility::makeHisto(my_3d_histos,"totrawamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500);
    utility::makeHisto(my_3d_histos,"amp123_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500);
    utility::makeHisto(my_3d_histos,"amp12_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/0.02,ymin,ymax, 500,0,500);	
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_amp2", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_amp3", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_goodSig_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_goodSig_vs_xy", "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    
    //Define 2d prof
    utility::makeHisto(my_2d_prof,"efficiency_vs_xy_DCRing", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);	
    utility::makeHisto(my_2d_prof,"efficiency_vs_xy_Strip2or5", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);	
    
    //Define 1d prof
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp1OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp2OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp3OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    
    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    utility::makeHisto(my_efficiencies,"event_sel_weight","",9,0,9);
    utility::makeHisto(my_efficiencies,"efficiency_vs_x","; X [mm]",xbins,xmin,xmax);
    utility::makeHisto(my_efficiencies,"efficiency_vs_xy","; X [mm]; Y [mm]",xbins,xmin,xmax, ybins,ymin,ymax);
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    const auto& isPadSensor = tr.getVar<bool>("isPadSensor");
    //const auto& xSlices = tr.getVar<std::vector<std::vector<double>>>("xSlices");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
    const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
    bool plotWaveForm = true;
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
        const auto& rawAmpLGAD = tr.getVec<std::vector<float>>("rawAmpLGAD");
        const auto& corrTime = tr.getVec<double>("corrTime");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& baselineRMS = tr.getVec<std::vector<float>>("baselineRMS");
        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& ntracks_alt = tr.getVar<int>("ntracks_alt");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& xSlope = tr.getVar<float>("xSlope");
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& xErrDUT = tr.getVar<float>("xErrDUT");
        const auto& x_var = tr.getVec<float>("x_var");
        //const auto& y_var = tr.getVec<float>("y_var");
        const auto& sensorCenter = tr.getVar<double>("sensorCenter");
        const auto& sensorCenterY = tr.getVar<double>("sensorCenterY");
        const auto& padx = tr.getVar<double>("padx");
        const auto& padxAdj = tr.getVar<double>("padxAdj");
        const auto& x_reco = tr.getVar<double>("x_reco");
        const auto& y_reco = tr.getVar<double>("y_reco");
        const auto& weighted_time = tr.getVar<double>("weighted_time");
        const auto& weighted2_time = tr.getVar<double>("weighted2_time");
        const auto& weighted_time_goodSig = tr.getVar<double>("weighted_time_goodSig");
        const auto& weighted2_time_goodSig = tr.getVar<double>("weighted2_time_goodSig");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& relFracDC = tr.getVar<double>("relFracDC");
        const auto& relFrac = tr.getVec<std::vector<double>>("relFrac");
        const auto& totAmpLGAD = tr.getVar<double>("totAmpLGAD");
        const auto& totRawAmpLGAD = tr.getVar<double>("totRawAmpLGAD");
        const auto& totGoodAmpLGAD = tr.getVar<double>("totGoodAmpLGAD");
        const auto& Amp123 = tr.getVar<double>("Amp123");
        const auto& Amp12 = tr.getVar<double>("Amp12");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& amp2Indexes = tr.getVar<std::pair<int,int>>("amp2Indexes");
        const auto& amp3Indexes = tr.getVar<std::pair<int,int>>("amp3Indexes");
        const auto& amp4Indexes = tr.getVar<std::pair<int,int>>("amp4Indexes");
        const auto& amp5Indexes = tr.getVar<std::pair<int,int>>("amp5Indexes");
        const auto& amp6Indexes = tr.getVar<std::pair<int,int>>("amp6Indexes");
        const auto& ampIndexesAdjPad = tr.getVar<std::pair<int,int>>("ampIndexesAdjPad");
        const auto& deltaXmax = tr.getVar<double>("deltaXmax");
        const auto& deltaXmaxpos = tr.getVar<double>("deltaXmaxpos");
        const auto& deltaXmaxneg = tr.getVar<double>("deltaXmaxneg"); 
        const auto& deltaXmaxTopPad = tr.getVar<double>("deltaXmaxTopPad"); 
        const auto& deltaXmaxBotPad = tr.getVar<double>("deltaXmaxBotPad");
        const auto& deltaXmaxAdjPad = tr.getVar<double>("deltaXmaxAdjPad"); 
        const auto& AmpLeftOverAmpLeftandRightTop = tr.getVar<double>("AmpLeftOverAmpLeftandRightTop");
        const auto& AmpLeftOverAmpLeftandRightBot = tr.getVar<double>("AmpLeftOverAmpLeftandRightBot");
        const auto& AmpTopOverAmpTopandBotRight = tr.getVar<double>("AmpTopOverAmpTopandBotRight");
        const auto& AmpTopOverAmpTopandBotLeft = tr.getVar<double>("AmpTopOverAmpTopandBotLeft");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");
        const auto& Amp1OverAmp1andTop = tr.getVar<double>("Amp1OverAmp1andTop");
        const auto& Amp1OverAmp1andBot = tr.getVar<double>("Amp1OverAmp1andBot");
        const auto& Amp1OverAmp1andAdjPad = tr.getVar<double>("Amp1OverAmp1andAdjPad");
        const auto& Amp2OverAmp2and3 = tr.getVar<double>("Amp2OverAmp2and3");
        const auto& Amp1OverAmp123 = tr.getVar<double>("Amp1OverAmp123");
        const auto& Amp2OverAmp123 = tr.getVar<double>("Amp2OverAmp123");
        const auto& Amp3OverAmp123 = tr.getVar<double>("Amp3OverAmp123");
        const auto& hasGlobalSignal_lowThreshold = tr.getVar<bool>("hasGlobalSignal_lowThreshold");
        const auto& hasGlobalSignal_highThreshold = tr.getVar<bool>("hasGlobalSignal_highThreshold");
        const auto& clusterSize = tr.getVar<int>("clusterSize");
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& stripCenterYPositionLGAD = tr.getVec<std::vector<double>>("stripCenterYPositionLGAD");
        const auto& stripWidth = tr.getVar<double>("stripWidth");
        const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
        const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold;
        bool passTrigger = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        bool pass = passTrigger && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = ((maxAmpIndex >= lowGoodStripIndex && maxAmpIndex <= highGoodStripIndex) || (isPadSensor == true));
        bool inBottomRow = y>ySlices[0][0] && y<ySlices[0][1];
        bool inTopRow = y>ySlices[1][0] && y<ySlices[1][1];
        bool maxAmpinPad1 = amp1Indexes.first==0 && amp1Indexes.second==0;
        bool maxAmpinPad2 = amp1Indexes.first==0 && amp1Indexes.second==1;
        bool maxAmpinPad3 = amp1Indexes.first==1 && amp1Indexes.second==1;
        bool maxAmpinPad4 = amp1Indexes.first==1 && amp1Indexes.second==0;
        bool hitInMiddleofPad = deltaXmaxAdjPad != 999 && deltaXmaxAdjPad != -999; 
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
                const auto& relFracChannel = relFrac[rowIndex][i];
                const auto& rawAmpChannel = rawAmpLGAD[rowIndex][i];
                const auto& noise = baselineRMS[rowIndex][i]; 
                bool goodNoiseAmp = ampChannel>noiseAmpThreshold;
                bool goodSignalAmp = ampChannel>signalAmpThreshold;
                double time = timeLGAD[rowIndex][i];
                bool isMaxChannel = amp1Indexes.first == rowIndex && amp1Indexes.second == int(i);
                bool goodHit = goodNoiseAmp && goodMaxLGADAmp;
                if(i==1 || i==4) goodHitGlobal2and5 = goodHitGlobal2and5 || (isMaxChannel && goodHit);
                utility::fillHisto(pass,                                                    my_histos["amp"+r+s], ampChannel);
                utility::fillHisto(pass && isMaxChannel,                                    my_histos["ampMax"+r+s], ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_histos["relFrac"+r+s], relFracChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad1 || maxAmpinPad2),       my_histos["relFrac_bottom"+r+s], relFracChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad3 || maxAmpinPad4),       my_histos["relFrac_top"+r+s], relFracChannel);
                utility::fillHisto(pass,                                                    my_histos["time"+r+s], time);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["timeDiff_channel"+r+s], time-photekTime);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["baselineRMS"+r+s], noise);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["weighted_timeDiff_channel"+r+s], weighted_time-photekTime);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_histos["weighted_time-time_channel"+r+s], weighted_time-time);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_2d_histos["baselineRMS_vs_x_channel"+r+s], x,noise);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["amp_vs_x_channel"+r+s], x,ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_x_channel"+r+s], x,relFracChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_y_channel"+r+s], y,relFracChannel);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s], deltaXmax, Amp1OverAmp1and2);
                utility::fillHisto(pass && goodNoiseAmp,                                    my_2d_histos["efficiency_vs_xy_lowThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(pass && goodSignalAmp,                                   my_2d_histos["efficiency_vs_xy_highThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_2d_histos["timeDiff_vs_x_channel"+r+s], x,time-photekTime);
                utility::fillHisto(pass && goodHit && inBottomRow,                          my_2d_histos["relFrac_vs_x_channel_bottom"+r+s], x, relFracChannel);
                utility::fillHisto(pass && goodHit && inBottomRow,                          my_2d_histos["amp_vs_x_channel_bottom"+r+s], x, ampChannel);
                utility::fillHisto(pass && goodHit && inTopRow,                             my_2d_histos["relFrac_vs_x_channel_top"+r+s], x, relFracChannel);
                utility::fillHisto(pass && goodHit && inTopRow,                             my_2d_histos["amp_vs_x_channel_top"+r+s], x, ampChannel);
                utility::fillHisto(pass && goodHit && inTopRow && time!=0 && photekTime!=0, my_2d_histos["delay_vs_x_channel_top"+r+s], x, timeLGAD[rowIndex][i] - photekTime);
                utility::fillHisto(firstEvent,                                              my_2d_histos["stripBoxInfo"+r+s], stripCenterXPositionLGAD[rowIndex][i],stripWidth);
                utility::fillHisto(firstEvent,                                              my_2d_histos["stripBoxInfoY"+r+s], stripCenterYPositionLGAD[rowIndex][i],stripWidth);
                utility::fillHisto(pass,                                                    my_3d_histos["baselineRMS_vs_xy_channel"+r+s], x,y,noise);
                utility::fillHisto(pass && goodHit,                                         my_3d_histos["amplitude_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad1 || maxAmpinPad2),       my_3d_histos["amplitudeTop_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad3 || maxAmpinPad4),       my_3d_histos["amplitudeBot_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad1 || maxAmpinPad4),       my_3d_histos["amplitudeLeft_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit && (maxAmpinPad2 || maxAmpinPad3),       my_3d_histos["amplitudeRight_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_3d_histos["raw_amp_vs_xy_channel"+r+s], x,y,rawAmpChannel);
                utility::fillHisto(pass && goodHit && isMaxChannel,                         my_3d_histos["timeDiff_vs_xy_channel"+r+s], x,y,time-photekTime);
                utility::fillHisto(passTrigger,                                             my_2d_prof["efficiency_vs_xy_highThreshold_prof_channel"+r+s], x,y,ampChannel > signalAmpThreshold);
                utility::fillHisto(passTrigger && isMaxChannel,                             my_2d_prof["efficiency_vs_xy_highThreshold_prof"], x,y,goodHit);
                utility::fillHisto(passTrigger && isMaxChannel,                             my_efficiencies["efficiency_vs_x"], goodHit,x);
                utility::fillHisto(passTrigger && isMaxChannel,                             my_efficiencies["efficiency_vs_xy"], goodHit,x,y);
            }
            rowIndex++;
        }
        utility::fillHisto(pass,                                                                           my_histos["timePhotek"],photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["deltaX"], x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad2), my_histos["deltaX_TopRow"], x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad3 || maxAmpinPad4), my_histos["deltaX_BotRow"], x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["deltaY"], y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad2 || maxAmpinPad3), my_histos["deltaY_RightCol"], y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad4), my_histos["deltaY_LeftCol"], y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["chi2"], chi2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ntracks_alt"], ntracks_alt);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["nplanes"], nplanes);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["npix"], npix);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["monicelli_err"], xErrDUT);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["slopeX"], xSlope);
        for(unsigned int ivar=0; ivar < x_var.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                               my_histos["deltaX_var"+std::to_string(ivar)], x_reco-x_var[ivar]);
        }
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank1"], ampLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank2"], ampLGAD[amp2Indexes.first][amp2Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank3"], ampLGAD[amp3Indexes.first][amp3Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank4"], ampLGAD[amp4Indexes.first][amp4Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank5"], ampLGAD[amp5Indexes.first][amp5Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ampRank6"], ampLGAD[amp6Indexes.first][amp6Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["timeDiff"], maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["timeDiff_amp2"], amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["timeDiff_amp3"], amp3Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["weighted_timeDiff"], weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["weighted2_timeDiff"], weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["weighted_timeDiff_goodSig"], weighted_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["weighted2_timeDiff_goodSig"], weighted2_time_goodSig-photekTime);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["relFracMaxAmp_vs_x"], padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass,                                                                           my_2d_histos["relFracDC_vs_x_channel_top"], x,relFracDC);
        utility::fillHisto(pass,                                                                           my_2d_histos["efficiency_vs_xy_denominator"], x,y);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["relFracTot_vs_x"], padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["relFracTot_vs_x"], padxAdj, relFrac[ampIndexesAdjPad.first][ampIndexesAdjPad.second]);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad2),                       my_2d_histos["AmpLeftOverAmpLeftandRightTop_vs_x"], x-sensorCenter,AmpLeftOverAmpLeftandRightTop);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad3 || maxAmpinPad4),                       my_2d_histos["AmpLeftOverAmpLeftandRightBot_vs_x"], x-sensorCenter,AmpLeftOverAmpLeftandRightBot);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad2 || maxAmpinPad3),                       my_2d_histos["AmpTopOverAmpTopandBotRight_vs_y"], y-sensorCenterY,AmpTopOverAmpTopandBotRight);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad4),                       my_2d_histos["AmpTopOverAmpTopandBotLeft_vs_y"], y-sensorCenterY,AmpTopOverAmpTopandBotLeft);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax"], fabs(deltaXmax),Amp1OverAmp1and2);
        utility::fillHisto(pass && maxAmpinPad1 && hitInMiddleofPad,                                       my_2d_histos["Amp1OverAmp1andTopPad1_vs_deltaXmaxneg"], deltaXmaxneg,Amp1OverAmp1andTop);
        utility::fillHisto(pass && maxAmpinPad2 && hitInMiddleofPad,                                       my_2d_histos["Amp1OverAmp1andTopPad2_vs_deltaXmaxpos"], deltaXmaxpos,Amp1OverAmp1andTop); 
        utility::fillHisto(pass && maxAmpinPad3 && hitInMiddleofPad,                                       my_2d_histos["Amp1OverAmp1andBotPad3_vs_deltaXmaxpos"], deltaXmaxpos,Amp1OverAmp1andBot);    
        utility::fillHisto(pass && maxAmpinPad4 && hitInMiddleofPad,                                       my_2d_histos["Amp1OverAmp1andBotPad4_vs_deltaXmaxneg"], deltaXmaxneg,Amp1OverAmp1andBot);  
        utility::fillHisto(pass && (maxAmpinPad1 || maxAmpinPad2) && hitInMiddleofPad,                     my_2d_histos["Amp1OverAmp1andTop_vs_deltaXmaxTopPad"], fabs(deltaXmaxTopPad),Amp1OverAmp1andTop);
        utility::fillHisto(pass && (maxAmpinPad3 || maxAmpinPad4) && hitInMiddleofPad,                     my_2d_histos["Amp1OverAmp1andBot_vs_deltaXmaxBotPad"], fabs(deltaXmaxBotPad),Amp1OverAmp1andBot);
        utility::fillHisto(pass && hitInMiddleofPad,                                                       my_2d_histos["Amp1OverAmp1andAdjPad_vs_deltaXmaxAdjPad"], fabs(deltaXmaxAdjPad),Amp1OverAmp1andAdjPad);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["Amp1OverAmp1andAdjPad_vs_x"], x-sensorEdges[0][0],Amp1OverAmp1andAdjPad);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos["Amp1OverAmp123_vs_deltaXmax"], fabs(deltaXmax),Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos["Xtrack_vs_Amp1OverAmp123"], x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos["Xtrack_vs_Amp2OverAmp123"], x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos["Xtrack_vs_Amp3OverAmp123"], x,Amp3OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_Xtrack"], x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_Xreco"], x_reco,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaY_vs_Ytrack"], y,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaY_vs_Yreco"], y_reco,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaXmax_vs_Xtrack"], x,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaXmax_vs_Xreco"], x_reco,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["weighted_timeDiff_vs_x"], x,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["Xreco_vs_Xtrack"], x,x_reco);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["Yreco_vs_Ytrack"], y,y_reco);
        utility::fillHisto(pass && highRelAmp1,                                                            my_2d_histos["deltaX_vs_Xtrack_A1OverA12Above0p75"], x,x_reco-x);	    
        utility::fillHisto(pass && highRelAmp1,                                                            my_2d_histos["Amp2OverAmp2and3_vs_deltaXmax"], deltaXmax,Amp2OverAmp2and3);
        utility::fillHisto(pass && goodDCAmp,                                                              my_2d_histos["efficiencyDC_vs_xy_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold,                                           my_2d_histos["efficiency_vs_xy_lowThreshold_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,                                          my_2d_histos["efficiency_vs_xy_highThreshold_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,                                          my_2d_histos["clusterSize_vs_x"], x,clusterSize);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["totgoodamplitude_vs_xy"], x,y,totGoodAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["totamplitude_vs_xy"], x,y,totAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["totamplitudePad_vs_xy"], x,y,totAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["totrawamplitude_vs_xy"], x,y,totRawAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["amp123_vs_xy"], x,y, Amp123);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["amp12_vs_xy"], x,y, Amp12);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["timeDiff_vs_xy"], x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["timeDiff_vs_xy_amp2"], x,y,amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["timeDiff_vs_xy_amp3"], x,y,amp3Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["weighted_timeDiff_vs_xy"], x,y,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["weighted2_timeDiff_vs_xy"], x,y,weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["weighted_timeDiff_goodSig_vs_xy"], x,y,weighted_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos["weighted2_timeDiff_goodSig_vs_xy"], x,y,weighted2_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof["Xtrack_vs_Amp1OverAmp123_prof"], x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof["Xtrack_vs_Amp2OverAmp123_prof"], x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof["Xtrack_vs_Amp3OverAmp123_prof"], x,Amp3OverAmp123);
        utility::fillHisto(passTrigger,                                                                    my_2d_prof["efficiency_vs_xy_Strip2or5"], x,y,goodHitGlobal2and5);
        utility::fillHisto(passTrigger,                                                                    my_2d_prof["efficiency_vs_xy_DCRing"], x,y,goodDCAmp);

        // Fill wave form histos once
        bool maxAmpInCenter = maxAmpIndex == 2;// || maxAmpIndex == 3;
        bool directHit = (abs( corrAmp[2] - corrAmp[4]) / corrAmp[2]) < 0.05;
        //if(plotWaveForm && pass && maxAmpInCenter && goodMaxLGADAmp && maxAmpLGAD > 99.0 &&  maxAmpLGAD < 101.0)
        //{
        //    std::cout<<abs( corrAmp[2] - corrAmp[4])<<" "<<corrAmp[2]<<" "<<(abs( corrAmp[2] - corrAmp[4]) / corrAmp[2])<<std::endl;
        //}
        if(plotWaveForm && pass && maxAmpInCenter && goodMaxLGADAmp && maxAmpLGAD > 116.0 && maxAmpLGAD < 120.0 && directHit)
        {
            const auto& channel = tr.getVecVec<float>("channel");
            const auto& time = tr.getVecVec<float>("time");
            //std::cout<<channel[0].size()<<" "<<channel[0][0]<<" "<<time[0].size()<<" "<<1e9*(time[0][0]-time[0][0])<<" "<<1e9*(time[0][501]-time[0][0])<<std::endl;
            //std::map<int, double> timeCalibrationCorrection = {{0,0.0}, {1,10.5553183648148}, {2,10.6590122524753}, {3,10.6470996902006}, {4,10.6075997712141}, {5,10.6432860123283}, {6,10.6622858488865}, {7,0.0}};
            const auto& timeCalibrationCorrection = tr.getVar<std::map<int, double>>("timeCalibrationCorrection");
            std::cout<<"x "<<x<<" y"<<y<<std::endl;

            for(unsigned int i = 0; i < channel.size(); i++)
            {
                auto t = timeCalibrationCorrection.at(i) - 10.0;
                if(i==1) t += -0.05*1;
                std::cout<<i<<" "<<t<<" "<<t/0.05<<" "<<int(t/0.05)<<" "<<maxAmpLGAD<<std::endl;
                int timeFix = int(t/0.05);
                if(i==0 || i==7) continue;
                std::string index = std::to_string(i);
                for(unsigned int j = 0; j < time[0].size(); j++)
                {                                        
                    unsigned int shift = j-timeFix+170;
                    if(shift>time[0].size()) continue;
                    my_histos["wave"+index]->SetBinContent(j, channel[i][shift]);
                }
            }
            if(channel[0][0] != 0) plotWaveForm = false;
        }
        
	// Example Fill event selection efficiencies
	my_efficiencies["event_sel_weight"]->SetUseWeightedEvents();
	my_efficiencies["event_sel_weight"]->FillWeighted(true,1.0,0);
    } //event loop
}

void Analyze::WriteHistos(TFile* outfile)
{
    outfile->cd();
    for(const auto& p : my_histos)       p.second->Write();
    for(const auto& p : my_2d_histos)    p.second->Write();
    for(const auto& p : my_3d_histos)    p.second->Write();
    for(const auto& p : my_2d_prof)      p.second->Write();
    for(const auto& p : my_1d_prof)      p.second->Write();
    for(const auto& p : my_efficiencies) p.second->Write();
    std::cout<<"Made it to the end of writing histos"<<std::endl;
}

