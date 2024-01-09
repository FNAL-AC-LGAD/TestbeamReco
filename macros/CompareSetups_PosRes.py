from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TGraph,TEfficiency,TGraphAsymmErrors,TLegend,TPaveText,gROOT,gStyle, kWhite, kBlack
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
import myFunctions as mf

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.5, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 200, help="Max Amp value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)

sensors_list = [
    # Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # Varying thickness KOJI
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
    # HPK pads Varying metal widths
    ["HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"],
]

tagVar_list = [
    # Varying thickness
    ["thickness"],
    # Varying thickness KOJI
    ["thickness"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
    # HPK pads Varying metal widths
    ["width"],
]

saveName_list = [
    # Varying thickness
    "HPK_PosResolution_vs_x_thickness",
    # Varying thickness KOJI
    "Koji_PosResolution_vs_x_thickness",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_PosResolution_vs_x_thicknessRes",
    # HPK pads Varying metal widths
    "HPK_Pads_PosResolution_vs_x_MetalWidth",
]

ylength_list = [
    # Varying thickness
    250,
    # Varying thickness KOJI
    90,
    # HPK pads Varying thickness and resistivity
    310,
    # HPK pads Varying metal widths
    300,
]

yoffset_list = [
    # Varying thickness
    20,
    # Varying thickness KOJI
    10,
    # HPK pads Varying thickness and resistivity
    10,
    # HPK pads Varying metal widths
    10,
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "ResolutionPosVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, saveName, ylength, yoffset in zip(sensors_list, tagVar_list, saveName_list, ylength_list, yoffset_list):
    sensor_reference = sensors[0]
    treat_as_2x2 = ("HPK_W9_23_3_20T_500x500_300M_E600_112V" in sensors)
    if treat_as_2x2:
        sensor_reference = "HPK_W9_23_3_20T_500x500_300M_E600_112V"

    colors = myStyle.GetColorsCompare(len(sensors))

    legend_height = 0.058*(len(sensors) + 2) # Entries + title + binary readout
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

    legendBox = TPaveText(legX1, legTopY1-0.055, legX2, 1-pad_margin-0.03, "NDC")
    legendBox.SetBorderSize(1)
    legendBox.SetLineColor(kBlack)
    legendBox.SetFillColor(0)
    legendBox.SetFillColorAlpha(0, 0.0)

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
    haxis.GetYaxis().SetTitle("Position resolution [#mum]")
    haxis.SetLineWidth(1)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    is_pad = ("500x500" in sensor_reference) or ("pad" in sensor_reference)
    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    pitch = geometry["pitch"]
    boxes = getStripBox(infile_reference, ymin, ylength-yoffset, pitch = pitch/1000.0)
    if not is_pad:
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
                vertical_line.DrawLine(center-swidth/2., ymin, center-swidth/2., ylength-10)
                vertical_line.DrawLine(center+swidth/2., ymin, center+swidth/2., ylength-10)

    binary_readout_res_sensor = TLine(-xlength, pitch/TMath.Sqrt(12), xlength, pitch/TMath.Sqrt(12))
    binary_readout_res_sensor.SetLineWidth(3)
    binary_readout_res_sensor.SetLineStyle(7)
    binary_readout_res_sensor.SetLineColor(kBlack)
    binary_readout_res_sensor.Draw("same")
    legendTop.AddEntry(binary_readout_res_sensor, "Pitch / #sqrt{12}","l")

    plotfile = []
    list_OneStrip_vs_x = []
    list_TwoStrip_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Resolution_Pos/PositionResVsX_tight.root"
        inFile = TFile(inName,"READ")
        hOneStrip = inFile.Get("h_one_strip")
        hTwoStrip = inFile.Get("track_twoStrip_tight")

        plotfile.append(inFile)
        list_OneStrip_vs_x.append(hOneStrip)
        list_TwoStrip_vs_x.append(hTwoStrip)

    sensor_type = "strip" if not is_pad else "channel"
    if treat_as_2x2:
        # Move 3x2 sensors to be centered as a 2x2 pad
        ref_idx = sensors.index(sensor_reference)
        list_2x2 = [list_TwoStrip_vs_x.pop(ref_idx)]
        moved_2x2 = mf.move_distribution(list_2x2, -0.025)
        moved_2x2[0].SetBinContent(moved_2x2[0].FindFirstBinAbove(0.001)-1, 0.001)
        moved_2x2[0].SetBinContent(moved_2x2[0].FindLastBinAbove(0.001)+1, 0.001)
        list_3x2 = list_TwoStrip_vs_x
        moved_3x2 = mf.move_distribution(list_3x2, -0.250)
        # Leave the 2x2 sensor in the very same position
        list_TwoStrip_vs_x = moved_3x2[:ref_idx] + moved_2x2 + moved_3x2[ref_idx:]

    pruned_TwoStrip_vs_x = mf.same_limits_compare(list_TwoStrip_vs_x)

    if treat_as_2x2:
        # Leave 2x2 with a symmetric x-axis
        ref_idx = sensors.index(sensor_reference)
        hist2x2 = pruned_TwoStrip_vs_x[ref_idx]
        hist2x2.SetBinContent(hist2x2.FindFirstBinAbove(0.0001), 0.0)
        hist2x2.SetBinContent(hist2x2.FindLastBinAbove(0.0001), 0.0)
        # Leave the 2x2 sensor in the very same position
        pruned_TwoStrip_vs_x[ref_idx] = mf.same_limits_compare([hist2x2])[0]

    # Remove bad behaved bins in central pad of this group of sensors
    if (saveName == "HPK_Pads_PosResolution_vs_x_thicknessRes"):
        swidth = myStyle.GetGeometry(sensor_reference)["width"]/1000.
        for hist in pruned_TwoStrip_vs_x:
            for b in range(1, hist.GetXaxis().GetNbins()+1):
                is_bad_zone = mf.is_inside_limits(b, hist, 1.001*swidth/2.)
                if is_bad_zone:
                    hist.SetBinContent(b, 0.0)
                    hist.SetBinError(b, 0.0)

    for i, hist_two in enumerate(pruned_TwoStrip_vs_x):
        hist_one = list_OneStrip_vs_x[i]
        # Move one strip markers to correct position wrt boxes
        for j, box in enumerate(boxes):
            x_position = (box.GetX1() + box.GetX2())/2.
            hist_one.SetPointX(j, x_position)
        hist_one.Draw("P same")
        hist_one.SetLineStyle(1)
        hist_one.SetMarkerStyle(33)
        hist_one.SetMarkerSize(3)
        hist_one.SetMarkerColor(colors[i])

        hist_two.SetLineWidth(3)
        hist_two.SetLineColor(colors[i])
        legendTop.AddEntry(hist_two, tag[i])
        hist_two.Draw("hist e same")

        if i==0:
            markOne = TGraph(hist_one)
            markOne.SetMarkerColor(kBlack)
            markTwo = hist_two.Clone()
            markTwo.SetLineColor(kBlack)
            legendBot.AddEntry(markOne, "Exactly one %s"%sensor_type, "P")
            legendBot.AddEntry(markTwo, "Two %s"%sensor_type, "L")

    legendHeader = tag[-1]
    legendTop.SetHeader(legendHeader, "C")
    legendTop.Draw()
    legendBot.Draw()
    legendBox.Draw("same")

    sensor_prod="Strip sensors"
    if is_pad:
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
