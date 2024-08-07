from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TLine,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import os
from stripBox import getStripBox
import optparse
import myStyle
import math
from array import array
import myFunctions as mf

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 1.2, help="X axis range [-x, x]")
parser.add_option('-y','--ylength', dest='ylength', default = 160.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']
strip_width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']

xlength = float(options.xlength)
ylength = float(options.ylength)

is_hotspot = options.hotspot
if is_hotspot:
    print(" >> (!) Hotspot not implemented (!)")

# Get position of the central channel in the "x" direction
position_center = mf.get_central_channel_position(inputfile, "x")


# Get Position resolution histogram
# ---------------------------------

# Define input file
indir_position = myStyle.GetPlotsDir(outdir, "CombinedResolution_PosMethod1/")
input_path_position = "%sCombinedPositionResVsX_tight.root"%(indir_position)

if not os.path.exists(input_path_position):
    print(" >> Summary plot uses Resolution X with tight cuts. File was not found!")
    exit()

inputfile_position = TFile(input_path_position, "READ")
hResolution_position = inputfile_position.Get("CombinedPosRes")
hResolution_position.SetLineWidth(3)
hResolution_position.SetLineColor(colors[2])

# inputfile_res = TFile("../output/Compare/ResolutionPosVsX/"+saveName+".root", "READ")
# hResolution_Oneposition = inputfile_res.Get("h_one_strip")
# hResolution_Oneposition.SetMarkerStyle(33)
# hResolution_Oneposition.SetMarkerSize(3)
# hResolution_Oneposition.SetMarkerColor(colors[0]) ## Check colors

# hResolution_Twoposition = inputfile_res.Get("track_twoStrip")
# hResolution_Twoposition.SetLineWidth(3)
# hResolution_Twoposition.SetLineColor(colors[1]) ## Check colors

hResolution_Oneposition = inputfile_position.Get("track_oneStrip_resolution")
hResolution_Oneposition.SetMarkerStyle(33)
hResolution_Oneposition.SetMarkerSize(3)
hResolution_Oneposition.SetMarkerColor(colors[0])

hResolution_Twoposition = inputfile_position.Get("track_twoStrip_resolution")
hResolution_Twoposition.SetLineWidth(3)
hResolution_Twoposition.SetLineColor(colors[1])

# Get Time resolution histogram
# ---------------------------------

# Define input file
indir_time = myStyle.GetPlotsDir(outdir, "Resolution_Time/")
input_path_time = "%sTimeDiffVsX_tight.root"%(indir_time)

if not os.path.exists(input_path_time):
    print(" >> Summary plot uses Resolution Time with tight cuts. File was not found!")
    exit()

inputfile_time = TFile(input_path_time, "READ")
hResolution_time = inputfile_time.Get("Time_DiffW2Tracker")
hResolution_time.SetLineWidth(3)
hResolution_time.SetLineColor(colors[4]) ## Check colors


# Draw histograms together
# ------------------------

canvas = TCanvas("cv", "cv", 1000, 800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

# Define hist for axes style
htemp = TH1F("htemp", "", 1, -xlength, xlength)
htemp.SetStats(0)
# htemp.SetMinimum(0.0)
# htemp.SetMaximum(info.yMax)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetRangeUser(0.0, ylength)

htemp.Draw("AXIS")

# Add left axis (Position)
left_axis = htemp.GetYaxis()
left_axis.SetTitle("Position resolution [#mum]")
left_axis.SetLabelSize(myStyle.GetSize()-4)
left_axis.SetTitleSize(myStyle.GetSize())
left_axis.SetLabelFont(myStyle.GetFont())
left_axis.SetTitleFont(myStyle.GetFont())
left_axis.SetAxisColor(colors[2])
left_axis.SetLabelColor(colors[2])
left_axis.SetRangeUser(0.0001, ylength)
left_axis.Draw()

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
right_axis.SetTitleOffset(1.3)
right_axis.Draw()

xlimit = 0
# Draw gray bars in the background (Position of metallic sections)
boxes = getStripBox(inputfile, 0.0001, ymax=ylength, pitch=pitch/1000.)
if ("500x500" not in dataset) and ("pad" not in dataset):
    boxes = boxes[1:len(boxes)-1]
    xlimit = abs((boxes[0].GetX1() + boxes[0].GetX2())/2.)
    xlimit+= pitch/(2 * 1000.)
for box in boxes:
    # Don't draw strips that are outside the x-axis range
    if (box.GetX2() < -xlength) or (xlength < box.GetX1()):
        continue
    box.Draw()
gPad.RedrawAxis("g")

# Define legend
pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
# legend = TLegend(0.50-0.3, 1-pad_margin-0.25, 0.50+0.3, 1-pad_margin-0.05)
legend = TLegend(0.50-0.35, 1-pad_margin-0.27, 0.50+0.35, 1-pad_margin-0.03)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
legend.SetBorderSize(1)
legend.SetLineColor(kBlack)
# legend.SetBorderSize(0)
# legend.SetFillColor(kWhite)
# legend.SetFillStyle(0)

# Clear central region in position res for HPK_W11_22_3_20T_500x500_150M_C600 sensor
# if "HPK_W11_22_3_20T_500x500_150M_C600" in dataset:
#     for i in range(1, hResolution_position.GetXaxis().GetNbins()+1):
#         if mf.is_inside_limits(i, hResolution_position, xmax=0.1):
#             hResolution_position.SetBinContent(i, 0.0)

# Draw compared histograms using the same non-empty bins, except for certain sensors
# where the first is followed!
use_first_hist_ref = ("W11_22_3_20T" in dataset)
list_histograms = [hResolution_position, hResolution_Twoposition, hResolution_time]
pruned_position, pruned_Twoposition, pruned_time = mf.same_limits_compare(list_histograms, xlimit=xlimit, use_first_binning=use_first_hist_ref)
hResolution_Oneposition.Draw("hist P same")
pruned_Twoposition.Draw("hist e same")
pruned_position.Draw("hist e same")
legend.AddEntry(pruned_position, "Combined position resolution", "l")
legend.AddEntry(hResolution_Oneposition, "One-channel position resolution", "p")
legend.AddEntry(pruned_Twoposition, "Two-channel position resolution", "l")
pruned_time.Draw("hist e same")
legend.AddEntry(pruned_time,"Time resolution", "l")

htemp.Draw("AXIS same")
left_axis.Draw()
right_axis.Draw()
legend.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, pad_margin, isPaperPlot = True)
# myStyle.SensorInfoSmart(dataset, pad_margin)

outdir_summary = myStyle.GetPlotsDir(outdir, "Resolution_Summary/")
save_path = "%sResolutionSummary_vs_x"%(outdir_summary)

# canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)
