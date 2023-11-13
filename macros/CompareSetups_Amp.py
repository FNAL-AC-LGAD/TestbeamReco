from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle
from  builtins import any

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 120, help="Max Amp value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)
legend2 = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.05)

#Make final plots
# Varying resistivity and capacitance
# sensors = ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
# tag = ["400 #Omega/sq 240 pF/mm2 (W4)", "1600 #Omega/sq 240 pF/mm2 (W2)", "400 #Omega/sq 600 pF/mm2 (W8)", "1600 #Omega/sq 600 pF/mm2 (W5)"]
# ylength = 160

# HPK Varying thickness
# sensors = ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]
# ylength = 160

# KOJI Varying thickness
# sensors = ["HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]
# ylength = 120
# xlength = 0.25

# BNL and HPK Varying metal widths
sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"]
tag = ["BNL 100 #mum srip width", "BNL 50 #mum strip width", "HPK 50 #mum strip width", "HPK 100 #mum strip width"]
ylength = 100

hname = "Amplitude"
ymin = 1

sensor_prod="BNL & HPK Production"
if ("BNL" in sensors[0]):
   sensor_prod = "BNL & HPK Production"
else:
   sensor_prod = "HPK Production"

totalAmplitude_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalAmplitude_vs_x.Draw("AXIS")
totalAmplitude_vs_x.SetStats(0)
totalAmplitude_vs_x.SetTitle("")
totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalAmplitude_vs_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
totalAmplitude_vs_x.SetLineWidth(3)
totalAmplitude_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[len(sensors)-2],sensors[len(sensors)-2]),"READ")
shift = inputfile.Get("stripBoxInfo03").GetMean(1)
boxes = getStripBox(inputfile,ymin,ylength-10.0,False, 18, True, shift)
for box in boxes[1:len(boxes)-1]:
   box.Draw()

# Draw dotted line for 100 micron strip width
if(any("100M" in iter for iter in sensors)):
   if(any("50M" in iter for iter in sensors)):
      for i in range(1,6):
         vertical_line = TLine((i-3)*0.5-0.05, 0, (i-3)*0.5-0.05, ylength-10) 
         vertical_line.SetLineWidth(2)
         vertical_line.SetLineColor(14)
         vertical_line.SetLineColorAlpha(14,0.4)
         vertical_line.SetLineStyle(9)
         vertical_line.DrawClone("same")

         vertical_line2 = TLine((i-3)*0.5+0.05, 0, (i-3)*0.5+0.05, ylength-10) 
         vertical_line2.SetLineWidth(2)
         vertical_line2.SetLineColor(14)
         vertical_line2.SetLineColorAlpha(14,0.4)
         vertical_line2.SetLineStyle(9)
         vertical_line2.DrawClone("same")

plotfile = []
plotList_amplitude_vs_x = []
for i in range(len(sensors)):
   plotfile.append(TFile("../output/"+sensors[i]+"/Amplitude/AmplitudeVsX_tight.root","READ"))
   plotList_amplitude_vs_x.append(plotfile[i].Get(hname))
   plotList_amplitude_vs_x[i].SetLineWidth(3)
   if("thickness" in tag[0]):
      plotList_amplitude_vs_x[i].SetLineColor(colors[i*2])
   else:
      plotList_amplitude_vs_x[i].SetLineColor(colors[i+1])
   plotList_amplitude_vs_x[i].Draw("hist same")
   legend2.AddEntry(plotList_amplitude_vs_x[i], tag[i])

# legend2.AddEntry(plotList_amplitude_vs_x, "")

legend2.Draw()
myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_prod)
totalAmplitude_vs_x.Draw("AXIS same")

# myStyle.SensorInfoSmart(dataset)

# canvas.SaveAs("../HPK_Amplitude_vs_x_ResCap.png")
# canvas.SaveAs("../HPK_Amplitude_vs_x_thickness.png")
# canvas.SaveAs("../Koji_Amplitude_vs_x_thickness.png")
canvas.SaveAs("../BNL_and_HPK_Amplitude_vs_x_MetalWidth.png")