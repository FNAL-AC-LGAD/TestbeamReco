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
//#include <fstream>
//#include <cstdio>

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
        const auto& eventCounter = tr.getVar<int>("eventCounter");
        const auto& filetag      = tr.getVar<std::string>("filetag");
       
        //------------------------------------
        //-- Print Event Number
        //------------------------------------
        if( maxevents != -1 && tr.getEvtNum() >= maxevents ) break;
        if( tr.getEvtNum() % 100000 == 0 ) printf( " Event %i\n", tr.getEvtNum() );        

        //-----------------------------------
        //  Initialize the tree
        //-----------------------------------       
        const auto& corrAmp = tr.getVec<double>("corrAmp");
        const auto& ampLGAD = utility::remapToLGADgeometry(tr, corrAmp, "ampLGAD");
        tr.createDerivedVar<double>("amp1",ampLGAD[0][0]);
        tr.createDerivedVar<double>("amp2",ampLGAD[0][1]);
        tr.createDerivedVar<double>("amp3",ampLGAD[0][2]);
        tr.createDerivedVar<double>("amp4",ampLGAD[0][3]);
        tr.createDerivedVar<double>("amp5",ampLGAD[0][4]);
        tr.createDerivedVar<double>("amp6",ampLGAD[0][5]);

        const auto& LP2_20 = tr.getVec<float>("LP2_20");
        const auto& timeLGAD = utility::remapToLGADgeometry(tr, LP2_20, "timeLGAD");
        tr.createDerivedVar<double>("time1",timeLGAD[0][0]*1e9 + 201.8);
        tr.createDerivedVar<double>("time2",timeLGAD[0][1]*1e9 + 201.8);
        tr.createDerivedVar<double>("time3",timeLGAD[0][2]*1e9 + 201.8);
        tr.createDerivedVar<double>("time4",timeLGAD[0][3]*1e9 + 201.8);
        tr.createDerivedVar<double>("time5",timeLGAD[0][4]*1e9 + 201.8);
        tr.createDerivedVar<double>("time6",timeLGAD[0][5]*1e9 + 201.8);

        const auto& photekIndex = tr.getVar<int>("photekIndex");
        tr.createDerivedVar<double>("timePhotek",LP2_20[photekIndex]*1e9 + 201.8);
        const auto& amp = tr.getVec<float>("amp");
        tr.createDerivedVar<double>("ampPhotek",amp[photekIndex]);

        std::set<std::string> varGeneral = 
        {
            "x",
            "y",
            "ampPhotek","timePhotek",            
            "amp1","amp2","amp3","amp4","amp5","amp6",
            "time1","time2","time3","time4","time5","time6",
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
        const auto& ntracks = tr.getVar<int>("ntracks");
        const auto& nplanes = tr.getVar<int>("nplanes");
        const auto& npix = tr.getVar<int>("npix");
        const auto& hitSensor = tr.getVar<bool>("hitSensor");
        const auto& chi2 = tr.getVar<float>("chi2");
        const auto& x = tr.getVar<double>("x");
        const auto& ampPhotek = tr.getVar<double>("ampPhotek");
        const auto& timePhotek = tr.getVar<double>("timePhotek");
        //bool hitMidStrips = 0.23 < x && x < 0.53;
        bool hitMidStrips = true;
        bool passAmpCut = (20.0 < ampLGAD[0][1] && 20.0 < ampLGAD[0][2]                         && ampLGAD[0][1] > ampLGAD[0][2]) ||
                          (20.0 < ampLGAD[0][1] && 20.0 < ampLGAD[0][2] && 20.0 < ampLGAD[0][3] && ampLGAD[0][2] > ampLGAD[0][1] && ampLGAD[0][2] > ampLGAD[0][3]) ||
                          (20.0 < ampLGAD[0][2] && 20.0 < ampLGAD[0][3] && 20.0 < ampLGAD[0][4] && ampLGAD[0][3] > ampLGAD[0][2] && ampLGAD[0][3] > ampLGAD[0][4]) ||
                          (20.0 < ampLGAD[0][3] && 20.0 < ampLGAD[0][4]                         && ampLGAD[0][4] > ampLGAD[0][3]);
        //bool passAmpCut = (20.0 < ampLGAD[0][1] && 20.0 < ampLGAD[0][2] && 20.0 < ampLGAD[0][3] && ampLGAD[0][2] > ampLGAD[0][1] && ampLGAD[0][2] > ampLGAD[0][3]);
        bool passTimeCut = timeLGAD[0][1] != 0 && timeLGAD[0][2] != 0 && timeLGAD[0][3] != 0;

        auto maxAmpIter = std::max_element(ampLGAD[0].begin(), ampLGAD[0].end());
        int d = std::distance(ampLGAD[0].begin(), maxAmpIter);
        bool passMaxFourInnerStrips = 0 < d && d < 5;
                                                  
        if ( ntracks==1 && nplanes>10 && npix>0 && hitSensor && 
             passAmpCut && hitMidStrips && passMaxFourInnerStrips && timePhotek != 0 && passTimeCut)
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

