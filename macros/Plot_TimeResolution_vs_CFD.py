from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TLine,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1,TGraph
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
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

def fit_histogram_in_range(histogram, limits, saveName):

    gaussian = TF1("gaussian", "gaus")
    gaussian.SetRange(limits[0], limits[1])

    histogram.Fit(gaussian, "R")
    canvas = TCanvas("canvas", "Histogram Fit", 1200, 600)
    histogram.Draw("hist")
    gaussian.Draw("same")
    print("FTBF fit:", gaussian.GetParameter(2) * 1000.0)
    timeResolution = round(((gaussian.GetParameter(2) * 1000.0)**2 - 100)**0.5,2)
    print("FTBF TR with photek correction:", timeResolution)

    legend = TLegend(0.2, 0.7, 0.4, 0.9)
    legend.AddEntry(gaussian, "Gaussian Fit", "l")
    legend.Draw()

    canvas.Update()
    canvas.SaveAs(saveName)
    canvas.Close()
    return timeResolution

temp = dataset.split('_')
saveName_temp = temp[0]+"_"+temp[1]+"_"+temp[2]+"_"+temp[3]

histogram_name = "weighted2_timeDiff_tracker"
# # For sensor W5_17_2
# cfd_and_limits = {'05': [-1, 1.5], '10': [-1.5, 1.5], '20': [-1.5, 1.5], '25': [-1.5, 1.5], '30': [-1.5, 1.5], '35': [-1.5, 1.5], '40': [-1.5, 1.5], '50': [-1.5, 1.5], '60': [-1.5, 1.5], '70': [-1.5, 1.5], '80': [-1.5, 1.5]}

# For sensor W9_15_2
cfd_and_limits = {'05': [-0.5, 1.5], '10': [-1, 1.5], '20': [-1.5, 1.5], '25': [-1.5, 1.5], '30': [-1.5, 1.5], '35': [-1.5, 1.2], '40': [-1.5, 1.2], '50': [-1.5, 1], '60': [-1.5, 0.7], '70': [-1, 0.5], '80': [-1, 0.5]}

# # For sensor W5_1_1
# cfd_and_limits = {'05': [-1.5, 1.5], '10': [-1.5, 1.5], '20': [-1.5, 1.5], '25': [-1.5, 1.5], '30': [-1.5, 1.5], '35': [-1.5, 1.5], '40': [-1.5, 1.5], '50': [-1.5, 1.5], '60': [-1.5, 1.5], '70': [-1.5, 1.5], '80': [-1.5, 1.5]}

# # For sensor W9_22_3
# cfd_and_limits = {'05': [-1.5, 1.5], '10': [-1.5, 1.5], '20': [-1.5, 1.5], '25': [-1.5, 1.5], '30': [-1.5, 1.5], '35': [-1.5, 1], '40': [-1.5, 1], '50': [-1.5, 0.5], '60': [-1, 0.5], '70': [-1, 0.5], '80': [-1, 0.5]}

# # For sensor W11_22_3
# cfd_and_limits = {'05': [-1, 1.5], '10': [-1, 1.5], '20': [-1.5, 1.5], '25': [-1.5, 1.5], '30': [-1.5, 1.5], '35': [-1.5, 1.5], '40': [-1.5, 1.5], '50': [-1.5, 1.5], '60': [-1.5, 1.5], '70': [-1.5, 1.5], '80': [-1.5, 1.5]}

# Begin calculating time resolution for every CFD
outdir2 = myStyle.GetPlotsDir(outdir, "CFDStudy/")
timeRes_arr = []
cfd_arr = []
for cfd, fit_limits_temp in cfd_and_limits.items():
    file_name = "../output/"+dataset+"/"+dataset+"_Analyze_"+cfd+"CFD.root"
    file = TFile.Open(file_name)
    if not file or file.IsZombie():
        print(f"Error opening file: {file_name}")
    histogram = file.Get(histogram_name)
    if not histogram:
        print(f"Error accessing histogram: {histogram_name} in file: {file_name}")
        file.Close()
    fit_limits = histogram.GetMean() + np.array(fit_limits_temp)*histogram.GetRMS()
    saveName = outdir2+saveName_temp+"_"+cfd+"CFD.png"
    timeRes_arr.append(fit_histogram_in_range(histogram, fit_limits, saveName))
    cfd_arr.append(cfd)

print(cfd_arr)
print(timeRes_arr)