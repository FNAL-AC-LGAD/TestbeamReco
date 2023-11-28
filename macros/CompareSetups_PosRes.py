from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle
from myFunctions import get_legend_comparation_plots

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

os.makedirs("../output/compare/", exist_ok=True)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 200, help="Max Amp value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)
canvas = TCanvas("cv","cv",1000,800)



sensors_list = [
    # Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # Varying thickness KOJI
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"]
]

saveName_list = [
    # Varying thickness
    "../output/compare/HPK_PosResolution_vs_x_thickness",
    # Varying thickness KOJI
    "../output/compare/Koji_PosResolution_vs_x_thickness"
]

xlength_list = [
    # Varying thickness
    1.5,
    # Varying thickness KOJI
    0.35
]

ylength_list = [
    # Varying thickness
    250,
    # Varying thickness KOJI
    90
]


pitch_list = [
    # Varying thickness
    500,
    # Varying thickness KOJI
    80
]

yoffset_list = [
    # Varying thickness
    20,
    # Varying thickness KOJI
    10
]



for sensors, saveName, xlength, ylength, pitch, yoffset in zip(sensors_list,saveName_list, xlength_list, ylength_list, pitch_list, yoffset_list):

    plotfile = []
    inputfile = []
    hists_oneStrip = []
    hists_twoStrip = []
    shift = []
    ymin = 1
    
    tag = get_legend_comparation_plots(sensors, ["thickness"])

    for i in range(len(sensors)):
        plotfile.append(TFile("../output/"+sensors[i]+"/Resolution_Pos/PositionResVsX_tight.root","READ"))
        inputfile.append(TFile("../output/"+sensors[i]+"/"+sensors[i]+"_Analyze.root","READ"))
        shift.append(inputfile[i].Get("stripBoxInfo03").GetMean(1))
        hists_oneStrip.append(plotfile[i].Get("h_one_strip"))
        hists_twoStrip.append(plotfile[i].Get("track_twoStrip_tight"))

    sensor_prod="test"
    if ("BNL" in sensors[0]):
       sensor_prod = "BNL Production"
    else:
       sensor_prod = "HPK Production"

    XRes_vs_x = TH1F("htemp","",1,-xlength,xlength)
    XRes_vs_x.Draw("hist")
    XRes_vs_x.SetStats(0)
    XRes_vs_x.SetTitle("")
    XRes_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    XRes_vs_x.GetYaxis().SetTitle("Position resolution [um]")
    XRes_vs_x.SetLineWidth(2)
    XRes_vs_x.GetXaxis().SetRangeUser(-xlength, xlength)
    XRes_vs_x.GetYaxis().SetRangeUser(ymin, ylength)

    boxes = getStripBox(inputfile[0],ymin,ylength-yoffset,False, 18, True, shift[0])
    for box in boxes[1:len(boxes)-1]:
       box.Draw()
    XRes_vs_x.Draw("AXIS same")
    XRes_vs_x.Draw("hist same")

    # legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.1,1-myStyle.GetMargin()-0.05)
    yLegend = 0.026*len(sensors)
    legend = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.3-yLegend,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetNColumns(1)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetBorderSize(0)
# legend.SetFillColor(kWhite)

    binary_readout_res_sensor = TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
    binary_readout_res_sensor.SetLineWidth(3)
    binary_readout_res_sensor.SetLineStyle(7)
    binary_readout_res_sensor.SetLineColor(kBlack) #kGreen+2 #(TColor.GetColor(136,34,85))
    binary_readout_res_sensor.Draw("same")
    legend.AddEntry(binary_readout_res_sensor, "Pitch / #sqrt{12}","l")

    for i in range(len(hists_twoStrip)):
        hists_twoStrip[i].Draw("hist same")
        hists_twoStrip[i].SetLineWidth(3)
        legend.AddEntry(hists_twoStrip[i],tag[i]+' - Two strip')
        hists_twoStrip[i].SetLineColor(colors[i*2])

    for i in range(len(hists_oneStrip)):
        hists_oneStrip[i].Draw("P same")
        hists_oneStrip[i].SetLineStyle(1)
        hists_oneStrip[i].SetMarkerStyle(33)
        hists_oneStrip[i].SetMarkerSize(3)
        legend.AddEntry(hists_oneStrip[i],tag[i]+' - Exactly one strip', "P")
        hists_oneStrip[i].SetMarkerColor(colors[i*2])

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()
    XRes_vs_x.SetMaximum(ylength)

    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)
    XRes_vs_x.Draw("AXIS same")
# myStyle.SensorInfoSmart(dataset)

# canvas.SaveAs("../HPK_PosResolution_vs_x_thickness.png")
# canvas.SaveAs("../Koji_PosResolution_vs_x_thickness.png")
    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    for i in range(len(plotfile)):
        plotfile[i].Close()
        inputfile[i].Close()
    canvas.Clear()
    legend.Clear()
