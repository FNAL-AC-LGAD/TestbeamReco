from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TLine,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import os
import optparse
import myStyle
import math
from array import array
import myFunctions as mf
import mySensorInfo as msi

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)
colors = [colors[1], colors[4], colors[2]]

## Defining Style
myStyle.ForceStyle()


datasets = [
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_185V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_180V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_170V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_160V",

    # "HPK_30um_500x500um_2x2pad_E600_FNAL_144V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_135V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_130V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_120V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_110V",

    # "HPK_20um_500x500um_2x2pad_E600_FNAL_110V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_108V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_100V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_95V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_90V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_85V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_75V",
]

variables = ["time_resolution", "jitter", "amp_max", "risetime", "baseline"]
y_label = ["Time resolution [ps]", "Jitter [ps]", "Amplitude peak [mV]",
           "Risetime [ps] (10 to 90%)", "Baseline RMS [mV]"]
y_low_limit = [0, 0, 0, 200, 1.4]
y_top_limit = [70, 0, 210, 800, 2.6]

outdir = myStyle.getOutputDir("Paper2023")
outdir = myStyle.GetPlotsDir(outdir, "Bias_scan/")

geometry_all = msi.sensorsGeom2023_biasScan


canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

# Define hist for axes style
htemp = TH1F("htemp", "", 1, 65, 205)
htemp.SetStats(0)
# htemp.SetMinimum(0.0)
# htemp.SetMaximum(info.yMax)
htemp.GetXaxis().SetTitle("Bias Voltage [V]")
# htemp.GetYaxis().SetRangeUser(0.0, ylength)

pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()

subsets = ["20um", "30um", "50um"]
for i, var in enumerate(variables):
    x_volts = [[], [], []]
    y_values = [[], [], []]
    ymax = 0.0
    for dataset in datasets:
        sensor_geometry = geometry_all[dataset]
        sensor_info = msi.variableInfo2023_biasScan[dataset]
        for j, thickness in enumerate(subsets):
            if thickness in dataset:
                idx = j
                break

        value = sensor_info[var]
        # Remove tracker component
        if "time_resolution" in var:
            value = math.sqrt(value**2 - 10**2)

        x_volts[idx].append(sensor_geometry["voltage"])
        y_values[idx].append(value)

    hists = []
    for j, thickness in enumerate(subsets):
        hist = ROOT.TGraph(len(x_volts[j]), array('f',x_volts[j]), array('f',y_values[j]))
        hist.SetName("%s_%s"%(var, thickness))
        # hist.SetLineWidth(3)
        # hist.SetLineStyle(1)
        hist.SetMarkerStyle(8)
        hist.SetMarkerSize(2)
        hist.SetMarkerColor(colors[j])
        hists.append(hist)

        ymax = max(y_values[j]) if (ymax < max(y_values[j])) else ymax

    htemp.GetYaxis().SetTitle(y_label[i])
    ymin = y_low_limit[i]
    ymax = y_top_limit[i] if y_top_limit[i] else 1.7*ymax
    htemp.GetYaxis().SetRangeUser(ymin, ymax)

    htemp.Draw("AXIS")
    gPad.RedrawAxis("g")

    # Create legend
    legend = TLegend(pad_center-0.30, 1-pad_margin-0.20, pad_center+0.30, 1-pad_margin-0.01)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetLineStyle(1)
    legend.SetLineWidth(2)

    for j, hist in enumerate(hists):
        thick = hist.GetName().split("_")[-1]
        hist.Draw("SAME P")
        legend_title = "HPK %s FNAL board"%thick
        legend.AddEntry(hist, legend_title, "p")

    legend.Draw()

    myStyle.BeamInfo()
    canvas.SaveAs("%s%s.gif"%(outdir, var))
    canvas.SaveAs("%s%s.pdf"%(outdir, var))

    canvas.Clear()


# if dataset in dict_one_strip_resolutions:
#     list_one_strip_values = dict_one_strip_resolutions[dataset]['resOneStrip']
# else:
#     print(" >> Sensor not found in One strip Reco dictionary. Please, add sensor with a default number if needed.")
#     exit()

# list_positions = []
# list_values = []
# for i, value in enumerate(list_one_strip_values):
#     if value > 0.0:
#         box = boxes[i]
#         x_position = (box.GetX1() + box.GetX2())/2.
#         list_positions.append(x_position)
#         list_values.append(value)

# if not list_values:
#     use_one_strip = False
# else:
#     hist_one_strip = ROOT.TGraph(len(list_values), array('f',list_positions), array('f',list_values))
#     hist_one_strip.SetName("h_one_strip")
#     # hist_one_strip.SetLineWidth(3)
#     hist_one_strip.SetLineStyle(1)
#     hist_one_strip.SetMarkerStyle(33)
#     hist_one_strip.SetMarkerSize(3)
#     hist_one_strip.SetMarkerColor(colors[0])

