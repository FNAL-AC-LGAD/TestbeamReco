from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT,kBlack
import ROOT
import os
import optparse
import myStyle
import stripBox
from myFunctions import get_legend_comparation_plots

myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode=True
gROOT.SetBatch( True )
tsize = myStyle.GetSize()

ROOT.gStyle.SetLabelSize(tsize-10,"x")
ROOT.gStyle.SetTitleSize(tsize,"x")
ROOT.gStyle.SetLabelSize(tsize-10,"y")
ROOT.gStyle.SetTitleSize(tsize,"y")
ROOT.gStyle.SetLabelSize(tsize-10,"z")
ROOT.gStyle.SetTitleSize(tsize,"z")

ROOT.gStyle.SetPadRightMargin(2*myStyle.GetMargin())
ROOT.gROOT.ForceStyle()

def getFitFunction(parameters, scale):
    for i,par in enumerate(parameters):
        if i==0:
            fitFunction = "%.6f"%(scale*par)
        else:
            fitFunction += " + %.6f*pow(x - 0.5, %i)"%(scale*par,i)
    return fitFunction

colors = myStyle.GetColors(True)

os.makedirs("../output/compare/", exist_ok=True)

sensor_reco = { "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'recomax': 0.7, 'recoPars':[0.250000, -1.147503, -0.798801, 7.368874, -38.344067]},
                "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'recomax': 0.84, 'recoPars':[0.250000, -0.693443, 0.894506, -9.526453, 38.944962, -58.650584]},
                "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'recomax': 0.71, 'recoPars':[0.250000, -1.162898, 0.988027, -6.238384, 17.134867, -89.438984]},
                "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'recomax': 0.85, 'recoPars':[0.250000, -0.609789, -0.026359, -3.221913, 19.537329, -35.866120]},
                "BNL_50um_1cm_400um_W3051_1_4_160V": {'recomax': 0.78, 'recoPars':[0.250000, -0.718665, -0.139214, 1.987639, -8.425333, -2.053463]},
                "BNL_50um_1cm_450um_W3051_2_2_170V": {'recomax': 0.79, 'recoPars':[0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931]},
                "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'recomax': 0.71, 'recoPars':[0.250000, -1.162898, 0.988027, -6.238384, 17.134867, -89.438984]},
                "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'recomax': 0.7, 'recoPars':[0.250000, -1.164642, 2.136270, -18.028266, 29.883977]}}
               
#Make final plots

sensors_list = [#BNL and HPK sensors - different metal widths
                [ "BNL_50um_1cm_450um_W3051_2_2_170V","BNL_50um_1cm_400um_W3051_1_4_160V" , "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
              # Varying resistivity and capacitance
                ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
              ]


tagVar_list = [#BNL and HPK sensors - different metal widths
               ["width"],
              # Varying resistivity and capacitance
               ["resistivityNumber", "capacitance"]
              ]

saveName_list = [#BNL and HPK sensors - different metal widths
                 "../output/compare/BNL_and_HPK_PosFit_vs_MetalWidth",
                 # Varying resistivity and capacitance
                 "../output/compare/HPK_PosFit_vs_ResCap"
                ]

maxWidth_list = [#BNL and HPK sensors - different metal widths
                 100,
                 # Varying resistivity and capacitance
                 50
                ]

xmax_list = [#BNL and HPK sensors - different metal widths
             0.82,
             # Varying resistivity and capacitance
             0.9
            ]



canvas = TCanvas("cv","cv",1000,800)

pitch = 500 #um
y_scale = 1000 # mm to micron
xmin=0.50
ymin=0.001
ymax=0.33*y_scale



for sensors, tagVars, saveName, maxWidth, xmax in zip(sensors_list, tagVar_list, saveName_list, maxWidth_list, xmax_list):

    sensor_prod="BNL and HPK Production"
    if ("BNL" in sensors[0]):
       sensor_prod = "BNL & HPK Production"
    else:
       sensor_prod = "HPK Production"

    tag = get_legend_comparation_plots(sensors, tagVars)

    temp_hist = TH1F("htemp","", 1, xmin, xmax)
    temp_hist.GetXaxis().SetTitle("Amplitude fraction")
    temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
    temp_hist.GetYaxis().SetTitle("Position [#mum]")
    temp_hist.Draw("axis")

# Add second axis at the right
    right_axis = ROOT.TGaxis(xmax,0.0001,xmax, ymax,0.0001, ymax/pitch,510,"+L")
    right_axis.UseCurrentStyle()
    right_axis.SetTitle("Pitch fraction")
    right_axis.SetLabelSize(myStyle.GetSize()-10)
    right_axis.SetTitleSize(myStyle.GetSize())
    right_axis.SetLabelFont(myStyle.GetFont())
    right_axis.SetTitleFont(myStyle.GetFont())
    right_axis.Draw()

    boxes = stripBox.getStripBoxForRecoFit(maxWidth, pitch, ymax, xmax, xmin)
    for box in boxes:
            box.DrawClone("same")

    for i,item in enumerate(sensors):
        sensor_Geometry = myStyle.GetGeometry(item)
        width = sensor_Geometry['stripWidth']
        horizontal_line = ROOT.TLine(xmin, width/2., xmax, width/2.)
        horizontal_line.SetLineWidth(3)
        horizontal_line.SetLineStyle(9)
        horizontal_line.SetLineColorAlpha(colors[i+1],0.4)
        horizontal_line.DrawClone("same")


    # legend = TLegend(1-myStyle.GetMargin()-0.65,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.05,1-myStyle.GetMargin()-0.05)
# legend.SetBorderSize(0)
# legend.SetFillColor(ROOT.kWhite)
    # legend.SetTextFont(myStyle.GetFont())
    # legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetFillStyle(0)

    
    yLegend = 0.026*len(sensors)
    legend = TLegend(1-myStyle.GetMargin()-0.7,1-myStyle.GetMargin()-0.2-yLegend,1-myStyle.GetMargin()-0.08,1-myStyle.GetMargin()-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)

    fitFunction_list = []
    for i,item in enumerate(sensors):
        fitFunction = getFitFunction(sensor_reco[item]['recoPars'], y_scale)
        recomax_s = sensor_reco[item]['recomax']
        sensor_Geometry = myStyle.GetGeometry(item)

        func1 = TF1("f1%i"%(i),fitFunction,xmin,recomax_s)
        func1.SetLineColor(colors[i+1])
        name = tag[i]
        fitFunction_list.append(func1)
        func1.DrawCopy("same")
        legend.AddEntry(fitFunction_list[-1], name,"L")

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()

    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod, 0.05)
    temp_hist.Draw("same axis")

# canvas.SaveAs("../BNL_and_HPK_PosFit_vs_MetalWidth.png")
# canvas.SaveAs("../HPK_PosFit_vs_ResCap.png")
    canvas.SaveAs(saveName + ".png")
    canvas.SaveAs(saveName + ".pdf")
    canvas.Clear()
    legend.Clear()



# BNL sensors - different metal widths
# sensors = ["BNL_50um_1cm_400um_W3051_1_4_160V", "BNL_50um_1cm_450um_W3051_2_2_170V"]
# maxWidth = 100
# xmax=0.82
# tag = ["100M", "50M"]
# sensor_reco = { "BNL_50um_1cm_400um_W3051_1_4_160V": {'recomax': 0.78, 'recoPars':[0.250000, -0.718665, -0.139214, 1.987639, -8.425333, -2.053463]},
#                 "BNL_50um_1cm_450um_W3051_2_2_170V": {'recomax': 0.79, 'recoPars':[0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931]}}

# # HPK sensors - different metal widths
# sensors = ["HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V"]
# maxWidth = 100
# xmax=0.92
# tag = ["W8 (17,2): 50M C600 50T", "W8 (18,2): 100M C600 50T", "W9 (15,2): 50M E600 20T", "W9 (14,2): 100M E600 20T"]
# sensor_reco = { "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'recomax': 0.71, 'recoPars':[0.250000, -1.162898, 0.988027, -6.238384, 17.134867, -89.438984]},
#                 "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'recomax': 0.7, 'recoPars':[0.250000, -1.164642, 2.136270, -18.028266, 29.883977]},
#                 "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V": {'recomax': 0.91, 'recoPars':[0.250000, -0.644361, -0.277179, 1.641745, -2.680530, 3.051593]},
#                 "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V": {'recomax': 0.81, 'recoPars':[0.250000, -0.555752, -0.084502, -2.616577, 21.159629, -51.815129]}}
