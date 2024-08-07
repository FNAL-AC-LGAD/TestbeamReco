from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
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
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 120, help="Max Amp value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)

sensors_list = [
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # BNL and HPK Varying metal widths
    ["BNL_50um_1cm_450um_W3051_2_2_170V","BNL_50um_1cm_400um_W3051_1_4_160V" , "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
    # # HPK pads Varying metal widths
    # ["HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"],
]

tagVar_list = [
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    # HPK Varying thickness
    ["thickness"],
    # KOJI Varying thickness
    ["thickness"],
    # BNL and HPK Varying metal widths
    ["manufacturer", "width"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
    # # HPK pads Varying metal widths
    # ["width"],
]

ylength_list = [
    # Varying resistivity and capacitance
    190,
    # HPK Varying thickness
    170,
    # KOJI Varying thickness
    90,
    # BNL and HPK Varying metal widths
    100,
    # HPK pads Varying thickness and resistivity
    200,
    # # HPK pads Varying metal widths
    # 200,
]

saveName_list = [
    # Varying resistivity and capacitance
    "HPK_Amplitude_vs_x_ResCap",
    # HPK Varying thickness
    "HPK_Amplitude_vs_x_thickness",
    # KOJI Varying thickness
    "Koji_Amplitude_vs_x_thickness",
    # BNL and HPK Varying metal widths
    "BNL_and_HPK_Amplitude_vs_x_MetalWidth",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_Amplitude_vs_x_thicknessRes",
    # # HPK pads Varying metal widths
    # "HPK_Pads_Amplitude_vs_x_MetalWidth",
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "AmplitudeVsX/")

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

    legend = TLegend(legX1, 1-pad_margin-legend_height-0.03, legX2, 1-pad_margin-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)

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
    haxis.GetYaxis().SetTitle("MPV signal amplitude [mV]")
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    xlimit = 0
    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, ylength-10, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
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
                vertical_line.DrawLine(center-swidth/2., ymin, center-swidth/2., ylength-10)
                vertical_line.DrawLine(center+swidth/2., ymin, center+swidth/2., ylength-10)

    plotfile = []
    list_amplitude_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Amplitude/AmplitudeVsX_tight.root"
        inFile = TFile(inName,"READ")
        hAmp = inFile.Get("AmplitudeNoSum")

        plotfile.append(inFile)
        list_amplitude_vs_x.append(hAmp)

    if treat_as_2x2:
        ref_idx = sensors.index(sensor_reference)
        list_2x2 = [list_amplitude_vs_x.pop(ref_idx)]
        moved_2x2 = mf.move_distribution(list_2x2, -0.025)
        list_3x2 = list_amplitude_vs_x
        moved_3x2 = mf.move_distribution(list_3x2, -0.250)
        list_amplitude_vs_x = moved_3x2[:ref_idx] + moved_2x2 + moved_3x2[ref_idx:]

    pruned_amplitude_vs_x = mf.same_limits_compare(list_amplitude_vs_x, xlimit=xlimit)
    for i, hist in enumerate(pruned_amplitude_vs_x):
        hist.SetLineWidth(3)
        hist.SetLineColor(colors[i])

        lengendEntry = legend.AddEntry(hist, tag[i])
        # lengendEntry.SetTextAlign(22)
        hist.Draw("hist same")

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()

    # sensor_prod="HPK production"
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
    legend.Clear()
    haxis.Delete()
