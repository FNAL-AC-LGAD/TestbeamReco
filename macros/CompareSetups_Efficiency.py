from ROOT import TFile,TTree,TLine,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
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
parser.add_option('-x','--xlength', dest='xlength', default = 1.75, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 1.4, help="Max Efficiency in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)
legend2 = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.05)

#Make final plots
# BNL and HPK sensors - different metal widths
sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"]
tag = ["BNL 100 #mum srip width", "BNL 50 #mum strip width", "HPK 50 #mum strip width", "HPK 100 #mum strip width"]

# Varying resistivity and capacitance
# sensors = ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
# tag = ["400 #Omega/sq 240 pF/mm2 (W4)", "1600 #Omega/sq 240 pF/mm2 (W2)", "400 #Omega/sq 600 pF/mm2 (W8)", "1600 #Omega/sq 600 pF/mm2 (W5)"]

# HPK Varying thickness
# sensors = ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"]
# tag = ["50 #mum active thickness", "20 #mum active thickness"]

hname = "hefficiency_vs_x_twoStrips_numerator_tight"
ymin = 0.01

sensor_prod="BNL & HPK Production"
if ("BNL" in sensors[0]):
   sensor_prod = "BNL & HPK Production"
else:
   sensor_prod = "HPK Production"

if ("KOJI" in sensors[0]):
   xlength = 0.35

totalEfficiency_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalEfficiency_vs_x.Draw("AXIS")
totalEfficiency_vs_x.SetStats(0)
totalEfficiency_vs_x.SetTitle("")
totalEfficiency_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalEfficiency_vs_x.GetYaxis().SetTitle("Two-strip efficiency")
totalEfficiency_vs_x.SetLineWidth(3)
totalEfficiency_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[len(sensors)-2],sensors[len(sensors)-2]),"READ")
shift = inputfile.Get("stripBoxInfo03").GetMean(1)
boxes = getStripBox(inputfile,ymin,ylength - 0.4,False, 18, True, shift)

for box in boxes:
   box.Draw()

# Draw dotted line for 100 micron strip width
if(any("100M" in iter for iter in sensors)):
   if(any("50M" in iter for iter in sensors)):
      for i in range(7):
         vertical_line = TLine((i-3)*0.5-0.05, 0, (i-3)*0.5-0.05, 1) 
         vertical_line.SetLineWidth(2)
         vertical_line.SetLineColor(14)
         vertical_line.SetLineColorAlpha(14,0.4)
         vertical_line.SetLineStyle(9)
         vertical_line.DrawClone("same")

         vertical_line2 = TLine((i-3)*0.5+0.05, 0, (i-3)*0.5+0.05, 1) 
         vertical_line2.SetLineWidth(2)
         vertical_line2.SetLineColor(14)
         vertical_line2.SetLineColorAlpha(14,0.4)
         vertical_line2.SetLineStyle(9)
         vertical_line2.DrawClone("same")

plotfile = []
plotList_Efficiency_vs_x = []
for i in range(len(sensors)):
   plotfile.append(TFile("../output/"+sensors[i]+"/Efficiency/EfficiencyVsX_tight.root","READ"))
   plotList_Efficiency_vs_x.append(plotfile[i].Get(hname))
   plotList_Efficiency_vs_x[i].SetLineWidth(3)
   if("thickness" in tag[0]):
      plotList_Efficiency_vs_x[i].SetLineColor(colors[i*2])
   else:
      plotList_Efficiency_vs_x[i].SetLineColor(colors[i+1])
   plotList_Efficiency_vs_x[i].Draw("hist same")
   legend2.AddEntry(plotList_Efficiency_vs_x[i], tag[i])

horizontal_line = TLine(-xlength, 1, xlength, 1)
horizontal_line.SetLineWidth(3)
horizontal_line.SetLineColor(1)
horizontal_line.SetLineStyle(9)
# horizontal_line.SetLineColorAlpha(colors[2*i],0.4)
horizontal_line.DrawClone("same")

legend2.Draw()
myStyle.BeamInfo()
myStyle.SensorProductionInfo(sensor_prod)
totalEfficiency_vs_x.Draw("AXIS same")

canvas.SaveAs("../BNL_and_HPK_Efficiency_vs_x_MetalWidth.png")
# canvas.SaveAs("../HPK_Efficiency_vs_x_ResCap.png")
# canvas.SaveAs("../HPK_Efficiency_vs_x_thickness.png")

# BNL sensors - different metal widths
# sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V"]
# tag = ["100 #mum strip width", "50 #mum strip width]

# HPK sensors - different metal widths
# sensors = ["HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V"]
# tag = ["W8 (17,2): 50M C600 50T", "W8 (18,2): 100M C600 50T", "W9 (15,2): 50M E600 20T", "W9 (14,2): 100M E600 20T"]