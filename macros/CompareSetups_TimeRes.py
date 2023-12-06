from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack, kGreen, TPaveText 
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
import math
import myFunctions as mf

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# # Removed. Check if needed to be re-implemented
# def remove_jitter(hTime, hJitter, new_hist):
#     nbins = hJitter.GetXaxis().GetNbins()
#     for i in range(1, nbins+1):
#         jitter = hJitter.GetBinContent(i)
#         time = hTime.GetBinContent(i)
#         value = 0
#         if (time >= jitter):
#             value = math.sqrt(time**2 - jitter**2)

#         new_hist.SetBinContent(i, value)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.5, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Max TR value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)
colors = myStyle.GetColors(True)

sensors_list = [
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    [ "HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
    # HPK pads Varying metal width 
    # ["HPK_W9_22_3_20T_500x500_150M_E600_112V","HPK_W9_23_3_20T_500x500_300M_E600_112V" ]
]

tagVar_list = [
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    # HPK Varying thickness
    ["thickness"],
    # KOJI Varying thickness
    ["thickness"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
]

ylength_list = [
    # Varying resistivity and capacitance
    70,
    # HPK Varying thickness
    160,
    # KOJI Varying thickness
    65,
    # HPK pads Varying thickness and resistivity
    100,
    # HPK pads Varying metal width 
    # 100
]

saveName_list = [
    # Varying resistivity and capacitance
    "HPK_TimeResolution_vs_x_ResCap",
    # HPK Varying thickness
    "HPK_TimeResolution_vs_x_thickness",
    # KOJI Varying thickness
    "Koji_TimeResolution_vs_x_thickness",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_TimeResolution_vs_x_thicknessRes",
    # HPK pads Varying metal width 
    # "HPK_Pads_TimeResolution_vs_x_width"
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "ResolutionTimeVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    sensor_reference = sensors[0]

    legend = TLegend(2*pad_margin+0.065, 1-pad_margin-0.35, 1-pad_margin-0.065, 1-pad_margin-0.25)
    legend.SetNColumns(2)
    # legend.SetBorderSize(1)
    # legend.SetLineColor(kBlack)

    yLegend = 0.026*len(sensors)
    legend2 = TLegend(2*pad_margin+0.065, 1-pad_margin-0.2-yLegend, 1-pad_margin-0.065, 1-pad_margin-0.03)
    # legend2.SetBorderSize(1)
    legend2.SetLineColor(kBlack)
    legend2.SetTextFont(myStyle.GetFont())
    legend2.SetTextSize(myStyle.GetSize()-4)

    xlength = float(options.xlength)
    if ("500x500" in sensor_reference):
        xlength = 0.8
    elif ("KOJI" in sensor_reference):
        xlength = 0.25

    tag = mf.get_legend_comparation_plots(sensors, tagVars)

    haxis = TH1F("htemp","",1,-xlength,xlength)
    haxis.Draw("AXIS")
    haxis.SetStats(0)
    haxis.SetTitle("")
    haxis.GetXaxis().SetTitle("Track x position [mm]")
    haxis.GetYaxis().SetTitle("Time resolution [ps]")
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, ylength-30, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    plotfile = []
    list_time_vs_x = []
    list_jitter_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Resolution_Time/TimeDiffVsX_tight.root"
        inFile = [TFile(inName,"READ")]
        hTime = inFile[0].Get("Time_DiffW2Tracker")
        hTime.SetLineWidth(3)
        if("thickness" in tagVars[0]):
            hTime.SetLineColor(colors[i*2])
        else:
            hTime.SetLineColor(colors[i+1])

        lengendEntry = legend2.AddEntry(hTime, tag[i])

        if(("thickness" in tagVars[0]) and ("500x500" not in sensor_reference)):
            inName = "../output/"+sname+"/Jitter/JitterVsX.root"
            inFile.append(TFile(inName,"READ"))
            hJitter = inFile[1].Get("jitter_vs_x")
            hJitter.SetLineWidth(3)
            hJitter.SetLineStyle(2)
            hJitter.SetLineColor(colors[i*2])

            list_jitter_vs_x.append(hJitter)
        plotfile.append(inFile)
        list_time_vs_x.append(hTime)

    pruned_time_vs_x = mf.same_limits_compare(list_time_vs_x + list_jitter_vs_x)
    for hist in pruned_time_vs_x:
        hist.Draw("hist same")

    # Draw legend
    if list_jitter_vs_x:
        legend.AddEntry(list_time_vs_x[0], "Time resolution")
        legend.AddEntry(list_jitter_vs_x[0], "Jitter")
        legendBox = TPaveText(2*pad_margin+0.065, 1-pad_margin-0.03, 1-pad_margin-0.065, 1-pad_margin-0.35, "NDC")
        legendBox.SetBorderSize(1)
        legendBox.SetLineColor(kBlack)
        legendBox.SetFillColor(0)
        legendBox.SetFillColorAlpha(0, 0.0)
        legend.Draw()
        legend2.Draw()
        legendBox.Draw("same")
    else:
        legend2.SetBorderSize(1)
        legend2.Draw()

    legendHeader = tag[-1]
    legend2.SetHeader(legendHeader, "C")

    sensor_prod="Strip sensors"
    if ("500x500" in sensor_reference):
        sensor_prod = "Pixel sensors"
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)

    haxis.Draw("AXIS same")

    canvas.SaveAs("%s%s.png"%(outdir, saveName))
    canvas.SaveAs("%s%s.pdf"%(outdir, saveName))
    for files in plotfile:
        for f in files:
            f.Close()
    infile_reference.Close()
    canvas.Clear()
    legend.Clear()
    legend2.Clear()
    haxis.Delete()
