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
    def __init__(self, inHistoName, f, outHistoName, doFits=True, xMin=0.0, xMax=1000.0, yMin=0.0, yMax=30.0, title="", xlabel="", ylabel="", color=ROOT.kBlack, rebin=None, unit=1.0, getMean=False, doGaus=True):
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
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name):
        print(name)
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
parser.add_option('--xmin', dest='xmin', default = 101.0, help="Limit x-axis in final plot")
parser.add_option('--xmax', dest='xmax', default = 239.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 80.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")

options, args = parser.parse_args()
dataset = options.Dataset
outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_AnalyzeCFD.root"%(outdir,dataset))
    print("%s%s_AnalyzeCFD.root"%(outdir,dataset))
else:
    inputfile = TFile("../test/myoutputfile.root")

dataset2 = "CFD_noSpy"
outdir2 = myStyle.getOutputDir(dataset2)
inputfile2 = TFile("%s%s_AnalyzeCFD.root"%(outdir2,dataset2))

xmin = float(options.xmin)
xmax = float(options.xmax)
ylength = float(options.ylength)
debugMode = options.debugMode

outdir = myStyle.GetPlotsDir(outdir, "BiasScans/")
all_histoInfos = [
    [
        #HistoInfo("timeDiff_30mV_vs_BV_channel00", inputfile, "timeDiff_30mV_vs_BV_channel00", True,  xmin,xmax, 0.0,ylength, "Spy 30mV",    "Bias Voltage [V]", "Time resolution [ps]", colors[0], None, 1000.0),
        #HistoInfo("timeDiff_vs_BV_channel00",      inputfile, "timeDiff_vs_BV_channel00",      True,  xmin,xmax, 0.0,ylength, "Spy CFD",     "Bias Voltage [V]", "Time resolution [ps]", colors[1], None, 1000.0),
        #HistoInfo("timeDiff_30mV_vs_BV_channel01", inputfile, "timeDiff_30mV_vs_BV_channel01", True,  xmin,xmax, 0.0,ylength, "FCFDv0 30mV", "Bias Voltage [V]", "Time resolution [ps]", colors[2], None, 1000.0),
        #HistoInfo("timeDiff_vs_BV_channel01",      inputfile, "timeDiff_vs_BV_channel01",      True,  xmin,xmax, 0.0,ylength, "FCFDv0 Spy",  "Bias Voltage [V]", "Time resolution [ps]", colors[0], None, 1000.0, False, True),
        HistoInfo("timeDiff_vs_BV_channel01",      inputfile2,"timeDiff_vs_BV_channel01",      True,  xmin,xmax, 0.0,ylength, "FCFDv0",      "LGAD Bias Voltage [V]", "Time resolution [ps]", ROOT.kBlack, None, 1000.0, False, True),
    ],
    #[
    #    #HistoInfo("timeDiff_30mV_vs_BV_channel00", inputfile, "timeMean_30mV_vs_BV_channel00", False, xmin,xmax,  -250,1500, "Spy 30mV",    "Bias Voltage [V]", "Mean #Delta t [ps]", colors[0], None, 1000.0),
    #    #HistoInfo("timeDiff_vs_BV_channel00",      inputfile, "timeMean_vs_BV_channel00",      True, xmin,xmax,  -150,150, "Spy CFD",     "Bias Voltage [V]", "Mean #Delta t [ps]", colors[1], None, 1000.0, getMean=True),
    #    #HistoInfo("timeDiff_30mV_vs_BV_channel01", inputfile, "timeMean_30mV_vs_BV_channel01", True, xmin,xmax,  -150,50, "FCFDv0 30mV", "Bias Voltage [V]", "Mean #Delta t [ps]", colors[2], None, 1000.0, getMean=True),
    #    HistoInfo("timeDiff_vs_BV_channel01",      inputfile, "timeMean_vs_BV_channel01",      True, xmin,xmax,  -150,150, "FCFDv0 Spy",  "Bias Voltage [V]", "Mean #Delta t [ps]", colors[0], None, 1000.0, getMean=True),
    #    HistoInfo("timeDiff_vs_BV_channel01",      inputfile2,"timeMean_vs_BV_channel01",      True, xmin,xmax,  -150,150, "FCFDv0",      "Bias Voltage [V]", "Mean #Delta t [ps]", colors[1], None, 1000.0, getMean=True),
    #],
    #[
    #    HistoInfo("timeDiff_30mV_vs_amp00", inputfile, "timeDiff_30mV_vs_amp00", True,  0.0,215.0, 0.0,ylength, "Spy 30mV",    "Amplitude [mV]", "Time resolution [ps]", colors[0], 5, 1000.0),
    #    HistoInfo("timeDiff_vs_amp00",      inputfile, "timeDiff_vs_amp00",      True,  0.0,215.0, 0.0,ylength, "Spy CFD",     "Amplitude [mV]", "Time resolution [ps]", colors[1], 5, 1000.0),
    #    HistoInfo("timeDiff_30mV_vs_amp01", inputfile, "timeDiff_30mV_vs_amp01", True,  0.0,215.0, 0.0,ylength, "FCFDv0 30mV", "Amplitude [mV]", "Time resolution [ps]", colors[2], 5, 1000.0),
    #    HistoInfo("timeDiff_vs_amp01",      inputfile, "timeDiff_vs_amp01",      True,  0.0,215.0, 0.0,ylength, "FCFDv0 CFD",  "Amplitude [mV]", "Time resolution [ps]", colors[3], 5, 1000.0),
    #],
    #[
    #    HistoInfo("timeDiff_30mV_vs_amp00", inputfile, "timeMean_30mV_vs_amp00", False,  0.0,215.0, -250,1500, "Spy 30mV",    "Amplitude [mV]", "Mean #Delta t [ps]", colors[0], None, 1000.0),
    #    HistoInfo("timeDiff_vs_amp00",      inputfile, "timeMean_vs_amp00",      False,  0.0,215.0, -250,1500, "Spy CFD",     "Amplitude [mV]", "Mean #Delta t [ps]", colors[1], None, 1000.0),
    #    HistoInfo("timeDiff_30mV_vs_amp01", inputfile, "timeMean_30mV_vs_amp01", False,  0.0,215.0, -250,1500, "FCFDv0 30mV", "Amplitude [mV]", "Mean #Delta t [ps]", colors[2], None, 1000.0),
    #    HistoInfo("timeDiff_vs_amp01",      inputfile, "timeMean_vs_amp01",      False,  0.0,215.0, -250,1500, "FCFDv0 CFD",  "Amplitude [mV]", "Mean #Delta t [ps]", colors[3], None, 1000.0),
    #],
    #[
    #    HistoInfo("timeDiff_30mV_vs_charge00", inputfile, "timeDiff_30mV_vs_charge00", True,  0.0,50.0, 0,ylength, "Spy 30mV",    "Charge [fC]", "Time resolution [ps]", colors[0], None, 1.0),
    #    HistoInfo("timeDiff_vs_charge00",      inputfile, "timeDiff_vs_charge00",      True,  0.0,50.0, 0,ylength, "Spy CFD",     "Charge [fC]", "Time resolution [ps]", colors[1], None, 1.0),
    #    HistoInfo("timeDiff_30mV_vs_charge01", inputfile, "timeDiff_30mV_vs_charge01", True,  0.0,50.0, 0,ylength, "FCFDv0 30mV", "Charge [fC]", "Time resolution [ps]", colors[2], None, 1.0),
    #    HistoInfo("timeDiff_vs_charge01",      inputfile, "timeDiff_vs_charge01",      True,  0.0,50.0, 0,ylength, "FCFDv0 CFD",  "Charge [fC]", "Time resolution [ps]", colors[3], None, 1.0),
    #],
    #[
    #    HistoInfo("timeDiff_30mV_vs_charge00", inputfile, "timeMean_30mV_vs_charge00", False,  0.0,50.0, -50,50, "Spy 30mV",    "Charge [fC]", "Mean #Delta t [ps]", colors[0], None, 1.0),
    #    HistoInfo("timeDiff_vs_charge00",      inputfile, "timeMean_vs_charge00",      False,  0.0,50.0, -50,50, "Spy CFD",     "Charge [fC]", "Mean #Delta t [ps]", colors[1], None, 1.0),
    #    HistoInfo("timeDiff_30mV_vs_charge01", inputfile, "timeMean_30mV_vs_charge01", False,  0.0,50.0, -50,50, "FCFDv0 30mV", "Charge [fC]", "Mean #Delta t [ps]", colors[2], None, 1.0),
    #    HistoInfo("timeDiff_vs_charge01",      inputfile, "timeMean_vs_charge01",      False,  0.0,50.0, -50,50, "FCFDv0 CFD",  "Charge [fC]", "Mean #Delta t [ps]", colors[3], None, 1.0),
    #],
    #[
    #    HistoInfo("timeDiff_vs_charge01",      inputfile, "timeMean_vs_charge01_colz", False,  0.0,50.0, -200,400, "FCFDv0 CFD",  "Charge [fC]", "Mean #Delta t [ps]", colors[3], None, 1.0),
    #],
    #[
    #    HistoInfo("slewrate_vs_BV_channel00", inputfile, "slewrate_vs_BV_channel00", False, xmin,xmax, 0.0, 150.0, "Spy",    "Bias Voltage [V]", "Slewrate [mV/ns]", colors[0]),
    #    HistoInfo("slewrate_vs_BV_channel01", inputfile, "slewrate_vs_BV_channel01", False, xmin,xmax, 0.0, 150.0, "FCFDv0", "Bias Voltage [V]", "Slewrate [mV/ns]", colors[1]),
    #],
    #[
    #    HistoInfo("amp_vs_BV_channel00", inputfile, "amp_vs_BV_channel00", True,  xmin,xmax, 0.0, 40.0, "Spy",    "Bias Voltage [V]", "MPV Charge [fC]", colors[0], None, 1.0, False, False),
    #    #HistoInfo("amp_vs_BV_channel01", inputfile, "amp_vs_BV_channel01", True,  xmin,xmax, 0.0, 60.0, "FCFDv0", "Bias Voltage [V]", "Mean Amplitude [mV]", colors[1], None, 1.0, False, False),
    #],
    #[
    #    HistoInfo("baselineRMS_vs_BV_channel00", inputfile, "baselineRMS_vs_BV_channel00", False,  xmin,xmax, 0.0, 2.0, "Spy",    "Bias Voltage [V]", "Noise [mV]", colors[0]),
    #    HistoInfo("baselineRMS_vs_BV_channel01", inputfile, "baselineRMS_vs_BV_channel01", False,  xmin,xmax, 0.0, 2.0, "FCFDv0", "Bias Voltage [V]", "Noise [mV]", colors[1]),
    #],
    #[
    #    HistoInfo("risetime_vs_BV_channel00", inputfile, "risetime_vs_BV_channel00", False,  xmin,xmax, 500.0, 2000.0, "Spy",    "Bias Voltage [V]", "Risetime [ps]", colors[0]),
    #    HistoInfo("risetime_vs_BV_channel01", inputfile, "risetime_vs_BV_channel01", False,  xmin,xmax, 500.0, 2000.0, "FCFDv0", "Bias Voltage [V]", "Risetime [ps]", colors[1]),
    #],
]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
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
            fitlow = myMean - 1.5*myRMS
            fithigh = myMean + 1.5*myRMS
            value = info.unit*myMean
            error = info.unit*tmpHist.GetMeanError()

            minEvtsCut = totalEvents/nXBins
            if i==0: print(info.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")

            #Do fit 
            if(info.doFits):
                if(nEvents > minEvtsCut):
                    if info.doGaus:
                        tmpHist.Rebin(2)            
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
                        #tmpHist.Rebin(2)
                        fit = fitLangaus.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
                        value = (7.0/30.0)*fit.GetParameter(1)
                        error =(7.0/30.0)*fit.GetParError(1)
                
                    ##For Debugging
                    #tmpHist.Draw("hist")
                    #fit.Draw("same")
                    #canvas.SaveAs(outdir+"q"+info.outHistoName +"_"+str(i)+".gif")
                    
                    #if (debugMode):
                    #    tmpHist.Draw("hist")
                    #    fit.Draw("same")
                    #    canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                    #    print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution: %.3f +/- %.3f"%(value, error))


                    # print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
                else:
                    value = 0.0
                    error = 0.0

            ## Removing telescope contribution
            #if value!=0.0:
            #    error = error*value/TMath.Sqrt(value*value - 10*10)
            #    value = TMath.Sqrt(value*value - 10*10)

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

    legend = TLegend(0.55,0.70, 0.85,0.89)
    legend.SetBorderSize(0)
    legend.SetFillColor(kWhite)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize())
    legend.SetFillStyle(0)

    print(len(histoInfos))
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
            info.th1.SetMarkerSize(0.7)
            info.th1.SetMarkerStyle(8)
            legend.AddEntry(info.th1, info.title, "lep")

            #info.th1.GetXaxis().SetTitle("Track x position [mm]")
            #info.th1.GetXaxis().SetRangeUser(xmin,xmax)
            #info.th1.GetYaxis().SetTitle("Time resolution [ps]")
            #ymin = info.th1.GetMinimum()
            #ymax = ylength 
            info.th1.Draw("P same")
            info.th1.Print("all")

        #legend.Draw()
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

    #text = ROOT.TLatex()
    #tsize=38
    #text.SetTextSize(tsize-4)
    #text.DrawLatexNDC(0.8,0.94,"#bf{FCFDv0}")

    canvas.SetGrid(0,1)

    canvas.SaveAs(outdir+"%s"%info.outHistoName+".gif")
    canvas.SaveAs(outdir+"%s"%info.outHistoName+".pdf")
    canvas.SaveAs(outdir+"%s"%info.outHistoName+".C")    
    #info.th1.Write()
    #outputfile.Close()
