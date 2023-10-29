from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 1000, help="Max Risetime value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = True, help="Run debug mode")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")

options, args = parser.parse_args()

dataset = options.Dataset
debugMode = options.debugMode
useTight = options.useTight
tight_ext = "_tight" if useTight else ""
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    print("Analyze file not found.")

colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']
xlength = float(options.xlength)
ylength = float(options.ylength)

outdirTmp = myStyle.GetPlotsDir(outdir, "Risetime_vs_X_fits/")

#Get 3D histograms

hname = "risetime_vs_xy%s"%(tight_ext)
if inputfile.Get(hname):
    th3_risetime_vs_xy = inputfile.Get(hname)

shift = inputfile.Get("stripBoxInfo03").GetMean(1)

#Build 2D risetime vs x histograms
list_th2_risetime_vs_x = th3_risetime_vs_xy.Project3D("zx")

#Build risetime histograms
th1 = th3_risetime_vs_xy.ProjectionX().Clone("th1")
th1_Nbins = th1.GetXaxis().GetNbins()
th1_Xmin = th1.GetXaxis().GetXmin() - shift
th1_Xmax = th1.GetXaxis().GetXmax() - shift
print(th1_Xmin)
print(th1_Xmax)
list_risetime_vs_x = TH1F("risetime_vs_x%s"%(tight_ext),"", th1_Nbins, th1_Xmin, th1_Xmax)

print ("Risetime vs X: " + str(th1.GetXaxis().GetBinLowEdge(1) - shift) + " -> " + str(th1.GetXaxis().GetBinUpEdge(th1.GetXaxis().GetNbins()) - shift))

print("Setting up Langaus")
fit = langaus.LanGausFit()
print("Setup Langaus")
canvas = TCanvas("cv","cv",1000,800)

n_channels = 0
#loop over X,Y bins

totalEvents = list_th2_risetime_vs_x.GetEntries()
for i in range(1, list_risetime_vs_x.GetXaxis().GetNbins()+1):
    tmpHist = list_th2_risetime_vs_x.ProjectionY("py",i,i)
    myTotalEvents=tmpHist.Integral()
    myMean = tmpHist.GetMean()
    myRMS = tmpHist.GetRMS()
    value = myMean            
    nEvents = tmpHist.GetEntries()

    nXBins = th1_Nbins
    minEvtsCut = 0.5*totalEvents/nXBins
    if i==1: print("nEvents > %.2f (Total events: %i; N bins: %i)"%(minEvtsCut,totalEvents,nXBins))

    if(nEvents > minEvtsCut):
        tmpHist.Rebin(2)
        
        myLanGausFunction = fit.fit(tmpHist, fitrange=(myMean-1*myRMS,myMean+3*myRMS))
        myMPV = myLanGausFunction.GetParameter(1)
        value = myMPV

        ##For Debugging
        if(debugMode):
            tmpHist.Draw("hist")
            myLanGausFunction.Draw("same")
            canvas.SaveAs(outdirTmp+"q_"+str(i)+".gif")
    else:
        value = 0.0

    value = value if(value>0.0) else 0.0

    list_risetime_vs_x.SetBinContent(i,value)
                    
# Save risetime histograms
outputfile = TFile("%sPlotRisetimeVsX.root"%(outdir),"RECREATE")
list_risetime_vs_x.Write()

outputfile.Close()

#Make final plots
print(outdir)
plotfile = TFile("%sPlotRisetimeVsX.root"%(outdir),"READ")
plotList_risetime_vs_x = plotfile.Get("risetime_vs_x%s"%(tight_ext))
plotList_risetime_vs_x.SetLineWidth(2)

totalRisetime_vs_x = TH1F("htemp","",1,-xlength,xlength)
totalRisetime_vs_x.Draw("hist")
totalRisetime_vs_x.SetStats(0)
totalRisetime_vs_x.SetTitle("")
totalRisetime_vs_x.GetXaxis().SetTitle("Track x position [mm]")
totalRisetime_vs_x.GetYaxis().SetTitle("Risetime [ps]")
totalRisetime_vs_x.SetLineWidth(2)

totalRisetime_vs_x.SetMaximum(ylength)

boxes = getStripBox(inputfile,0,ylength-10.0,False, 18, True, shift)
for box in boxes:
   box.Draw()
totalRisetime_vs_x.Draw("AXIS same")
totalRisetime_vs_x.Draw("hist same")


legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)

plotList_risetime_vs_x.Draw("hist same")

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"Risetime_vs_x_"+sensor+".gif")