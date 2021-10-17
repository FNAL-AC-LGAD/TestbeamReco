from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,TH1
import ROOT
import os

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, color=ROOT.kBlack, yMax=30.0, title="", xlabel="AC-LGAD Reconstructed Postition [mm]", ylabel="Resolution [#mum]"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th1 = self.getTH1(f, inHistoName)
        self.th1.SetLineColor(color)

    def getTH1(self, f, name):
        th1 = f.Get(name)
        return th1

inputfile = TFile("../test/myoutputfile.root")

all_histoInfos = [
    HistoInfo("wave1", inputfile, "strip 1", False, ROOT.kRed),#, 60.0, "AC-LGAD Reconstructed Position", "Tracker Postition [mm]"),
    HistoInfo("wave2", inputfile, "strip 2", False, ROOT.kBlack),#, 60.0, "AC-LGAD Reconstructed Position", "AC-LGAD Reconstructed Postition [mm]"),
    HistoInfo("wave3", inputfile, "strip 3", False, ROOT.kBlue),#, 60.0, "Max Amplitude Strip Position",   "Tracker Postition [mm]"),
    HistoInfo("wave4", inputfile, "strip 4", False, ROOT.kGreen+2),#, 60.0, "Max Amplitude Strip Position",   "AC-LGAD Reconstructed Postition [mm]"),
    HistoInfo("wave5", inputfile, "strip 5", False, ROOT.kGray+2),#, 60.0, "Max Amplitude Strip Position",   "AC-LGAD Reconstructed Postition [mm]"),
    #HistoInfo("wave6", inputfile, "strip 6", False, ROOT.kOrange+4),#, 60.0, "Max Amplitude Strip Position",   "AC-LGAD Reconstructed Postition [mm]"),
]

canvas = TCanvas("cv","cv",1000,1000)
gPad.SetLeftMargin(0.14)
gPad.SetRightMargin(0.05)
gPad.SetTopMargin(0.08)
gPad.SetBottomMargin(0.12)
gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
#ROOT.gPad.SetLogx()
#ROOT.gPad.SetLogy()
                        
# Plo  histograms
outputfile = TFile("plots_wave.root","RECREATE")

legend = ROOT.TLegend(0.2,0.25,0.5,0.48);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)

all_histoInfos[2].th1.Draw("l")
for info in all_histoInfos:
    info.th1.Draw("l same")
    info.th1.SetStats(0)
    info.th1.Smooth(2)
    info.th1.SetLineWidth(2)
    #info.th1.SetMinimum(0.0)
    #info.th1.SetMaximum(info.yMax)
    #info.th1.SetLineColor(kBlack)
    info.th1.SetTitle("")
    #info.th1.GetXaxis().SetTitle(info.xlabel)
    #info.th1.GetYaxis().SetTitle(info.ylabel)
    legend.AddEntry(info.th1, info.outHistoName,"l")

    info.th1.Draw("AXIS same")
    info.th1.Draw("l same")

legend.Draw();


canvas.SaveAs("WavePlot_BNL2020.gif")
canvas.SaveAs("WavePlot_BNL2020.pdf")

outputfile.Close()

