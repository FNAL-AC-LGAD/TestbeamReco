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
gStyle.SetPadBottomMargin(4*myStyle.GetMargin())
# gStyle.SetPadRightMargin(2*myStyle.GetMargin())
gStyle.SetLabelSize(myStyle.GetSize()-12,"x")
gROOT.ForceStyle()
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

list_cut_name_oneStrip  = ["Pass", "Signal over Noise", "OneStripReco", "High fraction", # "OneStripReco HighThreshold"
                           "High fraction & Good neighbour", "No good neighbour", "High fraction & No neighbour", "OneStripReco & OnMetal"]
list_cut_name_twoStrips = ["Pass", "Signal over highThreshold", "Good neighbour", "Good Amp fraction", "TwoStripsReco", "TwoStripsReco & OnMetal"]

event_oneStripReco  = inputfile.Get("event_oneStripReco")
event_twoStripsReco = inputfile.Get("event_twoStripsReco")


# Create 1D histograms
hist_oneStrip  = TH1D("cutFlow_oneStrip", "Cut flow oneStripReco;;Events %",len(list_cut_name_oneStrip),0,len(list_cut_name_oneStrip))
hist_oneStrip.GetYaxis().SetRangeUser(0.0, 1.1)
text_oneStrip = []

hist_twoStrips = TH1D("cutFlow_twoStrips","Cut flow twoStripsReco;;Events %",len(list_cut_name_twoStrips),0,len(list_cut_name_twoStrips))
hist_twoStrips.GetYaxis().SetRangeUser(0.0, 1.1)
text_twoStrips = []

for i,cut_name in enumerate(list_cut_name_oneStrip):
    efficiency_value = event_oneStripReco.GetEfficiency(i+1)/event_oneStripReco.GetEfficiency(1)
    hist_oneStrip.Fill(cut_name, efficiency_value)
    hist_oneStrip.SetBinError(i+1, 0)
    if i>0:
        text = TLatex(i+0.5,efficiency_value+0.01,"%3.1f%%"%(efficiency_value*100))
        text.SetTextAlign(21)
        text.SetTextSize(myStyle.GetSize()-4)
        text_oneStrip.append(text)


for i,cut_name in enumerate(list_cut_name_twoStrips):
    efficiency_value = event_twoStripsReco.GetEfficiency(i+1)/event_twoStripsReco.GetEfficiency(1)
    hist_twoStrips.Fill(cut_name, efficiency_value)
    hist_twoStrips.SetBinError(i+1, 0)
    if i>0:
        text = TLatex(i+0.5,efficiency_value+0.01,"%3.1f%%"%(efficiency_value*100))
        text.SetTextAlign(21)
        text.SetTextSize(myStyle.GetSize()-4)
        text_twoStrips.append(text)

left_text = TLatex()
left_text.SetTextSize(myStyle.GetSize()-4)

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
gStyle.SetOptStat(0)

hist_oneStrip.LabelsOption("u")
hist_oneStrip.Draw()
for p in text_oneStrip:
    p.Draw()
left_text.DrawLatexNDC(2*myStyle.GetMargin()+0.005,1-myStyle.GetMargin()+0.01,"#bf{One Strip Reco}")

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"PlotCutFlow_one.gif")
canvas.SaveAs(outdir+"PlotCutFlow_one.pdf")

canvas.Clear()

hist_twoStrips.LabelsOption("u")
hist_twoStrips.Draw()
for p in text_twoStrips:
    p.Draw()
left_text.DrawLatexNDC(2*myStyle.GetMargin()+0.005,1-myStyle.GetMargin()+0.01,"#bf{Two Strips Reco}")

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"PlotCutFlow_two.gif")
canvas.SaveAs(outdir+"PlotCutFlow_two.pdf")

# Save amplitude histograms
outputfile = TFile("%sPlotCutFlow.root"%(outdir),"RECREATE")

hist_oneStrip.Write()
hist_twoStrips.Write()

outputfile.Close()
