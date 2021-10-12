from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed
import os
from stripBox import getStripBox,getStripBoxY

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName)
        self.th1Mean = self.getTH1(self.th2, outHistoName)
        
        self.th2Y = self.getTH2(f, inHistoName, 'zy')
        self.th1Y = self.getTH1(self.th2Y, outHistoName)
        self.th1MeanY = self.getTH1(self.th2Y, outHistoName)

    def getTH2(self, f, name, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)
        return th2

    def getTH1(self, th2, name):
        return th2.ProjectionX().Clone(name)

inputfile = TFile("../test/myoutputfile.root")

all_histoInfos = [
    HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_00"),
    HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_01"),
    HistoInfo("timeDiff_vs_xy_channel10",inputfile, "channel_10"),
    HistoInfo("timeDiff_vs_xy_channel11",inputfile, "channel_11"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
    HistoInfo("weighted2_timeDiff_vs_xy", inputfile, "weighted2_time_diff"),
    HistoInfo("weighted_timeDiff_goodSig_vs_xy", inputfile, "weighted_time_goodSig"),
    HistoInfo("weighted2_timeDiff_goodSig_vs_xy", inputfile, "weighted2_time_goodSig"),
]

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
#gPad.SetLogy()
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, all_histoInfos[0].th2.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
        tmpHist = info.th2.ProjectionY("py",i,i)
        myRMS = tmpHist.GetRMS()
        myMean = tmpHist.GetMean()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = 0.0
        valueMean = myMean
        errorMean = 0.0

        #Do fit 
        if(nEvents > 50):
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myFitMean = fit.GetParameter(1)
            myFitMeanError = fit.GetParError(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
            valueMean = abs(1000.0*myFitMean)
            errorMean = 1000.0*myFitMeanError

            ##For Debugging
            #tmpHist.Draw("hist")
            #fit.Draw("same")
            #canvas.SaveAs("q_"+str(i)+".gif")
            #
            #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
        else:
            value = 0.0
            valueMean = 0.0

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
        info.th1Mean.SetBinContent(i,valueMean)
        info.th1Mean.SetBinError(i,errorMean)

#loop over Y bins
for i in range(0, all_histoInfos[0].th2Y.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
        tmpHist = info.th2Y.ProjectionY("py",i,i)
        myRMS = tmpHist.GetRMS()
        myMean = tmpHist.GetMean()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = 0.0
        valueMean = myMean
        errorMean = 0.0

        #Do fit 
        if(nEvents > 50):
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myFitMean = fit.GetParameter(1)
            myFitMeanError = fit.GetParError(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
            valueMean = abs(1000.0*myFitMean)
            errorMean = 1000.0*myFitMeanError

            ##For Debugging
            #tmpHist.Draw("hist")
            #fit.Draw("same")
            #canvas.SaveAs("q_"+str(i)+".gif")
            #
            #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
        else:
            value = 0.0
            valueMean = 0.0

        info.th1Y.SetBinContent(i,value)
        info.th1Y.SetBinError(i,error)
        info.th1MeanY.SetBinContent(i,valueMean)
        info.th1MeanY.SetBinError(i,errorMean)

# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for info in all_histoInfos:
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    info.th1.SetTitle(info.outHistoName)
    info.th1.SetMinimum(0.0)
    info.th1.SetMaximum(100.0)
    info.th1.SetLineColor(kBlack)

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
    boxes = getStripBox(inputfile,0.0,1.0,False,18,False)
    for box in boxes:
        box.Draw()

    info.th1Mean.SetLineColor(kRed)
    info.th1Mean.Draw("hist e same")
    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()
###y direction
for info in all_histoInfos:
    info.th1Y.Draw("hist e")
    info.th1Y.SetStats(0)
    info.th1Y.SetTitle(info.outHistoName)
    info.th1Y.SetMinimum(0.0)
    info.th1Y.SetMaximum(100.0)
    info.th1Y.SetLineColor(kBlack)

    ymin = info.th1Y.GetMinimum()
    ymax = info.th1Y.GetMaximum()
    boxes = getStripBoxY(inputfile,0.0,1.0)
    for box in boxes:
        box.Draw()

    info.th1MeanY.SetLineColor(kRed)
    info.th1MeanY.Draw("hist e same")
    info.th1Y.Draw("AXIS same")
    info.th1Y.Draw("hist e same")

    canvas.SaveAs("TimeRes_vs_y_"+info.outHistoName+".gif")
    canvas.SaveAs("TimeRes_vs_y_"+info.outHistoName+".pdf")
    info.th1Y.Write()


outputfile.Close()

