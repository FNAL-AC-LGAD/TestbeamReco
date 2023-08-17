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
    const auto& xBinSize = tr.getVar<double>("xBinSize");
    const auto& yBinSize = tr.getVar<double>("yBinSize");
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");
    const auto& regionsOfIntrest = tr.getVar<std::vector<utility::ROI>>("regionsOfIntrest");
    int xbins = 175;
    int ybins = 175;
    double xBinSizePad = 0.5;
    double yBinSizePad = 0.5;

    int timeDiffNbin = 200; // 200
    double timeDiffLow = -1.0;
    double timeDiffHigh = 1.0;
    int timeDiffYnbin = 50;

    int    bvNbin = 500;
    double bvLow  = 0.0;
    double bvHigh = 500.0;

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
            utility::makeHisto(my_histos,"timeDiffTracker_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"weighted2_timeDiff_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            //utility::makeHisto(my_histos,"timeDiff_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            //utility::makeHisto(my_histos,"timeDiffTracker_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            // utility::makeHisto(my_histos,"weighted_timeDiff_tracker_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"weighted_time-time_channel"+r+s, "", timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_histos,"relFrac_top"+r+s, "", 100, 0.0, 1.0 );
            utility::makeHisto(my_histos,"relFrac_bottom"+r+s, "", 100, 0.0, 1.0);
            utility::makeHisto(my_histos,"baselineRMS"+r+s,"", 200,-10.0,10.0);
            utility::makeHisto(my_histos,"risetime"+r+s,"", 150,0.0,1500.0);
            utility::makeHisto(my_histos,"charge"+r+s,"", 300,0.0,150.0);
            utility::makeHisto(my_histos,"ampChargeRatio"+r+s,"", 300,0.0,15.0);
            utility::makeHisto(my_histos,"slewrate"+r+s,"", 300,0.0,400.0);
            utility::makeHisto(my_histos,"slewRateChargeRatio"+r+s,"", 300,0.0,30.0);
            utility::makeHisto(my_histos,"deltaX_oneStrip"+r+s, "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);

            for (unsigned int ch = 0; ch < row.size(); ch++)
            {
                const auto& c = std::to_string(ch);
                utility::makeHisto(my_histos,"amp"+r+s+"From"+c,"", 405,-5.0,400.0);
            }
           
            for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
            {
                utility::makeHisto(my_histos,"baselineRMS"+r+s+regionsOfIntrest[k].getName(),"", 50,0.0,10.0);
                utility::makeHisto(my_histos,"risetime"+r+s+regionsOfIntrest[k].getName(),"", 100,200.0,1000.0);
                utility::makeHisto(my_histos,"charge"+r+s+regionsOfIntrest[k].getName(),"", 50,0.0,40.0);
                utility::makeHisto(my_histos,"ampChargeRatio"+r+s+regionsOfIntrest[k].getName(),"", 50,0.0,10.0);
                utility::makeHisto(my_histos,"slewrate"+r+s+regionsOfIntrest[k].getName(),"", 100,0.0,400.0);
                utility::makeHisto(my_histos,"slewRateChargeRatio"+r+s+regionsOfIntrest[k].getName(),"", 100,0.0,30.0);
                utility::makeHisto(my_histos,"baselineRMSSlewRateRatio"+r+s+regionsOfIntrest[k].getName(),"", 100,0.0,100.0);
                utility::makeHisto(my_histos,"timeDiff_channel"+r+s+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
                utility::makeHisto(my_histos,"timeDiffTracker_channel"+r+s+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
                utility::makeHisto(my_histos,"weighted2_timeDiff_channel"+r+s+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
                utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_channel"+r+s+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);

                utility::makeHisto(my_2d_histos,"AmpOverMaxAmp_vs_x_channel"+r+s+regionsOfIntrest[k].getName(), "; X [mm]; ampOverMaxAmp", 171,-0.855,0.855, 101,0.0,1.01);
            }

            //Define 2D histograms
            utility::makeHisto(my_2d_histos,"AmpOverMaxAmp_vs_x_channel"+r+s, "; X [mm]; ampOverMaxAmp", 171,-0.855,0.855, 101,0.0,1.01);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            // utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel"+r+s+"_NearHit", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel_top"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"delay_vs_x_channel_top"+r+s, "; X [mm]; Arrival time [ns]", (xmax-xmin)/xBinSize,xmin,xmax, 100,-11,-10);
            utility::makeHisto(my_2d_histos,"timeDiff_vs_x_channel"+r+s, "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_2d_histos,"timeDiffTracker_vs_x_channel"+r+s, "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel_bottom"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"relFrac_vs_y_channel"+r+s, "; Y [mm]; relFrac", (ymax-ymin)/yBinSize,ymin,ymax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s, "; X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{Max} + Amp_{2}", (5*pitch)/0.02,-2.5*pitch,2.5*pitch, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"risetime_vs_amp"+r+s, "; amp [mV]; risetime [ps]", 100,0.0,150.0, 100,100.0,1500.0);
            utility::makeHisto(my_2d_histos,"baselineRMS_vs_x_channel"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_y_channel"+r+s, "; Y [mm]; amp", (ymax-ymin)/yBinSize,ymin,ymax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel_top"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel_bottom"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"stripBoxInfo"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);
            utility::makeHisto(my_2d_histos,"stripBoxInfoY"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);

            utility::makeHisto(my_2d_histos,"timeDiff_vs_BV_channel"+r+s,    "; BV [V]; #Delta t [ps]", bvNbin,bvLow,bvHigh, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_2d_histos,"amp_vs_BV_channel"+r+s,         "; BV [V]; amp [mV]"     , bvNbin,bvLow,bvHigh, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"risetime_vs_BV_channel"+r+s,    "; BV [V]; risetime [ps]", bvNbin,bvLow,bvHigh, 100,100.0,1500.0);
            utility::makeHisto(my_2d_histos,"baselineRMS_vs_BV_channel"+r+s, "; BV [V]; amp [mV]"     , bvNbin,bvLow,bvHigh, 250,0.0,250); 
            utility::makeHisto(my_2d_histos,"slewrate_vs_BV_channel"+r+s,    "; BV [V]; slewrate"     , bvNbin,bvLow,bvHigh, 300,0.0,400.0); 

            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_noNeighb_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highFrac_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_numerator_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_prof,  "efficiency_vs_xy_prof_channel"+r+s, "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);


            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_noNeighb_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highFrac_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_numerator_tight_channel"+r+s, "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);


            /*for (unsigned int ch = 0; ch < row.size(); ch++)
            {
                const auto& c = std::to_string(ch);
                utility::makeHisto(my_2d_histos,"wave"+r+s+"From"+c+"","", timeDiffNbin,-5.,5.,100,-85,15);
                utility::makeHisto(my_2d_histos,"wave"+r+s+"From"+c+"goodHit","", timeDiffNbin,-5.,5.,100,-85,15);
            }*/

            //Define 3D histograms
            utility::makeHisto(my_3d_histos,"baselineRMS_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"amplitude_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
            
            utility::makeHisto(my_3d_histos,"baselineRMSNew_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 300,0,50 );
            utility::makeHisto(my_3d_histos,"amplitudeNew_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 300,0,500 );

            utility::makeHisto(my_3d_histos,"amplitudeTop_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeBot_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeLeft_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"amplitudeRight_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"raw_amp_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
            utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_channel"+r+s, "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_3d_histos,"timeDiffTracker_vs_xy_channel"+r+s, "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
            utility::makeHisto(my_3d_histos,"risetime_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 300,0.0,1500.0);
            utility::makeHisto(my_3d_histos,"charge_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,150.0);
            utility::makeHisto(my_3d_histos,"ampChargeRatio_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,100.0);
            utility::makeHisto(my_3d_histos,"slewRate_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,500.0);
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
    utility::makeHisto(my_histos,"slopeY", "; Track Y slope [mm per mm]; Events", 100,-0.001,0.001);
    utility::makeHisto(my_histos,"ampRank1", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank2", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank3", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank4", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank5", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"ampRank6", "", 450, -50.0, 400.0);
    utility::makeHisto(my_histos,"wave0", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave1", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave2", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave3", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave4", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave5", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave6", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"wave7", "; Time [ns]; Voltage [mV]", 500,-25.0,25.0);
    utility::makeHisto(my_histos,"deltaX", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_noNeighb", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_noNeighb_onMetal", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_highFrac", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_highFrac_onMetal", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_oneStrip", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_oneStrip_onMetal", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_twoStrips", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_twoStrips_noMetal", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaXBasic", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaYBasic", "; Y_{reco} - Y_{track} [mm]; Events", 200,-30.5,30.5);
    utility::makeHisto(my_histos,"dXdFrac", "; dX/dFraction [mm]; Events", 200,-19.0,1.0);
    utility::makeHisto(my_histos,"deltaX_TopRow", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_BotRow", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaY", "; Y_{reco} - Y_{track} [mm]; Events", 200,-30.5,30.5);
    utility::makeHisto(my_histos,"deltaY_oneStrip", "; Y_{reco} - Y_{track} [mm]; Events", 200,-30.5,30.5);
    utility::makeHisto(my_histos,"deltaY_twoStrips", "; Y_{reco} - Y_{track} [mm]; Events", 200,-30.5,30.5);
    utility::makeHisto(my_histos,"deltaY_RightCol", "; Y_{reco} - Y_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaY_LeftCol", "; Y_{reco} - Y_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"timePhotek", "", 500, -225.0, -175.0);
    utility::makeHisto(my_histos,"timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiff_amp2", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiff_amp3", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_tracker", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
   
    utility::makeHisto(my_histos,"timeDiffLGADXTrackerY", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffLGADXY", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffLGADXY0", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffLGADX", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTrackerX", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_LGADXY", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_LGADX", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_LGADXY", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_LGADX", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"average_timeDiff_LGADXY", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"average_timeDiff_LGADX", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    
    utility::makeHisto(my_histos,"weighted_timeDiff_LGADXY_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_LGADX_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_LGADXY_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_LGADX_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"average_timeDiff_LGADXY_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"average_timeDiff_LGADX_2Strip", "", timeDiffNbin,timeDiffLow,timeDiffHigh);


    utility::makeHisto(my_histos,"deltaX_tight", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_oneStrip_tight", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_oneStrip_onMetal_tight", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_twoStrips_tight", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"deltaX_twoStrips_noMetal_tight", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"timeDiff_tight", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker_tight", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tight", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_tight", "", timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_histos,"weighted_timeDiff_goodSig", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_goodSig", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"clusterSize", "; Cluster Size", 8,0.0,8.0);
    utility::makeHisto(my_histos,"risetime","", 150,0.0,1500.0);
    utility::makeHisto(my_histos,"charge","", 300,0.0,150.0);
    utility::makeHisto(my_histos,"ampChargeRatio","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"index_diff", "; index1 - index2; Events", 16,-8,8);

    utility::makeHisto(my_histos,"ampMax_Overall", "", 450, -50.0, 400.0); 
    utility::makeHisto(my_histos,"risetime_Overall","", 300,0.0,1500.0);
    utility::makeHisto(my_histos,"charge_Overall","", 300,0.0,150.0);
    utility::makeHisto(my_histos,"ampChargeRatio_Overall","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"baselineRMS_Overall","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"slewrate_Overall","", 300,0.0,400.0);
    utility::makeHisto(my_histos,"slewRateChargeRatio_Overall","", 300,0.0,50.0);
    utility::makeHisto(my_histos,"weighted2_jitter_Overall","", 200,0.0,100.0);
    utility::makeHisto(my_histos,"weighted2_jitter_NewDef_Overall","", 200,0.0,100.0);

    utility::makeHisto(my_histos,"timeDiff_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_tracker_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_Overall", "", timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_histos,"ampMax_Metal", "", 450, -50.0, 400.0); 
    utility::makeHisto(my_histos,"risetime_Metal","", 300,0.0,1500.0);
    utility::makeHisto(my_histos,"charge_Metal","", 300,0.0,150.0);
    utility::makeHisto(my_histos,"ampChargeRatio_Metal","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"baselineRMS_Metal","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"slewrate_Metal","", 300,0.0,400.0);
    utility::makeHisto(my_histos,"slewRateChargeRatio_Metal","", 300,0.0,50.0);
    utility::makeHisto(my_histos,"weighted2_jitter_Metal","", 200,0.0,100.0);
    utility::makeHisto(my_histos,"weighted2_jitter_NewDef_Metal","", 200,0.0,100.0); 

    utility::makeHisto(my_histos,"timeDiff_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_tracker_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_Metal", "", timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_histos,"ampMax_Gap", "", 450, -50.0, 400.0); 
    utility::makeHisto(my_histos,"risetime_Gap","", 300,0.0,1500.0);
    utility::makeHisto(my_histos,"charge_Gap","", 300,0.0,150.0);
    utility::makeHisto(my_histos,"ampChargeRatio_Gap","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"baselineRMS_Gap","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"slewrate_Gap","", 300,0.0,400.0);
    utility::makeHisto(my_histos,"slewRateChargeRatio_Gap","", 300,0.0,50.0);
    utility::makeHisto(my_histos,"weighted2_jitter_Gap","", 200,0.0,100.0);
    utility::makeHisto(my_histos,"weighted2_jitter_NewDef_Gap","", 200,0.0,100.0); 

    utility::makeHisto(my_histos,"timeDiff_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_tracker_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_Gap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_histos,"ampMax_MidGap", "", 450, -50.0, 400.0); 
    utility::makeHisto(my_histos,"risetime_MidGap","", 300,0.0,1500.0);
    utility::makeHisto(my_histos,"charge_MidGap","", 300,0.0,150.0);
    utility::makeHisto(my_histos,"ampChargeRatio_MidGap","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"baselineRMS_MidGap","", 300,0.0,15.0);
    utility::makeHisto(my_histos,"slewrate_MidGap","", 300,0.0,400.0);
    utility::makeHisto(my_histos,"slewRateChargeRatio_MidGap","", 300,0.0,50.0);
    utility::makeHisto(my_histos,"weighted2_jitter_MidGap","", 200,0.0,100.0);
    utility::makeHisto(my_histos,"weighted2_jitter_NewDef_MidGap","", 200,0.0,100.0); 

    utility::makeHisto(my_histos,"timeDiff_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"timeDiffTracker_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted_timeDiff_tracker_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_MidGap", "", timeDiffNbin,timeDiffLow,timeDiffHigh);

    for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
    {
        utility::makeHisto(my_histos,"timeDiff_ROI"+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
        utility::makeHisto(my_histos,"timeDiffTracker_ROI"+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
        utility::makeHisto(my_histos,"weighted2_timeDiff_ROI"+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
        utility::makeHisto(my_histos,"weighted2_timeDiff_tracker_ROI"+regionsOfIntrest[k].getName(), "", timeDiffNbin,timeDiffLow,timeDiffHigh);
    }

    //Global 2D histograms
    utility::makeHisto(my_2d_histos,"relFracTot_vs_x", "; X [mm]; relFracTot", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"relFracMaxAmp_vs_x", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"relFracDC_vs_x_channel_top", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"weighted_timeDiff_vs_x", "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_2d_histos,"weighted_timeDiff_tracker_vs_x", "", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_2d_histos,"clusterSize_vs_x", "; X [mm]; Cluster Size", (xmax-xmin)/xBinSize,xmin,xmax, 8,0.0,8.0);
    utility::makeHisto(my_2d_histos,"AmpLeftOverAmpLeftandRightTop_vs_x", "; X [mm]; AmpLeftoverAmpLeftandRightTop", (xmax-xmin)/xBinSize,xmin,xmax, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpLeftOverAmpLeftandRightBot_vs_x", "; X [mm]; AmpLeftoverAmpLeftandRightBot", (xmax-xmin)/xBinSize,xmin,xmax, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpTopOverAmpTopandBotRight_vs_y", "; Y [mm]; AmpTopOverAmpTopandBotRight", (ymax-ymin)/yBinSize,ymin,ymax, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"AmpTopOverAmpTopandBotLeft_vs_y", "; Y [mm]; AmpTopOverAmpTopandBotLeft", (ymax-ymin)/yBinSize,ymin,ymax, 25,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax", "",           (5*pitch)/0.01,-2.5*pitch,2.5*pitch, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTopPad1_vs_deltaXmaxneg","",   pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTopPad2_vs_deltaXmaxpos","",   pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBotPad3_vs_deltaXmaxpos","",   pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBotPad4_vs_deltaXmaxneg","",   pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andTop_vs_deltaXmaxTopPad","",    pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andBot_vs_deltaXmaxBotPad","",    pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andAdjPad_vs_deltaXmaxAdjPad","", pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp1andAdjPad_vs_x","",               pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp1OverAmp123_vs_deltaXmax",          "",    pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp2OverAmp2and3_vs_deltaXmax",        "",    pitch/0.02,-pitch/2.0,pitch/2.0, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Amp12_vs_x", "; X [mm]; Sum Amp12", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"Amp1_vs_x", "; X [mm]; Amp1", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"Amp2_vs_x", "; X [mm]; Amp2", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"BaselineRMS12_vs_x", "; X [mm]; Noise Sum 12", (xmax-xmin)/xBinSize,xmin,xmax, 40,0.0,10);

    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Xtrack", "; X_{track} [mm]; #Y_{reco} - Y_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-30.5,30.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Ytrack", "; Y_{track} [mm]; #Y_{reco} - Y_{track} [mm]", ((ymax-ymin)/.4),ymin,ymax, 200,-30.5,30.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Ytrack_1cm", "; Y_{track} [mm]; #Y_{reco} - Y_{track} [mm]", (8.8/0.4),-4.4,4.4, 200,-30.5,30.5);
    utility::makeHisto(my_histos,"y", "; Y_{track} [mm]; Events", 100,-5.5,5.5);
    utility::makeHisto(my_histos,"y_reco", "; Y_{reco} [mm]; Events", 100,-5.5,5.5);
    utility::makeHisto(my_histos,"ratioe", "; Y_{track}/Y_{reco}; Events", 200,-20.5,20.5);
    utility::makeHisto(my_2d_histos,"deltaXBasic_vs_Xtrack", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaYBasic_vs_Xtrack", "; X_{track} [mm]; #Y_{reco} - Y_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-30.5,30.5);
    utility::makeHisto(my_2d_histos,"deltaYBasic_vs_Ytrack", "; Y_{track} [mm]; #Y_{reco} - Y_{track} [mm]", (ymax-ymin)/yBinSize,ymin,ymax, 200,-30.5,30.5);
    utility::makeHisto(my_2d_histos,"dXdFrac_vs_Xtrack", "; X_{track} [mm]; dX/dFraction [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 500,-19.0,1.0);

    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_noNeighb", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_highFrac", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_oneStrip", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_twoStrips", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_twoStrips_hotspot", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);

    utility::makeHisto(my_2d_histos,"deltaX_vs_Xreco", "; X_{reco} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaY_vs_Yreco", "; Y_{reco} [mm]; #Y_{reco} - Y_{track} [mm]", (ymax-ymin)/yBinSize,ymin,ymax, 200,-30.5,30.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xtrack", "; X_{track} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xreco", "; X_{reco} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    // utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_A1OverA12Above0p75", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_amplitude1", "; amp; #X_{reco} - X_{track} [mm]", 500,0,500, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_amplitude2", "; amp; #X_{reco} - X_{track} [mm]", 500,0,500, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"Xreco_vs_Xtrack", "; X_{track} [mm]; #X_{reco} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_2d_histos,"Yreco_vs_Ytrack", "; Y_{track} [mm]; #Y_{reco} [mm]", (ymax-ymin)/yBinSize,ymin,ymax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp1OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + A_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp2OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + A_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"Xtrack_vs_Amp3OverAmp123", "; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + m_{3})", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);


    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_twoStrips_tight", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"Amp12_vs_x_tight", "; X [mm]; Sum Amp12", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"Amp1_vs_x_tight", "; X [mm]; Amp1", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"Amp2_vs_x_tight", "; X [mm]; Amp2", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
    utility::makeHisto(my_2d_histos,"BaselineRMS12_vs_x_tight", "; X [mm]; Noise Sum 12", (xmax-xmin)/xBinSize,xmin,xmax, 40,0.0,10);
    utility::makeHisto(my_2d_histos,"dXdFrac_vs_Xtrack_tight", "; X_{track} [mm]; dX/dFraction [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 500,-19.0,1.0);


    //Global 3D histograms
    utility::makeHisto(my_3d_histos,"amplitude_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
    utility::makeHisto(my_3d_histos,"amplitude_vs_xyROI","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
    utility::makeHisto(my_3d_histos,"totgoodamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);
    utility::makeHisto(my_3d_histos,"totamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);
    utility::makeHisto(my_3d_histos,"totamplitudePad_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSizePad,xmin,xmax, (ymax-ymin)/yBinSizePad,ymin,ymax, 250,0,500);
    utility::makeHisto(my_3d_histos,"totrawamplitude_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);
    utility::makeHisto(my_3d_histos,"amp123_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);
    utility::makeHisto(my_3d_histos,"amp12_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);
    
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiff_Even_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiff_Odd_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTracker_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTracker_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTracker_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);   
 
    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);    
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
   
    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"timeDiffLGADXTrackerY_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADXY0_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffLGADX_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTrackerX_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_amp2", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_amp3", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_tracker_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_vs_xy_hotspot", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_tracker_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_tracker_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);    

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_TrackerX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_TrackerX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);    

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy_2Strip", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy_2Strip_Odd", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADXY_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted_timeDiff_LGADX_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADX_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADXY_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"average_timeDiff_LGADX_vs_xy_2Strip_Even", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    utility::makeHisto(my_3d_histos,"weighted_timeDiff_goodSig_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_goodSig_vs_xy", "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"deltaX_vs_Xtrack_vs_Ytrack", "; X_{track} [mm]; Y_{track} [mm]; #X_{reco} - X_{track} [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 200,-0.5,0.5);
    utility::makeHisto(my_3d_histos,"deltaY_vs_Xtrack_vs_Ytrack", "; X_{track} [mm]; Y_{track} [mm]; #Y_{reco} - Y_{track} [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 200,-30.5,30.5);
    utility::makeHisto(my_3d_histos,"risetime_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 150,0.0,1500.0);
    utility::makeHisto(my_3d_histos,"baselineRMS_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 150,0.0,50.0);
    utility::makeHisto(my_3d_histos,"charge_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,150.0);
    utility::makeHisto(my_3d_histos,"ampChargeRatio_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,50.0);
    utility::makeHisto(my_3d_histos,"slewRate_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax,300,0.0,500.0);

    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"timeDiffTracker_vs_xy_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_vs_xy_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
    utility::makeHisto(my_3d_histos,"weighted2_timeDiff_LGADXY_vs_xy_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);
   
    for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
    {
        utility::makeHisto(my_3d_histos,"timeDiff_Pixel_vs_xy"+regionsOfIntrest[k].getName(), "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,            timeDiffHigh);
        utility::makeHisto(my_3d_histos,"timeDiffTracker_Pixel_vs_xy"+regionsOfIntrest[k].getName(), "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,timeDiffLow,     timeDiffHigh);
        utility::makeHisto(my_3d_histos,"weighted2_timeDiff_tracker_Pixel_vs_xy"+regionsOfIntrest[k].getName(), "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, timeDiffYnbin,ymin,ymax, timeDiffNbin,      timeDiffLow,timeDiffHigh);
    }

    //Efficiency
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    // utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_denominator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_noNeighb_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highFrac_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_numerator", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);

    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator_coarseBins", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator_coarseBins", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator_coarseBins", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator_coarseBins", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);


    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    // utility::makeHisto(my_2d_histos,"efficiencyDC_vs_xy_denominator_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_noNeighb_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highFrac_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_numerator_tight", "; X [mm]; Y [mm]", 2*(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);

    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator_coarseBins_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_numerator_coarseBins_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_oneStrip_numerator_coarseBins_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_twoStrips_numerator_coarseBins_tight", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);

    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_Denominator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_fullReco_Numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_OneGoodHit_Numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_TwoGoodHit_Numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_ThreeGoodHit_Numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_FourGoodHit_Numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);

    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_EdgeCut_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_noNeighb_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_highFrac_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_oneStrip_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_twoStrips_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );

    //Define 2d prof
    utility::makeHisto(my_2d_prof,"efficiency_vs_xy_DCRing", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);
    utility::makeHisto(my_2d_prof,"efficiency_vs_xy_Strip2or5", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);
    
    //Define 1d prof
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp1OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp2OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"Xtrack_vs_Amp3OverAmp123_prof","; #X_{track} [mm]; Amp_{Max} / (Amp_{Max} + Amp_{2} + Amp_{3})", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"clusterSize_vs_x_prof", "; X [mm]; Cluster Size", (xmax-xmin)/xBinSize,xmin,xmax);
    utility::makeHisto(my_1d_prof,"waveProf0", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf1", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf2", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf3", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf4", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf5", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf6", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    utility::makeHisto(my_1d_prof,"waveProf7", "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    
    for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
    {
        utility::makeHisto(my_1d_prof,"waveProf0"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf1"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf2"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf3"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf4"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf5"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf6"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
        utility::makeHisto(my_1d_prof,"waveProf7"+regionsOfIntrest[k].getName(), "; Time [ns]; Voltage [mV]", 500,0.0,25.0);
    }

   
    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    utility::makeHisto(my_efficiencies,"event_oneStripReco",";;Events %",9,0,9);
    utility::makeHisto(my_efficiencies,"event_twoStripsReco",";;Events %",9,0,9);
    utility::makeHisto(my_efficiencies,"efficiency_vs_x","; X [mm]",xbins,xmin,xmax);
    utility::makeHisto(my_efficiencies,"efficiency_vs_xy","; X [mm]; Y [mm]",xbins,xmin,xmax, ybins,ymin,ymax);
    std::cout<<"Finished defining histos"<<std::endl;
}

//Put everything you want to do per event here.
void Analyze::Loop(NTupleReader& tr, int maxevents)
{
    const auto& indexToGeometryMap = tr.getVar<std::map<int, std::vector<int>>>("indexToGeometryMap");
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    // const auto& numLGADchannels = tr.getVar<int>("numLGADchannels");
    // const auto& sensorCenter = tr.getVar<double>("sensorCenter");
    // const auto& sensorCenterY = tr.getVar<double>("sensorCenterY");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalMax = tr.getVar<double>("photekSignalMax");
    const auto& isPadSensor = tr.getVar<bool>("isPadSensor");
    const auto& isHPKStrips = tr.getVar<bool>("isHPKStrips");
    const auto& uses2022Pix = tr.getVar<bool>("uses2022Pix");
    const auto& usesMay2023Tracker = tr.getVar<bool>("usesMay2023Tracker");
    const auto& minPixHits = tr.getVar<int>("minPixHits");
    const auto& minStripHits = tr.getVar<int>("minStripHits");
    const auto& positionRecoMaxPoint = tr.getVar<double>("positionRecoMaxPoint");
    //const auto& xSlices = tr.getVar<std::vector<std::vector<double>>>("xSlices");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
    const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
    // const auto& sensorEdgesTight = tr.getVar<std::vector<std::vector<double>>>("sensorEdgesTight");
    // const auto& timeCalibrationCorrection = tr.getVar<std::map<int, double>>("timeCalibrationCorrection");
    const auto& stripWidth = tr.getVar<double>("stripWidth");
    const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
    const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
    const auto& firstFile = tr.getVar<bool>("firstFile");
    const auto& regionsOfIntrest = tr.getVar<std::vector<utility::ROI>>("regionsOfIntrest");
    const auto& voltage = tr.getVar<int>("voltage");
    const auto& pitch = tr.getVar<double>("pitch");
    const auto& xBinSize = tr.getVar<double>("xBinSize");
    
    std::vector<int> lowEdgeStrip  = (isPadSensor) ? indexToGeometryMap.at(lowGoodStripIndex)  : indexToGeometryMap.at(lowGoodStripIndex-1);
    std::vector<int> highEdgeStrip = (isPadSensor) ? indexToGeometryMap.at(highGoodStripIndex) : indexToGeometryMap.at(highGoodStripIndex+1);

    int lowGoodStrip = indexToGeometryMap.at(lowGoodStripIndex)[1];
    int highGoodStrip = indexToGeometryMap.at(highGoodStripIndex)[1];
    bool plotWaveForm = false;

    if(firstFile) InitHistos(tr, geometry);

    while( tr.getNextEvent() )
    {
        //This is added to count the number of events- do not change the next two lines.
        const auto& eventCounter = tr.getVar<int>("eventCounter");
        my_histos["EventCounter"]->Fill( eventCounter );

        //Print Event Number 
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 100000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );
                       
        //Can add some fun code here....try not to calculate too much in this file: use modules to do the heavy calculations
        /*const auto& channel = tr.getVecVec<float>("channel");
        const auto& time_real = tr.getVecVec<float>("time");*/
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        const auto& rawAmpLGAD = tr.getVec<std::vector<float>>("rawAmpLGAD");
        const auto& corrTime = tr.getVec<double>("corrTime");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& timeLGADTracker = tr.getVec<std::vector<double>>("timeLGADTracker");
        
        const auto& timeLGADXTrackerY = tr.getVec<std::vector<double>>("timeLGADXTrackerY");
        const auto& timeLGADXY = tr.getVec<std::vector<double>>("timeLGADXY");
        const auto& timeLGADXY0 = tr.getVec<std::vector<double>>("timeLGADXY0");
        const auto& timeLGADX = tr.getVec<std::vector<double>>("timeLGADX");
        const auto& timeTrackerX = tr.getVec<std::vector<double>>("timeTrackerX");

        //const auto& CFD_list = tr.getVar<std::vector<std::string> >("CFD_list");
        const auto& baselineRMS = tr.getVec<std::vector<float>>("baselineRMS");
        const auto& risetimeLGAD = tr.getVec<std::vector<double>>("risetimeLGAD");
        const auto& chargeLGAD = tr.getVec<std::vector<double>>("chargeLGAD");
        const auto& ampChargeRatioLGAD = tr.getVec<std::vector<double>>("ampChargeRatioLGAD");
        const auto& slewrateLGAD = tr.getVec<std::vector<double>>("slewrateLGAD");
        const auto& slewRateChargeRatioLGAD = tr.getVec<std::vector<double>>("slewRateChargeRatioLGAD");
        const auto& baselineRMSSlewRateRatioLGAD = tr.getVec<std::vector<double>>("baselineRMSSlewRateRatioLGAD");
        const auto& extraChannelIndex = tr.getVar<int>("extraChannelIndex");
        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& ntracks_alt = tr.getVar<int>("ntracks_alt");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& xSlope = tr.getVar<float>("xSlope");
        const auto& ySlope = tr.getVar<float>("ySlope");
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& xErrDUT = tr.getVar<float>("xErrDUT");
        const auto& padx = tr.getVar<double>("padx");
        const auto& padxAdj = tr.getVar<double>("padxAdj");
        const auto& x_reco = tr.getVar<double>("x_reco");
        const auto& x_reco_basic = tr.getVar<double>("x_reco_basic");
        const auto& y_reco = tr.getVar<double>("y_reco");
        const auto& y_reco_basic = tr.getVar<double>("y_reco_basic");
        const auto& dXdFrac = tr.getVar<double>("dXdFrac");
        const auto& weighted_time = tr.getVar<double>("weighted_time");
        const auto& weighted_time_tracker = tr.getVar<double>("weighted_time_tracker");
        const auto& weighted2_time = tr.getVar<double>("weighted2_time");
        const auto& weighted2_time_tracker = tr.getVar<double>("weighted2_time_tracker");
        const auto& weighted_time_goodSig = tr.getVar<double>("weighted_time_goodSig");
        const auto& weighted2_time_goodSig = tr.getVar<double>("weighted2_time_goodSig");
        const auto& weighted2_jitter = tr.getVar<double>("weighted2_jitter");
        const auto& weighted2_jitter_NewDef = tr.getVar<double>("weighted2_jitter_NewDef");

        const auto& average_time_LGADXY = tr.getVar<double>("average_time_LGADXY");
        const auto& average_time_LGADX = tr.getVar<double>("average_time_LGADX");
        const auto& weighted_time_LGADXY = tr.getVar<double>("weighted_time_LGADXY");                                  
        const auto& weighted2_time_LGADXY = tr.getVar<double>("weighted2_time_LGADXY");
        const auto& weighted_time_LGADX = tr.getVar<double>("weighted_time_LGADX");
        const auto& weighted2_time_LGADX = tr.getVar<double>("weighted2_time_LGADX");
        const auto& weighted_time_trackerX = tr.getVar<double>("weighted_time_trackerX");
        const auto& weighted2_time_trackerX = tr.getVar<double>("weighted2_time_trackerX");       

        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& hitSensorExtra = tr.getVar<bool>("hitSensorExtra");
        const auto& hitSensorTightY = tr.getVar<bool>("hitSensorTightY");
        const auto& hitSensorTight = tr.getVar<bool>("hitSensorTight");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& relFracDC = tr.getVar<double>("relFracDC");
        const auto& relFrac = tr.getVec<std::vector<double>>("relFrac");
        const auto& fracMax = tr.getVec<std::vector<double>>("fracMax");
        // const auto& timeNearMax = tr.getVec<std::vector<bool>>("timeNearMax");
        const auto& totAmpLGAD = tr.getVar<double>("totAmpLGAD");
        const auto& totRawAmpLGAD = tr.getVar<double>("totRawAmpLGAD");
        const auto& totGoodAmpLGAD = tr.getVar<double>("totGoodAmpLGAD");
        const auto& Amp123 = tr.getVar<double>("Amp123");
        const auto& Amp12 = tr.getVar<double>("Amp12");
        const auto& Noise12 = tr.getVar<double>("Noise12");
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
        const auto& goodNeighbour = tr.getVar<bool>("goodNeighbour");
        const auto& parityLGAD = tr.getVec<std::vector<int>>("parityLGAD");
        const auto& twoGoodChannel = tr.getVar<bool>("twoGoodChannel"); // Timing requirement
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold && corrAmp[photekIndex] < photekSignalMax;
        bool goodTrack = ntracks==1 && nplanes>=14 && npix>0 && chi2 < 3.0 && xSlope<0.0001 && xSlope>-0.0001;// && ntracks_alt==1;
        if(isPadSensor) goodTrack = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        else if(isHPKStrips || uses2022Pix) goodTrack = ntracks==1 && (nplanes-npix)>=minStripHits && npix>=minPixHits && chi2 < 40;
        if(usesMay2023Tracker) goodTrack = ntracks==1 && (nplanes-npix)>=minStripHits && npix>=minPixHits && chi2 < 100;
        
        // bool hitSensorOnlyTightY = stripCenterXPositionLGAD[0][numLGADchannels-1] < x && x < stripCenterXPositionLGAD[0][0] && hitSensorTightY;
        bool passExtra = goodTrack && hitSensorExtra && goodPhotek; // equivalent to pass_loose
        bool hitSensorTightYNoEdgeX = stripCenterXPositionLGAD[highEdgeStrip[0]][highEdgeStrip[1]] < x && x < stripCenterXPositionLGAD[lowEdgeStrip[0]][lowEdgeStrip[1]] && hitSensorTightY;
        if (isPadSensor)    hitSensorTightYNoEdgeX = hitSensorTightY; // Update to use xSlice/ySlice
        bool pass = goodTrack && hitSensor && goodPhotek; // equivalent to pass_loose
        bool pass_loose = goodTrack && hitSensor && goodPhotek; // uses sensorEdges limits
        bool pass_tight = goodTrack && hitSensorTight && goodPhotek; // uses sensorEdgesTight limits (removes half next-to-edge strips)
        bool pass_tightY = goodTrack && hitSensorTightY && goodPhotek; // uses sensorEdgesTight Y limits only
        bool pass_tightYNoEdgeX = goodTrack && hitSensorTightYNoEdgeX && goodPhotek; // uses sensorEdgesTight Y limits and removes half edge strips
        bool pass_tightY_noPhotek = goodTrack && hitSensorTightYNoEdgeX; // uses sensorEdgesTight Y limits, removes half edge strips and Photek

        bool maxAmpNotEdgeStrip = ((maxAmpIndex >= lowGoodStrip && maxAmpIndex <= highGoodStrip) || isPadSensor);
        bool inBottomRow = y>ySlices[0][0] && y<ySlices[0][1];
        bool inTopRow = y>ySlices[1][0] && y<ySlices[1][1];
        bool maxAmpinPad1 = amp1Indexes.first==0 && amp1Indexes.second==0;
        bool maxAmpinPad2 = amp1Indexes.first==0 && amp1Indexes.second==1;
        bool maxAmpinPad3 = amp1Indexes.first==1 && amp1Indexes.second==1;
        bool maxAmpinPad4 = amp1Indexes.first==1 && amp1Indexes.second==0;
        bool hitInMiddleofPad = deltaXmaxAdjPad != 999 && deltaXmaxAdjPad != -999; 
        bool goodOverNoiseAmp = maxAmpLGAD > noiseAmpThreshold;
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;
        bool goodDCAmp = corrAmp[0]>signalAmpThreshold;

        bool highRelAmp1 = Amp1OverAmp1and2>=0.75;
        bool twoGoodHits = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold && ampLGAD[amp2Indexes.first][amp2Indexes.second] > noiseAmpThreshold;
        bool oneGoodHit = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold;
        bool threeGoodHits = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold && ampLGAD[amp2Indexes.first][amp2Indexes.second] > noiseAmpThreshold && ampLGAD[amp3Indexes.first][amp3Indexes.second] > noiseAmpThreshold;
        bool fourGoodHits = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold && ampLGAD[amp2Indexes.first][amp2Indexes.second] > noiseAmpThreshold && ampLGAD[amp3Indexes.first][amp3Indexes.second] > noiseAmpThreshold && ampLGAD[amp4Indexes.first][amp4Indexes.second] > noiseAmpThreshold;
        bool allGoodHits = oneGoodHit || twoGoodHits || threeGoodHits || fourGoodHits;
        bool twoStripsReco = goodNeighbour && (Amp1OverAmp1and2 < positionRecoMaxPoint);
        bool highFraction = Amp1OverAmp1and2 > positionRecoMaxPoint;
        bool oneStripReco = !goodNeighbour || highFraction;
        bool fullReco = hasGlobalSignal_lowThreshold && (oneStripReco || twoStripsReco);
        bool hitOnMetal = false;
        bool hitOnMidGap = false;

        if(isHPKStrips)
        {
            twoGoodHits = false;
            if(amp1Indexes.second - 1 >= lowGoodStrip) twoGoodHits = twoGoodHits || ampLGAD[amp1Indexes.first][amp1Indexes.second-1] > noiseAmpThreshold;
            if(amp1Indexes.second + 1 <= highGoodStrip) twoGoodHits = twoGoodHits || ampLGAD[amp1Indexes.first][amp1Indexes.second+1] > noiseAmpThreshold;
        }

        if (uses2022Pix)
        {
            twoGoodHits = twoGoodHits && goodNeighbour;
        }
        int parityMax = parityLGAD[amp1Indexes.first][amp1Indexes.second];
        bool EvenChannel = parityMax == -1;
        bool OddChannel = parityMax == 1;
        double photekTime = corrTime[photekIndex];
        double maxAmp = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        double maxAmpTime = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        double maxAmpTimeTracker = timeLGADTracker[amp1Indexes.first][amp1Indexes.second];
        
        double maxAmpTimeLGADXTrackerY = timeLGADXTrackerY[amp1Indexes.first][amp1Indexes.second];
        double maxAmpTimeLGADXY = timeLGADXY[amp1Indexes.first][amp1Indexes.second];
        double maxAmpTimeLGADXY0 = timeLGADXY0[amp1Indexes.first][amp1Indexes.second];       
        double maxAmpTimeLGADX = timeLGADX[amp1Indexes.first][amp1Indexes.second];         
        double maxAmpTimeTrackerX = timeTrackerX[amp1Indexes.first][amp1Indexes.second]; 

        double amp2 = ampLGAD[amp2Indexes.first][amp2Indexes.second];
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
                auto passChannel = pass;
                const auto& maxAmpStr = std::to_string(maxAmpIndex);
                const auto& ampChannel = ampLGAD[rowIndex][i];
                const auto& relFracChannel = relFrac[rowIndex][i];
                const auto& fracMaxChannel = fracMax[rowIndex][i];
                const auto& rawAmpChannel = rawAmpLGAD[rowIndex][i];
                const auto& noise = baselineRMS[rowIndex][i]; 
                const auto& risetime = risetimeLGAD[rowIndex][i];
                const auto& charge = chargeLGAD[rowIndex][i];
                const auto& ampChargeRatio = ampChargeRatioLGAD[rowIndex][i];
                const auto& slewrate = slewrateLGAD[rowIndex][i];
                const auto& slewRateChargeRatio = slewRateChargeRatioLGAD[rowIndex][i];
                const auto& baselineRMSSlewRateRatio = baselineRMSSlewRateRatioLGAD[rowIndex][i];
                const auto& stripXPosition = stripCenterXPositionLGAD[rowIndex][i];
                bool goodNoiseAmp = ampChannel>noiseAmpThreshold;
                bool goodSignalAmp = ampChannel>signalAmpThreshold;
                double time = timeLGAD[rowIndex][i];
                double timeTracker = timeLGADTracker[rowIndex][i];
                bool isMaxChannel = amp1Indexes.first == rowIndex && amp1Indexes.second == int(i);
                bool fullReco_ch = isMaxChannel && (goodSignalAmp && (oneStripReco || twoStripsReco));
                bool goodNearHit = amp1Indexes.first == rowIndex && (amp1Indexes.second == int(i-1) || amp1Indexes.second == int(i) || amp1Indexes.second == int(i+1));
                bool goodHit = goodNoiseAmp && goodMaxLGADAmp;
                if(i==1 || i==4) goodHitGlobal2and5 = goodHitGlobal2and5 || (isMaxChannel && goodHit);
                
                if (stripCenterXPositionLGAD[rowIndex][i]!=0.0 && ((stripCenterXPositionLGAD[rowIndex][i]-stripWidth/2.)<x) && (x<(stripCenterXPositionLGAD[rowIndex][i]+stripWidth/2.)))
                {
                    hitOnMetal = true;
                }
                
                bool hitOnLeftMidGap = ((stripCenterXPositionLGAD[rowIndex][i]-pitch/2.-xBinSize/2.)<x) && (x<(stripCenterXPositionLGAD[rowIndex][i]-pitch/2.+xBinSize/2.));
                bool hitOnRightMidGap = ((stripCenterXPositionLGAD[rowIndex][i]+pitch/2.-xBinSize/2.)<x) && (x<(stripCenterXPositionLGAD[rowIndex][i]+pitch/2.+xBinSize/2.));
 
                if (hitOnLeftMidGap || hitOnRightMidGap)
                {
                    hitOnMidGap = true;
                }

                //Adding var specific to having a seperate channel from the rest of the sensor
                const auto& scopeIndex = geometry[rowIndex][i];
                if(scopeIndex == extraChannelIndex)
                {
                    passChannel = passExtra;
                    isMaxChannel = true;
                    goodHit = goodNoiseAmp;
                }

                utility::fillHisto(passChannel,                                                    my_histos, "amp"+r+s, ampChannel);
                utility::fillHisto(passChannel,                                                    my_histos, "amp"+r+s+"From"+maxAmpStr, ampChannel);
                utility::fillHisto(passChannel && isMaxChannel,                                    my_histos, "ampMax"+r+s, ampChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_histos, "relFrac"+r+s, relFracChannel);
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad3 || maxAmpinPad4),       my_histos, "relFrac_bottom"+r+s, relFracChannel);
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad1 || maxAmpinPad2),       my_histos, "relFrac_top"+r+s, relFracChannel);
                utility::fillHisto(passChannel,                                                    my_histos, "time"+r+s, time);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "timeDiff_channel"+r+s, time-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "timeDiffTracker_channel"+r+s, timeTracker-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "baselineRMS"+r+s, noise);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "risetime"+r+s, risetime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "charge"+r+s, charge);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "ampChargeRatio"+r+s, ampChargeRatio);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "slewRateChargeRatio"+r+s, slewRateChargeRatio); 
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "slewrate"+r+s, slewrate);
                
                utility::fillHisto(pass_tightY && isMaxChannel && goodOverNoiseAmp && oneStripReco,my_histos, "deltaX_oneStrip"+r+s, x_reco-x);
                for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
                {
                    if(regionsOfIntrest[k].passROI(x,y))
                    {
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "baselineRMS"+r+s+regionsOfIntrest[k].getName(), noise);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "risetime"+r+s+regionsOfIntrest[k].getName(), risetime);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "charge"+r+s+regionsOfIntrest[k].getName(), charge);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "ampChargeRatio"+r+s+regionsOfIntrest[k].getName(), ampChargeRatio);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "slewrate"+r+s+regionsOfIntrest[k].getName(), slewrate);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "slewRateChargeRatio"+r+s+regionsOfIntrest[k].getName(), slewRateChargeRatio);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "baselineRMSSlewRateRatio"+r+s+regionsOfIntrest[k].getName(), baselineRMSSlewRateRatio); 
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "timeDiff_channel"+r+s+regionsOfIntrest[k].getName(), time-photekTime);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "timeDiffTracker_channel"+r+s+regionsOfIntrest[k].getName(), timeTracker-photekTime);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "weighted2_timeDiff_channel"+r+s+regionsOfIntrest[k].getName(), weighted2_time-photekTime);
                        utility::fillHisto(passChannel && goodHit,                                 my_histos, "weighted2_timeDiff_tracker_channel"+r+s+regionsOfIntrest[k].getName(), weighted2_time_tracker-photekTime);
                        utility::fillHisto(pass_tightY && goodHit && goodNearHit,                  my_2d_histos, "AmpOverMaxAmp_vs_x_channel"+r+s+regionsOfIntrest[k].getName(), x-stripXPosition,fracMaxChannel);
                        utility::fillHisto(passChannel && goodHit,                                 my_3d_histos, "amplitude_vs_xyROI", x,y,maxAmp);
                    }
                }

                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "weighted2_timeDiff_channel"+r+s, weighted2_time-photekTime);
                // utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "weighted_timeDiff_tracker_channel"+r+s, weighted_time_tracker-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "weighted2_timeDiff_tracker_channel"+r+s, weighted2_time_tracker-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_histos, "weighted_time-time_channel"+r+s, weighted_time-time);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "baselineRMS_vs_x_channel"+r+s, x,noise);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "amp_vs_x_channel"+r+s, x,ampChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "risetime_vs_amp"+r+s,ampChannel, risetime);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "amp_vs_y_channel"+r+s, y,ampChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "relFrac_vs_x_channel"+r+s, x,relFracChannel);

                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "timeDiff_vs_BV_channel"+r+s, voltage,time-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "amp_vs_BV_channel"+r+s, voltage,ampChannel);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "risetime_vs_BV_channel"+r+s, voltage,risetime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "baselineRMS_vs_BV_channel"+r+s, voltage,noise);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "slewrate_vs_BV_channel"+r+s, voltage,slewrate);

                /*
                utility::fillHisto(passChannel && goodHit && goodNearHit,                          my_2d_histos, "relFrac_vs_x_channel"+r+s+"_NearHit", x,relFracChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "AmpOverAmpandAmpMax_vs_x_channel"+r+s, x,xTalkChannel);
                utility::fillHisto(passChannel && goodHit && goodNearHit,                          my_2d_histos, "AmpOverAmpandAmpMax_vs_x_channel"+r+s+"_NearHit", x,xTalkChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "Amp1OverAmp1and2_vs_x_channel"+r+s, x,Amp1OverAmp1and2);
                utility::fillHisto(passChannel && goodHit && goodNearHit,                          my_2d_histos, "Amp1OverAmp1and2_vs_x_channel"+r+s+"_NearHit", x,Amp1OverAmp1and2);
                */
                utility::fillHisto(passChannel && goodHit,                                         my_2d_histos, "relFrac_vs_y_channel"+r+s, y,relFracChannel);
                utility::fillHisto(passChannel && goodHit && isMaxChannel && goodNeighbour,        my_2d_histos, "Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s, deltaXmax, Amp1OverAmp1and2);

                utility::fillHisto(pass_tightY && goodHit && goodNearHit,                   my_2d_histos, "AmpOverMaxAmp_vs_x_channel"+r+s, x-stripXPosition,fracMaxChannel);

                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "timeDiff_vs_x_channel"+r+s, x,time-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_2d_histos, "timeDiffTracker_vs_x_channel"+r+s, x,timeTracker-photekTime);
                utility::fillHisto(passChannel && goodHit && inBottomRow,                          my_2d_histos, "relFrac_vs_x_channel_bottom"+r+s, x, relFracChannel);
                utility::fillHisto(passChannel && goodHit && inBottomRow,                          my_2d_histos, "amp_vs_x_channel_bottom"+r+s, x, ampChannel);
                utility::fillHisto(passChannel && goodHit && inTopRow,                             my_2d_histos, "relFrac_vs_x_channel_top"+r+s, x, relFracChannel);
                utility::fillHisto(passChannel && goodHit && inTopRow,                             my_2d_histos, "amp_vs_x_channel_top"+r+s, x, ampChannel);
                utility::fillHisto(passChannel && goodHit && inTopRow && time!=0 && photekTime!=0, my_2d_histos, "delay_vs_x_channel_top"+r+s, x, timeLGAD[rowIndex][i] - photekTime);
                utility::fillHisto(firstEvent,                                              my_2d_histos, "stripBoxInfo"+r+s, stripCenterXPositionLGAD[rowIndex][i],stripWidth);
                utility::fillHisto(firstEvent,                                              my_2d_histos, "stripBoxInfoY"+r+s, stripCenterYPositionLGAD[rowIndex][i],stripWidth);
                /*for (unsigned int j = 0; j < channel[geometry[1][i]].size(); j++)
                {
                    auto signal = channel[geometry[1][i]][j];
                    auto time_channel = 1e+9*time_real[0][j]+timeCalibrationCorrection.at(geometry[1][i]);
                    utility::fillHisto(pass,      my_2d_histos, "wave"+r+s+"From"+maxAmpStr+"", time_channel-photekTime, signal);
                    utility::fillHisto(pass && goodHit,      my_2d_histos, "wave"+r+s+"From"+maxAmpStr+"goodHit", time_channel-photekTime, signal);
                }*/
                utility::fillHisto(passChannel,                                                    my_3d_histos, "baselineRMS_vs_xy_channel"+r+s, x,y,noise);
                utility::fillHisto(passChannel && goodHit,                                         my_3d_histos, "amplitude_vs_xy_channel"+r+s, x,y,ampChannel);
     
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "baselineRMSNew_vs_xy_channel"+r+s, x,y,noise);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "amplitudeNew_vs_xy_channel"+r+s, x,y,ampChannel);
                
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad1 || maxAmpinPad2),       my_3d_histos, "amplitudeTop_vs_xy_channel"+r+s, x,y,ampChannel);
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad3 || maxAmpinPad4),       my_3d_histos, "amplitudeBot_vs_xy_channel"+r+s, x,y,ampChannel);
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad1 || maxAmpinPad4),       my_3d_histos, "amplitudeLeft_vs_xy_channel"+r+s, x,y,ampChannel);
                utility::fillHisto(passChannel && goodHit && (maxAmpinPad2 || maxAmpinPad3),       my_3d_histos, "amplitudeRight_vs_xy_channel"+r+s, x,y,ampChannel);
                utility::fillHisto(passChannel && goodHit,                                         my_3d_histos, "raw_amp_vs_xy_channel"+r+s, x,y,rawAmpChannel);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "timeDiff_vs_xy_channel"+r+s, x,y,time-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "timeDiffTracker_vs_xy_channel"+r+s, x,y,timeTracker-photekTime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "risetime_vs_xy_channel"+r+s, x,y,risetime);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "charge_vs_xy_channel"+r+s, x,y,charge);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "ampChargeRatio_vs_xy_channel"+r+s, x,y,ampChargeRatio);
                utility::fillHisto(passChannel && goodHit && isMaxChannel,                         my_3d_histos, "slewRate_vs_xy_channel"+r+s, x,y,slewrate);

                utility::fillHisto(passChannel && goodNoiseAmp,                                    my_2d_histos, "efficiency_vs_xy_numerator_channel"+r+s, x,y);
                utility::fillHisto(passChannel && goodNoiseAmp && !goodNeighbour && isMaxChannel,  my_2d_histos, "efficiency_vs_xy_noNeighb_numerator_channel"+r+s, x,y);
                utility::fillHisto(passChannel && goodNoiseAmp && highFraction && isMaxChannel,    my_2d_histos, "efficiency_vs_xy_highFrac_numerator_channel"+r+s, x,y);
                utility::fillHisto(passChannel && goodNoiseAmp && oneStripReco && isMaxChannel,    my_2d_histos, "efficiency_vs_xy_oneStrip_numerator_channel"+r+s, x,y);
                utility::fillHisto(passChannel && goodNoiseAmp && twoStripsReco && isMaxChannel,   my_2d_histos, "efficiency_vs_xy_twoStrips_numerator_channel"+r+s, x,y);
                utility::fillHisto(passChannel && fullReco_ch,                                     my_2d_histos, "efficiency_vs_xy_fullReco_numerator_channel"+r+s, x,y);

                utility::fillHisto(passChannel && goodPhotek && isMaxChannel,                my_2d_prof, "efficiency_vs_xy_prof_channel"+r+s, x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel,                  my_2d_prof, "efficiency_vs_xy_prof", x,y,goodHit);
                utility::fillHisto(passChannel && isMaxChannel,                              my_2d_prof, "efficiency_vs_xy_EdgeCut_prof", x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && !goodNeighbour,my_2d_prof,"efficiency_vs_xy_noNeighb_prof", x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && highFraction, my_2d_prof, "efficiency_vs_xy_highFrac_prof", x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && oneStripReco, my_2d_prof, "efficiency_vs_xy_oneStrip_prof", x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && twoStripsReco,my_2d_prof, "efficiency_vs_xy_twoStrips_prof", x,y,goodHit);

                utility::fillHisto(goodTrack && isMaxChannel,                               my_efficiencies, "efficiency_vs_x", goodHit,x);
                utility::fillHisto(goodTrack && isMaxChannel,                               my_efficiencies, "efficiency_vs_xy", goodHit,x,y);


                utility::fillHisto(pass_tightY_noPhotek && goodNoiseAmp,                                    my_2d_histos, "efficiency_vs_xy_numerator_tight_channel"+r+s, x,y);
                utility::fillHisto(pass_tightY_noPhotek && goodNoiseAmp && !goodNeighbour && isMaxChannel,  my_2d_histos, "efficiency_vs_xy_noNeighb_numerator_tight_channel"+r+s, x,y);
                utility::fillHisto(pass_tightY_noPhotek && goodNoiseAmp && highFraction && isMaxChannel,    my_2d_histos, "efficiency_vs_xy_highFrac_numerator_tight_channel"+r+s, x,y);
                utility::fillHisto(pass_tightY_noPhotek && goodNoiseAmp && oneStripReco && isMaxChannel,    my_2d_histos, "efficiency_vs_xy_oneStrip_numerator_tight_channel"+r+s, x,y);
                utility::fillHisto(pass_tightY_noPhotek && goodNoiseAmp && twoStripsReco && isMaxChannel,   my_2d_histos, "efficiency_vs_xy_twoStrips_numerator_tight_channel"+r+s, x,y);
                utility::fillHisto(pass_tightY_noPhotek && fullReco_ch,                                     my_2d_histos, "efficiency_vs_xy_fullReco_numerator_tight_channel"+r+s, x,y);


            }
            rowIndex++;
        }
        utility::fillHisto(pass,                                                                           my_histos, "timePhotek",photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "deltaX", x_reco-x);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && !goodNeighbour,               my_histos, "deltaX_noNeighb", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && !goodNeighbour && hitOnMetal, my_histos, "deltaX_noNeighb_onMetal", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && highFraction,                 my_histos, "deltaX_highFrac", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && highFraction && hitOnMetal,   my_histos, "deltaX_highFrac_onMetal", x_reco-x);
        utility::fillHisto(pass_tightY && maxAmpNotEdgeStrip && goodOverNoiseAmp && oneStripReco,          my_histos, "deltaX_oneStrip", x_reco-x);
        utility::fillHisto(pass_tightY && maxAmpNotEdgeStrip && goodOverNoiseAmp && oneStripReco && hitOnMetal,my_histos, "deltaX_oneStrip_onMetal", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "deltaX_twoStrips", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && !hitOnMetal,   my_histos, "deltaX_twoStrips_noMetal", x_reco-x);


        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp,                              my_histos, "deltaX_tight", x_reco-x);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodOverNoiseAmp && oneStripReco,            my_histos, "deltaX_oneStrip_tight", x_reco-x);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodOverNoiseAmp && oneStripReco && hitOnMetal, my_histos, "deltaX_oneStrip_onMetal_tight", x_reco-x);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,             my_histos, "deltaX_twoStrips_tight", x_reco-x);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && !hitOnMetal, my_histos, "deltaX_twoStrips_noMetal_tight", x_reco-x);


        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "deltaXBasic", x_reco_basic-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp  && twoGoodChannel,                my_histos, "deltaYBasic", y_reco_basic-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "dXdFrac", dXdFrac);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad2), my_histos, "deltaX_TopRow", x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad3 || maxAmpinPad4), my_histos, "deltaX_BotRow", x_reco-x);
        //std::cout<<"yreco "<<y_reco<<" y "<<y<<" deltaY "<<y_reco-y<<std::endl;
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoGoodChannel,                 my_histos, "deltaY", y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && oneStripReco && twoGoodChannel, my_histos, "deltaY_oneStrip", y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && twoGoodChannel,my_histos, "deltaY_twoStrips", y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad2 || maxAmpinPad3) && twoGoodChannel, my_histos, "deltaY_RightCol", y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad4) && twoGoodChannel, my_histos, "deltaY_LeftCol", y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "chi2", chi2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ntracks_alt", ntracks_alt);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "nplanes", nplanes);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "npix", npix);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "monicelli_err", xErrDUT);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "slopeX", xSlope);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "slopeY", ySlope);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank1", ampLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank2", ampLGAD[amp2Indexes.first][amp2Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank3", ampLGAD[amp3Indexes.first][amp3Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank4", ampLGAD[amp4Indexes.first][amp4Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank5", ampLGAD[amp5Indexes.first][amp5Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampRank6", ampLGAD[amp6Indexes.first][amp6Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiff", maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffTracker", maxAmpTimeTracker-photekTime);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffLGADXTrackerY",maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffLGADXY",maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffLGADXY0",maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffLGADX",maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiffTrackerX",maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted_timeDiff_LGADXY", weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted_timeDiff_LGADX", weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted2_timeDiff_LGADXY", weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted2_timeDiff_LGADX", weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "average_timeDiff_LGADXY", average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "average_timeDiff_LGADX", average_time_LGADX-photekTime);
   
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "weighted_timeDiff_LGADXY_2Strip", weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "weighted_timeDiff_LGADX_2Strip", weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "weighted2_timeDiff_LGADXY_2Strip", weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "weighted2_timeDiff_LGADX_2Strip", weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "average_timeDiff_LGADXY_2Strip", average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "average_timeDiff_LGADX_2Strip", average_time_LGADX-photekTime);
 
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiff_amp2", amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "timeDiff_amp3", amp3Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted_timeDiff", weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted_timeDiff_tracker", weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted2_timeDiff", weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted2_timeDiff_tracker", weighted2_time_tracker-photekTime);


        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp,                             my_histos, "timeDiff_tight", maxAmpTime-photekTime);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp,                             my_histos, "timeDiffTracker_tight", maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp,                             my_histos, "weighted2_timeDiff_tight", weighted2_time-photekTime);
        utility::fillHisto(pass_tight && maxAmpNotEdgeStrip && goodMaxLGADAmp,                             my_histos, "weighted2_timeDiff_tracker_tight", weighted2_time_tracker-photekTime);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted_timeDiff_goodSig", weighted_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "weighted2_timeDiff_goodSig", weighted2_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "clusterSize", clusterSize);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "charge", chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "risetime", risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "ampChargeRatio", ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos, "index_diff", amp1Indexes.second - amp2Indexes.second);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "ampMax_Overall", maxAmp);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "risetime_Overall",risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "charge_Overall",chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "ampChargeRatio_Overall",ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "baselineRMS_Overall",baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "slewrate_Overall", slewrateLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "slewRateChargeRatio_Overall", slewRateChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted2_jitter_Overall", weighted2_jitter);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted2_jitter_NewDef_Overall", weighted2_jitter_NewDef);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "timeDiff_Overall", maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "timeDiffTracker_Overall", maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted_timeDiff_Overall", weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted_timeDiff_tracker_Overall", weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted2_timeDiff_Overall", weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                my_histos, "weighted2_timeDiff_tracker_Overall", weighted2_time_tracker-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "ampMax_Metal", maxAmp);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "risetime_Metal",risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "charge_Metal",chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "ampChargeRatio_Metal",ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "baselineRMS_Metal",baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "slewrate_Metal", slewrateLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "slewRateChargeRatio_Metal", slewRateChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted2_jitter_Metal", weighted2_jitter);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted2_jitter_NewDef_Metal", weighted2_jitter_NewDef);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "timeDiff_Metal", maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "timeDiffTracker_Metal", maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted_timeDiff_Metal", weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted_timeDiff_tracker_Metal", weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted2_timeDiff_Metal", weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMetal,                my_histos, "weighted2_timeDiff_tracker_Metal", weighted2_time_tracker-photekTime); 

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "ampMax_Gap", maxAmp);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "risetime_Gap",risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "charge_Gap",chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "ampChargeRatio_Gap",ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "baselineRMS_Gap",baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "slewrate_Gap", slewrateLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "slewRateChargeRatio_Gap", slewRateChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted2_jitter_Gap", weighted2_jitter);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted2_jitter_NewDef_Gap", weighted2_jitter_NewDef);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "timeDiff_Gap", maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "timeDiffTracker_Gap", maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted_timeDiff_Gap", weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted_timeDiff_tracker_Gap", weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted2_timeDiff_Gap", weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !hitOnMetal,                my_histos, "weighted2_timeDiff_tracker_Gap", weighted2_time_tracker-photekTime);
 
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "ampMax_MidGap", maxAmp);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "risetime_MidGap",risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "charge_MidGap",chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "ampChargeRatio_MidGap",ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "baselineRMS_MidGap",baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "slewrate_MidGap", slewrateLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "slewRateChargeRatio_MidGap", slewRateChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted2_jitter_MidGap", weighted2_jitter);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted2_jitter_NewDef_MidGap", weighted2_jitter_NewDef);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "timeDiff_MidGap", maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "timeDiffTracker_MidGap", maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted_timeDiff_MidGap", weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted_timeDiff_tracker_MidGap", weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted2_timeDiff_MidGap", weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && hitOnMidGap,                my_histos, "weighted2_timeDiff_tracker_MidGap", weighted2_time_tracker-photekTime);
        
        for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
        {
            if(regionsOfIntrest[k].passROI(x,y))
            {
                utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                           my_histos, "timeDiff_ROI"+regionsOfIntrest[k].getName(), maxAmpTime-photekTime);
                utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                           my_histos, "timeDiffTracker_ROI"+regionsOfIntrest[k].getName(),  maxAmpTimeTracker-photekTime);
                utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                           my_histos, "weighted2_timeDiff_ROI"+regionsOfIntrest[k].getName(), weighted2_time-photekTime);
                utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                           my_histos, "weighted2_timeDiff_tracker_ROI"+regionsOfIntrest[k].getName(), weighted2_time_tracker-photekTime);
                if (regionsOfIntrest[k].getName()=="hotspot")
                {
                    utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,      my_2d_histos, "deltaX_vs_Xtrack_twoStrips_hotspot", x,x_reco-x);
                    utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                       my_3d_histos, "weighted2_timeDiff_tracker_vs_xy_hotspot", x,y,weighted2_time_tracker-photekTime);
                }
            }
        }

        // Save 2d histos
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos, "relFracMaxAmp_vs_x", padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass,                                                                           my_2d_histos, "relFracDC_vs_x_channel_top", x,relFracDC);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos, "relFracTot_vs_x", padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos, "relFracTot_vs_x", padxAdj, relFrac[ampIndexesAdjPad.first][ampIndexesAdjPad.second]);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad2),                       my_2d_histos, "AmpLeftOverAmpLeftandRightTop_vs_x", x,AmpLeftOverAmpLeftandRightTop);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad3 || maxAmpinPad4),                       my_2d_histos, "AmpLeftOverAmpLeftandRightBot_vs_x", x,AmpLeftOverAmpLeftandRightBot);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad2 || maxAmpinPad3),                       my_2d_histos, "AmpTopOverAmpTopandBotRight_vs_y", y,AmpTopOverAmpTopandBotRight);
        utility::fillHisto(pass && goodMaxLGADAmp && (maxAmpinPad1 || maxAmpinPad4),                       my_2d_histos, "AmpTopOverAmpTopandBotLeft_vs_y", y,AmpTopOverAmpTopandBotLeft);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoGoodHits,                    my_2d_histos, "Amp1OverAmp1and2_vs_deltaXmax", fabs(deltaXmax),Amp1OverAmp1and2);
        utility::fillHisto(pass && maxAmpinPad1 && hitInMiddleofPad,                                       my_2d_histos, "Amp1OverAmp1andTopPad1_vs_deltaXmaxneg", deltaXmaxneg,Amp1OverAmp1andTop);
        utility::fillHisto(pass && maxAmpinPad2 && hitInMiddleofPad,                                       my_2d_histos, "Amp1OverAmp1andTopPad2_vs_deltaXmaxpos", deltaXmaxpos,Amp1OverAmp1andTop);
        utility::fillHisto(pass && maxAmpinPad3 && hitInMiddleofPad,                                       my_2d_histos, "Amp1OverAmp1andBotPad3_vs_deltaXmaxpos", deltaXmaxpos,Amp1OverAmp1andBot);
        utility::fillHisto(pass && maxAmpinPad4 && hitInMiddleofPad,                                       my_2d_histos, "Amp1OverAmp1andBotPad4_vs_deltaXmaxneg", deltaXmaxneg,Amp1OverAmp1andBot);
        utility::fillHisto(pass && (maxAmpinPad1 || maxAmpinPad2) && hitInMiddleofPad,                     my_2d_histos, "Amp1OverAmp1andTop_vs_deltaXmaxTopPad", fabs(deltaXmaxTopPad),Amp1OverAmp1andTop);
        utility::fillHisto(pass && (maxAmpinPad3 || maxAmpinPad4) && hitInMiddleofPad,                     my_2d_histos, "Amp1OverAmp1andBot_vs_deltaXmaxBotPad", fabs(deltaXmaxBotPad),Amp1OverAmp1andBot);
        utility::fillHisto(pass && hitInMiddleofPad,                                                       my_2d_histos, "Amp1OverAmp1andAdjPad_vs_deltaXmaxAdjPad", fabs(deltaXmaxAdjPad),Amp1OverAmp1andAdjPad);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos, "Amp1OverAmp1andAdjPad_vs_x", x-sensorEdges[0][0],Amp1OverAmp1andAdjPad);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos, "Amp1OverAmp123_vs_deltaXmax", fabs(deltaXmax),Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos, "Xtrack_vs_Amp1OverAmp123", x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos, "Xtrack_vs_Amp2OverAmp123", x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_2d_histos, "Xtrack_vs_Amp3OverAmp123", x,Amp3OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaX_vs_Xtrack", x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaXBasic_vs_Xtrack", x,x_reco_basic-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaYBasic_vs_Xtrack", x,y_reco_basic-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaYBasic_vs_Ytrack", y,y_reco_basic-y);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && !goodNeighbour,               my_2d_histos, "deltaX_vs_Xtrack_noNeighb", x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && highFraction,                 my_2d_histos, "deltaX_vs_Xtrack_highFrac", x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodOverNoiseAmp && oneStripReco,                 my_2d_histos, "deltaX_vs_Xtrack_oneStrip", x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "deltaX_vs_Xtrack_twoStrips", x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "Amp12_vs_x", x, Amp12);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "Amp1_vs_x", x, maxAmp);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "Amp2_vs_x", x, amp2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "BaselineRMS12_vs_x", x, Noise12);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "dXdFrac_vs_Xtrack", x,dXdFrac);


        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "deltaX_vs_Xtrack_twoStrips_tight", x,x_reco-x);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "Amp12_vs_x_tight", x, Amp12);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "Amp1_vs_x_tight", x, maxAmp);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "Amp2_vs_x_tight", x, amp2);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "BaselineRMS12_vs_x_tight", x, Noise12);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,    my_2d_histos, "dXdFrac_vs_Xtrack_tight", x,dXdFrac);


        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaX_vs_Xreco", x_reco,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco  && twoGoodChannel,my_2d_histos, "deltaY_vs_Xtrack", x,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco  && twoGoodChannel,my_2d_histos, "deltaY_vs_Ytrack", y,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco  && twoGoodChannel,my_2d_histos, "deltaY_vs_Ytrack_1cm", y,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "y", y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "y_reco", y_reco);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_histos, "ratioe", y/y_reco);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco  && twoGoodChannel,my_2d_histos, "deltaY_vs_Yreco", y_reco,y_reco-y);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaXmax_vs_Xtrack", x,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaXmax_vs_Xreco", x_reco,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "weighted_timeDiff_vs_x", x,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "weighted_timeDiff_tracker_vs_x", x,weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "Xreco_vs_Xtrack", x,x_reco);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_2d_histos, "Yreco_vs_Ytrack", y,y_reco);
        // utility::fillHisto(pass && highRelAmp1,                                                            my_2d_histos, "deltaX_vs_Xtrack_A1OverA12Above0p75", x,x_reco-x);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaX_vs_amplitude1", maxAmp,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "deltaX_vs_amplitude2", amp2,x_reco-x);
        utility::fillHisto(pass && highRelAmp1,                                                            my_2d_histos, "Amp2OverAmp2and3_vs_deltaXmax", deltaXmax,Amp2OverAmp2and3);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos, "clusterSize_vs_x", x,clusterSize);

        // Save 3d histos
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "amplitude_vs_xy", x,y,maxAmp);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "baselineRMS_vs_xy", x,y,baselineRMS[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "risetime_vs_xy", x,y,risetimeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "charge_vs_xy", x,y,chargeLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "ampChargeRatio_vs_xy", x,y,ampChargeRatioLGAD[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "slewRate_vs_xy", x,y,slewrateLGAD[amp1Indexes.first][amp1Indexes.second]);

        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "totgoodamplitude_vs_xy", x,y,totGoodAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "totamplitude_vs_xy", x,y,totAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "totamplitudePad_vs_xy", x,y,totAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "totrawamplitude_vs_xy", x,y,totRawAmpLGAD);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "amp123_vs_xy", x,y, Amp123);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "amp12_vs_xy", x,y, Amp12);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiff_vs_xy", x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "timeDiff_Even_vs_xy", x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "timeDiff_Odd_vs_xy", x,y,maxAmpTime-photekTime);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffTracker_vs_xy", x,y,maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "timeDiffTracker_vs_xy_Odd", x,y,maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "timeDiffTracker_vs_xy_Even", x,y,maxAmpTimeTracker-photekTime);        

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffLGADXTrackerY_vs_xy", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffLGADXY_vs_xy", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffLGADXY0_vs_xy", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffLGADX_vs_xy", x,y,maxAmpTimeLGADX-photekTime);        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiffTrackerX_vs_xy", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                    my_3d_histos, "timeDiffLGADXTrackerY_vs_xy_Odd", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                    my_3d_histos, "timeDiffLGADXY_vs_xy_Odd", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                    my_3d_histos, "timeDiffLGADXY0_vs_xy_Odd", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                    my_3d_histos, "timeDiffLGADX_vs_xy_Odd", x,y,maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                    my_3d_histos, "timeDiffTrackerX_vs_xy_Odd", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                   my_3d_histos, "timeDiffLGADXTrackerY_vs_xy_Even", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                   my_3d_histos, "timeDiffLGADXY_vs_xy_Even", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                   my_3d_histos, "timeDiffLGADXY0_vs_xy_Even", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                   my_3d_histos, "timeDiffLGADX_vs_xy_Even", x,y,maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                   my_3d_histos, "timeDiffTrackerX_vs_xy_Even", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                 my_3d_histos, "timeDiffLGADXTrackerY_vs_xy_2Strip", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                 my_3d_histos, "timeDiffLGADXY_vs_xy_2Strip", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                 my_3d_histos, "timeDiffLGADXY0_vs_xy_2Strip", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                 my_3d_histos, "timeDiffLGADX_vs_xy_2Strip", x,y,maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                 my_3d_histos, "timeDiffTrackerX_vs_xy_2Strip", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel && twoStripsReco,   my_3d_histos, "timeDiffLGADXTrackerY_vs_xy_2Strip_Odd", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel && twoStripsReco,   my_3d_histos, "timeDiffLGADXY_vs_xy_2Strip_Odd", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel && twoStripsReco,   my_3d_histos, "timeDiffLGADXY0_vs_xy_2Strip_Odd", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel && twoStripsReco,   my_3d_histos, "timeDiffLGADX_vs_xy_2Strip_Odd", x,y,maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel && twoStripsReco,   my_3d_histos, "timeDiffTrackerX_vs_xy_2Strip_Odd", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel && twoStripsReco,  my_3d_histos, "timeDiffLGADXTrackerY_vs_xy_2Strip_Even", x,y,maxAmpTimeLGADXTrackerY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel && twoStripsReco,  my_3d_histos, "timeDiffLGADXY_vs_xy_2Strip_Even", x,y,maxAmpTimeLGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel && twoStripsReco,  my_3d_histos, "timeDiffLGADXY0_vs_xy_2Strip_Even", x,y,maxAmpTimeLGADXY0-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel && twoStripsReco,  my_3d_histos, "timeDiffLGADX_vs_xy_2Strip_Even", x,y,maxAmpTimeLGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel && twoStripsReco,  my_3d_histos, "timeDiffTrackerX_vs_xy_2Strip_Even", x,y,maxAmpTimeTrackerX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiff_vs_xy_amp2", x,y,amp2Time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "timeDiff_vs_xy_amp3", x,y,amp3Time-photekTime);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_vs_xy", x,y,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_tracker_vs_xy", x,y,weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_vs_xy", x,y,weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_tracker_vs_xy", x,y,weighted2_time_tracker-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted_timeDiff_vs_xy_Odd", x,y,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted_timeDiff_tracker_vs_xy_Odd", x,y,weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted2_timeDiff_vs_xy_Odd", x,y,weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted2_timeDiff_tracker_vs_xy_Odd", x,y,weighted2_time_tracker-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted_timeDiff_vs_xy_Even", x,y,weighted_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted_timeDiff_tracker_vs_xy_Even", x,y,weighted_time_tracker-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted2_timeDiff_vs_xy_Even", x,y,weighted2_time-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted2_timeDiff_tracker_vs_xy_Even", x,y,weighted2_time_tracker-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_LGADX_vs_xy", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_TrackerX_vs_xy", x,y,weighted_time_trackerX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_TrackerX_vs_xy", x,y,weighted2_time_trackerX-photekTime);
        
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "average_timeDiff_LGADXY_vs_xy", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "average_timeDiff_LGADX_vs_xy", x,y,average_time_LGADX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy_Odd", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_Odd", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted_timeDiff_LGADX_vs_xy_Odd", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy_Odd", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "average_timeDiff_LGADXY_vs_xy_Odd", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && OddChannel,                     my_3d_histos, "average_timeDiff_LGADX_vs_xy_Odd", x,y,average_time_LGADX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy_Even", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_Even", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted_timeDiff_LGADX_vs_xy_Even", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy_Even", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "average_timeDiff_LGADXY_vs_xy_Even", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && EvenChannel,                    my_3d_histos, "average_timeDiff_LGADX_vs_xy_Even", x,y,average_time_LGADX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy_2Strip", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_2Strip", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "weighted_timeDiff_LGADX_vs_xy_2Strip", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy_2Strip", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "average_timeDiff_LGADXY_vs_xy_2Strip", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco,                  my_3d_histos, "average_timeDiff_LGADX_vs_xy_2Strip", x,y,average_time_LGADX-photekTime);        

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy_2Strip_Odd", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_2Strip_Odd", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "weighted_timeDiff_LGADX_vs_xy_2Strip_Odd", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy_2Strip_Odd", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "average_timeDiff_LGADXY_vs_xy_2Strip_Odd", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && OddChannel,   my_3d_histos, "average_timeDiff_LGADX_vs_xy_2Strip_Odd", x,y,average_time_LGADX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "weighted_timeDiff_LGADXY_vs_xy_2Strip_Even", x,y,weighted_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_2Strip_Even", x,y,weighted2_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "weighted_timeDiff_LGADX_vs_xy_2Strip_Even", x,y,weighted_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "weighted2_timeDiff_LGADX_vs_xy_2Strip_Even", x,y,weighted2_time_LGADX-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "average_timeDiff_LGADXY_vs_xy_2Strip_Even", x,y,average_time_LGADXY-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco && EvenChannel, my_3d_histos, "average_timeDiff_LGADX_vs_xy_2Strip_Even", x,y,average_time_LGADX-photekTime);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted_timeDiff_goodSig_vs_xy", x,y,weighted_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "weighted2_timeDiff_goodSig_vs_xy", x,y,weighted2_time_goodSig-photekTime);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_3d_histos, "deltaX_vs_Xtrack_vs_Ytrack", x,y,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoStripsReco  && twoGoodChannel,my_3d_histos, "deltaY_vs_Xtrack_vs_Ytrack", x,y,y_reco-y);


        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp,                            my_3d_histos, "timeDiff_vs_xy_tight", x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp,                            my_3d_histos, "timeDiffTracker_vs_xy_tight", x,y,maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp,                            my_3d_histos, "weighted2_timeDiff_tracker_vs_xy_tight", x,y,weighted2_time_tracker-photekTime);
        utility::fillHisto(pass_tightYNoEdgeX && maxAmpNotEdgeStrip && goodMaxLGADAmp,                            my_3d_histos, "weighted2_timeDiff_LGADXY_vs_xy_tight", x,y,weighted2_time_LGADXY-photekTime);


        // Save profiles and efficiency histos
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof, "Xtrack_vs_Amp1OverAmp123_prof", x,Amp1OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof, "Xtrack_vs_Amp2OverAmp123_prof", x,Amp2OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip,                                                     my_1d_prof, "Xtrack_vs_Amp3OverAmp123_prof", x,Amp3OverAmp123);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_1d_prof, "clusterSize_vs_x_prof", x,clusterSize);

        utility::fillHisto(pass,                                                                           my_2d_histos, "efficiency_vs_xy_denominator", x,y);
        utility::fillHisto(pass && goodDCAmp,                                                              my_2d_histos, "efficiencyDC_vs_xy_numerator", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold,                                           my_2d_histos, "efficiency_vs_xy_numerator", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && !goodNeighbour,                         my_2d_histos, "efficiency_vs_xy_noNeighb_numerator", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && highFraction,                           my_2d_histos, "efficiency_vs_xy_highFrac_numerator", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && oneStripReco,                           my_2d_histos, "efficiency_vs_xy_oneStrip_numerator", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && twoStripsReco,                          my_2d_histos, "efficiency_vs_xy_twoStrips_numerator", x,y);
        utility::fillHisto(pass && fullReco,                                                               my_2d_histos, "efficiency_vs_xy_fullReco_numerator", x,y);

        utility::fillHisto(pass,                                                                           my_2d_histos, "efficiency_vs_xy_denominator_coarseBins", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold,                                           my_2d_histos, "efficiency_vs_xy_numerator_coarseBins", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && oneStripReco,                           my_2d_histos, "efficiency_vs_xy_oneStrip_numerator_coarseBins", x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && twoStripsReco,                          my_2d_histos, "efficiency_vs_xy_twoStrips_numerator_coarseBins", x,y);

        utility::fillHisto(pass,                                                                           my_2d_histos, "efficiency_vs_xy_fullReco_Denominator", x,y);  
        utility::fillHisto(pass && allGoodHits,                                                            my_2d_histos, "efficiency_vs_xy_fullReco_Numerator", x,y);
        utility::fillHisto(pass && oneGoodHit,                                                             my_2d_histos, "efficiency_vs_xy_OneGoodHit_Numerator", x,y); 
        utility::fillHisto(pass && twoGoodHits,                                                            my_2d_histos, "efficiency_vs_xy_TwoGoodHit_Numerator", x,y);
        utility::fillHisto(pass && threeGoodHits,                                                          my_2d_histos, "efficiency_vs_xy_ThreeGoodHit_Numerator", x,y);
        utility::fillHisto(pass && fourGoodHits,                                                           my_2d_histos, "efficiency_vs_xy_FourGoodHit_Numerator", x,y);

        // Use pass_tightY instead of simple pass (pass_loose)
        utility::fillHisto(pass_tightY_noPhotek,                                                           my_2d_histos, "efficiency_vs_xy_denominator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && goodDCAmp,                                              my_2d_histos, "efficiencyDC_vs_xy_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold,                           my_2d_histos, "efficiency_vs_xy_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && !goodNeighbour,         my_2d_histos, "efficiency_vs_xy_noNeighb_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && highFraction,           my_2d_histos, "efficiency_vs_xy_highFrac_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && oneStripReco,           my_2d_histos, "efficiency_vs_xy_oneStrip_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && twoStripsReco,          my_2d_histos, "efficiency_vs_xy_twoStrips_numerator_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && fullReco,                                               my_2d_histos, "efficiency_vs_xy_fullReco_numerator_tight", x,y);

        utility::fillHisto(pass_tightY_noPhotek,                                                           my_2d_histos, "efficiency_vs_xy_denominator_coarseBins_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold,                           my_2d_histos, "efficiency_vs_xy_numerator_coarseBins_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && oneStripReco,           my_2d_histos, "efficiency_vs_xy_oneStrip_numerator_coarseBins_tight", x,y);
        utility::fillHisto(pass_tightY_noPhotek && hasGlobalSignal_lowThreshold && twoStripsReco,          my_2d_histos, "efficiency_vs_xy_twoStrips_numerator_coarseBins_tight", x,y);


        utility::fillHisto(goodTrack,                                                                      my_2d_prof, "efficiency_vs_xy_DCRing", x,y,goodDCAmp);
        utility::fillHisto(goodTrack,                                                                      my_2d_prof, "efficiency_vs_xy_Strip2or5", x,y,goodHitGlobal2and5);
    
        for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
        {
            if(regionsOfIntrest[k].passROI(x,y))
            {
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "timeDiff_Pixel_vs_xy"+regionsOfIntrest[k].getName(), x,y,maxAmpTime-photekTime);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "timeDiffTracker_Pixel_vs_xy"+regionsOfIntrest[k].getName(), x,y,maxAmpTimeTracker-photekTime);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos, "weighted2_timeDiff_tracker_Pixel_vs_xy"+regionsOfIntrest[k].getName(), x,y,weighted2_time_tracker-photekTime);
            }
        }

        // Fill wave form histos once
        bool maxAmpInCenter = maxAmpIndex == 3;// || maxAmpIndex == 3;
        //bool directHit = (abs( corrAmp[2] - corrAmp[4]) / corrAmp[2]) < 0.05;
        //if(plotWaveForm && pass && maxAmpInCenter && goodMaxLGADAmp && maxAmpLGAD > 99.0 &&  maxAmpLGAD < 101.0)
        //{
        //    std::cout<<abs( corrAmp[2] - corrAmp[4])<<" "<<corrAmp[2]<<" "<<(abs( corrAmp[2] - corrAmp[4]) / corrAmp[2])<<std::endl;
        //}
        //if(plotWaveForm && pass && maxAmpInCenter && goodMaxLGADAmp && maxAmpLGAD > 100.0 && maxAmpLGAD < 120.0 && directHit)
        if(plotWaveForm && goodMaxLGADAmp && maxAmpInCenter)
        {
            const auto& channel = tr.getVecVec<float>("channel");
            const auto& time = tr.getVecVec<float>("time");
            const auto& timeCalibrationCorrection = tr.getVar<std::map<int, double>>("timeCalibrationCorrection");
            for(unsigned int k = 0; k < regionsOfIntrest.size(); k++)
            {
                if(regionsOfIntrest[k].passROI(x,y))
                {
                    for(unsigned int i = 0; i < channel.size(); i++)
                    {
                        auto t = timeCalibrationCorrection.at(i) - 10.0;
                        if(i==7) continue;
                        std::string index = std::to_string(i);
                        for(unsigned int j = 0; j < time[0].size(); j++)
                        {
                            my_histos["wave"+index]->Fill(1e9*time[0][j] - photekTime - t, channel[i][j]);
                            my_1d_prof["waveProf"+index+regionsOfIntrest[k].getName()]->Fill(1e9*time[0][j] - photekTime - t, channel[i][j]);
                        }
                    }
                }
            }
             
            for(unsigned int i = 0; i < channel.size(); i++)
            {
                auto t = timeCalibrationCorrection.at(i) - 10.0;
                if(i==7) continue;
                std::string index = std::to_string(i);
                for(unsigned int j = 0; j < time[0].size(); j++)
                {
                    my_1d_prof["waveProf"+index]->Fill(1e9*time[0][j] - photekTime - t, channel[i][j]);
             
                }
            }
        
        }	// Example Fill event selection efficiencies
        my_efficiencies["event_oneStripReco"]->SetUseWeightedEvents();
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass,1.0,0); // "Pass");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold,1.0,1); // "Signal over Noise");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && oneStripReco,1.0,2); // "OneStripReco");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && highFraction,1.0,3); // "High fraction");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && highFraction && goodNeighbour,1.0,4); // "Good neighbour but high fraction");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && !goodNeighbour,1.0,5); // "No good neighbour");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && highFraction && !goodNeighbour,1.0,6); // "Both high fraction and No neighbour");
        my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_lowThreshold && oneStripReco && hitOnMetal,1.0,7); // "OneStripReco && OnMetal");
        // my_efficiencies["event_oneStripReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold && oneStripReco,1.0,4); // "OneStripReco HighThreshold");

        my_efficiencies["event_twoStripsReco"]->SetUseWeightedEvents();
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass,1.0,0); // "Pass");
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold,1.0,1); // "Signal over highThreshold");
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold && goodNeighbour,1.0,2); // "Good neighbour");
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold && !highFraction,1.0,3); // "Good Amp fraction");
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold && twoStripsReco,1.0,4); // "TwoStripsReco");
        my_efficiencies["event_twoStripsReco"]->FillWeighted(pass && hasGlobalSignal_highThreshold && twoStripsReco && hitOnMetal,1.0,5); // "TwoStripsReco && OnMetal");
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

