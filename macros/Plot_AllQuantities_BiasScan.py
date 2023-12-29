from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gPad,gStyle, kWhite, TF1, TPaveStats
import ROOT
import os
import EfficiencyUtils
import langaus
import optparse
import time
#from stripBox import getStripBox
import myStyle
# from matplotlib import pyplot as plt
import mySensorInfo as msi


gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True
# plt.rcParams.update({'font.size': 20})

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)

colors = myStyle.GetColors(True)

fit = langaus.LanGausFit()

# datasets = ["HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V", "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W9_15_4_20T_0P5_500P_50M_E600_110V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V"]
# datasets = ["HPK_50um_500x500um_2x2pad_E600_FNAL_190V", "HPK_30um_500x500um_2x2pad_E600_FNAL_140V", "HPK_20um_500x500um_2x2pad_E600_FNAL_105V"]

datasets = [
    "HPK_50um_500x500um_2x2pad_E600_FNAL_190V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_185V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_180V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_170V",
    "HPK_50um_500x500um_2x2pad_E600_FNAL_160V",

    "HPK_30um_500x500um_2x2pad_E600_FNAL_144V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_140V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_135V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_130V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_120V",
    "HPK_30um_500x500um_2x2pad_E600_FNAL_110V",

    "HPK_20um_500x500um_2x2pad_E600_FNAL_110V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_108V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_105V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_100V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_95V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_90V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_85V",
    "HPK_20um_500x500um_2x2pad_E600_FNAL_75V",
]


# datasets = [
#     "HPK_W5_1_1_50T_500x500_150M_E600_185V",

#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_186V",
#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_188V",
#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V",
#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_192V",
#     "HPK_W5_17_2_50T_1P0_500P_50M_E600_194V"
# ]

regions = ["Overall", "Metal", "MidGap", "Gap"]
# regions = ["Overall"]

# Quantity of interest (qty) first and a number related to the fit method next
# --> (1) stat mean, (2) gauss fit, (3) langauss fit
names = [("weighted2_timeDiff_tracker", 2), ("weighted2_jitter", 3),
         ("ampMax", 3), ("risetime", 1), ("baselineRMS", 2),
         ("charge", 3)]

# Remove SaveAs output message
ROOT.gErrorIgnoreLevel = ROOT.kWarning

for reg in regions:
    print("Region: %s"%reg)
    mySensorInfo_txt = ""

    for dataset in datasets:
        outdir = myStyle.getOutputDir(dataset)
        inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
        outdir = myStyle.GetPlotsDir(outdir, "General_variables/")

        print("  Sensor: %s"%dataset)
        mySensorInfo_txt+= "\"%s\": ["%dataset
        for var, ifit in names:
            hname = "%s_%s"%(var, reg)
            hist = inputfile.Get(hname)
            myMean = hist.GetMean()
            myRMS = hist.GetRMS()
            value = myMean

            hist.Draw("hist")

            if(ifit == 3): # LanGauss fit
                myLanGausFunction = fit.fit(hist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
                myMPV = myLanGausFunction.GetParameter(1)
                if ("charge" in var) and (myMPV < 0):
                    # TODO: Fix this! Not quite working with higher voltage sensors :(
                    myLanGausFunction = fit.fit(hist, fitrange=(1.0, 10.0))
                    myMPV = myLanGausFunction.GetParameter(1)
                value = myMPV
                myLanGausFunction.Draw("same")
            elif(ifit == 2): # Gaussian fit
                gaussian = TF1("gaussian", "gaus")
                gaussian.SetRange(myMean-1.5*myRMS,myMean+1.5*myRMS)
                hist.Fit(gaussian, "QR")
                myMean = gaussian.GetParameter(1)
                mySigma = gaussian.GetParameter(2)
                # If quantity is weighted2_timediff_tracker, then value is the sigma of fit, not the mean
                if("timeDiff_tracker" in var):
                    value = 1000*mySigma
                else:
                    value = myMean
                gaussian.Draw("same")

            mySensorInfo_txt+= "%.2f, "%(value)
            hist.GetXaxis().SetTitle("Counts")
            hist.GetXaxis().SetTitle("Qty")
            canvas.SetRightMargin(0.18)
            canvas.SetLeftMargin(0.12)
            canvas.SaveAs("%s%s_%s.gif"%(outdir, reg, var))
        mySensorInfo_txt = mySensorInfo_txt[:-2]
        mySensorInfo_txt+= "],\n"
    print("-"*45)
    print("Region: %s"%reg)
    print(mySensorInfo_txt)
    print("-"*45)
