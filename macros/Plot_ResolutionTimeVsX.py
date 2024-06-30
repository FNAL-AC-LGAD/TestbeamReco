from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TGaxis,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite,TH1
import os
import optparse
from stripBox import getStripBox
import myStyle
import math
import myFunctions as mf

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()


class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, yMax=30.0,
                 xlabel="Track x position [mm]", ylabel="Time resolution [ps]",
                 sensor="", center_position=0.0, direction="x"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.sensor = sensor
        self.center_position = center_position
        self.direction = direction
        if("KOJI" in sensor):
            self.th2 = self.getTH2(f, inHistoName, sensor).RebinX(2)
            print(" (!!) Using RebinX(2) to handle low stat bins!")
        else:
            self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(outHistoName)

    def getTH2(self, f, name, sensor):
        axis = "zx" if (self.direction == "x") else "zy"
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)

        # Rebin low statistics sensors
        if sensor=="BNL2020":
            th2.RebinX(5)
        elif sensor=="BNL2021":
            th2.RebinX(10)
        # Rebin for SB1, SB3:
        if "BNL_50um_1cm_450um" in sensor:
            th2.RebinX(2)

        return th2

    def getTH1(self, hname):
        htitle = ";%s;%s"%(self.xlabel, self.ylabel)
        nxbin = self.th2.GetXaxis().GetNbins()
        xmin, xmax = mf.get_shifted_limits(self.th2, self.center_position)

        # Create and define th1 default style
        th1 = TH1D(hname, htitle, nxbin, xmin, xmax)
        th1.SetStats(0)
        th1.SetMinimum(0.0001)
        th1.SetMaximum(self.yMax)
        th1.SetLineWidth(3)
        th1.SetLineColor(kBlack)
        # th1.GetXaxis().SetRangeUser(-xlength,xlength)

        return th1


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 100.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-Y', '--alongY',dest='centerAlongY', action='store_true', default = False, help="Center plots in Y direction (for pads only)")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
parser.add_option('-n', dest='useNoSum', action='store_true', default = False, help="Use no sum column")
parser.add_option('-a', dest='plotAll', action='store_true', default = False, help="Plot no delay correction and LGAD correction too")

options, args = parser.parse_args()
dataset = options.Dataset

outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']/1000.
strip_width = sensor_Geometry['stripWidth']/1000.
strip_length = sensor_Geometry['length']

# Modify time reference (Photek) contribution from resolution results
rm_tracker = True
res_photek = 10 # ps

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

is_tight = options.useTight
noSum = options.useNoSum
show_all = options.plotAll
is_hotspot = options.hotspot

use_center_y = options.centerAlongY
# Get position of the central channel in the direction requested
# (x is default and y should be useful for pads only)
direction = "x" if not use_center_y else "y"
position_center = mf.get_central_channel_position(inputfile, direction)

outdir = myStyle.GetPlotsDir(outdir, "Resolution_Time/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["timeDiff_vs_xy", "Time_Diff", "Time resolution [ps]"],
    ["timeDiffTracker_vs_xy", "Time_DiffTracker", "Time resolution [ps]"],
    ["weighted2_timeDiff_LGADXY_vs_xy", "Time_DiffW2_LGADXY", "Time resolution [ps]"],
    ["weighted2_timeDiff_tracker_vs_xy", "Time_DiffW2Tracker", "Time resolution [ps]"],
]

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    for titles in list_htitles:
        titles[0]+= "_tight"
elif (noSum):
    print(" >> Using no sum.")
    for titles in list_htitles:
        titles[0]+= "_NoSum"

# Use hotspot extension if required
if (is_hotspot):
    list_htitles = [["weighted2_timeDiff_tracker_vs_xy_hotspot", "Time_DiffW2Tracker_hotspot", "Time resolution [ps]"]]


# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle,
                         sensor=dataset, center_position=position_center, direction=direction)
    all_histoInfos.append(info_obj)

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

if debugMode:
    q_name = "q_ResTimeVs%s0/"%(direction.upper())
    outdir_q = myStyle.CreateFolder(outdir, q_name)

# Get total number of bins in x-axis to loop over (all hists have the same number, in principle)
nbins = all_histoInfos[0].th2.GetXaxis().GetNbins()

box_reference = "stripBoxInfo00" if not use_center_y else "stripBoxInfoY00"
plot_xlimit = abs(inputfile.Get(box_reference).GetMean(1) - position_center) # - strip_width/2.
if ("pad" not in dataset) and ("500x500" not in dataset):
    plot_xlimit-= pitch/2.
