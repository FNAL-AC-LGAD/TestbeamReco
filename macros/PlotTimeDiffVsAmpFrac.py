from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
#myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Bias Voltage value in [V]")
parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Bias Voltage value in [V]")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

sensor = options.sensor
bias = options.biasvolt
xlength = float(options.xlength)
ylength = float(options.ylength)

dataset = options.Dataset
outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

#colors = myStyle.GetColors(True)

# Define histo names
hName = ["y_vs_timeDiffFrac_0"+str(i) for i in range(6)]

# Get 3D histograms 
th3_y_vs_timeDiffFrac = [inputfile.Get(name) for name in hName]

# Build 2D Amp. Fraction vs timeDiff profile histograms
th2_timeDiff_vs_ampFrac = [h.Project3DProfile("xy") for h in th3_y_vs_timeDiffFrac]
th2_y_vs_ampFrac = [h.Project3DProfile("zy") for h in th3_y_vs_timeDiffFrac]
th2_y_vs_timeDiff = [h.Project3DProfile("zx") for h in th3_y_vs_timeDiffFrac]

# Makeup
[(h.SetTitle("Time Diff. vs Amp. Fraction Profile, strips "+str(i)+str(i+1)),h.GetXaxis().SetTitle("Amp. Fraction"),h.GetYaxis().SetTitle("Time Diff. [ns]")) for i,h in enumerate(th2_timeDiff_vs_ampFrac)]
[(h.SetTitle("Y vs Amp. Fraction Profile, strips "+str(i)+str(i+1)),h.GetXaxis().SetTitle("Amp. Fraction"),h.GetYaxis().SetTitle("Y [mm]")) for i,h in enumerate(th2_y_vs_ampFrac)]
[(h.SetTitle("Y vs Time Diff. Profile, strips "+str(i)+str(i+1)),h.GetXaxis().SetTitle("Time Diff. [ns]"),h.GetYaxis().SetTitle("Y [mm]")) for i,h in enumerate(th2_y_vs_timeDiff)]

# Save profile histograms
outputfile = TFile("../output/PlotAmpFracVsTimeDiff.root","RECREATE")
[h.Write() for h in th2_timeDiff_vs_ampFrac + th2_y_vs_ampFrac + th2_y_vs_timeDiff]
outputfile.Close()
