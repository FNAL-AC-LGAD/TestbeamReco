from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TH2D,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox,getStripBoxY
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()


dataset = options.Dataset


outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "SimpleMaps/")

#Get 3D histograms 
th3_amplitude_vs_xy = inputfile.Get("amplitude_vs_xy")
th3_charge_vs_xy = inputfile.Get("charge_vs_xy")
th3_risetime_vs_xy = inputfile.Get("risetime_vs_xy")
th3_ampChargeRatio_vs_xy = inputfile.Get("ampChargeRatio_vs_xy")
th3_timeDiff_vs_xy = inputfile.Get("timeDiff_vs_xy")
th3_deltaX_vs_xy = inputfile.Get("deltaX_vs_Xtrack_vs_Ytrack")
th3_deltaY_vs_xy = inputfile.Get("deltaY_vs_Xtrack_vs_Ytrack")


outputfile=TFile("%splotsSimpleMapsvsXY.root"%outdir,"RECREATE")


def printProjectionColZ(th3,variable_title,tag,zmin,zmax):
	th2 = th3.Project3DProfile("yx")
	if "arrival time" in variable_title: th2.Scale(1000)
	canvas = TCanvas("cv","cv",1200,800)

	canvas.SetRightMargin(0.16);
	canvas.SetBottomMargin(0.12);

	th2.SetStats(0)
	th2.SetTitle(";x [mm];y [mm]; %s"%variable_title)
	th2.SetMinimum(zmin)
	th2.SetMaximum(zmax)

	th2.Draw("colz")


	#myStyle.BeamInfo()
	myStyle.SensorInfoSmart(dataset)

	canvas.SaveAs(outdir+tag+"_VsXY.gif")
	canvas.SaveAs(outdir+tag+"_VsXY.pdf")
	canvas.SaveAs(outdir+tag+"_VsXY.root")

	th2.Write()

printProjectionColZ(th3_amplitude_vs_xy,"Mean amplitude [mV]","amp1",15,130)
printProjectionColZ(th3_amplitude_vs_xy,"Mean amplitude [mV]","amp2",20,180)
printProjectionColZ(th3_charge_vs_xy,"Mean charge [fC]","charge1",2,30)
printProjectionColZ(th3_charge_vs_xy,"Mean charge [fC]","charge2",2,20)
printProjectionColZ(th3_risetime_vs_xy,"Mean risetime [ps]","risetime1",400,700)
printProjectionColZ(th3_risetime_vs_xy,"Mean risetime [ps]","risetime2",200,500)
printProjectionColZ(th3_ampChargeRatio_vs_xy,"Mean amplitude/charge ratio","ampChargeRatio1",1.5,6.5)
printProjectionColZ(th3_ampChargeRatio_vs_xy,"Mean amplitude/charge ratio","ampChargeRatio2",1.0,10.0)
printProjectionColZ(th3_timeDiff_vs_xy,"Mean arrival time (w.r.t MCP) [ps]","meanTime1",-200,100)
printProjectionColZ(th3_timeDiff_vs_xy,"Mean arrival time (w.r.t MCP) [ps]","meanTime2",-100,60)
printProjectionColZ(th3_deltaX_vs_xy,"deltaX","deltaX",-0.1,0.1)
printProjectionColZ(th3_deltaY_vs_xy,"deltaY","deltaY",-5,5)

outputfile.Close()
