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
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 40, help="Max Charge in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)
canvas = TCanvas("cv","cv",1000,800)

#Make final plots
# # Varying resistivity and capacitance
# plotfile = TFile("../output/HPK_W4_17_2_50T_1P0_500P_50M_C240_204V/PlotChargeVsX.root","READ")
# inputfile = TFile("../output/HPK_W4_17_2_50T_1P0_500P_50M_C240_204V/HPK_W4_17_2_50T_1P0_500P_50M_C240_204V_Analyze.root","READ")
# dataset = "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V"

# plotfile2 = TFile("../output/HPK_W2_3_2_50T_1P0_500P_50M_E240_180V/PlotChargeVsX.root","READ")
# inputfile2 = TFile("../output/HPK_W2_3_2_50T_1P0_500P_50M_E240_180V/HPK_W2_3_2_50T_1P0_500P_50M_E240_180V_Analyze.root","READ")
# dataset2 = "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V"

# plotfile3 = TFile("../output/HPK_W8_17_2_50T_1P0_500P_50M_C600_200V/PlotChargeVsX.root","READ")
# inputfile3 = TFile("../output/HPK_W8_17_2_50T_1P0_500P_50M_C600_200V/HPK_W8_17_2_50T_1P0_500P_50M_C600_200V_Analyze.root","READ")
# dataset3 = "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V"

# Varying thickness
plotfile = TFile("../output/HPK_W5_17_2_50T_1P0_500P_50M_E600_190V/PlotChargeVsX.root","READ")
inputfile = TFile("../output/HPK_W5_17_2_50T_1P0_500P_50M_E600_190V/HPK_W5_17_2_50T_1P0_500P_50M_E600_190V_Analyze.root","READ")
dataset = "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"

plotfile2 = TFile("../output/HPK_W9_15_2_20T_1P0_500P_50M_E600_114V/PlotChargeVsX.root","READ")
inputfile2 = TFile("../output/HPK_W9_15_2_20T_1P0_500P_50M_E600_114V/HPK_W9_15_2_20T_1P0_500P_50M_E600_114V_Analyze.root","READ")
dataset2 = "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"

# plotfile = TFile("../output/HPK_KOJI_50T_1P0_80P_60M_E240_190V/PlotChargeVsX.root","READ")
# inputfile = TFile("../output/HPK_KOJI_50T_1P0_80P_60M_E240_190V/HPK_KOJI_50T_1P0_80P_60M_E240_190V_Analyze.root","READ")
# dataset = "HPK_KOJI_50T_1P0_80P_60M_E240_190V"
# plotfile2 = TFile("../output/HPK_KOJI_20T_1P0_80P_60M_E240_112V/PlotChargeVsX.root","READ")
# inputfile2 = TFile("../output/HPK_KOJI_20T_1P0_80P_60M_E240_112V/HPK_KOJI_20T_1P0_80P_60M_E240_112V_Analyze.root","READ")
# dataset2 = "HPK_KOJI_20T_1P0_80P_60M_E240_112V"

hname = "charge_vs_x"

sensor_prod="test"
if ("BNL" in sensors[0]):
   sensor_prod = "BNL Production"
else:
   sensor_prod = "HPK Production"

shift2 = inputfile2.Get("stripBoxInfo03").GetMean(1)
shift = inputfile.Get("stripBoxInfo03").GetMean(1)

plotList_amplitude_vs_x = plotfile.Get(hname)
plotList_amplitude_vs_x.SetLineWidth(3)
# plotList_amplitude_vs_x.SetFillColorAlpha(colors[i],0.3)
plotList_amplitude_vs_x.SetLineColor(colors[0])
plotList_amplitude_vs_x2 = plotfile2.Get(hname)
plotList_amplitude_vs_x2.SetLineWidth(3)
plotList_amplitude_vs_x2.SetLineColor(colors[1])

totalAmplitude_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalAmplitude_vs_x.Draw("hist")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalAmplitude_vs_x.GetYaxis().SetTitle("Charge [fC]")
totalAmplitude_vs_x.SetLineWidth(3)

totalAmplitude_vs_x.SetMaximum(1500)

boxes = getStripBox(inputfile,0,ylength-100.0,False, 18, True, shift)
for box in boxes:
   box.Draw()
totalAmplitude_vs_x.Draw("AXIS same")
totalAmplitude_vs_x.Draw("hist same")


legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.32,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.12)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)

plotList_amplitude_vs_x.Draw("hist same")
plotList_amplitude_vs_x2.Draw("hist same")
# legend.AddEntry(plotList_amplitude_vs_x2[i], "Strip %i"%(ch+1))
# legend.Draw()

legend2 = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.12,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
# legend2.AddEntry(plotList_amplitude_vs_x2[0], "W4 (17,2): C240")
# legend2.AddEntry(plotList_amplitude_vs_x2[0], "W2 (3,2): E240")
# legend2.AddEntry(plotList_amplitude_vs_x[0], "W8 (17,2): C600")
legend2.AddEntry(plotList_amplitude_vs_x, "50T")
legend2.AddEntry(plotList_amplitude_vs_x2, "20T")
legend2.Draw()
myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_prod)
# myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("../HPKCharge_vs_x_thickness.png")