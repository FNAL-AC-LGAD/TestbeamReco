from ROOT import TFile,TLine,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite, kBlack
import os
# import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle
from  builtins import any
from myFunctions import get_legend_comparation_plots

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.25, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 120, help="Max Amp value in final plot")
options, args = parser.parse_args()
xlength = float(options.xlength)
ylength = float(options.ylength)
colors = myStyle.GetColors(True)

canvas = TCanvas("cv","cv",1000,800)

os.makedirs("../output/compare/", exist_ok=True)



sensors_list = [ # Varying resistivity and capacitance
                ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
                #HPK Varying thickness
                ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"],
                # KOJI Varying thickness
                ["HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"],
                # BNL and HPK Varying metal widths
                ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"]
        ]
tagVar_list = [ # Varying resistivity and capacitance
             ["resistivityNumber", "capacitance"],
                #HPK Varying thickness
            ["thickness"],
                # KOJI Varying thickness
            ["thickness"],
                # BNL and HPK Varying metal widths
            ["width"]
        ]

ylength_list = [ # Varying resistivity and capacitance 
                190,
                #HPK Varying thickness
                170,
                # KOJI Varying thickness
                100,
                # BNL and HPK Varying metal widths
                100
        ]

saveName_list = [ # Varying resistivity and capacitance 
                "../output/compare/HPK_Amplitude_vs_x_ResCap",
                #HPK Varying thickness
                "../output/compare/HPK_Amplitude_vs_x_thickness",
                # KOJI Varying thickness
                "../output/compare/Koji_Amplitude_vs_x_thicknessg",
                # BNL and HPK Varying metal widths
                "../output/compare/BNL_and_HPK_Amplitude_vs_x_MetalWidth"
        ]

#Make final plots
# Varying resistivity and capacitance
# sensors = ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"]
# # tag = ["400 #Omega/sq 240 pF/mm2 (W4)", "1600 #Omega/sq 240 pF/mm2 (W2)", "400 #Omega/sq 600 pF/mm2 (W8)", "1600 #Omega/sq 600 pF/mm2 (W5)"]
# tag = get_legend_comparation_plots(sensors, ["resistivityNumber", "capacitance"])
# ylength = 160
# saveName = "../HPK_Amplitude_vs_x_ResCap.png"

# HPK Varying thickness
# sensors = ["HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V"]
# # tag = ["50 #mum active thickness", "20 #mum active thickness"]
# tag = get_legend_comparation_plots(sensors, ["thickness"])
# ylength = 160
# saveName = "../HPK_Amplitude_vs_x_thickness.png"

# KOJI Varying thickness
# sensors = ["HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"]
# #tag = ["50 #mum active thickness", "20 #mum active thickness"]
# tag = get_legend_comparation_plots(sensors, ["thickness"])
# ylength = 120
# xlength = 0.25
# saveName = "../Koji_Amplitude_vs_x_thickness.png"

# BNL and HPK Varying metal widths
# sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"]
# # tag = ["BNL 100 #mum srip width", "BNL 50 #mum strip width", "HPK 50 #mum strip width", "HPK 100 #mum strip width"]
# tag = get_legend_comparation_plots(sensors, ["width"])
# ylength = 100
# saveName = "../BNL_and_HPK_Amplitude_vs_x_MetalWidth.png"

hname = "Amplitude"
ymin = 1


for sensors, tagVars, ylength, saveName in zip(sensors_list, tagVar_list, ylength_list, saveName_list):

    
    yLegend = 0.026*len(sensors)
    legend2 = TLegend(2*myStyle.GetMargin()+0.065,1-myStyle.GetMargin()-0.2-yLegend,1-myStyle.GetMargin()-0.065,1-myStyle.GetMargin()-0.03)
    legend2.SetBorderSize(1)
    legend2.SetLineColor(kBlack)
    legend2.SetTextFont(myStyle.GetFont())
    legend2.SetTextSize(myStyle.GetSize()-4)

    sensor_prod="BNL & HPK Production"
    if ("BNL" in sensors[0]):
       sensor_prod = "BNL & HPK Production"
    else:
       sensor_prod = "HPK Production"
    if ("KOJI" in sensors[0]):
        xlength = 0.25

    tag = get_legend_comparation_plots(sensors, tagVars)
     
    totalAmplitude_vs_x = TH1F("htemp","",1,-xlength,xlength)
    totalAmplitude_vs_x.Draw("AXIS")
    totalAmplitude_vs_x.SetStats(0)
    totalAmplitude_vs_x.SetTitle("")
    totalAmplitude_vs_x.GetXaxis().SetTitle("Track x position [mm]")
    totalAmplitude_vs_x.GetYaxis().SetTitle("MPV signal amplitude [mV]")
    totalAmplitude_vs_x.SetLineWidth(3)
    totalAmplitude_vs_x.GetYaxis().SetRangeUser(ymin, ylength)


    inputfile = TFile("../output/%s/%s_Analyze.root"%(sensors[len(sensors)-2],sensors[len(sensors)-2]),"READ")
    shift = inputfile.Get("stripBoxInfo03").GetMean(1)
    boxes = getStripBox(inputfile,ymin,ylength- 30,False, 18, True, shift)
    for box in boxes[1:len(boxes)-1]:
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
    plotList_amplitude_vs_x = []
    for i in range(len(sensors)):
        plotfile.append(TFile("../output/"+sensors[i]+"/Amplitude/AmplitudeVsX_tight.root","READ"))
        plotList_amplitude_vs_x.append(plotfile[i].Get(hname))
        plotList_amplitude_vs_x[i].SetLineWidth(3)
        if("thickness" in tagVars[0]):
            plotList_amplitude_vs_x[i].SetLineColor(colors[i*2])
        else:
            plotList_amplitude_vs_x[i].SetLineColor(colors[i+1])
        plotList_amplitude_vs_x[i].Draw("hist same")
        lengendEntry = legend2.AddEntry(plotList_amplitude_vs_x[i], tag[i])
        # lengendEntry.SetTextAlign(22)

# legend2.AddEntry(plotList_amplitude_vs_x, "")


    legend2.Draw()
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod)
    totalAmplitude_vs_x.Draw("AXIS same")

    # legendHeader = "Varying"
    # for j in range(len(tagVars)):
        # legendHeader +=  " " + tagVars[j]
    # legendHeader = "#bf{%s}"%legendHeader
    legendHeader = tag[-1]
    legend2.SetHeader(legendHeader, "C")
# myStyle.SensorInfoSmart(dataset)

# canvas.SaveAs("../HPK_Amplitude_vs_x_ResCap.png")
# canvas.SaveAs("../HPK_Amplitude_vs_x_thickness.png")
# canvas.SaveAs("../Koji_Amplitude_vs_x_thickness.png")
# canvas.SaveAs("../BNL_and_HPK_Amplitude_vs_x_MetalWidth.png")
    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    for i in range(len(plotfile)):
        plotfile[i].Close()
    inputfile.Close()
    canvas.Clear()
    legend2.Clear()
