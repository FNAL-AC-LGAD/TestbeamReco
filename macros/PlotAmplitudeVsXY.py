from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors
import os
import EfficiencyUtils



inputfile = TFile("/uscms/home/sxie/work/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.root")

amplitude_vs_xy_channel00 = inputfile.Get("amplitude_vs_xy_channel00")
