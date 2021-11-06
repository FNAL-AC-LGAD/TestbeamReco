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
for s in range(0,6):
    plotList_wave  = []
    canvas = TCanvas("canv"+str(s),"canv"+str(s),800,800)
    canvas.SetLeftMargin(0.12)
    canvas.SetRightMargin(0.12)
    canvas.SetBottomMargin(0.12)
    for ch in range(0,6):
        hamp = inputfile.Get("wave0"+str(s)+"From"+str(ch))
        hamp.SetTitleSize(0.1)
        hamp.SetTitle("Wave form in channel "+str(s)+" from a hit in "+str(ch))
        hamp.SetStats(0)
        hamp.GetYaxis().SetTitleSize(0.05)
        hamp.GetYaxis().SetLabelSize(0.035)
        hamp.GetYaxis().SetTitleOffset(1.0)
        hamp.GetYaxis().SetTitle("Signal [mV]")
        hamp.GetYaxis().SetRangeUser(-65.,15.)
        hamp.GetXaxis().SetTitleSize(0.05)
        hamp.GetXaxis().SetLabelSize(0.035)
        hamp.GetXaxis().SetTitleOffset(0.95)
        hamp.GetXaxis().SetTitle("time in channel "+str(s)+"-PhotekTime [ns]")
        plotList_wave.append(hamp)
        hamp.Draw("colz")
        par = ""
        if (ch==0):
            par = "("
        elif (ch==5):
            par = ")"
        canvas.SaveAs("waveCh"+str(s)+".pdf"+par)
        canvas.SaveAs("waveCh"+str(s)+str(ch)+".gif")

