from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s','--sensor', dest='sensor', default = "UIC_W1_1cm", help="Type of sensor (BNL2020, BNL2021, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 255, help="Bias Voltage value in [V]")
parser.add_option('-x','--xlength', dest='xlength', default = 3.0, help="Bias Voltage value in [V]")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

sensor = options.sensor
bias = options.biasvolt
xlength = float(options.xlength)

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

colors = myStyle.GetColors()

efficiency_lowThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator")
efficiency_highThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_highThreshold_numerator")
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")

#efficiency_lowThreshold_numerator_global.RebinX(3)
#efficiency_highThreshold_numerator_global.RebinX(3)
#efficiency_denominator_global.RebinX(3)

shift = inputfile.Get("stripBoxInfo03").GetMean(1)

EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -10, 10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -10, 10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_highThreshold_global", "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -10, 10 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.


efficiency_highThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel00")
efficiency_highThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel01")
efficiency_highThreshold_numerator_channel02 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel02")
efficiency_highThreshold_numerator_channel03 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel03")
efficiency_highThreshold_numerator_channel04 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel04")
efficiency_highThreshold_numerator_channel05 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel05")
efficiency_highThreshold_numerator_channel06 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel06")

#efficiency_highThreshold_numerator_channel00.RebinX(3)
#efficiency_highThreshold_numerator_channel01.RebinX(3)
#efficiency_highThreshold_numerator_channel02.RebinX(3)
#efficiency_highThreshold_numerator_channel03.RebinX(3)
#efficiency_highThreshold_numerator_channel04.RebinX(3)
#efficiency_highThreshold_numerator_channel05.RebinX(3)
#efficiency_highThreshold_numerator_channel06.RebinX(3)

EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel00, efficiency_denominator_global, outdir+"efficiency_channel00", "Efficiency Strip 1", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel01, efficiency_denominator_global, outdir+"efficiency_channel01", "Efficiency Strip 2", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel02, efficiency_denominator_global, outdir+"efficiency_channel02", "Efficiency Strip 3", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel03, efficiency_denominator_global, outdir+"efficiency_channel03", "Efficiency Strip 4", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel04, efficiency_denominator_global, outdir+"efficiency_channel04", "Efficiency Strip 5", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel05, efficiency_denominator_global, outdir+"efficiency_channel05", "Efficiency Strip 6", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel06, efficiency_denominator_global, outdir+"efficiency_channel06", "Efficiency Strip 7", "X [mm]", -10,10, "Y [mm]" , -10,10 , 0.0, 1.0 )


# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

#1D efficiency vs X
#binY_lowEdge = efficiency_denominator_global.GetYaxis().FindFixBin(-9)
#binY_highEdge = efficiency_denominator_global.GetYaxis().FindFixBin(3)

efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_global = efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel00 = efficiency_highThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel00")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel01 = efficiency_highThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel01")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel02 = efficiency_highThreshold_numerator_channel02.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel02")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel03 = efficiency_highThreshold_numerator_channel03.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel03")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel04 = efficiency_highThreshold_numerator_channel04.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel04")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel05 = efficiency_highThreshold_numerator_channel05.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel05")#,binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel06 = efficiency_highThreshold_numerator_channel06.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel06")#,binY_lowEdge,binY_highEdge)


efficiency_vs_x_highThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency Global", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel00", "Efficiency Strip 1", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel01", "Efficiency Strip 2", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel02 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel02, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel02", "Efficiency Strip 3", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel03 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel03, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel03", "Efficiency Strip 4", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel04 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel04, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel04", "Efficiency Strip 5", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel05 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel05, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel05", "Efficiency Strip 6", "X [mm]", -xlength, xlength, False, shift)
efficiency_vs_x_highThreshold_channel06 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel06, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel06", "Efficiency Strip 7", "X [mm]", -xlength, xlength, False, shift)



canvas = TCanvas("cv","cv",1000,800)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1,-xlength,xlength)
htemp.Draw()

boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for box in boxes:
    box.Draw()

efficiency_vs_x_highThreshold_channel00.Draw("LPsame")
efficiency_vs_x_highThreshold_channel01.Draw("LPsame")
efficiency_vs_x_highThreshold_channel02.Draw("LPsame")
efficiency_vs_x_highThreshold_channel03.Draw("LPsame")
efficiency_vs_x_highThreshold_channel04.Draw("LPsame")
efficiency_vs_x_highThreshold_channel05.Draw("LPsame")
efficiency_vs_x_highThreshold_channel06.Draw("LPsame")
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
efficiency_vs_x_highThreshold_channel06.SetLineWidth(2)

efficiency_vs_x_highThreshold_global.SetLineColor(1)
efficiency_vs_x_highThreshold_channel00.SetLineColor(colors[0])
efficiency_vs_x_highThreshold_channel01.SetLineColor(colors[1])
efficiency_vs_x_highThreshold_channel02.SetLineColor(colors[2])
efficiency_vs_x_highThreshold_channel03.SetLineColor(colors[3])
efficiency_vs_x_highThreshold_channel04.SetLineColor(colors[4])
efficiency_vs_x_highThreshold_channel05.SetLineColor(colors[5])
efficiency_vs_x_highThreshold_channel06.SetLineColor(colors[6])

# legend = TLegend(0.4,0.69,0.7,0.92);
legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
legend.SetNColumns(3)
legend.AddEntry(efficiency_vs_x_highThreshold_channel00, "Strip 1")
legend.AddEntry(efficiency_vs_x_highThreshold_channel01, "Strip 2")
legend.AddEntry(efficiency_vs_x_highThreshold_channel02, "Strip 3")
legend.AddEntry(efficiency_vs_x_highThreshold_channel03, "Strip 4")
legend.AddEntry(efficiency_vs_x_highThreshold_channel04, "Strip 5")
legend.AddEntry(efficiency_vs_x_highThreshold_channel05, "Strip 6")
legend.AddEntry(efficiency_vs_x_highThreshold_channel06, "Strip 7")
legend.Draw();

legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);
legend2.AddEntry(efficiency_vs_x_highThreshold_global, "At least two strips")
legend2.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

htemp.Draw("AXIS same")
canvas.SaveAs(outdir+"Efficiency_HighThreshold_vs_x_"+sensor+".gif")
canvas.SaveAs(outdir+"Efficiency_HighThreshold_vs_x_"+sensor+".pdf")

# Save efficiency plots
outputfile = TFile(outdir+"EfficiencyPlots_"+sensor+".root","RECREATE")
# efficiency_vs_x_highThreshold_global.Write("efficiency_vs_x_highThreshold_global")
efficiency_vs_x_highThreshold_channel00.Write("efficiency_vs_x_highThreshold_channel00")
efficiency_vs_x_highThreshold_channel01.Write("efficiency_vs_x_highThreshold_channel01")
efficiency_vs_x_highThreshold_channel02.Write("efficiency_vs_x_highThreshold_channel02")
efficiency_vs_x_highThreshold_channel03.Write("efficiency_vs_x_highThreshold_channel03")
efficiency_vs_x_highThreshold_channel04.Write("efficiency_vs_x_highThreshold_channel04")
efficiency_vs_x_highThreshold_channel05.Write("efficiency_vs_x_highThreshold_channel05")
efficiency_vs_x_highThreshold_channel06.Write("efficiency_vs_x_highThreshold_channel06")
outputfile.Close()


