from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle
import re

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
base = "../output"
datasets = [
    ['BNL_20um_1cm_450um_W3074_2_1_95V', 'BNL_20um_1cm_400um_W3074_1_4_95V'],
    ['BNL_50um_1cm_450um_W3052_2_4_185V','BNL_50um_1cm_400um_W3051_1_4_160V'],
    ['BNL_20um_1cm_450um_W3075_2_4_80V', 'BNL_20um_1cm_400um_W3075_1_2_80V'],
]

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Max Amp value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)
canvas = TCanvas("cv","cv",1000,800)

for d, dnames in enumerate(datasets):
    # varname  = 'efficiency_vs_x_twoStrips_channel0'
    # plotfile_name = 'Eff/EfficiencyPlots.root'

    varname = 'rms_track_twoStrips'
    plotfile_name = 'PositionRes/PlotRecoDiffVsX.root'

    pattern = re.compile(r'BNL_(\d+)um_(\d+)cm_(\d+)um_(\w+)_(\w+)_(\w+)_(\w+)')
    # thickness:       1
    # strip length:    2
    # gap width:       3
    # wafer:           4
    # wafer number 1:  5
    # wafer number 2:  6
    # bias voltage:    7
    label_names = [f'{pattern.match(i).group(4)} ({pattern.match(i).group(5)},{pattern.match(i).group(6)}): {500 - int(pattern.match(i).group(3))}um, {pattern.match(i).group(1)}T' for i in dnames]
    print(label_names)
    channel_good_index = []

    plotfile_name_1 = f'{base}/{dnames[0]}/{plotfile_name}'
    plotfile_name_2 = f'{base}/{dnames[1]}/{plotfile_name}'
    inputfile_name_1 = f'{base}/{dnames[0]}/{dnames[0]}_Analyze.root'
    inputfile_name_2 = f'{base}/{dnames[1]}/{dnames[1]}_Analyze.root'

    plotfile = TFile(plotfile_name_1,"READ")
    inputfile = TFile(inputfile_name_1,"READ")
    dataset = dnames[0]

    plotfile2 = TFile(plotfile_name_2,"READ")
    inputfile2 = TFile(inputfile_name_2,"READ")
    dataset2 = dnames[1]

    print(inputfile)
    print(plotfile)
    print(inputfile2)
    print(plotfile2)

    shift = inputfile.Get("stripBoxInfo03").GetMean(1)
    shift2 = inputfile2.Get("stripBoxInfo03").GetMean(1)

    plotList_amplitude_vs_x  = []
    plotList_amplitude_vs_x2  = []
    maximum = 50
    # for i,ch in enumerate(channel_good_index):
    print(f"{varname}")
    plot_amplitude = plotfile.Get(f"{varname}")
    plot_amplitude.SetLineWidth(2)
    plot_amplitude.SetFillColor(colors[0])
    plot_amplitude.SetFillStyle(3050)
    plot_amplitude.SetFillColorAlpha(colors[0],0.3)
    plot_amplitude.SetLineColor(colors[0])
    plotList_amplitude_vs_x.append(plot_amplitude)
    plot_amplitude2 = plotfile2.Get(f"{varname}")
    plot_amplitude2.SetLineWidth(2)
    plot_amplitude2.SetLineColor(colors[0])
    plotList_amplitude_vs_x2.append(plot_amplitude2)
    # maximum = max(plotList_amplitude_vs_x[0].GetMaximum(), plotList_amplitude_vs_x2[0].GetMaximum())

    totalAmplitude_vs_x = TH1F("htemp","",1,-xlength,xlength)
    totalAmplitude_vs_x.Draw("hist")
    totalAmplitude_vs_x.SetStats(0)
    totalAmplitude_vs_x.SetTitle("")
    totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    totalAmplitude_vs_x.GetYaxis().SetTitle("Position resolution [#mum]")
    totalAmplitude_vs_x.SetLineWidth(2)
    totalAmplitude_vs_x.SetMaximum(160)

    boxes = getStripBox(inputfile,0,ylength-10.0,False, 18, True, shift)
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

    # for i,ch in enumerate(channel_good_index):
    plotList_amplitude_vs_x[0].Draw("HIST same f")
    plotList_amplitude_vs_x2[0].Draw("HIST same")
    # legend.AddEntry(plotList_amplitude_vs_x2[i], "Strip %i"%(ch+1))
    # legend.Draw()

    legend2 = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.12,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
    print(plotList_amplitude_vs_x2)
    print(plotList_amplitude_vs_x)
    legend2.AddEntry(plotList_amplitude_vs_x2[0], label_names[0])
    legend2.AddEntry(plotList_amplitude_vs_x[0], label_names[1])
    legend2.Draw()
    myStyle.BeamInfo()
    # myStyle.SensorInfoSmart(dataset)
    canvas.SaveAs(f"../{varname}_vs_x_thickness_{d+1}.png")
