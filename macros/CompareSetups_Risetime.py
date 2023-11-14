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
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 999, help="Max Risetime value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)
legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.05)

#Make final plots
# Varying resistivity and capacitance
sensors = ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
tag = ["400 #Omega/sq 240 pF/mm2 (W4)", "1600 #Omega/sq 240 pF/mm2 (W2)", "400 #Omega/sq 600 pF/mm2 (W8)", "1600 #Omega/sq 600 pF/mm2 (W5)"]

# HPK Varying thickness
# sensors = ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]

# KOJI Varying thickness
# sensors = ["HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]

hname = "Risetime"
ymin = 1

sensor_prod="test"
if ("BNL" in sensors[0]):
   sensor_prod = "BNL Production"
else:
   sensor_prod = "HPK Production"

if ("KOJI" in sensors[0]):
   xlength = 0.25

totalRisetime_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalRisetime_vs_x.Draw("AXIS")
totalRisetime_vs_x.SetStats(0)
totalRisetime_vs_x.SetTitle("")
totalRisetime_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalRisetime_vs_x.GetYaxis().SetTitle("Risetime [ps]")
totalRisetime_vs_x.GetYaxis().SetTitleOffset(1)
totalRisetime_vs_x.SetLineWidth(3)
totalRisetime_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[0],sensors[0]),"READ")
shift = inputfile.Get("stripBoxInfo03").GetMean(1)
boxes = getStripBox(inputfile,ymin,ylength-60.0,False, 18, True, shift)
for box in boxes[1:len(boxes)-1]:
   box.Draw()

plotfile = []
plotList_Risetime_vs_x = []
for i in range(len(sensors)):
   plotfile.append(TFile("../output/"+sensors[i]+"/Risetime/RisetimeVsX_tight.root","READ"))
   plotList_Risetime_vs_x.append(plotfile[i].Get(hname))
   plotList_Risetime_vs_x[i].SetLineWidth(3)
   plotList_Risetime_vs_x[i].SetLineColor(colors[i*2])
   plotList_Risetime_vs_x[i].Draw("hist same")
   legend.AddEntry(plotList_Risetime_vs_x[i], tag[i])

legend.Draw()
myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_prod)
totalRisetime_vs_x.Draw("AXIS same")
# myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("../HPK_Risetime_vs_x_ResCap.png")
# canvas.SaveAs("../HPK_Risetime_vs_x_thickness.png")
# canvas.SaveAs("../Koji_Risetime_vs_x_thickness.png")
