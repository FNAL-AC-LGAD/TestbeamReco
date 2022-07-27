from ROOT import TFile,TTree,TCanvas,TH1D,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
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
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']

list_cut_name_oneStrip  = ["Full", "Pass", "Signal over Noise", "OneStripReco", "OneStripReco HighThreshold",
                           "High fraction", "No good neighbour", "Both high fraction and No neighbour"]
list_cut_name_twoStrips = ["Full", "Pass", "Signal over highThreshold", "Good neighbour", "Good Amp fraction", "TwoStripsReco"]

event_oneStripReco  = inputfile.Get("event_oneStripReco")
event_twoStripsReco = inputfile.Get("event_twoStripsReco")


# Create 1D histograms
hist_oneStrip  = TH1D("cutFlow_oneStrip", "Cut flow oneStripReco;;Events %",len(list_cut_name_oneStrip),0,len(list_cut_name_oneStrip))
hist_oneStrip.GetYaxis().SetRangeUser(0.0, 1.1)

hist_twoStrips = TH1D("cutFlow_twoStrips","Cut flow twoStripsReco;;Events %",len(list_cut_name_twoStrips),0,len(list_cut_name_twoStrips))
hist_twoStrips.GetYaxis().SetRangeUser(0.0, 1.1)

for i,cut_name in enumerate(list_cut_name_oneStrip):
    hist_oneStrip.Fill(cut_name, event_oneStripReco.GetEfficiency(i+1))
    hist_oneStrip.SetBinError(i+1, event_oneStripReco.GetEfficiencyErrorUp(i+1))

for i,cut_name in enumerate(list_cut_name_twoStrips):
    hist_twoStrips.Fill(cut_name, event_twoStripsReco.GetEfficiency(i+1))
    hist_twoStrips.SetBinError(i+1, event_twoStripsReco.GetEfficiencyErrorUp(i+1))



canvas = TCanvas("cv","cv",1000,1000)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
gStyle.SetOptStat(0)
gStyle.SetPadBottomMargin(10*myStyle.GetMargin())

hist_oneStrip.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"PlotCutFlow_one.gif")
canvas.SaveAs(outdir+"PlotCutFlow_one.pdf")

canvas.Clear()

hist_twoStrips.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"PlotCutFlow_two.gif")
canvas.SaveAs(outdir+"PlotCutFlow_two.pdf")

# Save amplitude histograms
outputfile = TFile("%sPlotCutFlow.root"%(outdir),"RECREATE")

hist_oneStrip.Write()
hist_twoStrips.Write()

outputfile.Close()
