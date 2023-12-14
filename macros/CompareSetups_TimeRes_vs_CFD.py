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

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-o', dest='Type', default = "p", help="Sensor type, use s for strips and p for pixels")
options, args = parser.parse_args()

sensor_type = options.Type

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)


## Defining Style
myStyle.ForceStyle()

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "CFD/")

if(sensor_type=='s'):
    # Strips W5_17_2 and W9_15_2
    Resolution_values_W5 = [65.88, 49.4, 38.37, 36.49, 35.55, 35.02, 34.74, 34.54, 35.06, 36.52, 40.22]
    Resolution_values_W9 = [90.59, 74.88, 55.06, 51.2, 49.11, 47.89, 47.99, 50.58, 54.0, 55.93, 66.41]
    suffix = "_strips"
    sensor_type_label = "Strip sensors"
    sensors = ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
if(sensor_type=='p'):
    # Pads W5_1_1 and W9_22_3
    Resolution_values_W5 = [48.81, 37.74, 32.21, 32.05, 32.28, 32.69, 33.27, 33.79, 33.83, 34.66, 37.43]
    Resolution_values_W9 = [62.29, 41.19, 31.76, 31.44, 32.07, 31.46, 32.6, 34.73, 36.11, 40.17, 48.33]
    suffix = "_pads"
    sensor_type_label = "Pixel sensors"
    sensors = ["HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"]

resolutions = [Resolution_values_W9, Resolution_values_W5]
CFD_values = [5, 10, 20, 25, 30, 35, 40, 50, 60, 70, 80]
colors = myStyle.GetColorsCompare(len(sensors))

# Create a canvas
canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
# Create a legend
legend_height = 0.058*(len(sensors) + 1) # Entries + title
legend = TLegend(pad_center-0.29, 1-pad_margin-legend_height-0.03, pad_center+0.29, 1-pad_margin-0.03)
legend.SetNColumns(1)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
legend.SetBorderSize(1)
legend.SetLineColor(kBlack)
# legend.SetLineStyle(1)
# legend.SetLineWidth(2)
legend_entries = mf.get_legend_comparation_plots(sensors, ["thickness"])

graphs = []
for i, sensor in enumerate(sensors):
    graph = ROOT.TGraph(len(CFD_values), array('d', CFD_values), array('d', resolutions[i]))
    graph.SetMarkerStyle(8)
    graph.SetMarkerSize(2)
    graph.SetMarkerColor(colors[i])
    graph.SetLineColor(colors[i])
    graph.SetLineWidth(3)
    graph.GetXaxis().SetRangeUser(0.0, 85.0)
    graph.GetYaxis().SetRangeUser(0.001, 90)
    # Set axis titles
    graph.GetXaxis().SetTitle("CFD [%]")
    graph.GetYaxis().SetTitle("Time resolution [ps]")
    graph.SetTitle("")

    opts = "APL" if i==0 else "PL same"
    graph.Draw(opts)

    legend.AddEntry(graph, legend_entries[i], "lp")
    graphs.append(graph)

legend.Draw()

# Update the canvas
canvas.Update()

# Save the canvas as an image
myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_type_label)
canvas.SaveAs("%sCFD_study%s.png"%(outdir,suffix))
canvas.SaveAs("%sCFD_study%s.pdf"%(outdir,suffix))
canvas.Clear()
