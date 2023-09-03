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



sensor_list = ["EIC_W2_1cm_500up_300uw_240V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W2_1cm_500up_100uw_220V"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)

pitch = 0.500 #mm
canvas = TCanvas("cv","cv",1000,800)
hdummy = ROOT.TH1D("","",1,0.0,10.0)
hdummy.GetXaxis().SetTitle("Time [ns]")
hdummy.GetYaxis().SetTitle("Amplitude [A.U.]")
hdummy.SetMaximum(0.014*100)
hdummy.SetMinimum(-0.059*100)
hdummy.Draw("AXIS")

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 

stripindexFirst = ["4"]
stripindexSecond = ["3"]
stripindexThird = ["3"]

legend = TLegend(myStyle.GetPadCenter()-0.35,1-myStyle.GetMargin()-0.12,myStyle.GetPadCenter()+0.35,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(3)
legend.SetFillStyle(0)

NSensors, NStrips = (3, 1)

hist_tempArray = []
for nSensor,item1 in enumerate(sensor_list):

    stripindex = []
    TH1DVar =  []
    hist_temp = ROOT.TH1D("","",500,-5.0,20.0)
    
    for nstrip,item2 in enumerate(stripindexFirst):
        
        if (nSensor == 0): stripindex.append(stripindexFirst[nstrip])
        if (nSensor == 1): stripindex.append(stripindexSecond[nstrip])
        if (nSensor == 2): stripindex.append(stripindexThird[nstrip])

        TH1DVar.append(list_input[nSensor].Get("waveProf%s"%(stripindex[nstrip])))
        TH1DVar[nstrip].Scale(-1.0/TH1DVar[nstrip].Integral(TH1DVar[nstrip].FindFixBin(5.0),TH1DVar[nstrip].FindFixBin(15.0)))
        
        NumXBins = TH1DVar[nstrip].GetXaxis().GetNbins()
        print(NumXBins)

        for i in range(0, NumXBins+1):            
            if (TH1DVar[nstrip].GetBinContent(i+1) !=0): hist_temp.SetBinContent(i+1,(TH1DVar[nstrip].GetBinContent(i+1))*100.0)
        print("check")
        hist_tempArray.append(hist_temp)
        hist_tempArray[nSensor].SetLineColor(colors[2*nSensor])
        hist_tempArray[nSensor].Draw("hist l same")        
        hist_tempArray[nSensor].SetLineWidth(3)
        legend.AddEntry(hist_tempArray[nSensor], myStyle.GetGeometry(item1)["sensor"],"L")
        print("check2")

legend.Draw()
myStyle.BeamInfo()

TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying width}")

canvas.SaveAs(outdir+"Norm_WaveForm_DiffWidth.gif")
canvas.SaveAs(outdir+"Norm_WaveForm_DiffWidth.pdf")


for e in list_input:
    e.Close()
