from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import time

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="Name of the file from where the plots are retrieved")
options, args = parser.parse_args()

file = options.file

color = [416+2, 432+2, 600, 880, 632, 400+2]
# [kGreen+2, kCyan+2, kBlue, kViolet, kRed, kYellow]

gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

#Make final plots
inputfile = TFile("../test/"+file,"READ")  
for s in range(6):
    plotList_amplitude  = []
    canvas = TCanvas("canv"+str(s),"canv"+str(s),800,800)
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.12)
    canvas.SetLogy()
    for ch in range(6):
        hamp = inputfile.Get("amp0"+str(s)+"From"+str(ch))
        hamp.Scale(1./hamp.Integral())
        hamp.SetLineColor(color[ch])
        hamp.SetLineWidth(2)
        if ch!=s: hamp.SetLineStyle(2) 
        hamp.SetTitleSize(0.1)
        hamp.SetTitle("Amplitude in channel "+str(s)+" from neighbors")# if ch==5 else hamp.SetTitle("")
        hamp.SetStats(0)
        hamp.GetYaxis().SetTitleSize(0.05)
        hamp.GetYaxis().SetLabelSize(0.035)
        hamp.GetYaxis().SetTitleOffset(1.0)
        hamp.GetYaxis().SetTitle("Event/Total events")
        hamp.GetYaxis().SetRangeUser(0.0005,0.2)
        hamp.GetXaxis().SetTitleSize(0.05)
        hamp.GetXaxis().SetLabelSize(0.035)
        hamp.GetXaxis().SetTitleOffset(0.95)
        hamp.GetXaxis().SetRangeUser(0.,60.)
        hamp.GetXaxis().SetTitle("amp [mV]")
        plotList_amplitude.append(hamp)
        hamp.Draw("hist same")
    legend = TLegend(0.70,0.65,0.85,0.85);
    legend.SetBorderSize(0)
    legend.SetTextSize(0.04)
    for n in range(0,len(plotList_amplitude)):
        legend.AddEntry(plotList_amplitude[n], "Strip "+str(n))
    legend.Draw();
    canvas.SaveAs("ampCh"+str(s)+"Norm.gif")

