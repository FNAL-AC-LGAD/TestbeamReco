from ROOT import TFile,TTree,TCanvas,TColor,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import time

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

gROOT.ForceStyle()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
options, args = parser.parse_args()

file = options.file

# color_RGB = [[0,119,187],[51,187,238],[0,153,136],[238,119,51],[204,51,17],[238,51,119]]
# [blue, cyan, teal, orange, red, magenta]

color_RGB = [[51,34,136],[51,187,238],[17,119,51],[153,153,51],[204,102,119],[136,34,85]]
# [indigo, cyan, green, olive, rose, wine]
color_list = []

for i in range(0,len(color_RGB)):
    c = TColor.GetColor(color_RGB[i][0],color_RGB[i][1],color_RGB[i][2])
    color_list.append(c)

# color = [416+2, 432+2, 600, 880, 632, 400+2]
# [kGreen+2, kCyan+2, kBlue, kViolet, kRed, kYellow]

gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

#Make final plots
inputfile = TFile("../test/"+file,"READ")  
for s in range(6):
    plotList_amplitude  = []
    canvas = TCanvas("canv"+str(s),"canv"+str(s),800,800)
    # canvas.SetLeftMargin(0.12)
    # canvas.SetBottomMargin(0.12)
    canvas.SetLogy()
    for ch in range(6):
        hamp = inputfile.Get("amp0"+str(s)+"From"+str(ch))
        hamp.Scale(1./hamp.Integral())
        hamp.SetLineColor(color_list[ch])
        hamp.SetLineWidth(2)
        if ch!=s:
            hamp.SetLineStyle(3)
            hamp.SetLineWidth(3)

        hamp.SetStats(0)
        hamp.SetTitle("")
        # hamp.GetYaxis().SetTitleSize(0.05)
        # hamp.GetYaxis().SetLabelSize(0.035)
        # hamp.GetYaxis().SetTitleOffset(1.0)
        hamp.GetYaxis().SetTitle("Event/Total events")
        hamp.GetYaxis().SetRangeUser(0.0005,0.2)
        # hamp.GetXaxis().SetTitleSize(0.05)
        # hamp.GetXaxis().SetLabelSize(0.035)
        # hamp.GetXaxis().SetTitleOffset(0.95)
        hamp.GetXaxis().SetRangeUser(0.,60.)
        hamp.GetXaxis().SetTitle("amp [mV]")
        plotList_amplitude.append(hamp)
        hamp.Draw("hist same")
    legend = TLegend(0.70,0.65,0.95,0.90)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextSize(0.04)
    for n in range(0,len(plotList_amplitude)):
        legend.AddEntry(plotList_amplitude[n], "Strip "+str(n))
    legend.Draw();
    canvas.SaveAs("ampCh"+str(s)+"Norm.gif")
    canvas.SaveAs("ampCh"+str(s)+"Norm.pdf")

