from ROOT import TFile,TTree,TLine,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack, TPaveText
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
from  builtins import any
import myFunctions as mf

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.75, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 1.4, help="Max Efficiency in final plot")
options, args = parser.parse_args()

sensors_list = [
    # BNL and HPK sensors - different metal widths
    ["BNL_50um_1cm_450um_W3051_2_2_170V", "BNL_50um_1cm_400um_W3051_1_4_160V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
    # HPK pads Varying metal widths
    ["HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"],
]

tagVar_list = [
    # BNL and HPK sensors - different metal widths
    ["manufacturer", "width"],
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

saveName_list = [
    # BNL and HPK sensors - different metal widths
    "BNL_and_HPK_Efficiency_vs_x_MetalWidth",
    #Varying resistivity and capacitance
    "HPK_Efficiency_vs_x_ResCap",
    # HPK Varying thickness
    "HPK_efficiency_vs_x_thickness",
    # KOJI Varying thickness
    "Koji_efficiency_vs_x_thickness",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_efficiency_vs_x_ThicknessRes",
    # HPK pads Varying metal widths
    "HPK_Pads_efficiency_vs_x_MetalWidth",
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "EfficiencyVsX/")

ymin = 0.01
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, saveName in zip(sensors_list, tagVar_list, saveName_list):
    sensor_reference = sensors[0]
    active_thickness_comp = ("HPK_W9_15_2" in sensor_reference)
    treat_as_2x2 = ("HPK_W9_23_3_20T_500x500_300M_E600_112V" in sensors)
    if treat_as_2x2:
        sensor_reference = "HPK_W9_23_3_20T_500x500_300M_E600_112V"

    colors = myStyle.GetColorsCompare(len(sensors))

    # Define legend boxes
    legend_height = 0.058 * (len(sensors) + 1) # Entries + title
    legX1 = 2 * pad_margin + 0.065
    legX2 = 1 - pad_margin - 0.065
    legTopY2 = 1 - pad_margin - 0.03
    legTopY1 = legTopY2 - legend_height
    # Top legend with each sensor info
    legendTop = TLegend(legX1, legTopY1, legX2, legTopY2)
    legendTop.SetTextFont(myStyle.GetFont())
    legendTop.SetTextSize(myStyle.GetSize()-4)
    # Bottom legend with extra info, full reco for instance
    legendBot = TLegend(legX1, legTopY1 - 0.055, legX2, legTopY1)
    legendBot.SetTextFont(myStyle.GetFont())
    legendBot.SetTextSize(myStyle.GetSize()-4)
    if active_thickness_comp:
        legendBot.SetNColumns(2)
    # Legend border in correct position
    legendBox = TPaveText(legX1, legTopY1 - 0.055, legX2, legTopY2, "NDC")
    legendBox.SetBorderSize(1)
    legendBox.SetLineColor(kBlack)
    legendBox.SetFillColor(0)
    legendBox.SetFillColorAlpha(0, 0.0)

    xlength = float(options.xlength)
    if ("500x500" in sensor_reference):
        xlength = 0.8
    elif ("KOJI" in sensor_reference):
        xlength = 0.35
    if ("HPK_W9_23_3_20T_500x500_300M_E600_112V" in sensor_reference):
        xlength = 0.50

    tag = mf.get_legend_comparation_plots(sensors, tagVars)

    ylength = 1.3 + 0.12 * (len(sensors) + 1)

    haxis = TH1F("htemp","",1,-xlength,xlength)
    haxis.Draw("AXIS")
    haxis.SetStats(0)
    haxis.SetTitle("")
    haxis.GetXaxis().SetTitle("Track x position [mm]")
    haxis.GetYaxis().SetTitle("Efficiency")
    # if ("500x500" in sensor_reference):
    #     haxis.GetYaxis().SetTitle("Two-channel efficiency")
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    xlimit = 0
    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, 1.0, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        xlimit = abs(boxes[0].GetX1()) if abs(boxes[0].GetX1()) > abs(boxes[0].GetX2()) else abs(boxes[0].GetX2())
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
                vertical_line.DrawLine(center-swidth/2., ymin, center-swidth/2., 1.0)
                vertical_line.DrawLine(center+swidth/2., ymin, center+swidth/2., 1.0)

    # Draw line at efficiency 1.0 as a reference
    horizontal_line = TLine(-xlength, 1.0, xlength, 1.0)
    horizontal_line.SetLineWidth(2)
    horizontal_line.SetLineColorAlpha(15, 0.5)
    horizontal_line.SetLineStyle(9)
    horizontal_line.DrawClone("same")

    plotfile = []
    list_efficiency_vs_x = []
    list_FullRecoEfficiency_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Efficiency/EfficiencyVsX_tight.root"
        inFile = TFile(inName,"READ")
        hEff = inFile.Get("hefficiency_vs_x_twoStrip_numerator_tight")
        plotfile.append(inFile)
        list_efficiency_vs_x.append(hEff)
        # Add total efficiency at the end
        hFullReco = inFile.Get("hefficiency_vs_x_fullReco_numerator_tight")
        # Add everytime for "active_thickness_comp"
        if active_thickness_comp:
            hFullReco.SetLineStyle(2)
            list_FullRecoEfficiency_vs_x.append(hFullReco)
        # Add once only for the other sets of sensors
        elif i is (len(sensors) - 1):
            hFullReco.SetLineStyle(1)
            list_FullRecoEfficiency_vs_x.append(hFullReco)

    if treat_as_2x2:
        ref_idx = sensors.index(sensor_reference)
        list_2x2 = [list_efficiency_vs_x.pop(ref_idx)]
        moved_2x2 = mf.move_distribution(list_2x2, -0.025)
        list_3x2 = list_efficiency_vs_x
        moved_3x2 = mf.move_distribution(list_3x2, -0.250)
        list_efficiency_vs_x = moved_3x2[:ref_idx] + moved_2x2 + moved_3x2[ref_idx:]

    pruned_efficiency_vs_x = mf.same_limits_compare(list_efficiency_vs_x + list_FullRecoEfficiency_vs_x, xlimit=xlimit)

    legend_str_type = "strip" if "500x500" not in sensor_reference else "column"
    # Add only two-strip efficiency in top legend
    for i, hist in enumerate(pruned_efficiency_vs_x):
        idx = i%len(list_efficiency_vs_x)
        is_two_strip_eff = (i < len(list_efficiency_vs_x))
        line_color = colors[idx]
        if (not is_two_strip_eff) and (not active_thickness_comp):
            line_color = kBlack
        hist.SetLineColor(line_color)
        hist.SetLineWidth(3)
        if is_two_strip_eff:
            text_legend = "Two-%s: %s"%(legend_str_type, tag[idx])
            lengendEntry = legendTop.AddEntry(hist, text_legend)
        hist.Draw("hist same")

    # Draw legend
    ref_eff = pruned_efficiency_vs_x[0].Clone()
    ref_eff.SetLineColor(kBlack)
    ref_fullReco = list_FullRecoEfficiency_vs_x[0].Clone()
    ref_fullReco.SetLineColor(kBlack)
    if active_thickness_comp:
        legendBot.AddEntry(ref_eff, "Two-strip eff")
        legendBot.AddEntry(ref_fullReco, "One-or-more strip eff")
    else:
        text_fullReco = "One-or-more %s any sensor"%(legend_str_type)
        legendBot.AddEntry(ref_fullReco, text_fullReco)
    legendTop.Draw()
    legendBot.Draw()
    legendBox.Draw("same")

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

    for file in plotfile:
        file.Close()
    infile_reference.Close()
    canvas.Clear()
    legendTop.Clear()
    legendBot.Clear()
    haxis.Delete()
