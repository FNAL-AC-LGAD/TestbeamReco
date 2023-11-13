from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle
import math

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Max TR value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)
legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.35,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.25)
legend.SetNColumns(2)
legend2 = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.05)

#Make final plots
# Varying resistivity and capacitance
# sensors = ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
# tag = ["400 #Omega/sq 240 pF/mm2 (W4)", "1600 #Omega/sq 240 pF/mm2 (W2)", "400 #Omega/sq 600 pF/mm2 (W8)", "1600 #Omega/sq 600 pF/mm2 (W5)"]
# ylength = 70

# HPK Varying thickness
# sensors = ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]
# ylength = 150

# KOJI Varying thickness
sensors = ["HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"]
tag = ["50 #mum active thickness", "20 #mum active thickness"]
tag = ["50 #mum active thickness", "20 #mum active thickness"]
xlength = 0.25
ylength = 65

hname = "weighted2_time_diffTracker"
hname2 = "jitter_vs_x"
tag2 = ["Time resolution", "Jitter"]#, "Time resolution - Jitter (quadrature)"]
ymin = 1

sensor_prod="test"
if ("BNL" in sensors[0]):
   sensor_prod = "BNL Production"
else:
   sensor_prod = "HPK Production"

totalTR_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalTR_vs_x.Draw("AXIS")
totalTR_vs_x.SetStats(0)
totalTR_vs_x.SetTitle("")
totalTR_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalTR_vs_x.GetYaxis().SetTitle("Time resolution [ps]")
totalTR_vs_x.SetLineWidth(3)
totalTR_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[0],sensors[0]),"READ")
shift = inputfile.Get("stripBoxInfo03").GetMean(1)
boxes = getStripBox(inputfile,ymin,ylength-10.0,False, 18, True, shift)
for box in boxes[1:len(boxes)-1]:
   box.Draw()

plotfile = []
plotfile2 = []
plotfile3 = []
plotList_TR_vs_x = []
plotList_TR_vs_x2 = []
# plotList_TR_vs_x3 = []

for i in range(len(sensors)):
   plotfile.append(TFile("../output/"+sensors[i]+"/TimeRes/timeDiffVsXandY.root","READ"))
   plotList_TR_vs_x.append(plotfile[i].Get(hname))
   plotList_TR_vs_x[i].SetLineWidth(3)
   if("thickness" in tag[0]):
      plotList_TR_vs_x[i].SetLineColor(colors[i*2])
   else:
      plotList_TR_vs_x[i].SetLineColor(colors[i+1])
   plotList_TR_vs_x[i].Draw("hist same")
   legend2.AddEntry(plotList_TR_vs_x[i], tag[i])

legend2.Draw()

if("thickness" in tag[0]):
   for i in range(len(sensors)):
      plotfile2.append(TFile("../output/"+sensors[i]+"/PlotJitterVsX.root","READ"))
      plotList_TR_vs_x2.append(plotfile2[i].Get(hname2))
      # plotList_TR_vs_x3.append(plotList_TR_vs_x2[i].Clone("landau_vs_x"))
      plotList_TR_vs_x2[i].SetLineWidth(3)
      plotList_TR_vs_x2[i].SetLineStyle(2)
      plotList_TR_vs_x2[i].SetLineColor(colors[i*2])
      plotList_TR_vs_x2[i].Draw("hist same")
      for number in range(1, plotList_TR_vs_x2[i].GetXaxis().GetNbins()+1):
         j = plotList_TR_vs_x2[i].GetBinContent(number)
         t = plotList_TR_vs_x[i].GetBinContent(number)
         if (t>=j):
            l = math.sqrt(t*t - j*j)
         else:
            l = 0
         # plotList_TR_vs_x3[i].SetBinContent(number, l)
   
      # plotList_TR_vs_x3[i].SetLineWidth(5)
      # plotList_TR_vs_x3[i].SetLineStyle(3)
      # plotList_TR_vs_x3[i].SetLineColor(colors[i*2])
      # plotList_TR_vs_x3[i].Draw("hist same")
   legend.AddEntry(plotList_TR_vs_x[0], tag2[0])   
   legend.AddEntry(plotList_TR_vs_x2[0], tag2[1])
   # legend.AddEntry(plotList_TR_vs_x3[0], tag2[2])
   # legend.SetTextSize(26)
   legend.Draw()

myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_prod)
totalTR_vs_x.Draw("AXIS same")
# myStyle.SensorInfoSmart(dataset)

# canvas.SaveAs("../HPK_TimeResolution_vs_x_ResCap.png")
# canvas.SaveAs("../HPK_TimeResolution_vs_x_thickness.png")
canvas.SaveAs("../Koji_TimeResolution_vs_x_thickness.png")