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

pitch = 0.500 #mm
canvas = TCanvas("cv","cv",1000,800)
hdummy = ROOT.TH1D("","",1,-2.5,27.5)
hdummy.GetXaxis().SetTitle("Track y position [mm]")
hdummy.GetYaxis().SetTitle("Mean arrival time [ns]")
hdummy.SetMaximum(0.59)
hdummy.SetMinimum(-0.04)
hdummy.Draw("AXIS")

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 

legend = TLegend(myStyle.GetPadCenter()-0.35,1-myStyle.GetMargin()-0.12,myStyle.GetPadCenter()+0.35,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(3)
legend.SetFillStyle(0)

file = TFile("../output/timeDelay1D.root","READ")

TH1DVar0p5 = file.Get("0p5py")
TH1DVar0p5.SetLineColor(colors[2*2])
TH1DVar0p5.SetMarkerColor(colors[2*2])
TH1DVar0p5.SetLineWidth(3)
TH1DVar0p5.Draw("hist ep same")
TH1DVar1p0 = file.Get("1p0py")
TH1DVar1p0.SetLineColor(colors[2*1])
TH1DVar1p0.SetMarkerColor(colors[2*1])
TH1DVar1p0.SetLineWidth(3)
TH1DVar1p0.Draw("hist ep same")
TH1DVar2p5 = file.Get("2p5py")
TH1DVar2p5.SetLineColor(colors[2*0])
TH1DVar2p5.SetMarkerColor(colors[2*0])
TH1DVar2p5.SetLineWidth(3)
TH1DVar2p5.Draw("hist ep same")

legend.AddEntry(TH1DVar2p5, "BNL 25-200","lep")
legend.AddEntry(TH1DVar1p0, "BNL 10-200","lep")
legend.AddEntry(TH1DVar0p5, "BNL 5-200","lep")
legend.Draw()
myStyle.BeamInfo()
TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying length}")

canvas.SaveAs(outdir+"TimeDelay1D_DiffLength.gif")
canvas.SaveAs(outdir+"TimeDelay1D_DiffLength.pdf")


