from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )

## Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL2020, BNL2021, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file)


efficiency_lowThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator")
efficiency_highThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_highThreshold_numerator")
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")

efficiency_lowThreshold_numerator_global.RebinX(3)
efficiency_highThreshold_numerator_global.RebinX(3)
efficiency_denominator_global.RebinX(3)

shift = (inputfile.Get("stripBoxInfo02").GetMean(1) + inputfile.Get("stripBoxInfo03").GetMean(1))/2.

EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, "efficiency_highThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.


efficiency_highThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel00")
efficiency_highThreshold_numerator_channel00.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel01")
efficiency_highThreshold_numerator_channel01.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Strip 1", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel02 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel02")
efficiency_highThreshold_numerator_channel02.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel02, efficiency_denominator_global, "efficiency_channel02", "Efficiency Strip 2", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel03 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel03")
efficiency_highThreshold_numerator_channel03.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel03, efficiency_denominator_global, "efficiency_channel03", "Efficiency Strip 3", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel04 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel04")
efficiency_highThreshold_numerator_channel04.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel04, efficiency_denominator_global, "efficiency_channel04", "Efficiency Strip 4", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel05 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel05")
efficiency_highThreshold_numerator_channel05.RebinX(3)
# EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel05, efficiency_denominator_global, "efficiency_channel05", "Efficiency Strip 5", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )



#1D efficiency vs X
binY_lowEdge = efficiency_denominator_global.GetYaxis().FindFixBin(10.0)
binY_highEdge = efficiency_denominator_global.GetYaxis().FindFixBin(11.4)

efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_global = efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel00 = efficiency_highThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel00",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel01 = efficiency_highThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel01",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel02 = efficiency_highThreshold_numerator_channel02.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel02",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel03 = efficiency_highThreshold_numerator_channel03.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel03",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel04 = efficiency_highThreshold_numerator_channel04.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel04",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel05 = efficiency_highThreshold_numerator_channel05.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel05",binY_lowEdge,binY_highEdge)


efficiency_vs_x_highThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency Global", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel00", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel01", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel02 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel02, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel02", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel03 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel03, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel03", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel04 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel04, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel04", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)
efficiency_vs_x_highThreshold_channel05 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel05, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel05", "Efficiency Strip 0", "X [mm]", -0.6, 0.6, False, shift)



canvas = TCanvas("cv","cv",1000,800)
# canvas.SetLeftMargin(0.12)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1,-0.65,0.65)
# efficiency_vs_x_highThreshold_global.Draw("ALP")
htemp.Draw()


#ymin = efficiency_vs_x_highThreshold_global.GetMinimum()
#ymax = efficiency_vs_x_highThreshold_global.GetMaximum()
boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for box in boxes:
    box.Draw()

efficiency_vs_x_highThreshold_channel00.Draw("LPsame")
efficiency_vs_x_highThreshold_channel01.Draw("LPsame")
efficiency_vs_x_highThreshold_channel02.Draw("LPsame")
efficiency_vs_x_highThreshold_channel03.Draw("LPsame")
efficiency_vs_x_highThreshold_channel04.Draw("LPsame")
efficiency_vs_x_highThreshold_channel05.Draw("LPsame")
efficiency_vs_x_highThreshold_global.Draw("LPsame")

# efficiency_vs_x_highThreshold_global.GetYaxis().SetRangeUser(0.0001,1.5)
htemp.GetYaxis().SetRangeUser(0.0001,1.5)
# efficiency_vs_x_highThreshold_global.SetTitle(";Relative X position [mm];Efficiency")


efficiency_vs_x_highThreshold_global.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel00.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel01.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel02.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel03.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel04.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel05.SetLineWidth(2)

efficiency_vs_x_highThreshold_global.SetLineColor(1)
efficiency_vs_x_highThreshold_channel00.SetLineColor(416+2) #kGreen+2
efficiency_vs_x_highThreshold_channel01.SetLineColor(432+2) #kCyan+2
efficiency_vs_x_highThreshold_channel02.SetLineColor(600) #kBlue
efficiency_vs_x_highThreshold_channel03.SetLineColor(880) #kViolet
efficiency_vs_x_highThreshold_channel04.SetLineColor(632) #kRed
efficiency_vs_x_highThreshold_channel05.SetLineColor(400+2) #kYellow+2

# legend = TLegend(0.4,0.69,0.7,0.92);
legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
legend.SetNColumns(3)
legend.AddEntry(efficiency_vs_x_highThreshold_channel00, "Strip 1")
legend.AddEntry(efficiency_vs_x_highThreshold_channel01, "Strip 2")
legend.AddEntry(efficiency_vs_x_highThreshold_channel02, "Strip 3")
legend.AddEntry(efficiency_vs_x_highThreshold_channel03, "Strip 4")
legend.AddEntry(efficiency_vs_x_highThreshold_channel04, "Strip 5")
legend.AddEntry(efficiency_vs_x_highThreshold_channel05, "Strip 6")
legend.Draw();

legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);
legend2.AddEntry(efficiency_vs_x_highThreshold_global, "At least two strips")
legend2.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

htemp.Draw("AXIS same")
canvas.SaveAs("Efficiency_HighThreshold_vs_x.gif")
canvas.SaveAs("Efficiency_HighThreshold_vs_x.pdf")



# Save efficiency plots
outputfile = TFile("EfficiencyPlots.root","RECREATE")
# efficiency_vs_x_highThreshold_global.Write("efficiency_vs_x_highThreshold_global")
efficiency_vs_x_highThreshold_channel00.Write("efficiency_vs_x_highThreshold_channel00")
efficiency_vs_x_highThreshold_channel01.Write("efficiency_vs_x_highThreshold_channel01")
efficiency_vs_x_highThreshold_channel02.Write("efficiency_vs_x_highThreshold_channel02")
efficiency_vs_x_highThreshold_channel03.Write("efficiency_vs_x_highThreshold_channel03")
efficiency_vs_x_highThreshold_channel04.Write("efficiency_vs_x_highThreshold_channel04")
efficiency_vs_x_highThreshold_channel05.Write("efficiency_vs_x_highThreshold_channel05")
outputfile.Close()


