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
parser.add_option('-x','--xlength', dest='xlength', default = 3.0, help="Limit x-axis in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-r', dest='recoMethod', default = 0, help="Reco method: 0: Full, 1:_oneStrip, 2:_twoStrips")
options, args = parser.parse_args()

method = options.recoMethod

recoMethod_dic = {0: "", 1: "_oneStrip", 2: "_twoStrips"}
recoMethod = recoMethod_dic[int(method)]

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
efficiency_fullReco_numerator_global = inputfile.Get("efficiency_vs_xy_fullReco_numerator")

#efficiency_lowThreshold_numerator_global.RebinX(3)
#efficiency_highThreshold_numerator_global.RebinX(3)
#efficiency_denominator_global.RebinX(3)

shift = inputfile.Get("stripBoxInfo03").GetMean(1)

# Plot and save 2D Histograms
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold%s_global"%(recoMethod), "Efficiency Low Threshold Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_lowThreshold%s_global"%(recoMethod), "Efficiency Low Threshold Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, outdir+"efficiency_highThreshold%s_global"%(recoMethod), "Efficiency High Threshold Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.
EfficiencyUtils.Plot2DEfficiency( efficiency_fullReco_numerator_global, efficiency_denominator_global, outdir+"efficiency_fullReco_global", "Efficiency Full Reco Global", "X [mm]", -10, 10, "Y [mm]" , -20, 20 , 0.0, 1.0 )


channel_good_index = []
th2_efficiency_vs_xy_ch = [[], [], []]
## th2_efficiency_vs_xy_ch = [[highThreshold], [lowThreshold], [fullReco]]

for i in range(7):
    hname_high = "efficiency_vs_xy_highThreshold%s_numerator_channel0%i"%(recoMethod, i)
    hname_low = "efficiency_vs_xy_lowThreshold%s_numerator_channel0%i"%(recoMethod, i)
    hname_full = "efficiency_vs_xy_fullReco_numerator_channel0%i"%(i)
    if inputfile.Get(hname_high):
        channel_good_index.append(i)
        th2_efficiency_vs_xy_ch[0].append(inputfile.Get(hname_high))
        th2_efficiency_vs_xy_ch[1].append(inputfile.Get(hname_low))
        th2_efficiency_vs_xy_ch[2].append(inputfile.Get(hname_full))

# Plot and save 2D Histograms per channel with fullReco
for i,ch in enumerate(channel_good_index):
    EfficiencyUtils.Plot2DEfficiency(th2_efficiency_vs_xy_ch[2][i], efficiency_denominator_global, outdir+"efficiencyFullReco_channel0%i"%(ch), "Efficiency Full Reco Strip %i"%(ch+1), "X [mm]", -10,10, "Y [mm]" , -20,20 , 0.0, 1.0 )


# for i,ch in enumerate(channel_good_index):
#     EfficiencyUtils.Plot2DEfficiency(th2_efficiency_vs_xy_ch[0][i], efficiency_denominator_global, outdir+"efficiency%s_channel0%i"%(recoMethod,ch), "Efficiency Strip %i"%(ch+1), "X [mm]", -10,10, "Y [mm]" , -20,20 , 0.0, 1.0 )


# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

# Plot 1D projections (vs X)
efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global")#,binY_lowEdge,binY_highEdge)

# Define list of histograms
## th1_efficiency_num_vs_x_ch = [[highThreshold], [lowThreshold], [fullReco]]
## list_efficiency_vs_x_ch = [[highThreshold], [lowThreshold], [fullReco]]

th1_efficiency_num_vs_x_ch = [[], [], []]
list_efficiency_vs_x_ch = [[], [], []]
list_threshold = ["highThreshold", "lowThreshold", "fullReco"]

for t,threshold in enumerate(list_threshold):
    for i,ch in enumerate(channel_good_index):
        th1_efficiency_num_vs_x_ch[t].append( th2_efficiency_vs_xy_ch[t][i].ProjectionX("efficiency_vs_x_%s_numerator_channel0%i"%(threshold,ch)) )
        list_efficiency_vs_x_ch[t].append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_num_vs_x_ch[t][i], efficiency_vs_x_denominator_global, "efficiency_vs_x_%s_channel0%i"%(threshold,ch), "Efficiency %s Strip %i"%(threshold,ch+1), "X [mm]", -xlength, xlength, False, shift) )
        # th1_efficiency_lowThreshold_num_vs_x_ch.append( th2_efficiency_low_vs_xy_ch[i].ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel0%i"%(ch)) )
        # list_efficiency_lowThreshold_vs_x_ch.append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_lowThreshold_num_vs_x_ch[i], efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel0%i"%(ch), "Efficiency Low Threshold Strip %i"%(ch+1), "X [mm]", -xlength, xlength, False, shift) )

    if t==0:
        th1_efficiency_num_vs_x_ch[0].append( efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global") )
        list_efficiency_vs_x_ch[0].append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_num_vs_x_ch[0][-1], efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency High Threshold Global", "X [mm]", -xlength, xlength, False, shift) )
    elif t==1:
        th1_efficiency_num_vs_x_ch[1].append( efficiency_lowThreshold_numerator_global.ProjectionX("efficiency_vs_x_lowThreshold_numerator_global") )
        list_efficiency_vs_x_ch[1].append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_num_vs_x_ch[1][-1], efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_global", "Efficiency Low Threshold Global", "X [mm]", -xlength, xlength, False, shift) )
    elif t==2:
        th1_efficiency_num_vs_x_ch[2].append( efficiency_fullReco_numerator_global.ProjectionX("efficiency_vs_x_fullReco_numerator_global") )
        list_efficiency_vs_x_ch[2].append( EfficiencyUtils.Make1DEfficiency(th1_efficiency_num_vs_x_ch[2][-1], efficiency_vs_x_denominator_global, "efficiency_vs_x_fullReco_global", "Efficiency Full Reco Global", "X [mm]", -xlength, xlength, False, shift) )

####
## Draw 1D projection
####
canvas = TCanvas("cv","cv",1000,800)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1,-xlength,xlength)
htemp.GetYaxis().SetRangeUser(0.0001,1.5)

