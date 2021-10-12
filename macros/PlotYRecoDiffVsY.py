from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack
import ROOT
import os
from stripBox import getStripBox,getStripBoxY
import optparse
ROOT.gROOT.SetBatch(True)


gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name):
        th2 = f.Get(name)
        return th2

    def getTH1(self, th2, name):
        return th2.ProjectionX().Clone(name)

inputfile = TFile("../test/myoutputfile.root")

all_histoInfos = [
    HistoInfo("deltaY_vs_Ytrack",inputfile, "deltaY_vs_Y", True, 80.0),
    HistoInfo("deltaY_vs_Yreco",inputfile, "deltaY_vs_Yreco", True, 80.0),
]

canvas = TCanvas("cv","cv",800,800)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.15)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, all_histoInfos[0].th2.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
        tmpHist = info.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = 0.0

        #Do fit 
        if(nEvents > 50):
            if(info.doFits):
                tmpHist.Rebin(2)
        
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMPV = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                error = 1000.0*mySigmaError
            
                ##For Debugging
                #tmpHist.Draw("hist")
                #fit.Draw("same")
                #canvas.SaveAs("q_"+str(i)+".gif")
                #
                #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
            else:
                value *= 1000.0
        else:
            value = 0.0

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile("plots.root","RECREATE")
for info in all_histoInfos:
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    info.th1.SetTitle(info.outHistoName)
    info.th1.SetMinimum(0.0)
    info.th1.SetMaximum(info.yMax)
    info.th1.SetLineColor(kBlack)

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
    boxes = getStripBoxY(inputfile,ymin,ymax) 
    for box in boxes:
        box.Draw()

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
   
    boxes2 = getStripBoxY(inputfile,ymin,ymax,True,ROOT.kRed)
    for box in boxes2:
        box.Draw("same")

    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    canvas.SaveAs("PositionRes_vs_y_"+info.outHistoName+".gif")
    canvas.SaveAs("PositionRes_vs_y_"+info.outHistoName+".pdf")
    info.th1.Write()

outputfile.Close()

