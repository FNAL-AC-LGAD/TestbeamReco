from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack, kGreen, TPaveText
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

sensors_list = [
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
    # HPK pads Varying metal widths
    ["HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"],
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
    # HPK pads Varying metal widths
    ["width"],
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
    100
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
    # HPK pads Varying metal widths
    "HPK_Pads_TimeResolution_vs_x_MetalWidth",
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "ResolutionTimeVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    sensor_reference = sensors[0]
    treat_as_2x2 = ("HPK_W9_23_3_20T_500x500_300M_E600_112V" in sensors)
    if treat_as_2x2:
        sensor_reference = "HPK_W9_23_3_20T_500x500_300M_E600_112V"

    colors = myStyle.GetColorsCompare(len(sensors))

    legend_height = 0.058*(len(sensors) + 1) # Entries + title
    legX1 = 2*pad_margin+0.065
    legX2 = 1-pad_margin-0.065
    legendTop = TLegend(legX1, 1-pad_margin-legend_height-0.03, legX2, 1-pad_margin-0.03)
    # legendTop.SetBorderSize(1)
    # legendTop.SetLineColor(kBlack)
    legendTop.SetTextFont(myStyle.GetFont())
    legendTop.SetTextSize(myStyle.GetSize()-4)

    legTopY1 = 1-pad_margin-legend_height-0.03
    legendBot = TLegend(legX1, legTopY1-0.055, legX2, legTopY1)
    legendBot.SetNColumns(2)
    # legendBot.SetBorderSize(1)
    # legendBot.SetLineColor(kBlack)
    legendBot.SetTextFont(myStyle.GetFont())
    legendBot.SetTextSize(myStyle.GetSize()-4)

    xlength = float(options.xlength)
    if ("500x500" in sensor_reference):
        xlength = 0.8
    elif ("KOJI" in sensor_reference):
        xlength = 0.25
    if ("HPK_W9_23_3_20T_500x500_300M_E600_112V" in sensor_reference):
        xlength = 0.50

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
    boxes = getStripBox(infile_reference, ymin, 0.9*ylength, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    # Draw dotted line for different strip widths
    if ("width" in tagVars):
        for i, sensor in enumerate(sensors):
            swidth = myStyle.GetGeometry(sensor)["width"]/1000.
            this_color = colors[i]
            for box in boxes:
                vertical_line = TLine()
                vertical_line.SetLineWidth(2)
                vertical_line.SetLineColor(this_color)
                vertical_line.SetLineColorAlpha(this_color, 0.4)
                vertical_line.SetLineStyle(9)
                center = (box.GetX1() + box.GetX2())/2.
                vertical_line.DrawLine(center-swidth/2., ymin, center-swidth/2., 0.9*ylength)
                vertical_line.DrawLine(center+swidth/2., ymin, center+swidth/2., 0.9*ylength)

    plotfile = []
    list_time_vs_x = []
    list_jitter_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Resolution_Time/TimeDiffVsX_tight.root"
        inFile = [TFile(inName,"READ")]
        hTime = inFile[0].Get("Time_DiffW2Tracker")

        if(("thickness" in tagVars[0]) and ("500x500" not in sensor_reference)):
            inName = "../output/"+sname+"/Jitter/JitterVsX.root"
            inFile.append(TFile(inName,"READ"))
            hJitter = inFile[1].Get("jitter_vs_x")
            hJitter.SetLineStyle(2)

            list_jitter_vs_x.append(hJitter)
        plotfile.append(inFile)
        list_time_vs_x.append(hTime)

    if treat_as_2x2:
        ref_idx = sensors.index(sensor_reference)
        list_2x2 = [list_time_vs_x.pop(ref_idx)]
        moved_2x2 = mf.move_distribution(list_2x2, -0.025)
        list_3x2 = list_time_vs_x
        moved_3x2 = mf.move_distribution(list_3x2, -0.250)
        list_time_vs_x = moved_3x2[:ref_idx] + moved_2x2 + moved_3x2[ref_idx:]
        # Jitter could be added here for 2x2 vs 3x2 if needed

    pruned_time_vs_x = mf.same_limits_compare(list_time_vs_x + list_jitter_vs_x)
    for i, hist in enumerate(pruned_time_vs_x):
        idx = i%len(list_time_vs_x)
        hist.SetLineWidth(3)
        hist.SetLineColor(colors[idx])

        if i < len(list_time_vs_x):
            lengendEntry = legendTop.AddEntry(hist, tag[idx])
        # hist.Draw("hist e same")
        hist.Draw("hist same")

    # Draw legend
    if list_jitter_vs_x:
        tmpTime = pruned_time_vs_x[0].Clone()
        tmpTime.SetLineColor(kBlack)
        tmpJitter = list_jitter_vs_x[0].Clone()
        tmpJitter.SetLineColor(kBlack)
        legendBot.AddEntry(tmpTime, "Time resolution")
        legendBot.AddEntry(tmpJitter, "Jitter")
        legendBox = TPaveText(legX1, legTopY1-0.055, legX2, 1-pad_margin-0.03, "NDC")
        legendBox.SetBorderSize(1)
        legendBox.SetLineColor(kBlack)
        legendBox.SetFillColor(0)
        legendBox.SetFillColorAlpha(0, 0.0)
        legendTop.Draw()
        legendBot.Draw()
        legendBox.Draw("same")
    else:
        legendTop.SetBorderSize(1)
        legendTop.Draw()

    legendHeader = tag[-1]
    legendTop.SetHeader(legendHeader, "C")

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
    legendTop.Clear()
    legendBot.Clear()
    haxis.Delete()
