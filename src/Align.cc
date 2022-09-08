#define Align_cxx
#include "TestbeamReco/interface/Align.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>
#include <fstream>

Align::Align()
{
}

//Define all your histograms here. 
void Align::InitHistos(NTupleReader& tr, [[maybe_unused]] const std::vector<std::vector<int>>& geometry)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    const auto& zScan = tr.getVar<std::vector<double>>("zScan");
    const auto& alphaScan = tr.getVar<std::vector<double>>("alphaScan");
    const auto& betaScan = tr.getVar<std::vector<double>>("betaScan");
    const auto& gammaScan = tr.getVar<std::vector<double>>("gammaScan");

    // double xBinSize = 0.05;
    const auto& xBinSize = tr.getVar<double>("xBinSize");
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    // double yBinSize = 0.25;
    const auto& yBinSize = tr.getVar<double>("yBinSize");
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");

    for(unsigned int ivar = 0; ivar<(zScan.size()); ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_varZ"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200, -0.5, 0.5);
    }
    for(unsigned int ivar = 0; ivar<(alphaScan.size()); ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_varA"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200, -0.5, 0.5);
    }
    for(unsigned int ivar = 0; ivar<(betaScan.size()); ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_varB"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200, -0.5, 0.5);
    }
    for(unsigned int ivar = 0; ivar<(gammaScan.size()); ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_varC"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200, -0.5, 0.5);
    }

    utility::makeHisto(my_2d_histos,"position_local","; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"position_local_denominator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"position_local_ch2","; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    
    utility::makeHisto(my_3d_histos,"position_tracker","; X_tracker - X_C [mm]; Y_tracker - Y_C [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 200,-0.005,0.005);

    std::cout<<"Finished making histos"<<std::endl;
}

//Put everything you want to do per event here.
void Align::Loop(NTupleReader& tr, int maxevents)
{
    const auto& indexToGeometryMap = tr.getVar<std::map<int, std::vector<int>>>("indexToGeometryMap");
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& photekSignalMax = tr.getVar<double>("photekSignalMax");
    const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
    const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
    const auto& firstFile = tr.getVar<bool>("firstFile");

    int lowGoodStrip = indexToGeometryMap.at(lowGoodStripIndex)[1];
    int highGoodStrip = indexToGeometryMap.at(highGoodStripIndex)[1];

    if(firstFile)
    {
        InitHistos(tr, geometry);
    }
    
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
        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        // const auto& chi2 = tr.getVar<float>("chi2");
        const auto& x_var = tr.getVec<double>("x_var");
        // const auto& y_var = tr.getVec<double>("y_var");
        const auto& x_varA = tr.getVec<double>("x_varA");
        //const auto& y_varA = tr.getVec<double>("y_varA");
        const auto& x_varB = tr.getVec<double>("x_varB");
        //const auto& y_varB = tr.getVec<double>("y_varB");
        const auto& x_varC = tr.getVec<double>("x_varC");
        //const auto& y_varC = tr.getVec<double>("y_varC");
        const auto& x_reco = tr.getVar<double>("x_reco");
        //const auto& y_reco = tr.getVar<double>("y_reco");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");

        // const auto& hitSensorZ = tr.getVec<bool>("hitSensorZ");
        // const auto& hitSensorA = tr.getVec<bool>("hitSensorA");
        // const auto& hitSensorB = tr.getVec<bool>("hitSensorB");
        // const auto& hitSensorC = tr.getVec<bool>("hitSensorC");

        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");
        const auto& xyz_tracker = tr.getVec<double>("xyz_tracker");

        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& hasGlobalSignal_highThreshold = tr.getVar<bool>("hasGlobalSignal_highThreshold");
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold && corrAmp[photekIndex] < photekSignalMax;
        bool goodTrack = ntracks==1 && nplanes>=5 && npix>0;// && chi2 < 3.0 && xSlope<0.0001 && xSlope>-0.0001;// && ntracks_alt==1;
        bool pass = goodTrack && goodPhotek && hitSensor;
        bool maxAmpNotEdgeStrip = (maxAmpIndex >= lowGoodStrip && maxAmpIndex <= highGoodStrip);
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;
        bool goodHitCh2 = goodMaxLGADAmp && maxAmpIndex==2;

        //******************************************************************
        //Make cuts and fill histograms here
    	//******************************************************************        
        //Loop over each channel in each sensor
        for(unsigned int ivar=0; ivar < x_var.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,    my_histos, "deltaX_varZ"+std::to_string(ivar), x_reco-x_var[ivar]);
        }

        for(unsigned int ivar=0; ivar < x_varA.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,    my_histos, "deltaX_varA"+std::to_string(ivar), x_reco-x_varA[ivar]);
        }

        for(unsigned int ivar=0; ivar < x_varB.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,    my_histos, "deltaX_varB"+std::to_string(ivar), x_reco-x_varB[ivar]);
        }

        for(unsigned int ivar=0; ivar < x_varC.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,    my_histos, "deltaX_varC"+std::to_string(ivar), x_reco-x_varC[ivar]);
        }

        utility::fillHisto(pass && hasGlobalSignal_highThreshold,               my_2d_histos, "position_local", x, y);
        utility::fillHisto(pass,                                                my_2d_histos, "position_local_denominator", x, y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold && goodHitCh2, my_2d_histos, "position_local_ch2", x, y);
        
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,               my_3d_histos, "position_tracker", xyz_tracker[0], xyz_tracker[1], xyz_tracker[2]);

    } //event loop
}

void Align::WriteHistos(TFile* outfile)
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

