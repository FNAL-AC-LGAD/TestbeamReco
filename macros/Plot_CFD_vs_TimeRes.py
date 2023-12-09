from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TLine,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import numpy as np
from array import array  # Import the array module
import os
import optparse
import myStyle
import math
from array import array
import myFunctions as mf
import mySensorInfo as msi

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)
# colors = [colors[1], colors[4], colors[2]]

## Defining Style
myStyle.ForceStyle()

outdir = myStyle.getOutputDir("Paper2023")
outdir = myStyle.GetPlotsDir(outdir, "CFD/")

Resolution_values_W5 = [66.02, 49.81, 39.71, 36.67, 36.20, 35.98, 35.79, 36.40, 37.84, 41.67]
Resolution_values_W9 = [87.43, 76.65, 58.75, 52.31, 51.84, 52.77, 54.56, 57.69, 67.42, 75.54]
CFD_values = [5, 10, 20, 30, 35, 40, 50, 60, 70, 80]

graph1 = ROOT.TGraph(len(CFD_values), array('d', CFD_values), array('d', Resolution_values_W5))
graph1.SetMarkerStyle(8)
graph1.SetMarkerSize(2)
graph1.SetMarkerColor(colors[0])
graph1.SetLineColor(colors[0])
graph1.SetLineWidth(3)
graph1.GetXaxis().SetRangeUser(0.0, 85.0)
graph1.GetYaxis().SetRangeUser(0.001, 100)

# Create TGraph for the second curve
graph2 = ROOT.TGraph(len(CFD_values), array('d', CFD_values), array('d', Resolution_values_W9))
graph2.SetMarkerStyle(8)
graph2.SetMarkerSize(2)
graph2.SetMarkerColor(colors[2])
graph2.SetLineColor(colors[2])
graph2.SetLineWidth(3)
graph2.GetYaxis().SetRangeUser(0.001, 100)

# Create a canvas
canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

# Draw the first graph
graph1.Draw("APL")  # A for axes, P for points, L for line

# Draw the second graph on the same canvas
graph2.Draw("PL same")

pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
# Create a legend
legend = TLegend(pad_center-0.30, 1-pad_margin-0.20, pad_center+0.30, 1-pad_margin-0.01)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
legend.SetBorderSize(1)
legend.SetLineColor(kBlack)
legend.SetLineStyle(1)
legend.SetLineWidth(2)
legend.AddEntry(graph2, "20 #mum active thickness", "lp")
legend.AddEntry(graph1, "50 #mum active thickness", "lp")
legend.Draw()

# Set axis titles
graph1.GetXaxis().SetTitle("CFD [%]")
graph1.GetYaxis().SetTitle("Time resolution [ps]")
graph1.SetTitle("")

# Update the canvas
canvas.Update()

# Save the canvas as an image
myStyle.BeamInfo()
myStyle.SensorProductionInfo("HPK Production")
canvas.SaveAs("%sCFD_study.png"%outdir)
canvas.SaveAs("%sCFD_study.pdf"%outdir)
canvas.Clear()

# # Keep the program running to display the plot
# ROOT.gApplication.Run()
