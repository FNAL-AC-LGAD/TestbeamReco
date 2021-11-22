from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,TH1
import ROOT
import os
from stripBox import getStripBox
import optparse
ROOT.gROOT.SetBatch(True)


gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
gStyle.SetPadTopMargin(0.05)    #0.05
gStyle.SetPadRightMargin(0.05)  #0.05
gStyle.SetPadBottomMargin(0.1)  #0.16
gStyle.SetPadLeftMargin(0.1)   #0.16

gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

font=43 # Helvetica
tsize=28
gStyle.SetTextFont(font)
gStyle.SetLabelFont(font,"x")
gStyle.SetTitleFont(font,"x")
gStyle.SetLabelFont(font,"y")
gStyle.SetTitleFont(font,"y")
gStyle.SetLabelFont(font,"z")
gStyle.SetTitleFont(font,"z")

gStyle.SetTextSize(tsize)
gStyle.SetLabelSize(tsize,"x")
gStyle.SetTitleSize(tsize,"x")
gStyle.SetLabelSize(tsize,"y")
gStyle.SetTitleSize(tsize,"y")
gStyle.SetLabelSize(tsize,"z")
gStyle.SetTitleSize(tsize,"z")

gStyle.SetTitleXOffset(1.0)
gStyle.SetTitleYOffset(1.4)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)

gStyle.SetGridColor(921)
gStyle.SetGridStyle()

gROOT.ForceStyle()

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0, title="", xlabel="AC-LGAD Reconstructed Postition [mm]", ylabel="Resolution [#mum]"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift())

    def getTH2(self, f, name):
        th2 = f.Get(name)
        th2.RebinX(2)
        return th2

    def getTH1(self, th2, name, centerShift):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift,th2.GetXaxis().GetXmax()-centerShift)
        return th1_temp

    def shift(self):
        return (self.f.Get("stripBoxInfo00").GetMean(1)+self.f.Get("stripBoxInfo01").GetMean(1))/2.

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
options, args = parser.parse_args()

file = options.file

inputfile = TFile("../test/"+file)

all_histoInfos = [
    HistoInfo("deltaX_vs_Xtrack",    inputfile, "track",    True,  70.0, "AC-LGAD Reconstructed Position", "Relative X position [mm]"),
    HistoInfo("deltaX_vs_Xreco",     inputfile, "reco",     True,  70.0, "AC-LGAD Reconstructed Position", "Reconstructed relative X position [mm]")
]

canvas = TCanvas("cv","cv",800,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
#ROOT.gPad.SetLogx()
#ROOT.gPad.SetLogy()
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
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = myRMSError

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
                #canvas.SetLogy()
                #canvas.SaveAs("q_"+str(i)+".gif")
                
                #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
            else:
                value *= 1000.0
                error *= 1000.0
        else:
            value = 0.0
            error = 0.0

        if i<=info.th1.FindBin(-0.25) or i>=info.th1.FindBin(0.25):
            value = 0.0
            error = 0.0

        # Removing telescope contribution
        if value!=0.0:
            error = error*value/TMath.Sqrt(value*value - 7*7)
            value = TMath.Sqrt(value*value - 7*7)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile("xRecoDiffVsX.root","RECREATE")
for info in all_histoInfos:
    #info.th1.Rebin(3)
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(info.yMax)
    info.th1.SetLineColor(kBlack)
    info.th1.SetTitle(info.title)
    info.th1.GetXaxis().SetTitle(info.xlabel)
    info.th1.GetXaxis().SetRangeUser(-0.63, 0.63)
    info.th1.GetYaxis().SetTitle(info.ylabel)

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
    boxes = getStripBox(inputfile,ymin,ymax,False,18,False,info.shift())
    for box in boxes:
        box.Draw()
   
    boxes2 = getStripBox(inputfile,ymin,ymax,True,ROOT.kRed,False,info.shift())
    for box in boxes2:
        box.Draw("same")

    gPad.RedrawAxis("g")
    
    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    canvas.SaveAs("PositionRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs("PositionRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()

outputfile.Close()

