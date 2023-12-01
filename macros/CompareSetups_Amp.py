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
colors = myStyle.GetColors(True)

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
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
]

tagVar_list = [
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    # HPK Varying thickness
    ["thickness"],
    # KOJI Varying thickness
    ["thickness"],
    # BNL and HPK Varying metal widths
    ["width"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
]

ylength_list = [
    # Varying resistivity and capacitance
    190,
    # HPK Varying thickness
    170,
    # KOJI Varying thickness
    100,
    # BNL and HPK Varying metal widths
    100,
    # HPK pads Varying thickness and resistivity
    200,
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
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "AmplitudeVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    sensor_reference = sensors[0]

    yLegend = 0.026*len(sensors)
    legend2 = TLegend(2*pad_margin+0.065, 1-pad_margin-0.2-yLegend, 1-pad_margin-0.065, 1-pad_margin-0.03)
    legend2.SetBorderSize(1)
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
    haxis.GetYaxis().SetTitle("MPV signal amplitude [mV]")
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, ylength-30, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    # Draw dotted line for 100 micron strip width
    if(any("100M" in iter for iter in sensors)):
        if(any("50M" in iter for iter in sensors)):
            for i in range(1,6):
                vertical_line = TLine((i-3)*0.5-0.05, 0, (i-3)*0.5-0.05, ylength-10)
                vertical_line.SetLineWidth(2)
                vertical_line.SetLineColor(14)
                vertical_line.SetLineColorAlpha(14,0.4)
                vertical_line.SetLineStyle(9)
                vertical_line.DrawClone("same")

                vertical_line2 = TLine((i-3)*0.5+0.05, 0, (i-3)*0.5+0.05, ylength-10)
                vertical_line2.SetLineWidth(2)
                vertical_line2.SetLineColor(14)
                vertical_line2.SetLineColorAlpha(14,0.4)
                vertical_line2.SetLineStyle(9)
                vertical_line2.DrawClone("same")

    plotfile = []
    list_amplitude_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Amplitude/AmplitudeVsX_tight.root"
        inFile = TFile(inName,"READ")
        hAmp = inFile.Get("AmplitudeNoSum")
        hAmp.SetLineWidth(3)
        if("thickness" in tagVars[0]):
            hAmp.SetLineColor(colors[i*2])
        else:
            hAmp.SetLineColor(colors[i+1])

        lengendEntry = legend2.AddEntry(hAmp, tag[i])
        # lengendEntry.SetTextAlign(22)
        plotfile.append(inFile)
        list_amplitude_vs_x.append(hAmp)

    pruned_amplitude_vs_x = mf.same_limits_compare(list_amplitude_vs_x)
    for hist in pruned_amplitude_vs_x:
        hist.Draw("hist same")

    legendHeader = tag[-1]
    legend2.SetHeader(legendHeader, "C")
    legend2.Draw()

    sensor_prod="HPK production"
    if ("BNL" in sensor_reference):
        sensor_prod = "BNL & HPK production"
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)

    haxis.Draw("AXIS same")

    canvas.SaveAs("%s%s.png"%(outdir, saveName))
    canvas.SaveAs("%s%s.pdf"%(outdir, saveName))

    for file in plotfile:
        file.Close()
    infile_reference.Close()
    canvas.Clear()
    legend2.Clear()
    haxis.Delete()
