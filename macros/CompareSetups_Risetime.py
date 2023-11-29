from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
from myFunctions import get_legend_comparation_plots

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 999, help="Max Risetime value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
# ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)

os.makedirs("../output/compare/", exist_ok=True)
#Make final plots

sensors_list = [
    # varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistyvity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
]

tagVar_list = [
    # varying resistivity and capacitance
    ["resistivityNumber", "capacitance"],
    # HPK Varying thickness
    ["thickness"],
    # KOJI Varying thickness
    ["thickness"],
    # HPK pads Varying thickness and resistyvity
    ["thickness", "resistivityNumber"]
]

ylength_list = [
    # varying resistivity and capacitance
    1199,
    # HPK Varying thickness
    999,
    # KOJI Varying thickness
    999,
    # HPK pads Varying thickness and resistyvity
    999,
]

saveName_list = [
    # varying resistivity and capacitance
    "../output/compare/HPK_Risetime_vs_x_ResCap",
    # HPK Varying thickness
    "../output/compare/HPK_Risetime_vs_x_thickness",
    # KOJI Varying thickness
    "../output/compare/Koji_Risetime_vs_x_thickness",
    # HPK pads Varying thickness and resistyvity
    "../output/compare/HPK_Padds_Risetime_vs_x_thicknessRes",
]


for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    yLegend = 0.026*len(sensors)
    legend = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.2-yLegend,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)

    hname = "Risetime"
    ymin = 1

    sensor_prod="test"
    if ("BNL" in sensors[0]):
        sensor_prod = "BNL Production"
    else:
        sensor_prod = "HPK Production"

    if ("KOJI" in sensors[0]):
        xlength = 0.25

    tag = get_legend_comparation_plots(sensors, tagVars)

    totalRisetime_vs_x = TH1F("htemp","",1,-xlength,xlength)
    totalRisetime_vs_x.Draw("AXIS")
    totalRisetime_vs_x.SetStats(0)
    totalRisetime_vs_x.SetTitle("")
    totalRisetime_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    totalRisetime_vs_x.GetYaxis().SetTitle("Risetime [ps]")
    totalRisetime_vs_x.GetYaxis().SetTitleOffset(1)
    totalRisetime_vs_x.SetLineWidth(3)
    totalRisetime_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

    inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[0],sensors[0]),"READ")
    # shift = inputfile.Get("stripBoxInfo03").GetMean(1)
    # boxes = getStripBox(inputfile,ymin,ylength-60.0,False, 18, True, shift)
    # for box in boxes[1:len(boxes)-1]:
    #     box.Draw()
    geometry = myStyle.GetGeometry(sensors[0])
    boxes = getStripBox(inputfile,ymin,ylength- 30,False, 18, True, pitch = geometry["pitch"]/1000.0)
    # boxes = getStripBox(inputfile,ymin,ylength- 30,False, 18, True, shift)
    if ("500x500" not in sensors[0]):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    plotfile = []
    plotList_Risetime_vs_x = []
    for i in range(len(sensors)):
        plotfile.append(TFile("../output/"+sensors[i]+"/Risetime/RisetimeVsX_tight.root","READ"))
        plotList_Risetime_vs_x.append(plotfile[i].Get(hname))
        plotList_Risetime_vs_x[i].SetLineWidth(3)
        plotList_Risetime_vs_x[i].SetLineColor(colors[i*2])
        plotList_Risetime_vs_x[i].Draw("hist same")
        legend.AddEntry(plotList_Risetime_vs_x[i], tag[i])

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)
    totalRisetime_vs_x.Draw("AXIS same")
    # myStyle.SensorInfoSmart(dataset)

    # canvas.SaveAs("../HPK_Risetime_vs_x_ResCap.png")
    # canvas.SaveAs("../HPK_Risetime_vs_x_thickness.png")
    # canvas.SaveAs("../Koji_Risetime_vs_x_thickness.png")
    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    for i in range(len(plotfile)):
        plotfile[i].Close()
    inputfile.Close()
    canvas.Clear()
    legend.Clear()
