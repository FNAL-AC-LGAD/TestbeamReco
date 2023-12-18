from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite,TH1
import ROOT
import os
import optparse
from stripBox import getStripBox
import myStyle
import math 
import time
import langaus

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()
organized_mode=True
fitLangaus = langaus.LanGausFit()


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, xMin=0.0, xMax=1000.0, yMin=0.0, yMax=30.0, title="", xlabel="", ylabel="", color=ROOT.kBlack, rebin=None, unit=1.0, getMean=False, doGaus=True, removeExtra=False, markerStyle=ROOT.kFullCircle):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.color = color
        self.rebin = rebin
        self.unit = unit
        self.getMean = getMean
        self.doGaus = doGaus
        self.removeExtra = removeExtra
        self.markerStyle = markerStyle
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name):
        #print(name)
        th2 = f.Get(name)
        if self.rebin: th2.RebinX(int(self.rebin))
        return th2

    def getTH1(self, th2, name):
        t = time.time()
        newName = "{}{}".format(name,t)
        th1_temp = TH1D(newName,newName,th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin(),th2.GetXaxis().GetXmax())
        return th1_temp

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--xmin', dest='xmin', default = 65.0, help="Limit x-axis in final plot")
parser.add_option('--xmax', dest='xmax', default = 205.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 70.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")

options, args = parser.parse_args()
dataset = options.Dataset
outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
    print("%s%s_Analyze.root"%(outdir,dataset))
else:
    inputfile = TFile("../test/myoutputfile.root")

dataset2 = "HPK_20um_500x500um_2x2pad_E600_FNAL"
outdir2 = myStyle.getOutputDir(dataset2)
inputfile2 = TFile("%s%s_Analyze.root"%(outdir2,dataset2))

dataset3 = "HPK_30um_500x500um_2x2pad_E600_FNAL"
outdir3 = myStyle.getOutputDir(dataset3)
inputfile3 = TFile("%s%s_Analyze.root"%(outdir3,dataset3))

xmin = float(options.xmin)
xmax = float(options.xmax)
ylength = float(options.ylength)
debugMode = options.debugMode

outdir = myStyle.GetPlotsDir(outdir, "BiasScans/")
all_histoInfos = [
    [
        HistoInfo("timeDiff_vs_BV_channel01", inputfile2,"timeDiff_vs_BV_channel01",     True,  xmin,xmax, 0.0,ylength, "HPK 20 #mum FNAL board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kBlack,   None, 1000.0, False, True, True),
        HistoInfo("timeDiff_vs_BV_channel20", inputfile2,"timeDiff_vs_BV_channel20",     True,  xmin,xmax, 0.0,ylength, "HPK 20 #mum UCSC board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kBlack,   None, 1000.0, False, True, True, ROOT.kOpenCircle),
        HistoInfo("timeDiff_vs_BV_channel01", inputfile3,"timeDiff_vs_BV_channel01",     True,  xmin,xmax, 0.0,ylength, "HPK 30 #mum FNAL board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kRed,     None, 1000.0, False, True, True),
        HistoInfo("timeDiff_vs_BV_channel20", inputfile3,"timeDiff_vs_BV_channel20",     True,  xmin,xmax, 0.0,ylength, "HPK 30 #mum UCSC board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kRed,     None, 1000.0, False, True, True, ROOT.kOpenCircle),
        HistoInfo("timeDiff_vs_BV_channel11", inputfile, "timeDiff_vs_BV_channel11",     True,  xmin,xmax, 0.0,ylength, "HPK 50 #mum FNAL board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kGreen+2, None, 1000.0, False, True, True),
        HistoInfo("timeDiff_vs_BV_channel20", inputfile, "timeDiff_vs_BV_channel20",     True,  xmin,xmax, 0.0,ylength, "HPK 50 #mum UCSC board", "Bias Voltage [V]", "Time resolution [ps]", ROOT.kGreen+2, None, 1000.0, False, True, True, ROOT.kOpenCircle),
    ],
    [
        HistoInfo("slewrate_vs_BV_channel01", inputfile2, "slewrate_vs_BV_channel01", False, xmin,xmax, 0.0, 320.0, "HPK 20 #mum FNAL board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kBlack,   None, 1.0, True, False, False),
        HistoInfo("slewrate_vs_BV_channel20", inputfile2, "slewrate_vs_BV_channel20", False, xmin,xmax, 0.0, 320.0, "HPK 20 #mum UCSC board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kBlack,   None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("slewrate_vs_BV_channel01", inputfile3, "slewrate_vs_BV_channel01", False, xmin,xmax, 0.0, 320.0, "HPK 30 #mum FNAL board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kRed,     None, 1.0, True, False, False),
        HistoInfo("slewrate_vs_BV_channel20", inputfile3, "slewrate_vs_BV_channel20", False, xmin,xmax, 0.0, 320.0, "HPK 30 #mum UCSC board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kRed,     None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("slewrate_vs_BV_channel11", inputfile,  "slewrate_vs_BV_channel11", False, xmin,xmax, 0.0, 320.0, "HPK 50 #mum FNAL board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kGreen+2, None, 1.0, True, False, False),
        HistoInfo("slewrate_vs_BV_channel20", inputfile,  "slewrate_vs_BV_channel20", False, xmin,xmax, 0.0, 320.0, "HPK 50 #mum UCSC board", "Bias Voltage [V]", "Slewrate [mV/ns]", ROOT.kGreen+2, None, 1.0, True, False, False, ROOT.kOpenCircle),
    ],
    [
        HistoInfo("amp_vs_BV_channel01", inputfile2, "amp_vs_BV_channel01", True,  xmin,xmax, 0.0, 230.0, "HPK 20 #mum FNAL board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kBlack,   None, 1.0, False, False, False),
        HistoInfo("amp_vs_BV_channel20", inputfile2, "amp_vs_BV_channel20", True,  xmin,xmax, 0.0, 230.0, "HPK 20 #mum UCSC board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kBlack,   None, 1.0, False, False, False, ROOT.kOpenCircle),
        HistoInfo("amp_vs_BV_channel01", inputfile3, "amp_vs_BV_channel01", True,  xmin,xmax, 0.0, 230.0, "HPK 30 #mum FNAL board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kRed,     None, 1.0, False, False, False),
        HistoInfo("amp_vs_BV_channel20", inputfile3, "amp_vs_BV_channel20", True,  xmin,xmax, 0.0, 230.0, "HPK 30 #mum UCSC board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kRed,     None, 1.0, False, False, False, ROOT.kOpenCircle),
        HistoInfo("amp_vs_BV_channel11", inputfile,  "amp_vs_BV_channel11", True,  xmin,xmax, 0.0, 230.0, "HPK 50 #mum FNAL board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kGreen+2, None, 1.0, False, False, False),
        HistoInfo("amp_vs_BV_channel20", inputfile,  "amp_vs_BV_channel20", True,  xmin,xmax, 0.0, 230.0, "HPK 50 #mum UCSC board", "Bias Voltage [V]", "MPV Amplitude [mV]", ROOT.kGreen+2, None, 1.0, False, False, False, ROOT.kOpenCircle),
    ],
    [
        HistoInfo("baselineRMS_vs_BV_channel01", inputfile2, "baselineRMS_vs_BV_channel01", False,  xmin,xmax, 1.0, 3.0, "HPK 20 #mum FNAL board", "Bias Voltage [V]", "Noise [mV]", ROOT.kBlack,   None, 1.0, True, False, False),
        HistoInfo("baselineRMS_vs_BV_channel20", inputfile2, "baselineRMS_vs_BV_channel20", False,  xmin,xmax, 1.0, 3.0, "HPK 20 #mum UCSC board", "Bias Voltage [V]", "Noise [mV]", ROOT.kBlack,   None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("baselineRMS_vs_BV_channel01", inputfile3, "baselineRMS_vs_BV_channel01", False,  xmin,xmax, 1.0, 3.0, "HPK 30 #mum FNAL board", "Bias Voltage [V]", "Noise [mV]", ROOT.kRed,     None, 1.0, True, False, False),
        HistoInfo("baselineRMS_vs_BV_channel20", inputfile3, "baselineRMS_vs_BV_channel20", False,  xmin,xmax, 1.0, 3.0, "HPK 30 #mum UCSC board", "Bias Voltage [V]", "Noise [mV]", ROOT.kRed,     None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("baselineRMS_vs_BV_channel11", inputfile,  "baselineRMS_vs_BV_channel11", False,  xmin,xmax, 1.0, 3.0, "HPK 50 #mum FNAL board", "Bias Voltage [V]", "Noise [mV]", ROOT.kGreen+2, None, 1.0, True, False, False),
        HistoInfo("baselineRMS_vs_BV_channel20", inputfile,  "baselineRMS_vs_BV_channel20", False,  xmin,xmax, 1.0, 3.0, "HPK 50 #mum UCSC board", "Bias Voltage [V]", "Noise [mV]", ROOT.kGreen+2, None, 1.0, True, False, False, ROOT.kOpenCircle),
    ],
    [
        HistoInfo("risetime_vs_BV_channel01", inputfile2, "risetime_vs_BV_channel01", False,  xmin,xmax, 200.0, 800.0, "HPK 20 #mum FNAL board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kBlack,   None, 1.0, True, False, False),
        HistoInfo("risetime_vs_BV_channel20", inputfile2, "risetime_vs_BV_channel20", False,  xmin,xmax, 200.0, 800.0, "HPK 20 #mum UCSC board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kBlack,   None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("risetime_vs_BV_channel01", inputfile3, "risetime_vs_BV_channel01", False,  xmin,xmax, 200.0, 800.0, "HPK 30 #mum FNAL board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kRed,     None, 1.0, True, False, False),
        HistoInfo("risetime_vs_BV_channel20", inputfile3, "risetime_vs_BV_channel20", False,  xmin,xmax, 200.0, 800.0, "HPK 30 #mum UCSC board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kRed,     None, 1.0, True, False, False, ROOT.kOpenCircle),
        HistoInfo("risetime_vs_BV_channel11", inputfile,  "risetime_vs_BV_channel11", False,  xmin,xmax, 200.0, 800.0, "HPK 50 #mum FNAL board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kGreen+2, None, 1.0, True, False, False),
        HistoInfo("risetime_vs_BV_channel20", inputfile,  "risetime_vs_BV_channel20", False,  xmin,xmax, 200.0, 800.0, "HPK 50 #mum UCSC board", "Bias Voltage [V]", "Risetime [ps] (10 to 90%)", ROOT.kGreen+2, None, 1.0, True, False, False, ROOT.kOpenCircle),
    ],
]

canvas = TCanvas("cv","cv",1000,800)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
marg = 1.0
ROOT.gPad.SetLeftMargin(0.15)
ROOT.gPad.SetRightMargin(0.08)
ROOT.gPad.SetTopMargin(0.08)
ROOT.gPad.SetBottomMargin(0.15)
print("Finished setting up langaus fit class")

nXBins = all_histoInfos[0][0].th2.GetXaxis().GetNbins()

#loop over X bins
for i in range(0, nXBins+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for histoInfos in all_histoInfos:
        for info in histoInfos:
            totalEvents = info.th2.GetEntries()
            tmpHist = info.th2.ProjectionY("py",i,i)
            myRMS = tmpHist.GetRMS()
            myMean = tmpHist.GetMean()
            nEvents = tmpHist.GetEntries()
            fitlow = myMean - 2.4*myRMS
            fithigh = myMean + 2.4*myRMS
            value = info.unit*myMean
            error = info.unit*tmpHist.GetMeanError()

            minEvtsCut = totalEvents/nXBins
            #if i==0: print(info.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")

            #Do fit 
            if(info.doFits):
                if(nEvents > minEvtsCut):
                    if info.doGaus:
                        #tmpHist.Rebin(2)            
                        fit = TF1('fit','gaus',fitlow,fithigh)
                        tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                        myFitMean = fit.GetParameter(1)
                        myFitMeanError = fit.GetParError(1)
                        mySigma = fit.GetParameter(2)
                        mySigmaError = fit.GetParError(2)
                        if info.getMean:
                            value = info.unit*myFitMean                
                            error = info.unit*myFitMeanError                         
                        else:
                            value = info.unit*mySigma                
                            error = info.unit*mySigmaError 
                    else:
                        tmpHist.Rebin(2)
                        fit = fitLangaus.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
                        value = fit.GetParameter(1)
                        error = fit.GetParError(1)
                
                    ##For Debugging
                    #tmpHist.Draw("hist")
                    #fit.Draw("same")
                    #canvas.SaveAs(outdir+"q"+info.outHistoName+"_"+info.title.replace(" ","_")+"_"+str(i)+".gif")
                    
                    #if (debugMode):
                    #    tmpHist.Draw("hist")
                    #    fit.Draw("same")
                    #    canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                    #    print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution: %.3f +/- %.3f"%(value, error))


                    # print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
                else:
                    value = 0.0
                    error = 0.0

            # Removing telescope contribution
            if value!=0.0 and info.removeExtra:
                error = error*value/TMath.Sqrt(value*value - 9*9)
                value = TMath.Sqrt(value*value - 9*9)

            info.th1.SetBinContent(i,value)
            info.th1.SetBinError(i,error)
                 
# Plot 2D histograms
for histoInfos in all_histoInfos:
    #outputfile = TFile("%stimeDiffVsX.root"%(outdir),"RECREATE")
    htemp = TH1F("htemp","",1,histoInfos[0].xMin,histoInfos[0].xMax)
    htemp.SetLineColor(kWhite)
    htemp.SetStats(0)
    htemp.GetYaxis().SetRangeUser(histoInfos[0].yMin, histoInfos[0].yMax)
    htemp.GetXaxis().SetTitle(histoInfos[0].xlabel)
    htemp.GetYaxis().SetTitle(histoInfos[0].ylabel)  
    htemp.GetXaxis().SetTitleOffset(0.95)
    htemp.GetYaxis().SetTitleOffset(1.3)
    htemp.Draw("")

    legend = TLegend(0.18,0.75, 0.90,0.89)
    legend.SetBorderSize(1)
    legend.SetNColumns(2)
    #legend.SetFillColor(kWhite)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-15)
    #legend.SetFillStyle(0)

    #print(len(histoInfos))
    #if(len(histoInfos) > 1):
    if(True):
        for info in histoInfos:
            info.th1.SetStats(0)
            # info.th1.GetXaxis().SetTitle(info.xlabel)
            # info.th1.GetYaxis().SetTitle(info.ylabel)
            #info.th1.SetMinimum(0.0001)
            #info.th1.SetMaximum(ylength)
            info.th1.SetLineWidth(3)
            info.th1.SetLineColor(info.color)
            info.th1.SetMarkerColor(info.color)
            info.th1.SetMarkerSize(1.2)
            info.th1.SetMarkerStyle(info.markerStyle)
            legend.AddEntry(info.th1, info.title, "ep")

            #info.th1.GetXaxis().SetTitle("Track x position [mm]")
            #info.th1.GetXaxis().SetRangeUser(xmin,xmax)
            #info.th1.GetYaxis().SetTitle("Time resolution [ps]")
            #ymin = info.th1.GetMinimum()
            #ymax = ylength 
            info.th1.Draw("LPEX0 same")
            #info.th1.Print("all")

        legend.Draw()
        #gPad.RedrawAxis("g")
    else:
        info = histoInfos[0]
        info.th2.SetStats(0)
        tp = info.th2.ProfileX()
        tp.SetLineColor(ROOT.kRed)
        ROOT.gPad.SetRightMargin(0.15)
        info.th2.Draw("colz same")
        tp.Draw("same")

    text = ROOT.TLatex()
    tsize=38
    text.SetTextSize(tsize-4)
    text.DrawLatexNDC(0.15,0.94,"#bf{FNAL 120 GeV proton beam}")
    canvas.SetGrid(0,1)

    canvas.SaveAs(outdir+"%s"%info.outHistoName+".gif")
    canvas.SaveAs(outdir+"%s"%info.outHistoName+".pdf")
    #info.th1.Write()
    #outputfile.Close()
