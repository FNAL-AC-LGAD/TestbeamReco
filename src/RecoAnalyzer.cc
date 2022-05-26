#define RecoAnalyzer_cxx
#include "TestbeamReco/interface/RecoAnalyzer.h"
#include "TestbeamReco/interface/Utility.h"
#include "TestbeamReco/interface/NTupleReader.h"

#include <TH1D.h>
#include <TH2D.h>
#include <TEfficiency.h>
#include <TFile.h>
#include <iostream>

RecoAnalyzer::RecoAnalyzer()
{
}

//Define all your histograms here. 
void RecoAnalyzer::InitHistos(NTupleReader& tr, const std::vector<std::vector<int>>& geometry)
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
    // const auto& regionsOfIntrest = tr.getVar<std::vector<utility::ROI>>("regionsOfIntrest");
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

            //Define 1D histograms
            utility::makeHisto(my_histos,"amp"+r+s,"", 450,-50.0,400.0);
            utility::makeHisto(my_histos,"relFrac"+r+s, "", 100, 0.0, 1.0);
            // utility::makeHisto(my_histos,"risetime"+r+s,"", 150,0.0,1500.0);
            // for (unsigned int ch = 0; ch < row.size(); ch++)
            // {
            //     const auto& c = std::to_string(ch);
            //     utility::makeHisto(my_histos,"amp"+r+s+"From"+c,"", 405,-5.0,400.0);
            // }
            
            //Define 2D histograms
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_numerator_channel"+r+s,"; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_prof,  "efficiency_vs_xy_highThreshold_prof_channel"+r+s, "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);
            utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_numerator_channel"+r+s, "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
            utility::makeHisto(my_2d_histos,"relFrac_vs_x_channel"+r+s, "; X [mm]; relFrac", (xmax-xmin)/xBinSize,xmin,xmax, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"relFrac_vs_y_channel"+r+s, "; Y [mm]; relFrac", (ymax-ymin)/yBinSize,ymin,ymax, 100,0.0,1.0);            
            utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s, "; X_{track} - X_{Max Strip} [mm]; Amp_{Max} / Amp_{Max} + Amp_{2}", (5*pitch)/0.02,-2.5*pitch,2.5*pitch, 100,0.0,1.0);
            utility::makeHisto(my_2d_histos,"amp_vs_x_channel"+r+s, "; X [mm]; amp", (xmax-xmin)/xBinSize,xmin,xmax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"amp_vs_y_channel"+r+s, "; Y [mm]; amp", (ymax-ymin)/yBinSize,ymin,ymax, 250,0.0,500);
            utility::makeHisto(my_2d_histos,"stripBoxInfo"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);            
            utility::makeHisto(my_2d_histos,"stripBoxInfoY"+r+s, "", 1,-9999.0,9999.0, 1,-9999.9,9999.9);  
            /*for (unsigned int ch = 0; ch < row.size(); ch++)
            {
                const auto& c = std::to_string(ch);
                utility::makeHisto(my_2d_histos,"wave"+r+s+"From"+c+"","", timeDiffNbin,-5.,5.,100,-85,15);
                utility::makeHisto(my_2d_histos,"wave"+r+s+"From"+c+"goodHit","", timeDiffNbin,-5.,5.,100,-85,15);
            }*/

            //Define 3D histograms
            utility::makeHisto(my_3d_histos,"amplitude_vs_xy_channel"+r+s,"; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
        }
        rowIndex++;
    }
    //Global 1D histograms
    utility::makeHisto(my_histos,"ntracks_alt", "; ntracks_alt; Events", 10,0,10);
    utility::makeHisto(my_histos,"chi2", "; Track chi2/ndf; Events", 60,0,30);
    utility::makeHisto(my_histos,"nplanes", "; nplanes; Events", 20,0,20);
    utility::makeHisto(my_histos,"npix", "; npix; Events", 4,0,4);
    utility::makeHisto(my_histos,"slopeX", "; Track X slope [mm per mm]; Events", 100,-0.001,0.001);
    utility::makeHisto(my_histos,"slopeY", "; Track Y slope [mm per mm]; Events", 100,-0.001,0.001);
    utility::makeHisto(my_histos,"deltaX", "; X_{reco} - X_{track} [mm]; Events", 200,-0.5,0.5);
    utility::makeHisto(my_histos,"clusterSize", "; Cluster Size", 8,0.0,8.0);

    utility::makeHisto(my_histos,"index_diff", "; index1 - index2; Events", 8,-4,4);

    //Global 2D histograms
    utility::makeHisto(my_2d_histos,"relFracTot_vs_x", "; X [mm]; relFracTot", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"relFracMaxAmp_vs_x", "; X [mm]; relFrac", (xmax-xmin)/xBinSize,-0.4,0.4, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_oneStrip_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_highThreshold_twoStrips_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_highThreshold_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_highThreshold_oneStrip_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_prof  ,"efficiency_vs_xy_highThreshold_twoStrips_prof", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax );
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_oneStrip_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_lowThreshold_twoStrips_numerator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);
    utility::makeHisto(my_2d_histos,"efficiency_vs_xy_denominator", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax);

    utility::makeHisto(my_2d_histos,"Amp1OverAmp1and2_vs_deltaXmax", "",           (5*pitch)/0.01,-2.5*pitch,2.5*pitch, 100,0.0,1.0);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);

    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_oneStrip", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_Xtrack_twoStrips", "; X_{track} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);

    utility::makeHisto(my_2d_histos,"deltaX_vs_Xreco", "; X_{reco} [mm]; #X_{reco} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xtrack", "; X_{track} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaXmax_vs_Xreco", "; X_{reco} [mm]; #X_{max} - X_{track} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_amplitude1", "; amp; #X_{reco} - X_{track} [mm]", 500,0,500, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"deltaX_vs_amplitude2", "; amp; #X_{reco} - X_{track} [mm]", 500,0,500, 200,-0.5,0.5);
    utility::makeHisto(my_2d_histos,"Xreco_vs_Xtrack", "; X_{track} [mm]; #X_{reco} [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (xmax-xmin)/xBinSize,xmin,xmax);

    //Define 3D histograms
    utility::makeHisto(my_3d_histos,"amplitude_vs_xy","; X [mm]; Y [mm]",(xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500 );
    utility::makeHisto(my_3d_histos,"amp12_vs_xy", "; X [mm]; Y [mm]", (xmax-xmin)/xBinSize,xmin,xmax, (ymax-ymin)/yBinSize,ymin,ymax, 250,0,500);


    //Define 2d prof
    utility::makeHisto(my_2d_prof,"efficiency_vs_xy_Strip2or5", "; X [mm]; Y [mm]", xbins,xmin,xmax, ybins,ymin,ymax);	
    
    //Define 1d prof
    
    //Define TEfficiencies if you are doing trigger studies (for proper error bars) or cut flow charts.
    utility::makeHisto(my_efficiencies,"event_sel_weight","",9,0,9);
    utility::makeHisto(my_efficiencies,"efficiency_vs_x","; X [mm]",xbins,xmin,xmax);
    utility::makeHisto(my_efficiencies,"efficiency_vs_xy","; X [mm]; Y [mm]",xbins,xmin,xmax, ybins,ymin,ymax);
    std::cout<<"Finished defining histos"<<std::endl;
}

//Put everything you want to do per event here.
void RecoAnalyzer::Loop(NTupleReader& tr, int maxevents)
{
    const auto& geometry = tr.getVar<std::vector<std::vector<int>>>("geometry");
    const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
    const auto& noiseAmpThreshold = tr.getVar<double>("noiseAmpThreshold");
    const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");
    const auto& photekSignalMax = tr.getVar<double>("photekSignalMax");
    const auto& isPadSensor = tr.getVar<bool>("isPadSensor");
    const auto& isHPKStrips = tr.getVar<bool>("isHPKStrips");
    const auto& uses2022Pix = tr.getVar<bool>("uses2022Pix");
    const auto& minPixHits = tr.getVar<int>("minPixHits");
    const auto& minStripHits = tr.getVar<int>("minStripHits");
    const auto& positionRecoMaxPoint = tr.getVar<double>("positionRecoMaxPoint");
    const auto& sensorEdges = tr.getVar<std::vector<std::vector<double>>>("sensorEdges");
    // const auto& timeCalibrationCorrection = tr.getVar<std::map<int, double>>("timeCalibrationCorrection");
    const auto& stripWidth = tr.getVar<double>("stripWidth");
    const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
    const auto& highGoodStripIndex = tr.getVar<int>("highGoodStripIndex");
    const auto& firstFile = tr.getVar<bool>("firstFile");
    const auto& regionsOfIntrest = tr.getVar<std::vector<utility::ROI>>("regionsOfIntrest");

    for(const auto& roi : regionsOfIntrest)
    {
        std::cout<<roi.getName()<<" "<<roi.passROI(0.0,0.0)<<" "<<roi.passROI(10000.0,0.0)<<std::endl;
    }

    int lowGoodStrip = (geometry[0].size()==1) ? lowGoodStripIndex-1 : lowGoodStripIndex;
    int highGoodStrip = (geometry[0].size()==1) ? highGoodStripIndex-1 : highGoodStripIndex;

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
        const auto& padx = tr.getVar<double>("padx");
        const auto& x_reco = tr.getVar<double>("x_reco");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& relFrac = tr.getVec<std::vector<double>>("relFrac");
        const auto& Amp12 = tr.getVar<double>("Amp12");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& amp1Indexes = tr.getVar<std::pair<int,int>>("amp1Indexes");
        const auto& amp2Indexes = tr.getVar<std::pair<int,int>>("amp2Indexes");
        const auto& deltaXmax = tr.getVar<double>("deltaXmax");
        const auto& Amp1OverAmp1and2 = tr.getVar<double>("Amp1OverAmp1and2");
        const auto& hasGlobalSignal_lowThreshold = tr.getVar<bool>("hasGlobalSignal_lowThreshold");
        const auto& hasGlobalSignal_highThreshold = tr.getVar<bool>("hasGlobalSignal_highThreshold");
        const auto& clusterSize = tr.getVar<int>("clusterSize");
        const auto& stripCenterXPositionLGAD = tr.getVec<std::vector<double>>("stripCenterXPositionLGAD");
        const auto& stripCenterYPositionLGAD = tr.getVec<std::vector<double>>("stripCenterYPositionLGAD");
        const auto& goodNeighbour = tr.getVar<bool>("goodNeighbour");
        
        //Define selection bools
        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold && corrAmp[photekIndex] < photekSignalMax;
        bool goodTrack = ntracks==1 && nplanes>=14 && npix>0 && chi2 < 3.0 && xSlope<0.0001 && xSlope>-0.0001;// && ntracks_alt==1;
        if(isPadSensor)      goodTrack = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        else if(isHPKStrips || uses2022Pix) goodTrack = ntracks==1 && (nplanes-npix)>=minStripHits && npix>=minPixHits && chi2 < 40;
        bool pass = goodTrack && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = ((maxAmpIndex >= lowGoodStrip && maxAmpIndex <= highGoodStrip) || isPadSensor);
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;
        // bool highRelAmp1 = Amp1OverAmp1and2>=0.75;
        bool twoGoodHits = ampLGAD[amp1Indexes.first][amp1Indexes.second] > noiseAmpThreshold && ampLGAD[amp2Indexes.first][amp2Indexes.second] > noiseAmpThreshold;
        bool oneStripReco = !(goodNeighbour && (Amp1OverAmp1and2 < positionRecoMaxPoint));

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

        double maxAmp = ampLGAD[amp1Indexes.first][amp1Indexes.second];
        double amp2 = ampLGAD[amp2Indexes.first][amp2Indexes.second];
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
                const auto& maxAmpStr = std::to_string(maxAmpIndex);
                const auto& ampChannel = ampLGAD[rowIndex][i];
                const auto& relFracChannel = relFrac[rowIndex][i];
                bool goodNoiseAmp = ampChannel>noiseAmpThreshold;
                bool goodSignalAmp = ampChannel>signalAmpThreshold;
                bool isMaxChannel = amp1Indexes.first == rowIndex && amp1Indexes.second == int(i);
                bool goodHit = goodNoiseAmp && goodMaxLGADAmp;
                if(i==1 || i==4) goodHitGlobal2and5 = goodHitGlobal2and5 || (isMaxChannel && goodHit);
                utility::fillHisto(pass,                                                    my_histos["amp"+r+s], ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_histos["relFrac"+r+s], relFracChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["amp_vs_x_channel"+r+s], x,ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["amp_vs_y_channel"+r+s], y,ampChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_x_channel"+r+s], x,relFracChannel);
                utility::fillHisto(pass && goodHit,                                         my_2d_histos["relFrac_vs_y_channel"+r+s], y,relFracChannel);
                utility::fillHisto(pass && goodHit && isMaxChannel && goodNeighbour,        my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax_channel"+r+s], deltaXmax, Amp1OverAmp1and2);
                utility::fillHisto(pass && goodNoiseAmp,                                    my_2d_histos["efficiency_vs_xy_lowThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(pass && goodSignalAmp,                                   my_2d_histos["efficiency_vs_xy_highThreshold_numerator_channel"+r+s], x,y);
                utility::fillHisto(firstEvent,                                              my_2d_histos["stripBoxInfo"+r+s], stripCenterXPositionLGAD[rowIndex][i],stripWidth);
                utility::fillHisto(firstEvent,                                              my_2d_histos["stripBoxInfoY"+r+s], stripCenterYPositionLGAD[rowIndex][i],stripWidth);

                utility::fillHisto(pass && goodHit,                                         my_3d_histos["amplitude_vs_xy_channel"+r+s], x,y,ampChannel);
                utility::fillHisto(goodTrack && goodPhotek,                                 my_2d_prof["efficiency_vs_xy_highThreshold_prof_channel"+r+s], x,y,ampChannel > signalAmpThreshold);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel,                 my_2d_prof["efficiency_vs_xy_highThreshold_prof"], x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && oneStripReco, my_2d_prof["efficiency_vs_xy_highThreshold_oneStrip_prof"], x,y,goodHit);
                utility::fillHisto(goodTrack && goodPhotek && isMaxChannel && !oneStripReco,my_2d_prof["efficiency_vs_xy_highThreshold_twoStrips_prof"], x,y,goodHit);
                utility::fillHisto(goodTrack && isMaxChannel,                               my_efficiencies["efficiency_vs_x"], goodHit,x);
                utility::fillHisto(goodTrack && isMaxChannel,                               my_efficiencies["efficiency_vs_xy"], goodHit,x,y);
            }
            rowIndex++;
        }
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["deltaX"], x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["chi2"], chi2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["ntracks_alt"], ntracks_alt);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["nplanes"], nplanes);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["npix"], npix);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["slopeX"], xSlope);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["slopeY"], ySlope);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["clusterSize"], clusterSize);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_histos["index_diff"], amp1Indexes.second - amp2Indexes.second);

        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["relFracMaxAmp_vs_x"], padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass,                                                                           my_2d_histos["efficiency_vs_xy_denominator"], x,y);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_2d_histos["relFracTot_vs_x"], padx, relFrac[amp1Indexes.first][amp1Indexes.second]);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && twoGoodHits,                    my_2d_histos["Amp1OverAmp1and2_vs_deltaXmax"], fabs(deltaXmax),Amp1OverAmp1and2);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_Xtrack"], x,x_reco-x);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && oneStripReco,                   my_2d_histos["deltaX_vs_Xtrack_oneStrip"], x,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && !oneStripReco,                  my_2d_histos["deltaX_vs_Xtrack_twoStrips"], x,x_reco-x);

        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_Xreco"], x_reco,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaXmax_vs_Xtrack"], x,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaXmax_vs_Xreco"], x_reco,deltaXmax);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["Xreco_vs_Xtrack"], x,x_reco);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_amplitude1"], maxAmp,x_reco-x);
        utility::fillHisto(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp,                                   my_2d_histos["deltaX_vs_amplitude2"], amp2,x_reco-x);

        utility::fillHisto(pass && hasGlobalSignal_lowThreshold,                                           my_2d_histos["efficiency_vs_xy_lowThreshold_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold,                                          my_2d_histos["efficiency_vs_xy_highThreshold_numerator"], x,y);

        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && oneStripReco,                           my_2d_histos["efficiency_vs_xy_lowThreshold_oneStrip_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold && oneStripReco,                          my_2d_histos["efficiency_vs_xy_highThreshold_oneStrip_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_lowThreshold && !oneStripReco,                          my_2d_histos["efficiency_vs_xy_lowThreshold_twoStrips_numerator"], x,y);
        utility::fillHisto(pass && hasGlobalSignal_highThreshold && !oneStripReco,                         my_2d_histos["efficiency_vs_xy_highThreshold_twoStrips_numerator"], x,y);
        
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["amplitude_vs_xy"], x,y,maxAmp);
        utility::fillHisto(pass && goodMaxLGADAmp,                                                         my_3d_histos["amp12_vs_xy"], x,y, Amp12);

        utility::fillHisto(goodTrack,                                                                      my_2d_prof["efficiency_vs_xy_Strip2or5"], x,y,goodHitGlobal2and5);
        
        // Example Fill event selection efficiencies
        my_efficiencies["event_sel_weight"]->SetUseWeightedEvents();
        my_efficiencies["event_sel_weight"]->FillWeighted(true,1.0,0);
    } //event loop
}

void RecoAnalyzer::WriteHistos(TFile* outfile)
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

