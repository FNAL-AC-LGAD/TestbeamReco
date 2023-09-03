from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TProfile,TLatex,TMath,TEfficiency,TGraph,TGraphErrors,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
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

sensor_list = ["EIC_W1_1cm_500up_200uw_255V"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)

pitch = 0.500 #mm
canvas = TCanvas("cv","cv",1000,800)
hdummy = ROOT.TH1D("","",1,0.0,10.0)
hdummy.GetXaxis().SetTitle("Time [ns]")
hdummy.GetYaxis().SetTitle("Amplitude [mV]")
hdummy.SetMaximum(14.9)
hdummy.SetMinimum(-84.9)
hdummy.Draw("AXIS")

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 

legend = TLegend(myStyle.GetPadCenter()-0.40,1-myStyle.GetMargin()-0.12,myStyle.GetPadCenter()+0.40,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(3)
legend.SetFillStyle(0)

NSensors, NStrips = (1, 3)
#for nSensor,item1 in enumerate(sensor_list):
hist_tempArray = []
stripindex = ["1hot","1cold","1gap"];
TH1DVar =  []
colorIndex  = [2,4,1]
#hist_temp = ROOT.TH1D("","",500,-5.0,20.0)
for nstrip,item2 in enumerate(stripindex):
    hist_temp = ROOT.TH1D("","",500,-5.0,20.0)
    TH1DVar.append(list_input[0].Get("waveProf%s"%(stripindex[nstrip])))
    NumXBins = TH1DVar[nstrip].GetXaxis().GetNbins()
    for i in range(0, NumXBins+1):
        if (TH1DVar[nstrip].GetBinContent(i+1) !=0): 
            hist_temp.SetBinContent(i+1,(TH1DVar[nstrip].GetBinContent(i+1)))     
    hist_tempArray.append(hist_temp)
    hist_tempArray[nstrip].SetLineColor(colorIndex[nstrip])
    hist_tempArray[nstrip].Draw("hist l same")
    hist_tempArray[nstrip].SetLineWidth(3) 
    print(nstrip)
        #TH1DVar[nstrip].SetLineColor(colorIndex[nstrip])
        #TH1DVar[nstrip].Draw("hist l same")
        #TH1DVar[nstrip].SetLineWidth(3)   
        #TH1DVar[nstrip].SetTitle("")
hist_tempArray[2].SetLineStyle(2)
legend.AddEntry(hist_tempArray[0], "High-gain region")
legend.AddEntry(hist_tempArray[1], "Low-gain region")
legend.AddEntry(hist_tempArray[2], "Gap region")
legend.Draw()
myStyle.BeamInfo()
TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{BNL 10-200, 255V}")

canvas.SaveAs(outdir+"WaveForm_DiffROI_v2.gif")
canvas.SaveAs(outdir+"WaveForm_DiffROI_v2.pdf")


for e in list_input:
    e.Close()