for t,threshold in enumerate(list_threshold):
    htemp.Draw()

    boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
    for box in boxes:
        box.Draw()

    legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
    legend.SetNColumns(3)
    legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);

    for i,ch in enumerate(channel_good_index):
        list_efficiency_vs_x_ch[t][i].Draw("LPsame")
        list_efficiency_vs_x_ch[t][i].SetLineWidth(2)
        list_efficiency_vs_x_ch[t][i].SetLineColor(colors[i])
        legend.AddEntry(list_efficiency_vs_x_ch[t][i], "Strip %i"%(i+1))
        legend.Draw()

    # list_efficiency_vs_x_ch[t][-1].Draw("LPsame")
    # list_efficiency_vs_x_ch[t][-1].SetLineWidth(2)
    # list_efficiency_vs_x_ch[t][-1].SetLineColor(1)
    # legend2.AddEntry(list_efficiency_vs_x_ch[t][-1], "Overall")
    # legend2.Draw()

    # myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    htemp.Draw("AXIS same")
    if t==3: recoMethod=""
    canvas.SaveAs(outdir+"Efficiency_%s%s_vs_x"%(threshold,recoMethod)+".gif")
    canvas.SaveAs(outdir+"Efficiency_%s%s_vs_x"%(threshold,recoMethod)+".pdf")
    canvas.Clear()

# Save efficiency plots
outputfile = TFile(outdir+"EfficiencyPlots%s"%(recoMethod)+".root","RECREATE")

for t,threshold in enumerate(list_threshold):
    for i,ch in enumerate(channel_good_index):
        list_efficiency_vs_x_ch[t][i].Write("efficiency_vs_x_%s_channel0%i"%(threshold,ch))

outputfile.Close()


