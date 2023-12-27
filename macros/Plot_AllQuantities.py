from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gPad,gStyle, kWhite, TF1, TPaveStats
import os
import EfficiencyUtils
import langaus
import optparse
import time
#from stripBox import getStripBox
import myStyle
from matplotlib import pyplot as plt
gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True
plt.rcParams.update({'font.size': 20})

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)

run = 0
fit = langaus.LanGausFit()

# datasets = ["HPK_W2_3_2_50T_1P0_500P_50M_E240_180V", "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V", "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V", "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V", "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V", "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V", "HPK_W9_15_2_20T_1P0_500P_50M_E600_114V", "HPK_W9_15_4_20T_0P5_500P_50M_E600_110V", "HPK_KOJI_50T_1P0_80P_60M_E240_190V", "HPK_KOJI_20T_1P0_80P_60M_E240_112V", "HPK_W5_1_1_50T_500x500_150M_E600_185V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"]
datasets = ["HPK_W11_22_3_20T_500x500_150M_C600_116V", "HPK_W9_22_3_20T_500x500_150M_E600_112V", "HPK_W8_1_1_50T_500x500_150M_C600_200V", "HPK_W5_1_1_50T_500x500_150M_E600_185V", "HPK_W9_23_3_20T_500x500_300M_E600_112V"]

# qty = ["ampMax_Overall", "risetime_Overall", "charge_Overall", "baselineRMS_Overall", "weighted2_jitter_Overall", "weighted2_timeDiff_tracker_Overall"]
# qty = ["ampMax_Metal", "risetime_Metal", "charge_Metal", "baselineRMS_Metal", "weighted2_jitter_Metal", "weighted2_timeDiff_tracker_Metal"]
qty = ["ampMax_MidGap", "risetime_MidGap", "charge_MidGap", "baselineRMS_MidGap", "weighted2_jitter_MidGap", "weighted2_timeDiff_tracker_MidGap"]
# qty = ["ampMax_Gap", "risetime_Gap", "charge_Gap", "baselineRMS_Gap", "weighted2_jitter_Gap", "weighted2_timeDiff_tracker_Gap"]
fit_var = [3,1,3,2,3,2] # 1 - stat mean, 2 - gauss fit, 3 - langauss fit

for var in range(len(qty)):
    for iter in range(len(datasets)):
        dataset = datasets[iter]
        outdir=""
        outdir = myStyle.getOutputDir(dataset)
        inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

        colors = myStyle.GetColors(True)
        sensor_Geometry = myStyle.GetGeometry(dataset)
        sensor = sensor_Geometry['sensor']
        pitch  = sensor_Geometry['pitch']

        hist = inputfile.Get(qty[var])
        myMean = hist.GetMean()
        myRMS = hist.GetRMS()
        value = myMean

        hist.Draw("hist")

        if(fit_var[var]==3): # LanGauss fit
            myLanGausFunction = fit.fit(hist, fitrange=(myMean-1.5*myRMS,myMean+3*myRMS))
            myMPV = myLanGausFunction.GetParameter(1)
            value = myMPV
            myLanGausFunction.Draw("same")
        elif(fit_var[var]==2): # Gaussian fit
            gaussian = TF1("gaussian", "gaus")
            gaussian.SetRange(myMean-1.5*myRMS,myMean+1.5*myRMS)
            hist.Fit(gaussian, "R")
            myMean = gaussian.GetParameter(1)
            mySigma = gaussian.GetParameter(2)
            if( var == 5): # If quantity is weighted2_timediff_tracker, then value is the sigma of fit, not the mean
                value = 1000*mySigma
            else:
                value = myMean
            gaussian.Draw("same")

        print(qty[var]," = ",datasets[iter]," : ",value)
        hist.GetXaxis().SetTitle("Counts")
        hist.GetXaxis().SetTitle("Qty")
        canvas.SetRightMargin(0.18)
        canvas.SetLeftMargin(0.12)
        canvas.SaveAs(outdir+qty[var]+".gif")
