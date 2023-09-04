from ROOT import TFile,TTree,TLine,TCanvas,TH1F,TH2F,TProfile,TLatex,TMath,TEfficiency,TGraph,TGraphErrors,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
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

pitch = 0.500 #mm
canvas = TCanvas("cv","cv",1000,800)
hdummy = ROOT.TH1D("","",1,-5.49,5.49)
hdummy.GetXaxis().SetTitle("Track y position [mm]")
hdummy.GetYaxis().SetTitle("Mean arrival time [ps]")
hdummy.SetMaximum(154.9)
hdummy.SetMinimum(-14.99)
hdummy.Draw("AXIS")

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 

legend = TLegend(myStyle.GetPadCenter()-0.40,1-myStyle.GetMargin()-0.10,myStyle.GetPadCenter()+0.40,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(2)
legend.SetFillStyle(0)

file = TFile("../output/timeDelay1D.root","READ")

TH1DVar3rd = file.Get("2py")
TH1DVar3rd.SetLineColor(colors[2*2])
TH1DVar3rd.SetMarkerColor(colors[2*2])
TH1DVar3rd.SetLineWidth(3)
TH1DVar3rd.Draw("hist ep same")

TH1DVar4th = file.Get("3py")
TH1DVar4th.SetLineColor(colors[2*1])
TH1DVar4th.SetMarkerColor(colors[2*1])
TH1DVar4th.SetLineWidth(3)
TH1DVar4th.Draw("hist ep same")

legend.AddEntry(TH1DVar3rd, "Strip at x = 0.5 mm","lep")
legend.AddEntry(TH1DVar4th, "Strip at x = 0.0 mm","lep")
legend.Draw()

myStyle.BeamInfo()
TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{BNL 10-200, 255V}")

canvas.SaveAs(outdir+"TimeDelay1D_DiffStrip_1cm.gif")
canvas.SaveAs(outdir+"TimeDelay1D_DiffStrip_1cm.pdf")


