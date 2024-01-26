from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite,TH1,kGray, TGraph
import ROOT
import optparse
from stripBox import getStripBox
import myStyle
import math
import time
import langaus
import myFunctions as mf

gROOT.SetBatch(True)
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()
fitLangaus = langaus.LanGausFit()


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, info_ch="", doFits=True, xMin=0.0, xMax=1000.0, yMin=0.0, yMax=30.0, title="", xlabel="Bias voltage [V]", ylabel="",
                 color=ROOT.kBlack, rebin=None, unit=1.0, doGaus=True, getGausMean=False, doLanGaus=False, rm_photek=False, markerStyle=ROOT.kFullCircle):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.info_ch = info_ch
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
        self.doGaus = doGaus
        self.getGausMean = getGausMean
        self.doLanGaus = doLanGaus
        self.rm_photek = rm_photek
        self.markerStyle = markerStyle
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name):
        #print(name)
        th2 = f.Get(name)
        if self.rebin: th2.RebinX(int(self.rebin))
        return th2

    def getTH1(self, th2, name):
        if self.info_ch:
            name+= "_%s"%(self.info_ch)
        th1_temp = TH1D(name, name, th2.GetXaxis().GetNbins(), th2.GetXaxis().GetXmin(), th2.GetXaxis().GetXmax())
        th1_temp.SetStats(0)
        th1_temp.SetLineWidth(3)
        th1_temp.SetLineColor(self.color)
        th1_temp.SetMarkerColor(self.color)
        th1_temp.SetMarkerSize(1.2)
        th1_temp.SetMarkerStyle(self.markerStyle)
        return th1_temp

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('--xmin', dest='xmin', default = 65.0, help="Limit x-axis in final plot")
parser.add_option('--xmax', dest='xmax', default = 205.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 90.0, help="Max TimeResolution value in final plot")
# parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")

options, args = parser.parse_args()
# dataset = options.Dataset
outdir = myStyle.GetPlotsDir((myStyle.getOutputDir("Compare")), "")
outdir = myStyle.GetPlotsDir(outdir, "Bias_scan/")

dataset_20um = "HPK_20um_500x500um_2x2pad_E600_FNAL"
infile_20um = TFile("%s%s_Analyze.root"%(myStyle.getOutputDir(dataset_20um),dataset_20um))

dataset_30um = "HPK_30um_500x500um_2x2pad_E600_FNAL"
infile_30um = TFile("%s%s_Analyze.root"%(myStyle.getOutputDir(dataset_30um),dataset_30um))

dataset_50um = "HPK_50um_500x500um_2x2pad_E600_FNAL"
infile_50um = TFile("%s%s_Analyze.root"%(myStyle.getOutputDir(dataset_50um),dataset_50um))

xmin = float(options.xmin)
xmax = float(options.xmax)
ylength = float(options.ylength)
debugMode = options.debugMode

sensors = [dataset_20um, dataset_30um, dataset_50um]
print(sensors)

legend_entry = mf.get_legend_comparation_plots(sensors, ["thickness"])

