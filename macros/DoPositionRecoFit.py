from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1
import os
import EfficiencyUtils
import langaus
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-r", "--run", required=False,
   help="run fits or not")
args = vars(ap.parse_args())

RunFits = False
if args['run'] == 'true':
   RunFits = True
     

if (RunFits):

    #inputfile = TFile("/uscms/home/sxie/work/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V_output.root")
    inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.20210430.root")

    #Get dX vs a1/(a1+a2) hist
    Amp1OverAmp1and2_vs_deltaXmax = inputfile.Get("Amp1OverAmp1and2_vs_deltaXmax")
      
    #Define profile hist
    Amp1OverAmp1and2_vs_deltaXmax_profile = Amp1OverAmp1and2_vs_deltaXmax.ProjectionY().Clone("Amp1OverAmp1and2_vs_deltaXmax_profile")

    canvas = TCanvas("cv","cv",800,800)

    #loop over  Amp1OverAmp1and2 bins   
    for i in range(1, Amp1OverAmp1and2_vs_deltaXmax.GetYaxis().GetNbins()):

       print ("Bin " + str(i))

       ##For Debugging
       #if not (i==46 and j==5):
       #    continue

       tmpHist = Amp1OverAmp1and2_vs_deltaXmax.ProjectionX("px",i,i)
       myMean = tmpHist.GetMean()
       myRMS = tmpHist.GetRMS()
       
       myGausFunction = TF1("mygaus","gaus(0)",0,0.1);
       tmpHist.Fit(myGausFunction,"","",0,0.1);
       mean = myGausFunction.GetParameter(1)
       meanErr = myGausFunction.GetParError(1)
       sigma = myGausFunction.GetParameter(2)

       ##For Debugging
       tmpHist.Draw("hist")
       myGausFunction.Draw("same")
       canvas.SaveAs("q_"+str(i)+".gif")

       print ("Bin : " + str(i) + " -> " + str(mean))
       Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinContent(i,mean)
       Amp1OverAmp1and2_vs_deltaXmax_profile.SetBinError(i,meanErr)
            
    # Save amplitude histograms
    outputfile = TFile("positionRecoFitPlots.root","RECREATE")   
    Amp1OverAmp1and2_vs_deltaXmax_profile.Write()
    outputfile.Close()



#Make final plots
