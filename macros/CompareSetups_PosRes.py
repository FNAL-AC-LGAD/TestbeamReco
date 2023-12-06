from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
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
colors = myStyle.GetColors(True)

sensors_list = [
    # Varying thickness
    ["HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
    # Varying thickness KOJI
    ["HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V"],
    # HPK pads Varying thickness and resistivity
    ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V"],
]

tagVar_list = [
    # Varying thickness
    ["thickness"],
    # Varying thickness KOJI
    ["thickness"],
    # HPK pads Varying thickness and resistivity
    ["thickness", "resistivityNumber"],
]

saveName_list = [
    # Varying thickness
    "HPK_PosResolution_vs_x_thickness",
    # Varying thickness KOJI
    "Koji_PosResolution_vs_x_thickness",
    # HPK pads Varying thickness and resistivity
    "HPK_Pads_PosResolution_vs_x_thicknessRes",
]

xlength_list = [
    # Varying thickness
    1.5,
    # Varying thickness KOJI
    0.35,
    # HPK pads Varying thickness and resistivity
    0.8,
]

ylength_list = [
    # Varying thickness
    250,
    # Varying thickness KOJI
    90,
    # HPK pads Varying thickness and resistivity
    200,
]

yoffset_list = [
    # Varying thickness
    20,
    # Varying thickness KOJI
    10,
    # HPK pads Varying thickness and resistivity
    10,
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "ResolutionPosVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, saveName, xlength, ylength, yoffset in zip(sensors_list, tagVar_list, saveName_list, xlength_list, ylength_list, yoffset_list):
    sensor_reference = sensors[0]

    yLegend = 0.026*len(sensors)
    legend = TLegend(2*pad_margin+0.065, 1-pad_margin-0.3-yLegend, 1-pad_margin-0.065, 1-pad_margin-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetNColumns(1)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
    # legend.SetBorderSize(0)
    # legend.SetFillColor(kWhite)

    tag = mf.get_legend_comparation_plots(sensors, tagVars)

    haxis = TH1F("htemp","",1,-xlength,xlength)
    haxis.Draw("AXIS")
    haxis.SetStats(0)
    haxis.SetTitle("")
    haxis.GetXaxis().SetTitle("Track x position [mm]")
    haxis.GetYaxis().SetTitle("Position resolution [#mum]")
    haxis.SetLineWidth(1)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    pitch = geometry["pitch"]
    boxes = getStripBox(infile_reference, ymin, ylength-yoffset, pitch = pitch/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    binary_readout_res_sensor = TLine(-xlength, pitch/TMath.Sqrt(12), xlength, pitch/TMath.Sqrt(12))
    binary_readout_res_sensor.SetLineWidth(3)
    binary_readout_res_sensor.SetLineStyle(7)
    binary_readout_res_sensor.SetLineColor(kBlack)
    binary_readout_res_sensor.Draw("same")
    legend.AddEntry(binary_readout_res_sensor, "Pitch / #sqrt{12}","l")

    plotfile = []
    list_OneStrip_vs_x = []
    list_TwoStrip_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Resolution_Pos/PositionResVsX_tight.root"
        inFile = TFile(inName,"READ")
        hOneStrip = inFile.Get("h_one_strip")
        hTwoStrip = inFile.Get("track_twoStrip_tight")

        hOneStrip.Draw("P same")
        hOneStrip.SetLineStyle(1)
        hOneStrip.SetMarkerStyle(33)
        hOneStrip.SetMarkerSize(3)
        hOneStrip.SetMarkerColor(colors[i*2])
        legend.AddEntry(hOneStrip, tag[i]+' - Exactly one strip', "P")

        hTwoStrip.SetLineWidth(3)
        hTwoStrip.SetLineColor(colors[i*2])
        legend.AddEntry(hTwoStrip, tag[i]+' - Two strip')

        plotfile.append(inFile)
        list_OneStrip_vs_x.append(hOneStrip)
        list_TwoStrip_vs_x.append(hTwoStrip)

    pruned_TwoStrip_vs_x = mf.same_limits_compare(list_TwoStrip_vs_x)
    for hist in pruned_TwoStrip_vs_x:
        hist.Draw("hist same")

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()

    sensor_prod="HPK production"
    if ("BNL" in sensor_reference):
        sensor_prod = "BNL production"
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
