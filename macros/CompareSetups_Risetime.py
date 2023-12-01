from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
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
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
# parser.add_option('-y','--ylength', dest='ylength', default = 999, help="Max Risetime value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)
colors = myStyle.GetColors(True)

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
    "HPK_Risetime_vs_x_ResCap",
    # HPK Varying thickness
    "HPK_Risetime_vs_x_thickness",
    # KOJI Varying thickness
    "Koji_Risetime_vs_x_thickness",
    # HPK pads Varying thickness and resistyvity
    "HPK_Padds_Risetime_vs_x_thicknessRes",
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "RisetimeVsX/")

ymin = 1
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):
    sensor_reference = sensors[0]

    yLegend = 0.026*len(sensors)
    legend = TLegend(2*pad_margin+0.065, 1-pad_margin-0.2-yLegend, 1-pad_margin-0.065, 1-pad_margin-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)

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
    haxis.GetYaxis().SetTitle("Risetime [ps]")
    # haxis.GetYaxis().SetTitleOffset(1)
    haxis.SetLineWidth(3)
    haxis.GetYaxis().SetRangeUser(ymin, ylength)

    infile_reference = TFile("../output/%s/%s_Analyze.root"%(sensor_reference, sensor_reference),"READ")
    geometry = myStyle.GetGeometry(sensor_reference)
    boxes = getStripBox(infile_reference, ymin, ylength-30, pitch = geometry["pitch"]/1000.0)
    if ("500x500" not in sensor_reference) and ("pad" not in sensor_reference):
        boxes = boxes[1:len(boxes)-1]
    for box in boxes:
        box.Draw()

    plotfile = []
    list_risetime_vs_x = []
    for i, sname in enumerate(sensors):
        inName = "../output/"+sname+"/Risetime/RisetimeVsX_tight.root"
        inFile = TFile(inName,"READ")
        hRisetime = inFile.Get("Risetime")
        hRisetime.SetLineWidth(3)
        hRisetime.SetLineColor(colors[i*2])

        lengendEntry = legend.AddEntry(hRisetime, tag[i])
        plotfile.append(inFile)
        list_risetime_vs_x.append(hRisetime)

    pruned_risetime_vs_x = mf.same_limits_compare(list_risetime_vs_x)
    for hist in pruned_risetime_vs_x:
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
