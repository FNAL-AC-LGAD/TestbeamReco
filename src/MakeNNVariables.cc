#define MakeNNVariables_cxx
#include "TestbeamReco/interface/MakeNNVariables.h"
#include "TestbeamReco/interface/NTupleReader.h"
#include "TestbeamReco/interface/MiniTupleMaker.h"
#include "TestbeamReco/interface/Utility.h" 

#include <TH1D.h>
#include <TH2D.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TEfficiency.h>
#include <TRandom3.h>
#include <iostream>
#include <stdio.h> 

MakeNNVariables::MakeNNVariables()
{
    InitHistos();
}

void MakeNNVariables::InitHistos()
{
}//END of init histos

void MakeNNVariables::Loop(NTupleReader& tr, int maxevents)
{
    int count = 0, numPassTrain = 0, numPassTest  = 0, numPassVal = 0;

    while( tr.getNextEvent() )
    {
        //const auto& eventCounter = tr.getVar<int>("eventCounter");
        const auto& filetag      = tr.getVar<std::string>("filetag");
       
        //------------------------------------
        //-- Print Event Number
        //------------------------------------
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 100000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );        

        //-----------------------------------
        //  Initialize the tree
        //-----------------------------------       
        const auto& ampLGAD = tr.getVec<std::vector<double>>("ampLGAD");
        tr.createDerivedVar<double>("amp1",ampLGAD[0][0]);
        tr.createDerivedVar<double>("amp2",ampLGAD[0][1]);
        tr.createDerivedVar<double>("amp3",ampLGAD[0][2]);
        tr.createDerivedVar<double>("amp4",ampLGAD[0][3]);
        tr.createDerivedVar<double>("amp5",ampLGAD[0][4]);
        tr.createDerivedVar<double>("amp6",ampLGAD[0][5]);

        const auto& photekIndex = tr.getVar<int>("photekIndex");
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        tr.createDerivedVar<double>("ampPhotek",corrAmp[photekIndex]);

        //Correct for jitter in trigger time
        const auto& timeLGAD = tr.getVec<std::vector<double>>("timeLGAD");
        const auto& corrTime = tr.getVec<double>("corrTime");
        double timeShift = 201.8;
        double rawPhotekTime = corrTime[photekIndex] + timeShift;
        if(rawPhotekTime < -4.2)
        {
            timeShift += 6.0889;
        }
        else if(-4.2 <= rawPhotekTime && rawPhotekTime < -1.0)
        {
            timeShift += 3.066;
        }
        else if(rawPhotekTime > 2.5)
        {
            timeShift += -2.941;
        }
        tr.createDerivedVar<double>("time1",(timeLGAD[0][0] != 0) ? timeLGAD[0][0] + timeShift : -10.0);
        tr.createDerivedVar<double>("time2",(timeLGAD[0][1] != 0) ? timeLGAD[0][1] + timeShift : -10.0);
        tr.createDerivedVar<double>("time3",(timeLGAD[0][2] != 0) ? timeLGAD[0][2] + timeShift : -10.0);
        tr.createDerivedVar<double>("time4",(timeLGAD[0][3] != 0) ? timeLGAD[0][3] + timeShift : -10.0);
        tr.createDerivedVar<double>("time5",(timeLGAD[0][4] != 0) ? timeLGAD[0][4] + timeShift : -10.0);
        tr.createDerivedVar<double>("time6",(timeLGAD[0][5] != 0) ? timeLGAD[0][5] + timeShift : -10.0);
        tr.createDerivedVar<double>("timePhotek",corrTime[photekIndex] + timeShift);
        
        //const auto& timeLGAD = utility::remapToLGADgeometry(tr, LP2_20, "timeLGAD");
        //tr.createDerivedVar<double>("time1",timeLGAD[0][0]*1e9 + timeShift + 10.53);
        //tr.createDerivedVar<double>("time2",timeLGAD[0][1]*1e9 + timeShift + 10.60);
        //tr.createDerivedVar<double>("time3",timeLGAD[0][2]*1e9 + timeShift + 10.60);
        //tr.createDerivedVar<double>("time4",timeLGAD[0][3]*1e9 + timeShift + 10.57);
        //tr.createDerivedVar<double>("time5",timeLGAD[0][4]*1e9 + timeShift + 10.56);
        //tr.createDerivedVar<double>("time6",timeLGAD[0][5]*1e9 + timeShift + 10.08);
        //tr.createDerivedVar<double>("timePhotek",LP2_20[photekIndex]*1e9 + timeShift);

        std::set<std::string> varGeneral = 
        {
            "x","deltaXmax","xCenterMaxStrip",
            "y",
            "ampPhotek","timePhotek",            
            "amp1","amp2","amp3","amp4","amp5","amp6",
            "time1","time2","time3","time4","time5","time6",
            "weighted_time",
            "Amp1OverAmp1and2","Amp2OverAmp2and3","Amp1OverAmp123","Amp2OverAmp123","Amp3OverAmp123",
        };
        
        if( tr.isFirstEvent() ) 
        {
            std::string myTreeName = "myMiniTree";
            myMiniTupleTrain = new MiniTupleMaker( filetag+"_Train.root", myTreeName );
            myMiniTupleTrain->setTupleVars(varGeneral);
            myMiniTupleTrain->initBranches(tr);

            myMiniTupleTest = new MiniTupleMaker( filetag+"_Test.root", myTreeName );
            myMiniTupleTest->setTupleVars(varGeneral);
            myMiniTupleTest->initBranches(tr);

            myMiniTupleVal = new MiniTupleMaker( filetag+"_Val.root", myTreeName ); 
            myMiniTupleVal->setTupleVars(varGeneral);
            myMiniTupleVal->initBranches(tr);
        }
        
        //-----------------------------------
        //-- Fill Histograms Below
        //-----------------------------------                                                  
        const auto& photekSignalThreshold = tr.getVar<double>("photekSignalThreshold");
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& maxAmpIndex = tr.getVar<int>("maxAmpIndex");
        const auto& lowGoodStripIndex = tr.getVar<int>("lowGoodStripIndex");
        const auto& maxAmpLGAD = tr.getVar<double>("maxAmpLGAD");
        const auto& signalAmpThreshold = tr.getVar<double>("signalAmpThreshold");

        bool goodPhotek = corrAmp[photekIndex] > photekSignalThreshold;
        bool passTrigger = ntracks==1 && nplanes>10 && npix>0 && chi2 < 30.0;
        bool pass = passTrigger && hitSensor && goodPhotek;
        bool maxAmpNotEdgeStrip = maxAmpIndex >= lowGoodStripIndex && maxAmpIndex <= 4;
        bool goodMaxLGADAmp = maxAmpLGAD > signalAmpThreshold;

        if(pass && maxAmpNotEdgeStrip && goodMaxLGADAmp && corrTime[photekIndex] != 0)
        {
            int mod = count % 10;
            if(mod < 8)
            {
                myMiniTupleTrain->fill();
                numPassTrain++;
            }
            else if(mod == 8)
            {
                myMiniTupleTest->fill();
                numPassTest++;
            }
            else
            {
                myMiniTupleVal->fill();
                numPassVal++;
            }
            count++;
        }
    }//END of while tr.getNextEvent loop   
    std::cout << "Total: " << count << "   Train: " << numPassTrain << "   Test: " << numPassTest << "   Val: " << numPassVal << std::endl;

}//END of function
      
void MakeNNVariables::WriteHistos( TFile* outfile ) 
{
    const auto& outFileName = std::string(outfile->GetName());
    remove(outFileName.c_str());

    delete myMiniTupleTrain;
    delete myMiniTupleTest;
    delete myMiniTupleVal;
}

