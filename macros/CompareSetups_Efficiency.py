from ROOT import TFile,TTree,TLine,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
from  builtins import any
from myFunctions import get_legend_comparation_plots

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.75, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 1.4, help="Max Efficiency in final plot")
options, args = parser.parse_args()
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)

os.makedirs("../output/compare/", exist_ok=True)

sensors_list = [
    # BNL and HPK sensors - different metal widths
    [ "BNL_50um_1cm_450um_W3051_2_2_170V","BNL_50um_1cm_400um_W3051_1_4_160V" , "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK pads Varying thickness and resistyvity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
]

tagVar_list = [
    # BNL and HPK sensors - different metal widths
    ["width"],
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    #HPK Varying thickness
    ["thickness"],
    # HPK pads Varying thickness and resistyvity
    ["thickness", "resistivityNumber"]
]

saveName_list = [
    # BNL and HPK sensors - different metal widths
    "../output/compare/BNL_and_HPK_Efficiency_vs_x_MetalWidth",
    #Varying resistivity and capacitance
    "../output/compare/HPK_Efficiency_vs_x_ResCap",
    #HPK Varying thickness
    "../output/compare/HPK_efficiency_vs_x_thickness",
    # HPK pads Varying thickness and resistyvity
    "../output/compare/HPK_Pads_efficiency_vs_x_ThicknessRes"
]

#Make final plots
for sensors, tagVars, saveName in zip(sensors_list, tagVar_list, saveName_list):
    hname = "hefficiency_vs_x_twoStrip_numerator_tight"
    ymin = 0.01

    xlength = float(options.xlength)
    sensor_prod="BNL & HPK Production"
    if ("BNL" in sensors[0]):
        sensor_prod = "BNL & HPK Production"
    else:
        sensor_prod = "HPK Production"

    if ("KOJI" in sensors[0]):
        xlength = 0.35

    if ("500x500" in sensors[0]):
        xlength = 0.8

    ylength = 1.3 + 0.1*len(sensors)

    yLegend = 0.026*len(sensors)
    legend2 = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.2-yLegend,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.03)
    legend2.SetBorderSize(1)
    legend2.SetLineColor(kBlack)
    legend2.SetTextFont(myStyle.GetFont())
    legend2.SetTextSize(myStyle.GetSize()-4)
    
    tag = get_legend_comparation_plots(sensors,tagVars)

    totalEfficiency_vs_x = TH1F("htemp","",1,-xlength,xlength)
    totalEfficiency_vs_x.Draw("AXIS")
    totalEfficiency_vs_x.SetStats(0)
    totalEfficiency_vs_x.SetTitle("")
    totalEfficiency_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    totalEfficiency_vs_x.GetYaxis().SetTitle("Two-strip efficiency")
    if ("500x500" in sensors[0]):
        totalEfficiency_vs_x.GetYaxis().SetTitle("Two-channel efficiency")
    totalEfficiency_vs_x.SetLineWidth(3)
    totalEfficiency_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

    inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[len(sensors)-2],sensors[len(sensors)-2]),"READ")
    # shift = inputfile.Get("stripBoxInfo03").GetMean(1)
    geometry = myStyle.GetGeometry(sensors[0])
    boxes = getStripBox(inputfile,ymin,ylength - 0.4,False, 18, True, pitch = geometry["pitch"]/1000.0)

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
    plotList_Efficiency_vs_x = []
    for i in range(len(sensors)):
        plotfile.append(TFile("../output/"+sensors[i]+"/Efficiency/EfficiencyVsX_tight.root","READ"))
        plotList_Efficiency_vs_x.append(plotfile[i].Get(hname))
        plotList_Efficiency_vs_x[i].SetLineWidth(3)
        if("thickness" in tag[0]):
            plotList_Efficiency_vs_x[i].SetLineColor(colors[i*2])
        else:
            plotList_Efficiency_vs_x[i].SetLineColor(colors[i+1])
        plotList_Efficiency_vs_x[i].Draw("hist same")
        legend2.AddEntry(plotList_Efficiency_vs_x[i], tag[i])

    horizontal_line = TLine(-xlength, 1, xlength, 1)
    horizontal_line.SetLineWidth(3)
    horizontal_line.SetLineColor(1)
    horizontal_line.SetLineStyle(9)
    # horizontal_line.SetLineColorAlpha(colors[2*i],0.4)
    horizontal_line.DrawClone("same")

    legendHeader = tag[-1]
    legend2.SetHeader(legendHeader, "C")
    
    legend2.Draw()
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)
    totalEfficiency_vs_x.Draw("AXIS same")

    # canvas.SaveAs("../BNL_and_HPK_Efficiency_vs_x_MetalWidth.png")
    # canvas.SaveAs("../HPK_Efficiency_vs_x_ResCap.png")
    # canvas.SaveAs("../hpk_efficiency_vs_x_thickness.png")
    # canvas.SaveAs("../BNL_and_HPK_Amplitude_vs_x_MetalWidth.png")
    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    for i in range(len(plotfile)):
        plotfile[i].Close()
    inputfile.Close()
    canvas.Clear()
    legend2.Clear()

# BNL sensors - different metal widths
# sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V"]
# tag = ["100 #mum strip width", "50 #mum strip width]

# HPK sensors - different metal widths
# sensors = ["HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V"]
# tag = ["W8 (17,2): 50M C600 50T", "W8 (18,2): 100M C600 50T", "W9 (15,2): 50M E600 20T", "W9 (14,2): 100M E600 20T"]
