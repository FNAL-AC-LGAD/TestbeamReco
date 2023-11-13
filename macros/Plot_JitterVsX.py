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

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-m', dest='minEventsCut', default = 100, help="Minimum events requirement")
options, args = parser.parse_args()

fit = langaus.LanGausFit()

dataset = options.Dataset
debugMode = options.debugMode
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

outdir = myStyle.GetPlotsDir(outdir, "Jitter/")
if debugMode:
    outdirTmp2 = myStyle.CreateFolder(outdir, "Jitter_vs_X_fits0/")

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']

temp = inputfile.Get("weighted2_jitter_vs_xy")
hist = temp.Project3D("zx")
hist1D = temp.Project3D("x")
# jitter_vs_x = hist1D.Clone("jitter_vs_x")

shift = inputfile.Get("stripBoxInfo03").GetMean(1)
th1_Nbins = hist1D.GetXaxis().GetNbins()
th1_Xmin = hist1D.GetXaxis().GetXmin()-shift
th1_Xmax = hist1D.GetXaxis().GetXmax()-shift
jitter_vs_x = TH1F("jitter_vs_x","", th1_Nbins, th1_Xmin, th1_Xmax)

nXBins = jitter_vs_x.GetXaxis().GetNbins()
for i in range(1,hist.GetXaxis().GetNbins()+1):
    tmpHist = hist.ProjectionY("py",i,i)
    myTotalEvents=tmpHist.Integral()
    myMean = tmpHist.GetMean()
    myRMS = tmpHist.GetRMS()
    value = myMean
    nEvents = tmpHist.GetEntries()
    minEvtsCut = myTotalEvents/nXBins

    if(nEvents>minEventsCut):
        tmpHist.Rebin(2)
        myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1.5*myRMS,myMean+3*myRMS))
        myMPV = myLanGausFunction.GetParameter(1)
        value = myMPV
        # gaussian = TF1("gaussian", "gaus")
        # gaussian.SetRange(myMean-2*myRMS,myMean+2*myRMS)
        # tmpHist.Fit(gaussian, "R")
        # myMean = gaussian.GetParameter(1)
        # mySigma = gaussian.GetParameter(2)
        # value = myMean

        # ##For Debugging Gaussian
        # tmpHist.Draw("hist")
        # gaussian.Draw("same")
        # outdir_tmp = myStyle.GetPlotsDir(outdir, "jitter_x_fits/")
        # canvas.SaveAs(outdir_tmp+"q_"+str(i)+".gif")
        #For Debugging Landau
        if(debugMode):
            tmpHist.Draw("hist")
            myLanGausFunction.Draw("same")
            canvas.SaveAs(outdirTmp2+"q_"+str(i)+".gif")

        jitter_vs_x.SetBinContent(i,value)
    else:
        jitter_vs_x.SetBinContent(i,0)
            
jitter_vs_x.Draw("hist")
jitter_vs_x.SetStats(0)
jitter_vs_x.SetTitle("Weighted jitter vs X")
jitter_vs_x.GetXaxis().SetTitle("Track x position [mm]")
jitter_vs_x.GetYaxis().SetTitle("Jitter [ps]")
jitter_vs_x.GetYaxis().SetRangeUser(0,100.0)
canvas.SetRightMargin(0.18)
canvas.SetLeftMargin(0.12)
#myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin())
canvas.SaveAs(outdir+"weighted2_jitter_vs_x.png")


file = TFile(outdir+"JitterVsX.root", "RECREATE")
jitter_vs_x.Write()
file.Close()
