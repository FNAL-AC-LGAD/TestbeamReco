from ROOT import TFile,TTree,TLine,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
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
colors = myStyle.GetColors(True)

sensors_list = [
    # BNL and HPK sensors - different metal widths
    ["BNL_50um_1cm_450um_W3051_2_2_170V","BNL_50um_1cm_400um_W3051_1_4_160V" , "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
]

tagVar_list = [
    # BNL and HPK sensors - different metal widths
    ["width"],
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    #HPK Varying thickness
    ["thickness"],
    # KOJI Varying thickness
    ["thickness"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
]

saveName_list = [
    # BNL and HPK sensors - different metal widths
    "BNL_and_HPK_Efficiency_vs_x_MetalWidth",
    #Varying resistivity and capacitance
    "HPK_Efficiency_vs_x_ResCap",
    #HPK Varying thickness
    "HPK_efficiency_vs_x_thickness",
    # KOJI Varying thickness
    "Koji_efficiency_vs_x_thickness",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_efficiency_vs_x_ThicknessRes",
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "EfficiencyVsX/")

ymin = 0.01
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, saveName in zip(sensors_list, tagVar_list, saveName_list):
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
        xlength = 0.35

    tag = mf.get_legend_comparation_plots(sensors, tagVars)

    ylength = 1.3 + 0.1*len(sensors)

    haxis = TH1F("htemp","",1,-xlength,xlength)
    haxis.Draw("AXIS")
    haxis.SetStats(0)
    haxis.SetTitle("")
    haxis.GetXaxis().SetTitle("Track x position [mm]")
    haxis.GetYaxis().SetTitle("Two-strip efficiency")
    if ("500x500" in sensor_reference):
        haxis.GetYaxis().SetTitle("Two-channel efficiency")
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, ylength-0.4, pitch = geometry["pitch"]/1000.0)
    for box in boxes:
        box.Draw()

    # Draw dotted line for 100 micron strip width
    if(any("100M" in iter for iter in sensors)):
        if(any("50M" in iter for iter in sensors)):
            for i in range(7):
                vertical_line = TLine((i-3)*0.5-0.05, 0, (i-3)*0.5-0.05, 1)
                vertical_line.SetLineWidth(2)
                vertical_line.SetLineColor(14)
                vertical_line.SetLineColorAlpha(14,0.4)
                vertical_line.SetLineStyle(9)
                vertical_line.DrawClone("same")

                vertical_line2 = TLine((i-3)*0.5+0.05, 0, (i-3)*0.5+0.05, 1)
                vertical_line2.SetLineWidth(2)
                vertical_line2.SetLineColor(14)
                vertical_line2.SetLineColorAlpha(14,0.4)
                vertical_line2.SetLineStyle(9)
                vertical_line2.DrawClone("same")

    plotfile = []
    list_efficiency_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Efficiency/EfficiencyVsX_tight.root"
        inFile = TFile(inName,"READ")
        hEff = inFile.Get("hefficiency_vs_x_twoStrip_numerator_tight")
        hEff.SetLineWidth(3)
        if("thickness" in tagVars[0]): # Check this
            hEff.SetLineColor(colors[i*2])
        else:
            hEff.SetLineColor(colors[i+1])
        legend2.AddEntry(hEff, tag[i])

        plotfile.append(inFile)
        list_efficiency_vs_x.append(hEff)

    pruned_efficiency_vs_x = mf.same_limits_compare(list_efficiency_vs_x)
    for hist in pruned_efficiency_vs_x:
        hist.Draw("hist same")

    horizontal_line = TLine(-xlength, 1, xlength, 1)
    horizontal_line.SetLineWidth(3)
    horizontal_line.SetLineColor(1)
    horizontal_line.SetLineStyle(9)
    # horizontal_line.SetLineColorAlpha(colors[2*i],0.4)
    horizontal_line.DrawClone("same")

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
