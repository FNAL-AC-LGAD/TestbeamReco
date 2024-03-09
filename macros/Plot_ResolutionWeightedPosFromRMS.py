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


def get_profX(finput, hname, is_tight):
    if is_tight:
        hname+="_tight"

    hist_vs_x = finput.Get(hname)
    mean_vs_x = hist_vs_x.ProfileX()

    return mean_vs_x


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, yMax=30.0,
                 xlabel="", ylabel="Position resolution [#mum]",
                 sensor="", center_position = 0.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.sensor = sensor
        self.center_position = center_position
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(outHistoName)

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)

        return th2

    def getTH1(self, hname):
        htitle = ";%s;%s"%(self.xlabel, self.ylabel)
        nxbin = self.th2.GetXaxis().GetNbins()
        xmin, xmax = mf.get_shifted_limits(self.th2, self.center_position)

        # Create and define th1 default style
        th1 = TH1D(hname, htitle, nxbin, xmin, xmax)
        # th1.SetStats(0)
        th1.SetMinimum(0.0001)
        th1.SetMaximum(self.yMax)
        # th1.SetLineWidth(3)
        # th1.SetLineColor(kBlack)
        # # th1.GetXaxis().SetRangeUser(-xlength,xlength)

        return th1


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.0, help="X axis range [-x, x]")
parser.add_option('-y','--ylength', dest='ylength', default = 250.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
outdirtemp=outdir
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']
strip_width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']

# Define tracker contribution
# rm_tracker True shows expected and measured curves without tracker component
rm_tracker = False
# trkr_value = 5 # um
trkr_value = 0.0 # um To avoid having this factor removed in any curve!

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

is_tight = options.useTight
if(is_tight):
    tight_postfix = "_tight"
else:
    tight_postfix = ""
# Get position of the central channel in the "x" direction
position_center = mf.get_central_channel_position(inputfile, "x")

outdir = myStyle.GetPlotsDir(outdir, "WeightedResolution_PosRMS/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["deltaX_vs_Xtrack_oneStrip", "track_oneStrip", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_twoStrip", "track_twoStrip", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_BothStrip", "track_BothReco", "Position resolution [#mum]"],
]

# if (is_tight):
#     print(" >> Using tight cuts!")
#     list_htitles = [["deltaX_vs_Xtrack_oneStrip_tight", "track_oneStrip_tight", "Position resolution [#mum]"],["deltaX_vs_Xtrack_twoStrip_tight", "track_twoStrip_tight", "Position resolution [#mum]"],
#     ["deltaX_vs_Xtrack_BothStrip_tight", "track_BothReco_tight", "Position resolution [#mum]"],
# ]

# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle, sensor=dataset, center_position=position_center)
    all_histoInfos.append(info_obj)

# Define bin limit of the histograms drawn
plot_xlimit = abs(inputfile.Get("stripBoxInfo00").GetMean(1) - position_center)
if ("pad" not in dataset) and ("500x500" not in dataset):
    plot_xlimit-= pitch/(2. * 1000)

# Get histogram for One+Two strip Reconstruction's resolution
# -------------------------------------------------------

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_ResPosVsX0/")

nbins = all_histoInfos[0].th2.GetXaxis().GetNbins()

# Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
for i in range(1, nbins+1):
    for info_entry in all_histoInfos:
        totalEvents = info_entry.th2.GetEntries()
        tmpHist = info_entry.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        # myMean = 0.0
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = 1000*TMath.Sqrt(myRMS*myRMS + myMean*myMean)
        error = myRMSError
        
        minEvtsCut = totalEvents/nbins
        if ("HPK_W9_15_2" in dataset):
            minEvtsCut = 0.25*totalEvents/nbins
        if ("500x500" in dataset):
            minEvtsCut = 0.1*totalEvents/nbins
        if ("W9_23_3_20T_500x500_300M" in dataset):
            minEvtsCut = 0.50*totalEvents/nbins

        if (i == 1):
            msg_nentries = "%s: nEvents > %.2f "%(info_entry.inHistoName, minEvtsCut)
            msg_nentries+= "(Total events: %i)"%(totalEvents)
            print(msg_nentries)
        if ((nEvents>minEvtsCut) and (debugMode)):
            gStyle.SetOptStat(1)
            tmpHist.Draw("hist")
            canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
        # Fill only when inside limits
        if not mf.is_inside_limits(i, info_entry.th1, xmax=plot_xlimit):
            continue

        info_entry.th1.SetBinContent(i, value)

weightedhist = all_histoInfos[0].th1.Clone("weighted_pos_resRMS")
for i in range(1, nbins+1):
    # Apply weights
    tmpHistBoth = all_histoInfos[2].th1
    value = tmpHistBoth.GetBinContent(i)
    # Removing tracker's contribution
    if rm_tracker and (value > trkr_value):
        # error = error*value/TMath.Sqrt(value**2 - trkr_value**2)
        value = TMath.Sqrt(value**2 - trkr_value**2)
    # Mark bins with resolution smaller than tracker
    elif (trkr_value > value) and (value > 0.0):
        print("  WARNING: Bin %i got resolution smaller than tracker (%.3f)"%(i, value))
        value = 2.0
        # error = 2.0
    weightedhist.SetBinContent(i, value)

# Define output file
output_path = "%sWeightedPositionResVsX"%(outdir)

if(is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

# Define hist for axes style
htemp = TH1F("htemp", "", 1, -xlength, xlength)
htemp.SetStats(0)
# htemp.SetMinimum(0.0)
# htemp.SetMaximum(info.yMax)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetRangeUser(0.0, ylength)
htemp.GetYaxis().SetTitle("Position resolution [#mum]")

legend_reco = "strip"

pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()

htemp.Draw("AXIS")

hist = weightedhist
hist.SetLineColor(colors[2])
hist.SetLineWidth(3)

# Draw gray bars in the background (Position of metallic sections)
boxes = getStripBox(inputfile, ymax=ylength, shift=position_center, pitch=pitch/1000.)
for box in boxes:
    box.Draw()
gPad.RedrawAxis("g")

# Create legend
legend = TLegend(pad_center-0.25, 1-pad_margin-0.385, pad_center+0.25, 1-pad_margin-0.095)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetBorderSize(0)
# legend.SetFillColor(kWhite)
# legend.SetFillStyle(0)

# Draw all other elements with Two Strip Reconstructed histogram only
if "BothReco" in info_entry.inHistoName:
    # Get correct legend for Two Strip Reco
    this_legend = "Variance, observed"
# If not twoStrip, set a default title for the legend
else:
    this_legend = info_entry.outHistoName.replace("track_", "")

# Add this entry histogram
hist.Draw("HIST SAME")
legend.AddEntry(hist, this_legend, "l")
hist.Write()

htemp.Draw("AXIS same")
legend.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, isPaperPlot=True)

save_path = "%sWeightedPositionResolution_vs_x"%(outdir)
# Choose another name if not Two Strip Reconstructed histogram
if "twoStrip" not in info_entry.inHistoName:
    save_path = "%sPosRes-%s"%(outdir, this_legend)
elif (is_tight):
    save_path+= "_tight"
canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)

canvas.Clear()

outputfile.Close()


# Open the ROOT file
file1 = TFile.Open("%sWeightedPositionResVsX.root"%(outdir))
file2 = TFile.Open("%sWeightedPositionResVsX_tight.root"%(myStyle.getOutputDir(dataset)+'WeightedResolution_Pos/'))
file3 = TFile.Open("%sPositionResVsX_tight.root"%(myStyle.getOutputDir(dataset)+'Resolution_Pos/'))
hists = []
hists.append(file1.Get("weighted_pos_resRMS"))
hists.append(file2.Get("weighted_pos_res"))
hists.append(file3.Get("track_twoStrip_tight"))
hists.append(file3.Get("h_one_strip"))

legNames = ["Combined res. 1", "Combined res. 2", "Two-strip res.", "One-strip res."]
canvas = TCanvas("cv2","cv2",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
legend2 = TLegend(pad_center-0.32, 1-pad_margin-0.285, pad_center+0.32, 1-pad_margin-0.095)
legend2.SetTextFont(myStyle.GetFont())
legend2.SetTextSize(myStyle.GetSize()-4)
legend2.SetNColumns(2)

for i in range(len(hists)):
    if(i==0):
        hists[i].Draw("hist")
        hists[i].GetXaxis().SetRangeUser(-xlength,xlength)
        hists[i].SetLineColor(colors[i])
        legend2.AddEntry(hists[i], legNames[i], "l")
    elif("One" in legNames[i]):
        hists[i].Draw("P same")
        hists[i].SetMarkerColor(colors[i])
        hists[i].SetLineStyle(1)
        hists[i].SetMarkerStyle(33)
        hists[i].SetMarkerSize(3)
        legend2.AddEntry(hists[i], legNames[i], "P")
    else:
        hists[i].Draw("hist same")
        hists[i].SetLineColor(colors[i])
        legend2.AddEntry(hists[i], legNames[i], "l")
legend2.Draw()
myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, isPaperPlot=True)
canvas.SaveAs("%scombinedplot.gif"%(myStyle.getOutputDir(dataset)+'WeightedResolution_PosRMS/'))
