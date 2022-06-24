from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import os
from stripBox import getStripBox
import optparse
import myStyle
import math

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
organized_mode=True

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0, title="", xlabel="", ylabel="Position resolution [#mum]", sensor=""):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor))
        # self.sensor = sensor

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)
        return th2

    def getTH1(self, th2, name, centerShift, fine_value):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift-fine_value,th2.GetXaxis().GetXmax()-centerShift-fine_value)
        return th1_temp

    def shift(self):
        return self.f.Get("stripBoxInfo03").GetMean(1)

    def fine_tuning(self, sensor):
        value = 0.0
        if sensor=="BNL2020": value = 0.0075
        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 0, help="Bias Voltage value in [V]")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="X axis range [-x, x]") 
parser.add_option('-y','--ylength', dest='ylength', default = 10000.0, help="Y axis upper limit") 
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
bias   = sensor_Geometry['BV'] if options.biasvolt == 0 else options.biasvolt
length  = sensor_Geometry['length']*1000.0
xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

outdir = myStyle.GetPlotsDir(outdir, "PositionResY/")
if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_resY0/")

all_histoInfos = [
    HistoInfo("deltaY_vs_Ytrack",   inputfile, "track", True,  ylength, "", "Track y position [mm]","Position resolution [#mum]",sensor),
    HistoInfo("deltaYBasic_vs_Ytrack",   inputfile, "trackBasic", True,  ylength, "", "Track y position [mm]","Position resolution [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "track_oneStrip", True,  ylength, "", "Track x position [mm]","Position resolution_oneStrip [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xtrack_twoStrips",   inputfile, "track_twoStrips", True,  ylength, "", "Track x position [mm]","Position resolution_twoStrips [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xtrack",   inputfile, "rms_track", False,  ylength, "", "Track x position [mm]","Position resolution RMS [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "rms_track_oneStrip", False,  ylength, "", "Track x position [mm]","Position resolution_oneStrip RMS [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xtrack_twoStrips",   inputfile, "rms_track_twoStrips", False,  ylength, "", "Track x position [mm]","Position resolution_twoStrips RMS [#mum]",sensor),
    # HistoInfo("deltaXmax_vs_Xtrack",   inputfile, "maxtrack", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaX_vs_Xreco",    inputfile, "reco",  True, ylength, "", "Reconstructed x position [mm]","Position resolution [#mum]",sensor),
]

#### histograms for expected resolution
otherInfile = TFile("%stimeDiffVsY.root"%(outdir))
#sigma_timeDiff_vs_y = otherInfile.Get("time_diff")
sigma_timeDiff_vs_y = otherInfile.Get("time_diffTracker")

nbinsy = sigma_timeDiff_vs_y.GetNbinsX()
low_y = sigma_timeDiff_vs_y.GetBinLowEdge(1) - all_histoInfos[0].shift()
high_y = sigma_timeDiff_vs_y.GetBinLowEdge(nbinsy)- all_histoInfos[0].shift()

expected_res_vs_y = ROOT.TH1F("h_exp","",nbinsy,low_y,high_y)
for ibin in range(expected_res_vs_y.GetNbinsX()+1):
    if sigma_timeDiff_vs_y.GetBinError(ibin)>0:
        expected_res = (1/math.sqrt(2))*50.0*sigma_timeDiff_vs_y.GetBinContent(ibin)
    else:
        expected_res=0

    #print("Bin %i, res %f, %f"%(ibin,expected_res,sigma_timeDiff_vs_y.GetBinContent(ibin)))
    expected_res_vs_y.SetBinContent(ibin,expected_res)


canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

print("Finished setting up langaus fit class")

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()
#loop over X bins
for i in range(0, nXBins+1):

    for info in all_histoInfos:
        totalEvents = info.th2.GetEntries()
        tmpHist = info.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = myRMSError

        minEvtsCut = 0.5*totalEvents/nXBins

        if i==0: print(info.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")
        #Do fit 
        if(nEvents > minEvtsCut):
            if(info.doFits):
                # tmpHist.Rebin(2)
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMPV = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                error = 1000.0*mySigmaError
            
                ##For Debugging
                if (debugMode):
                    tmpHist.Draw("hist")
                    fit.Draw("same")
                    canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                    print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution: %.3f +/- %.3f"%(value, error))
            else:
                value *= 1000.0
                error *= 1000.0
                ##For Debugging
                # if (debugMode):
                #     tmpHist.Draw("hist")
                #     fit.Draw("same")
                #     canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                #     print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution_rms: %.3f +/- %.3f"%(value, error))
        else:
            value = 0.0
            error = 0.0

            #if "track_twoStrips" in info.outHistoName:
            expected_res_vs_y.SetBinContent(i,0)

        # Removing telescope contribution
        #if value>6.0:
        #    error = error*value/TMath.Sqrt(value*value - 6*6)
        #    value = TMath.Sqrt(value*value - 6*6)
        #else:
        #    value = 0.0 # 20.0 to check if there are strange resolution values
        #    error = 0.0
        #if i<=info.th1.FindBin(-0.2) and sensor=="BNL2020":
        #    value = 0.0
        #    error = 0.0

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile(outdir+"PlotRecoDiffVsY.root","RECREATE")
for info in all_histoInfos:
    htemp = TH1F("htemp","",1,-xlength,xlength)
    htemp.SetStats(0)
    htemp.SetMinimum(0.0001)
    htemp.SetMaximum(info.yMax)
    # htemp.SetLineColor(kBlack)
    htemp.GetXaxis().SetTitle(info.xlabel)
    htemp.GetYaxis().SetTitle(info.ylabel)
    # info.th1.Draw("hist e")
    # info.th1.SetStats(0)
    # info.th1.SetMinimum(0.0001)
    # info.th1.SetMaximum(info.yMax)
    info.th1.SetLineColor(kBlack)
    # info.th1.SetTitle(info.title)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    htemp.Draw("AXIS")

    ymin = info.th1.GetMinimum()
    ymax = info.yMax

    default_res = ROOT.TLine(-xlength,length/TMath.Sqrt(12),xlength,length/TMath.Sqrt(12))
    default_res.SetLineWidth(4)
    default_res.SetLineStyle(9)
    default_res.SetLineColor(416+2) #kGreen+2 #(TColor.GetColor(136,34,85))
    default_res.Draw("same")

    gPad.RedrawAxis("g")

    htemp.Draw("AXIS same")
    # info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")


    legend = TLegend(myStyle.GetPadCenter()-0.27,1-myStyle.GetMargin()-0.2,myStyle.GetPadCenter()+0.27,1-myStyle.GetMargin()-0.1)
    # legend.SetBorderSize(0)
    # legend.SetFillColor(kWhite)
    # legend.SetTextFont(myStyle.GetFont())
    # legend.SetTextSize(myStyle.GetSize())
    #legend.SetFillStyle(0)
    legend.AddEntry(default_res, "Binary readout","l")
    legend.AddEntry(info.th1, "Two-strip reconstruction")

    #if "track_twoStrips" in info.outHistoName:
    expected_res_vs_y.Draw("hist same")
    legend.AddEntry(expected_res_vs_y,"Expected resolution")
    #expected_res_vs_y.Print("all")


    legend.Draw();

    # myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    canvas.SaveAs(outdir+"PositionRes_vs_y_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"PositionRes_vs_y_"+info.outHistoName+".pdf")
    info.th1.Write()
    htemp.Delete()

outputfile.Close()