if ("500x500" in dataset):
    plot_xlimit+= strip_width/2.
# Loop over X bins
for i in range(1, nbins+1):
    for info_entry in all_histoInfos:
        totalEvents = info_entry.th2.GetEntries()
        # TODO: Add support for px projection in case of use of use_center_y option
        tmpHist = info_entry.th2.ProjectionY("py",i,i)
        myRMS = tmpHist.GetRMS()
        myMean = tmpHist.GetMean()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = 0.0
        valueMean = myMean
        errorMean = 0.0

        # Define minimum of bin's entries to be fitted
        minEvtsCut = totalEvents/nbins
        if ("HPK_50um" in dataset):
            minEvtsCut = 0.7*minEvtsCut
        if("20T" in dataset):
            minEvtsCut = 0.3*totalEvents/nbins
        if(sensor == "HPK_W8_1_1_50T_500x500_150M_C600"):
            minEvtsCut = 400
        # if(is_tight):
        #     minEvtsCut = 0

        if (i == 1):
            msg_nentries = "%s: nEvents > %.2f "%(info_entry.inHistoName, minEvtsCut)
            msg_nentries+= "(Total events: %i)"%(totalEvents)
            print(msg_nentries)

        #Do fit 
        if(nEvents > minEvtsCut):
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myFitMean = fit.GetParameter(1)
            myFitMeanError = fit.GetParError(1)
            valueMean = abs(1000.0*myFitMean)
            errorMean = 1000.0*myFitMeanError

            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            valueRaw = 1000.0*mySigma
            errorRaw = 1000.0*mySigmaError

            value = valueRaw
            error  = errorRaw

            # For Debugging
            if (debugMode):
                tmpHist.Draw("hist")
                fit.Draw("same")
                canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
                bin_center = info_entry.th1.GetXaxis().GetBinCenter(i)
                msg_binres = "Bin: %i (x center = %.3f)"%(i, bin_center)
                # msg_binres+= " -> Resolution: %.3f +/- %.3f"%(value, error)
                msg_binres+= " -> Entries: %.3f"%(tmpHist.GetEntries())
                print(msg_binres)
        else:
            valueMean = 0.0
            value = 0.0
            valueRaw = 0.0

        # Removing telescope contribution
        if rm_tracker and (value > 0.0):
            value = math.sqrt((value*value) - (res_photek*res_photek))
            error  = errorRaw*(valueRaw/value)

        # Fill only when inside limits
        if not mf.is_inside_limits(i, info_entry.th1, xmax=plot_xlimit):
            continue

        info_entry.th1.SetBinContent(i, value)
        info_entry.th1.SetBinError(i, error)

        # info_entry.th1Mean.SetBinContent(i,valueMean)
        # info_entry.th1Mean.SetBinError(i,errorMean)

# Define output file
output_path = "%sTimeDiffVs%s"%(outdir, direction.upper())
if (is_hotspot):
    output_path+= "_hotspot"
elif (is_tight):
    output_path+= "_tight"
elif (noSum):
    output_path+= "_noSum"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

# Define hist for axes style
htemp = TH1F("htemp", "", 1, -xlength, xlength)
htemp.SetStats(0)
htemp.GetXaxis().SetTitle("Track %s position [mm]"%(direction))
htemp.GetYaxis().SetRangeUser(0.0001, ylength)
htemp.GetYaxis().SetTitle("Time resolution [ps]")  
htemp.SetLineColor(colors[2])

# # Uncomment only if each single plot is required
# # Draw th1 separated, one in its own canvas
# for info in all_histoInfos:
#     # Draw axes
#     htemp.Draw("AXIS")

#     # ymin = info.th1.GetMinimum()
#     # ymax = ylength

#     #boxes = getStripBox(inputfile, ymin=ymin, ymax=ymax, strips=True, shift=position_center)
#     #for i,box in enumerate(boxes):
#         #if (i!=0 and i!=(len(boxes)-1)): box.Draw()

#     gPad.RedrawAxis("g")
#     info.th1.Draw("hist e same")
#     #myStyle.BeamInfo()
#     #myStyle.SensorInfoSmart(dataset)

#     save_path = "%s%s"%(outdir, info.outHistoName)
#     if (is_hotspot):
#         save_path+= "-hotspot"
#     elif (is_tight):
#         save_path+= "-tight"

#     canvas.SaveAs("%s.gif"%save_path)
#     # canvas.SaveAs("%s.pdf"%save_path)

#     canvas.Clear()