all_histoInfos = [
    [
        HistoInfo("timeDiff_vs_BV_channel01", infile_20um, "timeDiff_vs_BV", "20umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[0]+"   ", ylabel="Time resolution [ps]", color=ROOT.kBlack,   unit=1000.0, doGaus=True, rm_photek=True),
        HistoInfo("timeDiff_vs_BV_channel20", infile_20um, "timeDiff_vs_BV", "20umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[0]+"   ", ylabel="Time resolution [ps]", color=ROOT.kBlack,   unit=1000.0, doGaus=True, rm_photek=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("timeDiff_vs_BV_channel01", infile_30um, "timeDiff_vs_BV", "30umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[1]+"   ", ylabel="Time resolution [ps]", color=ROOT.kRed,     unit=1000.0, doGaus=True, rm_photek=True),
        HistoInfo("timeDiff_vs_BV_channel20", infile_30um, "timeDiff_vs_BV", "30umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[1]+"   ", ylabel="Time resolution [ps]", color=ROOT.kRed,     unit=1000.0, doGaus=True, rm_photek=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("timeDiff_vs_BV_channel11", infile_50um, "timeDiff_vs_BV", "50umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[2]+"   ", ylabel="Time resolution [ps]", color=ROOT.kGreen+2, unit=1000.0, doGaus=True, rm_photek=True),
        HistoInfo("timeDiff_vs_BV_channel20", infile_50um, "timeDiff_vs_BV", "50umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=ylength, title=legend_entry[2]+"   ", ylabel="Time resolution [ps]", color=ROOT.kGreen+2, unit=1000.0, doGaus=True, rm_photek=True, markerStyle=ROOT.kOpenCircle),
    ],
    [
        HistoInfo("slewrate_vs_BV_channel01", infile_20um, "slewrate_vs_BV", "20umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[0]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kBlack,   doGaus=False),
        HistoInfo("slewrate_vs_BV_channel20", infile_20um, "slewrate_vs_BV", "20umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[0]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kBlack,   doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("slewrate_vs_BV_channel01", infile_30um, "slewrate_vs_BV", "30umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[1]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kRed,     doGaus=False),
        HistoInfo("slewrate_vs_BV_channel20", infile_30um, "slewrate_vs_BV", "30umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[1]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kRed,     doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("slewrate_vs_BV_channel11", infile_50um, "slewrate_vs_BV", "50umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[2]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kGreen+2, doGaus=False),
        HistoInfo("slewrate_vs_BV_channel20", infile_50um, "slewrate_vs_BV", "50umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=0.0, yMax=320.0, title=legend_entry[2]+"   ", ylabel="Slewrate [mV/ns]", color=ROOT.kGreen+2, doGaus=False, markerStyle=ROOT.kOpenCircle),
    ],
    [
        HistoInfo("amp_vs_BV_channel01", infile_20um, "amp_vs_BV", "20umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[0]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kBlack,   doLanGaus=True),
        HistoInfo("amp_vs_BV_channel20", infile_20um, "amp_vs_BV", "20umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[0]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kBlack,   doLanGaus=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("amp_vs_BV_channel01", infile_30um, "amp_vs_BV", "30umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[1]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kRed,     doLanGaus=True),
        HistoInfo("amp_vs_BV_channel20", infile_30um, "amp_vs_BV", "30umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[1]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kRed,     doLanGaus=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("amp_vs_BV_channel11", infile_50um, "amp_vs_BV", "50umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[2]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kGreen+2, doLanGaus=True),
        HistoInfo("amp_vs_BV_channel20", infile_50um, "amp_vs_BV", "50umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=260.0, title=legend_entry[2]+"   ", ylabel="MPV Amplitude [mV]", color=ROOT.kGreen+2, doLanGaus=True, markerStyle=ROOT.kOpenCircle),
    ],
    [
        HistoInfo("baselineRMS_vs_BV_channel01", infile_20um, "baselineRMS_vs_BV", "20umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[0]+"   ", ylabel="Noise [mV]", color=ROOT.kBlack,   doGaus=False),
        HistoInfo("baselineRMS_vs_BV_channel20", infile_20um, "baselineRMS_vs_BV", "20umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[0]+"   ", ylabel="Noise [mV]", color=ROOT.kBlack,   doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("baselineRMS_vs_BV_channel01", infile_30um, "baselineRMS_vs_BV", "30umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[1]+"   ", ylabel="Noise [mV]", color=ROOT.kRed,     doGaus=False),
        HistoInfo("baselineRMS_vs_BV_channel20", infile_30um, "baselineRMS_vs_BV", "30umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[1]+"   ", ylabel="Noise [mV]", color=ROOT.kRed,     doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("baselineRMS_vs_BV_channel11", infile_50um, "baselineRMS_vs_BV", "50umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[2]+"   ", ylabel="Noise [mV]", color=ROOT.kGreen+2, doGaus=False),
        HistoInfo("baselineRMS_vs_BV_channel20", infile_50um, "baselineRMS_vs_BV", "50umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=1.0, yMax=3.0, title=legend_entry[2]+"   ", ylabel="Noise [mV]", color=ROOT.kGreen+2, doGaus=False, markerStyle=ROOT.kOpenCircle),
    ],
    [
        HistoInfo("risetime_vs_BV_channel01", infile_20um, "risetime_vs_BV", "20umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[0]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kBlack,   doGaus=False),
        HistoInfo("risetime_vs_BV_channel20", infile_20um, "risetime_vs_BV", "20umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[0]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kBlack,   doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("risetime_vs_BV_channel01", infile_30um, "risetime_vs_BV", "30umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[1]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kRed,     doGaus=False),
        HistoInfo("risetime_vs_BV_channel20", infile_30um, "risetime_vs_BV", "30umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[1]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kRed,     doGaus=False, markerStyle=ROOT.kOpenCircle),
        HistoInfo("risetime_vs_BV_channel11", infile_50um, "risetime_vs_BV", "50umFNAL", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[2]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kGreen+2, doGaus=False),
        HistoInfo("risetime_vs_BV_channel20", infile_50um, "risetime_vs_BV", "50umUCSC", doFits=False, xMin=xmin, xMax=xmax, yMin=200.0, yMax=900.0, title=legend_entry[2]+"   ", ylabel="Risetime [ps] (10 to 90%)", color=ROOT.kGreen+2, doGaus=False, markerStyle=ROOT.kOpenCircle),
    ],
    [
        HistoInfo("jitter_vs_BV_channel01", infile_20um, "jitter_vs_BV", "20umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[0]+"   ", ylabel="Jitter [ps]", color=ROOT.kBlack,   doLanGaus=True),
        HistoInfo("jitter_vs_BV_channel20", infile_20um, "jitter_vs_BV", "20umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[0]+"   ", ylabel="Jitter [ps]", color=ROOT.kBlack,   doLanGaus=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("jitter_vs_BV_channel01", infile_30um, "jitter_vs_BV", "30umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[1]+"   ", ylabel="Jitter [ps]", color=ROOT.kRed,     doLanGaus=True),
        HistoInfo("jitter_vs_BV_channel20", infile_30um, "jitter_vs_BV", "30umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[1]+"   ", ylabel="Jitter [ps]", color=ROOT.kRed,     doLanGaus=True, markerStyle=ROOT.kOpenCircle),
        HistoInfo("jitter_vs_BV_channel11", infile_50um, "jitter_vs_BV", "50umFNAL", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[2]+"   ", ylabel="Jitter [ps]", color=ROOT.kGreen+2, doLanGaus=True),
        HistoInfo("jitter_vs_BV_channel20", infile_50um, "jitter_vs_BV", "50umUCSC", xMin=xmin, xMax=xmax, yMin=0.0, yMax=60.0, title=legend_entry[2]+"   ", ylabel="Jitter [ps]", color=ROOT.kGreen+2, doLanGaus=True, markerStyle=ROOT.kOpenCircle),
    ],
]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
pad_margin = myStyle.GetMargin()
print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_BiasScan0/")

nXBins = all_histoInfos[0][0].th2.GetXaxis().GetNbins()

#loop over X bins
for i in range(1, nXBins+1):
    for histoInfos in all_histoInfos:
        for info in histoInfos:
            totalEvents = info.th2.GetEntries()
            tmpHist = info.th2.ProjectionY("py",i,i)
            myRMS = tmpHist.GetRMS()
            myMean = tmpHist.GetMean()
            nEvents = tmpHist.GetEntries()
            fitlow = myMean - 1.5*myRMS # 1.5 - 2.4
            fithigh = myMean + 1.5*myRMS # 1.5 - 2.4
            value = info.unit*myMean
            error = info.unit*tmpHist.GetMeanError()

            minEvtsCut = 0.0
            # minEvtsCut = totalEvents/nXBins
            # if i==1:
            #     print(info.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")

            #Do fit 
            if(info.doFits):
                if(nEvents > minEvtsCut):
                    if info.doLanGaus:
                        tmpHist.Rebin(2)
                        fit = fitLangaus.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
                        value = fit.GetParameter(1)
                        error = fit.GetParError(1)
                    elif info.doGaus:
                        #tmpHist.Rebin(2)
                        fit = TF1('fit','gaus',fitlow,fithigh)
                        tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                        myFitMean = fit.GetParameter(1)
                        myFitMeanError = fit.GetParError(1)
                        mySigma = fit.GetParameter(2)
                        mySigmaError = fit.GetParError(2)
                        if info.getGausMean:
                            value = info.unit*myFitMean
                            error = info.unit*myFitMeanError
                        else:
                            value = info.unit*mySigma
                            error = info.unit*mySigmaError

                    #For Debugging
                    if (debugMode):
                        tmpHist.Draw("hist")
                        fit.Draw("same")
                        volt = info.th1.GetXaxis().GetBinLowEdge(i)
                        canvas.SaveAs("%sq_%s-%iV.gif"%(outdir_q, info.th1.GetName(), volt))
                        print("%s - %iV: %.2f +/- %.2f"%(info.th1.GetName(), volt, value, error))
                else:
                    value = 0.0
                    error = 0.0

            # Removing telescope contribution
            if value!=0.0 and info.rm_photek:
                error = error*value/TMath.Sqrt(value*value - 10*10)
                value = TMath.Sqrt(value*value - 10*10)

            info.th1.SetBinContent(i,value)
            info.th1.SetBinError(i,error)
                 
# Plot 2D histograms
for histoInfos in all_histoInfos:
    info_ref = histoInfos[0]
    htemp = TH1F("htemp", "", 1, info_ref.xMin, info_ref.xMax)
    htemp.SetLineColor(kWhite)
    htemp.SetStats(0)
    htemp.GetYaxis().SetRangeUser(info_ref.yMin, info_ref.yMax)
    htemp.GetXaxis().SetTitle(info_ref.xlabel)
    htemp.GetYaxis().SetTitle(info_ref.ylabel)
    htemp.Draw("axis")

    legend_height = 0.058*(len(sensors) + 2) # Entries + title
    legend = TLegend(0.15,1-pad_margin-legend_height-0.03, 0.9,1-pad_margin-0.03)
    legend.SetBorderSize(1)
    legend.SetNColumns(2)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
    legendHeader = "%s #bf{for different boards}"%(legend_entry[-1])
    legend.SetHeader(legendHeader, "C")
    gPad.RedrawAxis("g")

    for i,info in enumerate(histoInfos):
        if i==0:
            mark = TGraph(info.th1)
            mark.SetMarkerColor(kGray)
            mark.SetLineColor(kGray)
            mark.SetMarkerSize(0)
            legend.AddEntry(mark, "FNAL board", "p")
            mark.SetMarkerStyle(ROOT.kOpenCircle)
            legend.AddEntry(mark, "UCSC board", "p")
        legend.AddEntry(info.th1, info.title, "ep")
        info.th1.Draw("LPEX0 same")
    legend.Draw()
    # else:
    #     info = info_ref
    #     info.th2.SetStats(0)
    #     tp = info.th2.ProfileX()
    #     tp.SetLineColor(ROOT.kRed)
    #     ROOT.gPad.SetRightMargin(0.15)
    #     info.th2.Draw("colz same")
    #     tp.Draw("same")

    sensor_prod = "Pixel sensors"
    myStyle.BeamInfo() 
    myStyle.SensorProductionInfo(sensor_prod)
    htemp.Draw("axis same")

    # canvas.SaveAs("%s%s.gif"%(outdir, info.outHistoName))
    canvas.SaveAs("%s%s.pdf"%(outdir, info.outHistoName))
    htemp.Delete()
