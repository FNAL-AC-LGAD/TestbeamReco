from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack, kGreen, TPaveText 
import os
import langaus
import optparse
from stripBox import getStripBox
import myStyle
import math
from myFunctions import get_legend_comparation_plots

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
os.makedirs("../output/compare/", exist_ok=True)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 150, help="Max TR value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)

sensors_list = [
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # HPK Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # KOJI Varying thickness
    [ "HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistyvity
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
    # HPK pads Varying thickness and resistyvity
    ["thickness", "resistivityNumber"],
]

ylength_list = [
    # Varying resistivity and capacitance
    70,
    # HPK Varying thickness
    160,
    # KOJI Varying thickness
    65,
    # HPK pads Varying thickness and resistyvity
    100,
    # HPK pads Varying metal width 
    # 100
]

saveName_list = [
    # Varying resistivity and capacitance
    "../output/compare/HPK_TimeResolution_vs_x_ResCap",
    # HPK Varying thickness
    "../output/compare/HPK_TimeResolution_vs_x_thickness",
    # KOJI Varying thickness
    "../output/compare/Koji_TimeResolution_vs_x_thickness",
    # HPK pads Varying thickness and resistyvity
    "../output/compare/HPK_Pads_TimeResolution_vs_x_thicknessRes",
    # HPK pads Varying metal width 
    # "../output/compare/HPK_Pads_TimeResolution_vs_x_width"
]

#Make final plots
hname = "Time_DiffW2Tracker"
# hname2 = "jitter_vs_x"
hname2 = "weighted2_jitter"
tag2 = ["Time resolution", "Jitter"]#, "Time resolution - Jitter (quadrature)"]
ymin = 1

for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    xlength = float(options.xlength)
    sensor_prod="test"
    if ("BNL" in sensors[0]):
        sensor_prod = "BNL Production"
    else:
        sensor_prod = "HPK Production"
    if ("KOJI" in sensors[0]):
        xlength = 0.25
        hname2 = "jitter_vs_x"

    if ("500x500" in sensors[0]):
        xlength = 0.8

    legend = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.35,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.25)
    legend.SetNColumns(2)
    # legend.SetBorderSize(1)
    # legend.SetLineColor(kBlack)

    yLegend = 0.026*len(sensors)
    legend2 = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.2-yLegend,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.03)
    # legend2.SetBorderSize(1)
    legend2.SetLineColor(kBlack)
    legend2.SetTextFont(myStyle.GetFont())
    legend2.SetTextSize(myStyle.GetSize()-4)

    tag = get_legend_comparation_plots(sensors, tagVars)

    totalTR_vs_x = TH1F("htemp","",1,-xlength,xlength)
    totalTR_vs_x.Draw("AXIS")
    totalTR_vs_x.SetStats(0)
    totalTR_vs_x.SetTitle("")
    totalTR_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    totalTR_vs_x.GetYaxis().SetTitle("Time resolution [ps]")
    totalTR_vs_x.SetLineWidth(3)
    totalTR_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

    inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[0],sensors[0]),"READ")
    geometry = myStyle.GetGeometry(sensors[0])
    boxes = getStripBox(inputfile,ymin,ylength- 30,False, 18, True, pitch = geometry["pitch"]/1000.0)
    # boxes = getStripBox(inputfile,ymin,ylength- 30,False, 18, True, shift)
    if ("500x500" not in sensors[0]):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    plotfile = []
    plotfile2 = []
    plotList_TR_vs_x = []
    plotList_TR_vs_x2 = []
    # plotList_TR_vs_x3 = []

    for i in range(len(sensors)):
        plotfile.append(TFile("../output/"+sensors[i]+"/Resolution_Time/TimeDiffVsX_tight.root","READ"))
        plotList_TR_vs_x.append(plotfile[i].Get(hname))
        plotList_TR_vs_x[i].SetLineWidth(3)
        if("thickness" in tag[0]):
            plotList_TR_vs_x[i].SetLineColor(colors[i*2])
        else:
            plotList_TR_vs_x[i].SetLineColor(colors[i+1])
        plotList_TR_vs_x[i].Draw("hist same")
        legend2.AddEntry(plotList_TR_vs_x[i], tag[i])


    # if("thickness" in tag[0]):
    # if("thickness" in tagVars[0]):
    if(("thickness" in tagVars[0]) and ("500x500" not in sensors[0])):
        for i in range(len(sensors)):
            plotfile2.append(TFile("../output/"+sensors[i]+"/Jitter/JitterVsX.root","READ"))
            print("../output/"+sensors[i]+"/Jitter/JitterVsX.root")

            plotList_TR_vs_x2.append(plotfile2[i].Get(hname2))
            # plotList_TR_vs_x3.append(plotList_TR_vs_x2[i].Clone("landau_vs_x"))
            plotList_TR_vs_x2[i].SetLineWidth(3)
            plotList_TR_vs_x2[i].SetLineStyle(2)
            plotList_TR_vs_x2[i].SetLineColor(colors[i*2])
            plotList_TR_vs_x2[i].Draw("hist same")
            for number in range(1, plotList_TR_vs_x2[i].GetXaxis().GetNbins()+1):
                j = plotList_TR_vs_x2[i].GetBinContent(number)
                t = plotList_TR_vs_x[i].GetBinContent(number)
                if (t>=j):
                    l = math.sqrt(t*t - j*j)
                else:
                    l = 0
                # plotList_TR_vs_x3[i].SetBinContent(number, l)

            # plotList_TR_vs_x3[i].SetLineWidth(5)
            # plotList_TR_vs_x3[i].SetLineStyle(3)
            # plotList_TR_vs_x3[i].SetLineColor(colors[i*2])
            # plotList_TR_vs_x3[i].Draw("hist same")
        legend.AddEntry(plotList_TR_vs_x[0], tag2[0])
        legend.AddEntry(plotList_TR_vs_x2[0], tag2[1])
        # legend.AddEntry(plotList_TR_vs_x3[0], tag2[2])
        # legend.SetTextSize(26)
        legendBox = TPaveText(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.03,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.35, "NDC")
        legendBox.SetBorderSize(1)
        legendBox.SetLineColor(kBlack)
        legendBox.SetFillColor(0)
        legendBox.SetFillColorAlpha(0,0.)
        legend.Draw()
        legend2.Draw()
        legendBox.Draw("same")

    else:
        legend2.SetBorderSize(1)
        legend2.Draw()


    legendHeader = tag[-1]
    legend2.SetHeader(legendHeader, "C")
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)
    totalTR_vs_x.Draw("AXIS same")
    # myStyle.SensorInfoSmart(dataset)

    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    for i in range(len(plotfile)):
        plotfile[i].Close()
    for i in range(len(plotfile2)):
        plotfile2[i].Close()
    inputfile.Close()
    canvas.Clear()
    legend.Clear()
    legend2.Clear()
