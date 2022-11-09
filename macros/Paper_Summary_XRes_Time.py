from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TLine,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import os
from stripBox import getStripBox
import optparse
import myStyle
import math
from array import array

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0, title="", xlabel="", ylabel="Position resolution [#mum]", sensor="", addShift = False):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor), addShift)
        self.fine_tune = self.fine_tuning(sensor)
        self.sensor = sensor

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)
        return th2

    def getTH1(self, th2, name, centerShift, fine_value, shift):
        if shift:
            th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-fine_value,th2.GetXaxis().GetXmax()-fine_value) # -centerShift
        else:
            th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin(),th2.GetXaxis().GetXmax()) # -centerShift
        return th1_temp

    def shift(self):
        real_center = self.f.Get("stripBoxInfo03").GetMean(1)
        if not self.f.Get("stripBoxInfo06"): real_center = (self.f.Get("stripBoxInfo02").GetMean(1) + real_center)/2.
        return real_center

    def fine_tuning(self, sensor):
        # value = 0.0
        value = self.th2.GetXaxis().GetBinWidth(2)/2.
        if "1cm_500up_300uw" in sensor: value = 0.0
        elif "1cm_500up_100uw" in sensor: value = self.shift()
        # if sensor=="BNL2020": value = 0.0075
        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.2, help="X axis range [-x, x]")
parser.add_option('-y','--ylength', dest='ylength', default = 160.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
options, args = parser.parse_args()

useShift = options.noShift
dataset = options.Dataset
outdir=""
outdir = myStyle.getOutputDir(dataset)

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']
strip_width  = sensor_Geometry['stripWidth']
strip_length  = sensor_Geometry['length']

xlength = float(options.xlength)
ylength = float(options.ylength)
# ylength = 200.0
# ylength = 80.0
debugMode = options.debugMode
pref_hotspot = "_hotspot" if (options.hotspot) else ""

Analyze_infile = TFile("%s%s_Analyze.root"%(outdir,dataset))

XRes_indir = myStyle.GetPlotsDir(outdir, "Paper_XRes/")
XRes_infile = TFile("%sPlotXRes%s.root"%(XRes_indir, pref_hotspot))

Time_indir = myStyle.GetPlotsDir(outdir, "Paper_TimeRes/")
Time_infile = TFile("%stimeDiffVsX%s.root"%(Time_indir, pref_hotspot))

### Draw canvas
canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

# outdir = myStyle.GetPlotsDir(outdir, "Paper_XRes/")

## Get hists
h_XRes_exp = XRes_infile.Get("h_exp")
h_XRes_twoStrip = XRes_infile.Get("h_twoStrip")
# l_exp_sqrt12 = XRes_infile.Get("l_sqrt12")

h_time = Time_infile.Get("h_time")

### Create oneStripRes curve (this is per channel)

this_shift = 0

if useShift:
    # max_strip_edge = Analyze_infile.Get("stripBoxInfo01").GetMean(1) + strip_width/2000.
    real_center = Analyze_infile.Get("stripBoxInfo03").GetMean(1)
    if not Analyze_infile.Get("stripBoxInfo06"): real_center = (Analyze_infile.Get("stripBoxInfo02").GetMean(1) + real_center)/2.
    # max_strip_edge -= real_center
    this_shift = real_center



# ### Create oneStripRes curve (this is per channel)
# this_shift = hist_info_twoStrip.shift() if useShift else 0
# boxes = getStripBox(inputfile,0.0,hist_info_twoStrip.yMax,False,18,True,this_shift)

boxes = getStripBox(Analyze_infile,0.0,ylength,False,18,True,this_shift)

# oneStripBins = [-1.00, -0.50, 0.00, 0.50, 1.00] if strip_width==300 else [-1.25, -0.75, -0.25, 0.25, 0.75, 1.25]
# oneStripHist = TH1F("oneStripRes","", len(oneStripBins)-1, array('f',oneStripBins))
# oneStripHist.SetLineWidth(3)
# # oneStripHist.SetLineStyle(1)
# oneStripHist.SetLineColor(colors[0])

## This was for using in oneStripReco. No longer needed
# for i,box in enumerate(boxes):
#     if (i!=0 and i!=(len(boxes)-1)):
#         xl = box.GetX1()
#         xr = box.GetX2()
#         oneStripHist.Fill(xl, oneStripResValue_list[i])

# Get lines with binary readout in the sensor, binary readout in the strip, and oneStripReco

# binary_readout_res_sensor = ROOT.TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
# binary_readout_res_sensor.SetLineWidth(3)
# binary_readout_res_sensor.SetLineStyle(7)
# binary_readout_res_sensor.SetLineColor(colors[4]) #kGreen+2 #(TColor.GetColor(136,34,85))

# Plot 2D histograms
outdir = myStyle.getOutputDir("Paper2022")
# outputfile = TFile(outdir+"Summary_XRes_and_Time.root","RECREATE")

htemp = TH1F("htemp","",1,-xlength,xlength)
htemp.SetStats(0)
# htemp.SetMinimum(0.0)
# htemp.SetMaximum(info.yMax)
htemp.GetYaxis().SetRangeUser(0.0, ylength)
# htemp.SetLineColor(kBlack)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetTitle("Position resolution [#mum]")

# Add right axis (Time)
right_axis = ROOT.TGaxis(xlength,0.0001,xlength,ylength,0.0001,ylength,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Time resolution [ps]")
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())
right_axis.SetLineColor(colors[4]) ## Check: Use the same color as time-line?
right_axis.SetLabelColor(colors[4])
right_axis.Draw()

## Prepare histogram styles
h_XRes_twoStrip.SetLineWidth(3)
h_XRes_twoStrip.SetLineColor(colors[2])

h_time.SetLineWidth(3)
h_time.SetLineColor(colors[4]) ## Check colors

# l_exp_sqrt12.SetLineWidth(3)
# l_exp_sqrt12.SetLineColor(colors[1])


htemp.Draw("AXIS")

for i,box in enumerate(boxes):
    if (i!=0 and i!=(len(boxes)-1)):
        box.Draw()

gPad.RedrawAxis("g")

h_XRes_twoStrip.Draw("hist e same")
h_time.Draw("hist e same")
# l_exp_sqrt12.Draw()

legend = TLegend(myStyle.GetPadCenter()-0.25,1-myStyle.GetMargin()-0.25, myStyle.GetPadCenter()+0.25,1-myStyle.GetMargin()-0.05)
# legend.SetBorderSize(0)
# legend.SetFillColor(kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
#legend.SetFillStyle(0)

# legend.AddEntry(l_exp_sqrt12, "Pitch / #sqrt{12}","l")
legend.AddEntry(h_XRes_twoStrip, "Position resolution","l")
legend.AddEntry(h_time,"Time resolution","l")

# legend.AddEntry(weighted_hist, "Effective resolution","l")
    
htemp.Draw("AXIS same")
right_axis.Draw()
legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, myStyle.GetMargin())

canvas.SaveAs("%sSummary_XRes_Time_vs_x%s_%s.gif"%(outdir, pref_hotspot, dataset))
canvas.SaveAs("%sSummary_XRes_Time_vs_x%s_%s.pdf"%(outdir, pref_hotspot, dataset))
# hist_info_twoStrip.th1.Write()
htemp.Delete()

# outputfile.Close()

