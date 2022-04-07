#define InitialAnalyzer_cxx
#include "TestbeamReco/interface/InitialAnalyzer.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>
#include <fstream>

InitialAnalyzer::InitialAnalyzer()
{
}

//Define all your histograms here. 
//void InitialAnalyzer::InitHistos(NTupleReader& tr, const std::vector<std::vector<int>>& geometry)
void InitialAnalyzer::InitHistos(NTupleReader& tr, const std::vector<std::vector<int>>& geometry)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    // const auto& pitch = tr.getVar<double>("pitch");
    const auto& xBinSize = tr.getVar<double>("xBinSize");
    const auto& yBinSize = tr.getVar<double>("yBinSize");
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");

    int timeDiffNbin = 800; // 200
    double timeDiffLow = -1.0;
    double timeDiffHigh = 1.0;
    // int timeDiffYnbin = 50;


    //Time map: use 100 micron bins along strip

    int rowIndex = 0;
    for(const auto& row : geometry)
    {
        if(row.size()<2) continue;
        for(unsigned int i = 0; i < row.size(); i++)
        {
            const auto& r = std::to_string(rowIndex);
            const auto& s = std::to_string(i);
    utility::makeHisto(my_3d_histos,"amplitude_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 500,0,500 );
    utility::makeHisto(my_3d_histos,"timeDiff_vs_xy_channel"+r+s, "; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, timeDiffNbin,timeDiffLow,timeDiffHigh);

    }
    rowIndex++;
}
    std::cout<<"Finished making histos"<<std::endl;
}

//Put everything you want to do per event here.
void InitialAnalyzer::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    //const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& photekSignalMax = tr.getVar<double>("photekSignalMax");
    const auto& minPixHits = tr.getVar<int>("minPixHits");
    const auto& minStripHits = tr.getVar<int>("minStripHits");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");

    //const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
    const auto& firstFile = tr.getVar<bool>("firstFile");
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
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");

        const auto& rawAmpLGAD = tr.getVec<std::vector<float>>("rawAmpLGAD");

        const auto& corrTime = tr.getVec<double>("corrTime");
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        //const auto& x_var = tr.getVec<double>("x_var");
        ////const auto& y_var = tr.getVec<double>("y_var");
        ////const auto& x_reco = tr.getVar<double>("x_reco");
        ////const auto& y_reco = tr.getVar<double>("y_reco");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        //const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        //const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        //const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
        //const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold && corrAmp[photekIndex] < photekSignalMax;
        bool passTrigger = ntracks==1 && (nplanes-npix)>=minStripHits && npix>=minPixHits && chi2 < 40;
        bool pass = passTrigger && hitSensor && goodPhotek;

        double photekTime = corrTime[photekIndex];
        const auto& x = tr.getVar<double>("x");
        const auto& y = tr.getVar<double>("y");

        //******************************************************************
        //Make cuts and fill histograms here
    	//******************************************************************        
        //Loop over each channel in each sensor
        int rowIndex=0;
        for(const auto& row : ampLGAD)
        {
            for(unsigned int i = 0; i < row.size(); i++)
            {
                const auto& r = std::to_string(rowIndex);
                const auto& s = std::to_string(i);
                // const auto& ampChannel = ampLGAD[rowIndex][i];
                // const auto& relFracChannel = relFrac[rowIndex][i];
                const auto& rawAmpChannel = rawAmpLGAD[rowIndex][i];
                // const auto& noise = baselineRMS[rowIndex][i]; 
                // const auto& risetime = risetimeLGAD[rowIndex][i];
                // const auto& charge = chargeLGAD[rowIndex][i];
                // const auto& ampChargeRatio = ampChargeRatioLGAD[rowIndex][i];
                bool goodNoiseAmp = rawAmpChannel>noiseAmpThreshold;
                double time = timeLGAD[rowIndex][i];

                utility::fillHisto(pass && goodNoiseAmp,                 my_3d_histos["amplitude_vs_xy_channel"+r+s], x,y,rawAmpChannel);
                utility::fillHisto(pass && goodNoiseAmp,                 my_3d_histos["timeDiff_vs_xy_channel"+r+s], x,y,time-photekTime);

        }
        rowIndex++;

    }



    } //event loop
}

void InitialAnalyzer::WriteHistos(TFile* outfile)
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

