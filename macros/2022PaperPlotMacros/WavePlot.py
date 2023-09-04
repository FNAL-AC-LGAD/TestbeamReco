from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,TH1
import ROOT
import optparse
import os
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()

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

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
options, args = parser.parse_args()

file = options.file
inputfile = TFile("../test/"+file)

colors = myStyle.GetColors()

all_histoInfos = [
    HistoInfo("wave1", inputfile, "Strip 1", False, colors[0]),
    HistoInfo("wave2", inputfile, "Strip 2", False, colors[1]),
    HistoInfo("wave3", inputfile, "Strip 3", False, colors[2]),
    HistoInfo("wave4", inputfile, "Strip 4", False, colors[3]),
    HistoInfo("wave5", inputfile, "Strip 5", False, colors[4]),
    #HistoInfo("wave6", inputfile, "strip 6", False, colors[5]),
]

canvas = TCanvas("cv","cv",1000,800)
gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
                        
# Plo  histograms
outputfile = TFile("plots_wave.root","RECREATE")

legend = ROOT.TLegend(2*myStyle.GetMargin()+0.05,2*myStyle.GetMargin()+0.05,2*myStyle.GetMargin()+0.05+0.3,2*myStyle.GetMargin()+0.05+0.4);

all_histoInfos[2].th1.Draw("l")
for info in all_histoInfos:
    info.th1.Draw("l same")
    info.th1.SetStats(0)
    info.th1.Smooth(2)
    info.th1.SetLineWidth(2)
    info.th1.SetTitle("")
    legend.AddEntry(info.th1, info.outHistoName,"l")

    info.th1.Draw("AXIS same")
    info.th1.Draw("l same")

legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo("BNL2020", 220)

canvas.SaveAs("WavePlot_BNL2020.gif")
canvas.SaveAs("WavePlot_BNL2020.pdf")

outputfile.Close()

