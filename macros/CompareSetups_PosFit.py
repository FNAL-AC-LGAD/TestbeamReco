from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT,kBlack
import ROOT
import os
import optparse
import myStyle
import stripBox
import myFunctions as mf

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
myStyle.ForceStyle()
marginR = 2*myStyle.GetMargin()
myStyle.ChangeMargins(mright=marginR)

tsize = myStyle.GetSize()

# ROOT.gStyle.SetLabelSize(tsize-10,"x")
# ROOT.gStyle.SetTitleSize(tsize,"x")
# ROOT.gStyle.SetLabelSize(tsize-10,"y")
# ROOT.gStyle.SetTitleSize(tsize,"y")
# ROOT.gStyle.SetLabelSize(tsize-10,"z")
# ROOT.gStyle.SetTitleSize(tsize,"z")

ROOT.gROOT.ForceStyle()

def getFitFunction(parameters, scale):
    for i,par in enumerate(parameters):
        if i==0:
            fitFunction = "%.6f"%(scale*par)
        else:
            fitFunction += " + %.6f*pow(x - 0.5, %i)"%(scale*par,i)
    return fitFunction

sensor_reco = {
    # 4th degree poly
    # "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'recomax': 0.69, 'recoPars':[0.250000, -1.102187, -2.496727, 25.676521, -97.950055]},
    # 5th degree poly
    "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V": {'recomax': 0.69, 'recoPars':[0.250000, -1.113364, -1.909585, 15.749963, -30.768253, -157.913623]},
    "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V": {'recomax': 0.84, 'recoPars':[0.250000, -0.693443, 0.894506, -9.526453, 38.944962, -58.650584]},
    "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V": {'recomax': 0.71, 'recoPars':[0.250000, -1.162898, 0.988027, -6.238384, 17.134867, -89.438984]},
    "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V": {'recomax': 0.85, 'recoPars':[0.250000, -0.623392, 0.074807, -3.237477, 17.697710, -31.574229]},
    "BNL_50um_1cm_400um_W3051_1_4_160V": {'recomax': 0.78, 'recoPars':[0.250000, -0.718665, -0.139214, 1.987639, -8.425333, -2.053463]},
    "BNL_50um_1cm_450um_W3051_2_2_170V": {'recomax': 0.79, 'recoPars':[0.250000, -0.779099, 0.955034, -12.717777, 62.983960, -115.093931]},
    "BNL_50um_1cm_450um_W3052_2_4_185V": {'recomax': 0.79, 'recoPars':[0.250000, -0.810944, 1.960402, -28.122023, 158.066782, -313.770118]},
    # 4th degree poly
    # "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'recomax': 0.70, 'recoPars':[0.250000, -1.152450, 1.628628, -12.547487, 12.409411]}
    # 5th degree poly
    "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V": {'recomax': 0.70, 'recoPars':[0.250000, -1.057035, -2.963484, 58.283739, -422.846674, 923.928427]}
}

sensors_list = [
    #BNL and HPK sensors - different metal widths
    ["BNL_50um_1cm_450um_W3051_2_2_170V","BNL_50um_1cm_400um_W3051_1_4_160V" , "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V"],
    # Varying resistivity and capacitance
    ["HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "BNL_50um_1cm_450um_W3052_2_4_185V", "BNL_50um_1cm_450um_W3051_2_2_170V", "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V"],
]

tagVar_list = [
    #BNL and HPK sensors - different metal widths
    ["manufacturer", "width"],
    # Varying resistivity and capacitance
    ["resistivityNumber", "capacitance"]
]

saveName_list = [
    #BNL and HPK sensors - different metal widths
    "BNL_and_HPK_PosFit_vs_MetalWidth",
    # Varying resistivity and capacitance
    "HPK_PosFit_vs_ResCap"
]

outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "ReconstructionFit/")

xmin = 0.50
xmax = 0.98
ymin = 0.001
ymax = 330 # um
pad_margin = myStyle.GetMargin()

canvas = TCanvas("cv","cv",1000,800)

for sensors, tagVars, saveName in zip(sensors_list, tagVar_list, saveName_list):
    sensor_reference = sensors[0]
    colors = myStyle.GetColorsCompare(len(sensors))

    # Get max width and pitch
    max_width, pitch = 0.0, 0.0
    for sensor in sensors:
        geometry = myStyle.GetGeometry(sensor)
        this_pitch = geometry["pitch"] # um
        this_width = geometry["width"] # um
        max_width = this_width if this_width > max_width else max_width
        pitch = this_pitch if this_pitch > pitch else pitch

    legend_height = 0.052*(len(sensors) + 1) # Entries + title
    legX1 = 1-marginR-0.6
    legX2 = 1-marginR-0.03

    yLegend = 0.026*len(sensors)
    legend = TLegend(legX1, 1-pad_margin-legend_height-0.03, legX2, 1-pad_margin-0.03)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4 -2)

    tag = mf.get_legend_comparation_plots(sensors, tagVars)

    haxis = TH1F("htemp","", 1, xmin, xmax)
    haxis.GetXaxis().SetTitle("Amplitude fraction")
    haxis.GetYaxis().SetTitle("Position [#mum]")
    haxis.GetYaxis().SetRangeUser(ymin, ymax)
    haxis.Draw("AXIS")

    # Add second axis at the right
    right_axis = ROOT.TGaxis(xmax,0.0001,xmax, ymax,0.0001, ymax/pitch,510,"+L")
    right_axis.UseCurrentStyle()
    right_axis.SetTitle("Pitch fraction")
    right_axis.SetLabelSize(myStyle.GetSize()-4)
    right_axis.SetTitleSize(myStyle.GetSize())
    right_axis.SetLabelFont(myStyle.GetFont())
    right_axis.SetTitleFont(myStyle.GetFont())
    right_axis.Draw()

    # Draw metal in background
    boxes = stripBox.getStripBoxForRecoFit(max_width, pitch, ymax, xmax, xmin)
    for box in boxes:
        box.DrawClone("same")

    # Draw lines with different metal widths
    for i,item in enumerate(sensors):
        sensor_Geometry = myStyle.GetGeometry(item)
        width = sensor_Geometry['stripWidth']
        horizontal_line = ROOT.TLine(xmin, width/2., xmax, width/2.)
        horizontal_line.SetLineWidth(3)
        horizontal_line.SetLineStyle(9)
        horizontal_line.SetLineColorAlpha(colors[i], 0.4)
        horizontal_line.DrawClone("same")

    # Draw fit functions
    fitFunction_list = []
    for i,item in enumerate(sensors):
        fitFunction = getFitFunction(sensor_reco[item]['recoPars'], scale = 1000.)
        recomax = sensor_reco[item]['recomax']

        func1 = TF1("f1%i"%(i), fitFunction, xmin, recomax)
        func1.SetLineColor(colors[i])
        name = tag[i]
        fitFunction_list.append(func1)
        func1.DrawCopy("same")
        legend.AddEntry(fitFunction_list[-1], name,"L")

    legendHeader = tag[-1]
    legend.SetHeader(legendHeader, "C")
    legend.Draw()

    sensor_prod="Strip sensors"
    if ("500x500" in sensor_reference):
        sensor_prod = "Pixel sensors"
    myStyle.BeamInfo()
    myStyle.SensorProductionInfo(sensor_prod, mright = marginR)

    haxis.Draw("AXIS same")

    canvas.SaveAs("%s%s.png"%(outdir, saveName))
    canvas.SaveAs("%s%s.pdf"%(outdir, saveName))

    canvas.Clear()
    legend.Clear()
    haxis.Delete()
