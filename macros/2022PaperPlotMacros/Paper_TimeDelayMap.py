from ROOT import TFile,TTree,TCanvas,TProfile2D,TCutG,TH1F,TH2F,TProfile,TLatex,TMath,TEfficiency,TGraph,TGraphErrors,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox
import array
import EfficiencyUtils
import numpy as np

myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode=True
gROOT.SetBatch( True )
tsize = myStyle.GetSize()

ROOT.gROOT.ForceStyle()
outdir = myStyle.getOutputDir("Paper2022")
colors = myStyle.GetColors(True)
dataset = "EIC_W1_1cm_500up_200uw_255V"
sensor_list = ["EIC_W1_1cm_500up_200uw_255V"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/delayCorrections.root"%(name),"READ")
    list_input.append(file)


canvas = TCanvas("cv","cv",1000,800)
ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0)

BinCenter = 0.015
BinWidth = 0.5
left = (BinCenter - BinWidth)
right = (BinCenter + BinWidth)

for nSensor,item1 in enumerate(sensor_list):

    timeDelayHisto = list_input[nSensor].Get("timeDiff_coarse_vs_xy_channel03_pyx")
    timeDelayHisto.GetZaxis().SetTitle("Mean arrival time [ns]")
    timeDelayHisto.GetZaxis().SetTitleOffset(1.2)
    #timeDelayHisto.SetMinimum(0.00)
    timeDelayHisto.GetXaxis().SetTitle("Track x position [mm]")
    timeDelayHisto.GetYaxis().SetTitle("Track y position [mm]") 
    bin0 = timeDelayHisto.GetXaxis().FindBin(BinCenter);
    bin1 = timeDelayHisto.GetXaxis().FindBin(left);
    bin2 = timeDelayHisto.GetXaxis().FindBin(right);
        
    cutg = TCutG("cutg",4);
    cutg.SetPoint(0,left,-4.75);
    cutg.SetPoint(1,left,4.75);
    cutg.SetPoint(2,right,4.75);
    cutg.SetPoint(3,right,-4.75);    
    timeDelayHisto.GetYaxis().SetRangeUser(-4.95,4.95)
    timeDelayHisto.GetXaxis().SetRangeUser(left-0.05,right+0.025)
    timeDelayHisto.SetStats(0)
    timeDelayHisto.Draw("colz same [cutg]")
    
myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset,2.25*myStyle.GetMargin())
canvas.SetRightMargin(3.5*myStyle.GetMargin())
#canvas.SetLeftMargin(0.12)
canvas.SaveAs(outdir+"DelayMap_BNL10-200.gif")
canvas.SaveAs(outdir+"DelayMap_BNL10-200.pdf")


for e in list_input:
    e.Close()





