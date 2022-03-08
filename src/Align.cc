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

    //Define 1D histograms
    const auto& pitch = tr.getVar<double>("pitch");
    const auto& xmin = tr.getVar<double>("xmin");
    const auto& xmax = tr.getVar<double>("xmax");
    double xBinSize = 0.005; // 0.016
    double xBinSizePad = 0.025;
    double yBinSizePad = 0.025;
    const auto& ymin = tr.getVar<double>("ymin");
    const auto& ymax = tr.getVar<double>("ymax");
    int xbins = 175;
    int ybins = 175;


    int timeDiffNbin = 400; // 200
    double timeDiffLow = -1.0;
    double timeDiffHigh = 1.0;
    int timeDiffYnbin = 50;
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
    const auto& isPadSensor = tr.getVar<bool>("isPadSensor");
    const auto& isHPKStrips = tr.getVar<bool>("isHPKStrips");
    //const auto& xSlices = tr.getVar<std::vector<std::vector<double>>>("xSlices");
    const auto& ySlices = tr.getVar<std::vector<std::vector<double>>>("ySlices");
    const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
    // const auto& timeCalibrationCorrection = tr.getVar<std::map<int, double>>("timeCalibrationCorrection");
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
        /*const auto& channel = tr.getVecVec<float>("channel");
        const auto& time_real = tr.getVecVec<float>("time");*/
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
        const auto& ySlope = tr.getVar<float>("ySlope");
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
        bool passTrigger = ntracks==1 && nplanes>=14 && npix>0 && chi2 < 3.0 && xSlope<0.0001 && xSlope>-0.0001;// && ntracks_alt==1;
        if(isPadSensor)      passTrigger = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        else if(isHPKStrips) passTrigger = ntracks==1 && nplanes>=14 && npix>0 && chi2 < 40 && ySlope+0.0001415<0.0001 && ySlope+0.0001415>-0.0001;// && ntracks_alt==1;
        bool pass = passTrigger && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = ((maxAmpIndex >= lowGoodStripIndex && maxAmpIndex <= highGoodStripIndex) || isPadSensor);
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
        bool twoGoodHits = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold && ampLGAD[amp2Indexes.first][amp2Indexes.second] > noiseAmpThreshold;
        double photekTime = corrTime[photekIndex];
        double maxAmpTime = timeLGAD[amp1Indexes.first][amp1Indexes.second];
        double amp2Time = timeLGAD[amp2Indexes.first][amp2Indexes.second];
        double amp3Time = timeLGAD[amp3Indexes.first][amp3Indexes.second];
        double firstEvent = tr.isFirstEvent();

        //******************************************************************
        //Make cuts and fill histograms here
    	//******************************************************************        
        //Loop over each channel in each sensor
        for(unsigned int ivar=0; ivar < x_var.size(); ivar++)
        {
            utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                               my_histos["deltaX_var"+std::to_string(ivar)], x_reco-x_var[ivar]);
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

