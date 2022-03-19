#define Align_cxx
#include "TestbeamReco/interface/Align.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>

Align::Align()
{
}

//Define all your histograms here. 
void Align::InitHistos(NTupleReader& tr, const std::vector<std::vector<int>>& geometry)
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    //This event counter histogram is necessary so that we know that all the condor jobs ran successfully. If not, when you use the hadder script, you will see a discrepancy in red as the files are being hadded.
    my_histos.emplace( "EventCounter", std::make_shared<TH1D>( "EventCounter", "EventCounter", 2, -1.1, 1.1 ) ) ;

    int nvar=35;
    for(int ivar=0;ivar<nvar;ivar++)
    {
        utility::makeHisto(my_histos,"deltaX_var"+std::to_string(ivar), "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    }
    std::cout<<"Finished making histos"<<std::endl;
}

//Put everything you want to do per event here.
void Align::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    const auto& isHPKStrips = tr.getVar<bool>("isHPKStrips");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
    const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
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
        const auto& x_var = tr.getVec<double>("x_var");
        //const auto& y_var = tr.getVec<double>("y_var");
        const auto& x_reco = tr.getVar<double>("x_reco");
        //const auto& y_reco = tr.getVar<double>("y_reco");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
        const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold;
        bool passTrigger = ntracks==1 && nplanes>=5 && npix>0;// && chi2 < 3.0 && xSlope<0.0001 && xSlope>-0.0001;// && ntracks_alt==1;
        bool pass = passTrigger && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = (maxAmpIndex >= lowGoodStripIndex && maxAmpIndex <= highGoodStripIndex);
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;

        //******************************************************************
        //Make cuts and fill histograms here
    	//******************************************************************        
        //Loop over each channel in each sensor
        for(unsigned int ivar=0; ivar < x_var.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp, my_histos["deltaX_var"+std::to_string(ivar)], x_reco-x_var[ivar]);
        }
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

