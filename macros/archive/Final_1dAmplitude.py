from ROOT import TFile,TTree,TCanvas,TColor,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import time
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
gStyle.SetTitleXOffset(0.9)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "HPK C2 45#mum", help="Type of sensor (BNL2020, BNL2021, HPK C2, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 170, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

# color_RGB = [[0,119,187],[51,187,238],[0,153,136],[238,119,51],[204,51,17],[238,51,119]]
# [blue, cyan, teal, orange, red, magenta]

# color_RGB = [[51,34,136],[51,187,238],[17,119,51],[153,153,51],[204,102,119],[136,34,85]]
# # [indigo, cyan, green, olive, rose, wine]
# colors = []

# for i in range(0,len(color_RGB)):
#     c = TColor.GetColor(color_RGB[i][0],color_RGB[i][1],color_RGB[i][2])
#     colors.append(c)

# color = [416+2, 432+2, 600, 880, 632, 400+2]
# [kGreen+2, kCyan+2, kBlue, kViolet, kRed, kYellow]

colors = myStyle.GetColors()

gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

#Make final plots
inputfile = TFile("../test/"+file,"READ")  
for s in range(6):
    plotList_amplitude  = []
    canvas = TCanvas("canv"+str(s),"canv"+str(s),1000,800)
    canvas.SetLogy()
    for ch in range(6):
        hamp = inputfile.Get("amp0"+str(s)+"From"+str(ch))
        hamp.Rebin(6)
        hamp.Scale(1./hamp.Integral())
        hamp.SetLineColor(colors[ch])
        # hamp.SetLineWidth(4)
        if ch==s:
            hamp.SetLineStyle(7)
        #     hamp.SetLineWidth(3)

        hamp.SetStats(0)
        hamp.SetTitle("")
        # hamp.GetYaxis().SetTitleSize(0.05)
        # hamp.GetYaxis().SetLabelSize(0.035)
        # hamp.GetYaxis().SetTitleOffset(1.0)
        hamp.GetYaxis().SetTitle("A.U.")
        hamp.GetYaxis().SetRangeUser(0.0005,1.)
        # hamp.GetXaxis().SetTitleSize(0.05)
        # hamp.GetXaxis().SetLabelSize(0.035)
        # hamp.GetXaxis().SetTitleOffset(0.95)
        hamp.GetXaxis().SetRangeUser(0.,250.)
        hamp.GetXaxis().SetTitle("Signal amplitude [mV]")
        plotList_amplitude.append(hamp)
        hamp.Draw("hist same")
    legend = TLegend(1-myStyle.GetMargin()-0.02-0.4,1-myStyle.GetMargin()-0.02-0.25,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
    legend.SetNColumns(2)
    for n in range(0,len(plotList_amplitude)):
        legend.AddEntry(plotList_amplitude[n], "Strip "+str(n+1))
    legend.Draw();
    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)
    canvas.SaveAs("ampOverCh"+str(s)+"_"+sensor+".gif")
    canvas.SaveAs("ampOverCh"+str(s)+"_"+sensor+".pdf")