# Draw weighted2_timeDiff_tracker_vs_xy in its own canvas
for info in all_histoInfos:
    if ("weighted2_timeDiff_tracker_vs_xy" not in info.inHistoName) and (not is_hotspot):
        continue
    # Draw axes
    htemp.Draw("AXIS")

    this_ymin = info.th1.GetMinimum()
    this_ymax = info.th1.GetMaximum()
    boxes = getStripBox(inputfile, ymin=this_ymin, ymax=this_ymax, shift=position_center, pitch=pitch, direction=direction)
    for box in boxes:
        box.Draw()

    # Define legend
    pad_center = myStyle.GetPadCenter()
    pad_margin = myStyle.GetMargin()
    legend = TLegend(pad_center-0.23, 1-pad_margin-0.15, pad_center+0.23, 1-pad_margin-0.05)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
    legend.SetBorderSize(1)
    legend.SetLineColor(kBlack)

    # Add left axis (Time resolution)
    left_axis = TGaxis(-xlength,0.0001,-xlength,ylength,0.0001,ylength,510, "-")
    left_axis.UseCurrentStyle()
    # left_axis.SetTitle("Time resolution [ps]")
    left_axis.SetLabelSize(myStyle.GetSize()-4)
    left_axis.SetTitleSize(myStyle.GetSize())
    left_axis.SetLabelFont(myStyle.GetFont())
    left_axis.SetTitleFont(myStyle.GetFont())
    left_axis.SetLineColor(colors[4])
    left_axis.SetLabelColor(colors[4])

    info.th1.SetLineColor(colors[4])
    info.th1.SetLineWidth(4)
    legend.AddEntry(info.th1, "Time resolution")

    gPad.RedrawAxis("g")

    info.th1.Draw("hist e same")
    htemp.Draw("AXIS same")
    left_axis.Draw()
    legend.Draw()
    myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset, isPaperPlot=True)

    save_path = "%sWeighted2Only%s"%(outdir, direction.upper())
    if (is_hotspot):
        save_path+= "-hotspot"
    elif (is_tight):
        save_path+= "-tight"

    # canvas.SaveAs("%s.gif"%save_path)
    canvas.SaveAs("%s.pdf"%save_path)

    canvas.Clear()

# Draw ALL values in the same canvas
htemp.Draw("AXIS")

sub_colors = [colors[5], kBlack, colors[1], colors[2]]
sub_widths = [2, 2, 2, 4]
legend_name = [
    "Single-channel, no delay correction",
    "Single-channel, tracker delay correction",
    "Multi-channel, LGAD delay correction",
    "Multi-channel, tracker delay correction",]
if is_hotspot:
    legend_name = ["Multi-channel, tracker delay correction"]

if ("HPK_20um_500x500um_2x2pad_E600" in dataset):
    for i,legend_text in enumerate(legend_name):
        legend_name[i] = legend_text.split(", ")[0]

# Define legend
pad_margin = myStyle.GetMargin()
legend_height = 0.058*(3 + 1) # Correction methods + title
legX1 = 2*pad_margin+0.025
legX2 = 1-pad_margin-0.025
legend = TLegend(legX1, 1-pad_margin-legend_height-0.03, legX2, 1-pad_margin-0.03)
legend.SetBorderSize(1)
legend.SetLineColor(kBlack)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
legend.SetHeader("#bf{Correction methods}", "C")

for i,info_entry in enumerate(all_histoInfos):
    hist = info_entry.th1
    hist.SetLineColor(sub_colors[i])
    hist.SetLineWidth(sub_widths[i])
    ymin = hist.GetMinimum()
    ymax = hist.GetMaximum()

    # Define and draw gray bars in the background (Position of metallic sections)
    if i==0:
        boxes = getStripBox(inputfile, ymin=ymin, ymax=0.9*ymax, strips=True, shift=position_center, pitch=pitch, direction=direction)
        for box in boxes:
            box.Draw()
        gPad.RedrawAxis("g")

    hist.Write()

    # Skip some histograms if not needed
    if (not show_all and ("LGADXY" in info_entry.outHistoName)):
        continue
    if ("HPK_20um_500x500um_2x2pad_E600" in dataset) and (info_entry.outHistoName == "Time_Diff"):
        continue

    hist.Draw("hist e same")
    legend.AddEntry(hist, legend_name[i], "lep")

htemp.Draw("AXIS same")
legend.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, isPaperPlot=True)

save_path = "%sTimeResolution_vs_%s-AllMethods"%(outdir, direction)
if (is_hotspot):
    save_path+= "-hotspot"
elif (is_tight):
    save_path+= "-tight"
elif (noSum):
    save_path+= "_noSum"
canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)

outputfile.Close()
