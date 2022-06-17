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
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 0, help="Bias Voltage value in [V]")
parser.add_option('-x','--xlength', dest='xlength', default = 3.0, help="Bias Voltage value in [V]")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-r', dest='recoMethod', default = 0, help="Reco method: 1:_oneStrip, 2:_twoStrips or empty")
options, args = parser.parse_args()

recoMethod_dic = {0: "", 1: "_oneStrip", 2: "_twoStrips"}
recoMethod = recoMethod_dic[int(options.recoMethod)]

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "Eff/")

colors = myStyle.GetColors()

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
bias   = sensor_Geometry['BV'] if options.biasvolt == 0 else options.biasvolt
xlength = float(options.xlength)


efficiency_lowThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_lowThreshold%s_numerator"%(recoMethod))
efficiency_highThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_highThreshold%s_numerator"%(recoMethod))
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")

#efficiency_lowThreshold_numerator_global.RebinX(3)
#efficiency_highThreshold_numerator_global.RebinX(3)
#efficiency_denominator_global.RebinX(3)

shift = inputfile.Get("stripBoxInfo03").GetMean(1)

EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold%s_global"%(recoMethod), "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold%s_global"%(recoMethod), "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_highThreshold%s_global"%(recoMethod), "Efficiency Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.

channel_good_index = []
th2_efficiency_high_vs_xy_ch = []
th2_efficiency_low_vs_xy_ch = []
for i in range(7):
    hname_high = "efficiency_vs_xy_highThreshold%s_numerator_channel0%i"%(recoMethod, i)
    hname_low = "efficiency_vs_xy_lowThreshold%s_numerator_channel0%i"%(recoMethod, i)
    if inputfile.Get(hname_high):
        channel_good_index.append(i)
        th2_efficiency_high_vs_xy_ch.append(inputfile.Get(hname_high))
        th2_efficiency_low_vs_xy_ch.append(inputfile.Get(hname_low))


for i,ch in enumerate(channel_good_index):
    EfficiencyUtils.Plot2DEfficiency(th2_efficiency_high_vs_xy_ch[i], efficiency_denominator_global, outdir+"efficiency%s_channel0%i"%(recoMethod,ch), "Efficiency Strip %i"%(ch+1), "X [mm]", -10,10, "Y [mm]" , -20,20 , 0.0, 1.0 )


# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global")#,binY_lowEdge,binY_highEdge)

th1_efficiency_highThreshold_num_vs_x_ch = []
list_efficiency_highThreshold_vs_x_ch = []
th1_efficiency_lowThreshold_num_vs_x_ch = []
list_efficiency_lowThreshold_vs_x_ch = []
for i,ch in enumerate(channel_good_index):
    th1_efficiency_highThreshold_num_vs_x_ch.append( th2_efficiency_high_vs_xy_ch[i].ProjectionX("efficiency_vs_x_highThreshold_numerator_channel0%i"%(ch)) )
    list_efficiency_highThreshold_vs_x_ch.append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_highThreshold_num_vs_x_ch[i], efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel0%i"%(ch), "Efficiency High Threshold Strip %i"%(ch+1), "X [mm]", -xlength, xlength, False, shift) )
    th1_efficiency_lowThreshold_num_vs_x_ch.append( th2_efficiency_low_vs_xy_ch[i].ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel0%i"%(ch)) )
    list_efficiency_lowThreshold_vs_x_ch.append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_lowThreshold_num_vs_x_ch[i], efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel0%i"%(ch), "Efficiency Low Threshold Strip %i"%(ch+1), "X [mm]", -xlength, xlength, False, shift) )

th1_efficiency_highThreshold_num_vs_x_ch.append( efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global") )
list_efficiency_highThreshold_vs_x_ch.append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_highThreshold_num_vs_x_ch[-1], efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency High Threshold Global", "X [mm]", -xlength, xlength, False, shift) )
th1_efficiency_lowThreshold_num_vs_x_ch.append( efficiency_lowThreshold_numerator_global.ProjectionX("efficiency_vs_x_lowThreshold_numerator_global") )
list_efficiency_lowThreshold_vs_x_ch.append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_lowThreshold_num_vs_x_ch[-1], efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_global", "Efficiency Low Threshold Global", "X [mm]", -xlength, xlength, False, shift) )

## Draw 1D projection HighThreshold
canvas = TCanvas("cv","cv",1000,800)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1,-xlength,xlength)
htemp.GetYaxis().SetRangeUser(0.0001,1.5)
htemp.Draw()

boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for box in boxes:
    box.Draw()

legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
legend.SetNColumns(3)
legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);

for i,hist in enumerate(list_efficiency_highThreshold_vs_x_ch):
    hist.Draw("LPsame")
    hist.SetLineWidth(2)
    hist.SetLineColor(colors[i]) if (i<len(channel_good_index)) else hist.SetLineColor(1)
    legend.AddEntry(hist, "Strip %i"%(i+1)) if (i<len(channel_good_index)) else legend2.AddEntry(hist, "Overall")
    legend.Draw() if (i<len(channel_good_index)) else legend2.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

htemp.Draw("AXIS same")
canvas.SaveAs(outdir+"Efficiency_HighThreshold%s_vs_x_"%(recoMethod)+".gif")
canvas.SaveAs(outdir+"Efficiency_HighThreshold%s_vs_x_"%(recoMethod)+".pdf")

## Draw 1D projection LowThreshold
canvas.Clear()
htemp.Draw()

boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for box in boxes:
    box.Draw()

legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
legend.SetNColumns(3)
legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);

for i,hist in enumerate(list_efficiency_lowThreshold_vs_x_ch):
    hist.Draw("LPsame")
    hist.SetLineWidth(2)
    hist.SetLineColor(colors[i]) if (i<len(channel_good_index)) else hist.SetLineColor(1)
    legend.AddEntry(hist, "Strip %i"%(i+1)) if (i<len(channel_good_index)) else legend2.AddEntry(hist, "Overall")
    legend.Draw() if (i<len(channel_good_index)) else legend2.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

htemp.Draw("AXIS same")
canvas.SaveAs(outdir+"Efficiency_LowThreshold%s_vs_x_"%(recoMethod)+".gif")
canvas.SaveAs(outdir+"Efficiency_LowThreshold%s_vs_x_"%(recoMethod)+".pdf")

# Save efficiency plots
outputfile = TFile(outdir+"EfficiencyPlots%s_"%(recoMethod)+".root","RECREATE")

for i,ch in enumerate(channel_good_index):
    list_efficiency_highThreshold_vs_x_ch[i].Write("efficiency_vs_x_highThreshold_channel0%i"%(ch))
    list_efficiency_lowThreshold_vs_x_ch[i].Write("efficiency_vs_x_lowThreshold_channel0%i"%(ch))

outputfile.Close()


