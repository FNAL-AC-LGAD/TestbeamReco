from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite,TH1
import os
import optparse
from stripBox import getStripBox
import myStyle
import math 

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)
colors = myStyle.GetColors(True)

## Defining Style
myStyle.ForceStyle()

organized_mode=True

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, yMax=30.0,
                 xlabel = "Track x position [mm]", ylabel="Time resolution [ps]",
                 sensor="", center_position=0.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.sensor = sensor
        self.center_position = center_position
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name, sensor, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)

        # Rebin low statistics sensors
        if sensor=="BNL2020":
            th2.RebinX(5)
        elif sensor=="BNL2021":
            th2.RebinX(10)
        # if "1cm_500up_300uw" in sensor:
        #     th2.RebinX(2)

        return th2

    def getTH1(self, th2, hname):
        htitle = ";%s;%s"%(self.xlabel, self.ylabel)
        nxbin = th2.GetXaxis().GetNbins()
        xmin, xmax = th2.GetXaxis().GetXmin(), th2.GetXaxis().GetXmax()

        zero_bin = self.th2.GetXaxis().FindBin(0.0)
        central_bin = self.th2.GetXaxis().FindBin(self.center_position)
        bin_diff = central_bin - zero_bin

        bin_width = self.th2.GetXaxis().GetBinWidth(zero_bin)

        # Move distribution so that the bin with the center of
        # the central channel is at zero
        # print("Zero bin: %i, Real center: %i; Diff: %i"%(zero_bin, central_bin, bin_diff))
        if (bin_diff != 0.0):
            xmin-= bin_width*bin_diff
            xmax-= bin_width*bin_diff

        # Even number of bins have 0.0 as lowedge in zero bin.
        # Slightly move this bin to make it look symmetric
        if (self.th2.GetXaxis().GetBinLowEdge(zero_bin) == 0.0):
            xmin-= bin_width/2.
            xmax-= bin_width/2.

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
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
# parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")

options, args = parser.parse_args()
# use_shift = options.noShift
dataset = options.Dataset
outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else:
    inputfile = TFile("../test/myoutputfile.root")


sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']
strip_width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']

# Modify time reference (Photek) contribution from resolution results
rm_tracker = True
res_photek = 10 # ps

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode
# pref_hotspot = "_hotspot" if (options.hotspot) else ""

is_tight = options.useTight
# tight_ext = "_tight" if is_tight else ""
is_hotspot = options.hotspot


# Get total number of channels used and central channel's position
channel_info = []
for key in inputfile.GetListOfKeys():
    if "stripBoxInfo0" in key.GetName():
        channel_info.append(key.GetName())
n_channels = len(channel_info)
# print(channel_info)
# TODO: Update this to work with pads (second index)
# Even number of bins
if (n_channels%2 == 0):
    central_idx = round(n_channels/2)
    l_channel = inputfile.Get("stripBoxInfo0%i"%(central_idx-1)).GetMean(1)
    r_channel = inputfile.Get("stripBoxInfo0%i"%(central_idx)).GetMean(1)
    position_center = (l_channel + r_channel)/2
# Odd number of bins
else:
    central_idx =  round((n_channels-1)/2)
    position_center = (inputfile.Get("stripBoxInfo0%i"%central_idx)).GetMean(1)

outdir = myStyle.GetPlotsDir(outdir, "Paper_Resolution_Time/")

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
    print("    Using tight cuts!")
    for titles in list_htitles:
        titles[0]+= "_tight"

# Use hotspot extension if required
if (is_hotspot):
    list_htitles = [["weighted2_timeDiff_tracker_vs_xy_hotspot", "Time_DiffW2Tracker_hotspot", "Time resolution [ps]"]]


# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle,
                         sensor=dataset, center_position=position_center)
    all_histoInfos.append(info_obj)

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_ResTimeVsX0/")

# Get total number of bins in x-axis to loop over (all hists have the same number, in principle)
nbins = all_histoInfos[0].th2.GetXaxis().GetNbins()

#loop over X bins
for i in range(1, nbins+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
        totalEvents = info.th2.GetEntries()
        tmpHist = info.th2.ProjectionY("py",i,i)
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

        if i==0:
            msg_nentries = "%s: nEvents > %.2f "%(info.inHistoName, minEvtsCut)
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

            
            if (debugMode):
                tmpHist.Draw("hist")
                fit.Draw("same")
                canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info.outHistoName, i))
                bin_center = info.th1.GetXaxis().GetBinCenter(i)
                msg_binres = "Bin: %i (x center = %.3f)"%(i, bin_center)
                msg_binres+= " -> Resolution: %.3f +/- %.3f"%(value, error)
                print(msg_binres)
        else:
            valueMean = 0.0
            value = 0.0
            valueRaw = 0.0

        # Removing telescope contribution
        if rm_tracker and (value > 0.0):
            value = math.sqrt((value*value) - (res_photek*res_photek))
            error  = errorRaw*(valueRaw/value)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)

        # info.th1Mean.SetBinContent(i,valueMean)
        # info.th1Mean.SetBinError(i,errorMean)

# Define output file
output_path = "%sTimeDiffVsX"%(outdir)
if (is_hotspot):
    output_path+= "_hotspot"
elif (is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

# Define hist for axes style
htemp = TH1F("htemp", "", 1, -xlength, xlength)
htemp.SetStats(0)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetRangeUser(0.0, ylength)
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

# Draw ALL values in the same canvas
htemp.Draw("AXIS")

sub_colors = [colors[5], kBlack, colors[1], colors[2]]
sub_widths = [2, 2, 2, 4]
legend_name = ["Single-channel, no delay correction",
                "Single-channel, tracker delay correction",
                "Multi-channel, LGAD delay correction",
                "Multi-channel, tracker delay correction",]
if is_hotspot:
    legend_name = ["Multi-channel, tracker delay correction"]

# Define legend
pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
legend = TLegend(pad_center-0.20, 2*pad_margin+0.01, pad_center+0.20, 2*pad_margin+0.16)
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-20)

for i,info in enumerate(all_histoInfos):
    hist = info.th1
    hist.SetLineColor(sub_colors[i])
    hist.SetLineWidth(sub_widths[i])
    ymin = hist.GetMinimum()
    ymax = hist.GetMaximum()

    # Define and draw gray bars in the background (Position of metallic sections)
    if i==0:
        boxes = getStripBox(inputfile, ymin=ymin, ymax=ymax, strips=True, shift=position_center)
        for box in boxes:
            box.Draw()
        gPad.RedrawAxis("g")

    hist.Draw("hist e same")
    legend.AddEntry(hist, legend_name[i], "lep")

    hist.Write()

htemp.Draw("AXIS same")
legend.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

save_path = "%sTimeResolution_vs_x-AllMethods"%(outdir)
if (is_hotspot):
    save_path+= "-hotspot"
elif (is_tight):
    save_path+= "-tight"
canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)

outputfile.Close()
