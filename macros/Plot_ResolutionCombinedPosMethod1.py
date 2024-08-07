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
                 sensor="", center_position = 0.0, offset=0.0):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.yMax = yMax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.sensor = sensor
        self.center_position = center_position
        if(("KOJI" in sensor) and ("twoStrip" in inHistoName)):
            self.th2 = self.getTH2(f, inHistoName, sensor).RebinX(2)
            print(" (!!) Using RebinX(2) to handle low stat bins!")
        else:
            self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(outHistoName)

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)

        return th2

    def getTH1(self, hname):
        htitle = ";%s;%s"%(self.xlabel, self.ylabel)
        nxbin = self.th2.GetXaxis().GetNbins()
        xmin, xmax = (mf.get_shifted_limits(self.th2, self.center_position))

        # Create and define th1 default style
        th1 = TH1D(hname, htitle, nxbin, xmin - offset, xmax - offset)
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
parser.add_option('-M', dest='MPVnoFit', action='store_true', default = False, help="Use MPV value for two ch reco if not enough entries for fit")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
outdirtemp=outdir
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']/1000. # convert to mm
strip_width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']
deltaXoffset = sensor_Geometry['stripCenterXPosition']
# Define tracker contribution
# rm_tracker True shows expected and measured curves without tracker component
rm_tracker = True
trkr_value = 5 # um
# trkr_value = 0.0 # um To avoid having this factor removed in any curve!

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode
useMPVifNOfit = options.MPVnoFit
# if "W11_22_3_20T_500x500_150M" in dataset:
#     useMPVifNOfit = True

is_tight = options.useTight
if(is_tight):
    tight_postfix = "_tight"
else:
    tight_postfix = ""
# Get position of the central channel in the "x" direction
position_center = mf.get_central_channel_position(inputfile, "x")

outdir = myStyle.GetPlotsDir(outdir, "CombinedResolution_PosMethod1/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["deltaX_vs_Xtrack_oneStrip_pitchWide", "track_oneStrip_resolution", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_twoStrip", "track_twoStrip_resolution", "Position resolution [#mum]"],
]
inName = outdirtemp+"Efficiency/EfficiencyVsX"+tight_postfix+".root"
inFile = TFile(inName,"READ")
hTwoEff = inFile.Get("hefficiency_vs_x_twoStrip_numerator_coarseBins"+tight_postfix)
hOneEff = inFile.Get("hefficiency_vs_x_oneStrip_numerator_coarseBins"+tight_postfix)
# Use of tight cut histograms not needed because will be Combined with the tight histograms which have value = 0 outside tight region
if (is_tight):
    print(" >> Using tight cuts!")
    list_htitles = [["deltaX_vs_Xtrack_oneStrip_pitchWide_tight", "track_oneStrip_resolution", "Position resolution [#mum]"],["deltaX_vs_Xtrack_twoStrip_tight", "track_twoStrip_resolution", "Position resolution [#mum]"]
    ]

# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    if("oneStrip" in hname):
        offset=0.0#deltaXoffset
    else:
        offset=0.0
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle, sensor=dataset, center_position=position_center, offset=offset)
    all_histoInfos.append(info_obj)

# Define bin limit of the histograms drawn
if("KOJI" in dataset):
    plot_xlimit = 0.25
else:
    plot_xlimit = 1.5
# plot_xlimit = abs(inputfile.Get("stripBoxInfo00").GetMean(1) - position_center)
if ("pad" not in dataset) and ("500x500" not in dataset):
    plot_xlimit-= pitch/(2.)


# Get histogram for One+Two strip Reconstruction's resolution
# -------------------------------------------------------

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_ResPosVsX0/")


# Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
for info_entry in all_histoInfos:
    nbins = info_entry.th2.GetXaxis().GetNbins()
    for i in range(1, nbins+1):
        totalEvents = info_entry.th2.GetEntries()
        tmpHist = info_entry.th2.ProjectionY("py",i,i)
        if("twoStrip" in info_entry.outHistoName): #NewChange - results in matching std. dev and gauss sigma values
            narrow_range = 0.6 * pitch
            tmpHist.GetXaxis().SetRangeUser(-narrow_range, narrow_range)
        if("oneStrip" in info_entry.outHistoName):
            tmpHist.GetXaxis().SetRangeUser(-pitch,pitch)
        myMean = tmpHist.GetMean()
        myMeanError = tmpHist.GetMeanError()
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        # Define shorter quantities to make propagation of error easy of reading
        mean2 = myMean * myMean
        rms2 = myRMS * myRMS
        value = 1000 * TMath.Sqrt(mean2 + rms2)
        if ((myMean!=0) or (myRMS!=0)):
            mean_err2 = myMeanError * myMeanError
            rms_err2 = myRMSError * myRMSError
            error = 1000 * TMath.Sqrt((mean2*mean_err2 + rms2*rms_err2)/(mean2 + rms2))
            # print(myMeanError, ", ", myRMSError, ", ", error)
        else:
            value = 0 # if both mean and std. dev. are 0 then the value will immediately be 0, but adding this as a safety measure.
            error = 0

        # Define minimum of bin's entries to be fitted
        minEvtsCut = totalEvents/nbins
        if ("HPK_W9_15_2" in dataset):
            minEvtsCut = 0.25*totalEvents/nbins
        if ("500x500" in dataset):
            minEvtsCut = 0.2*totalEvents/nbins
        if ("W9_23_3_20T_500x500_300M" in dataset):
            minEvtsCut = 0.50*totalEvents/nbins

        if (i == 1):
            msg_nentries = "%s: nEvents > %.2f "%(info_entry.inHistoName, minEvtsCut)
            msg_nentries+= "(Total events: %i)"%(totalEvents)
            print(msg_nentries)

        # Do fit
        if(nEvents > minEvtsCut):
            # tmpHist.Rebin(2)
            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myMPV = fit.GetParameter(1)
            myMPVError = fit.GetParError(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            # Save sigma value of fit only for two-ch position resolution
            if("twoStrip" in info_entry.outHistoName):
                mpv2 = myMPV * myMPV
                sigma2 = mySigma * mySigma
                value = 1000.0 * TMath.Sqrt(mpv2 + sigma2)
                if ((myMPV!=0) or (mySigma!=0)):
                    mpv_err2 = myMPVError * myMPVError
                    sigma_err2 = mySigmaError * mySigmaError
                    error = 1000 * TMath.Sqrt((mpv2*mpv_err2 + sigma2*sigma_err2)/(mpv2 + sigma2))
                else:
                    value = 0 # if both mean and sigma are 0 then the value will immediately be 0, but adding this as a safety measure.
                    error = 0
        elif ("twoStrip" in info_entry.outHistoName) and (not useMPVifNOfit):
            value = 0.0
            error = 0.0

        # For Debugging
        if (debugMode):
            gStyle.SetOptStat(1111111)
            tmpHist.Draw("hist")
            if(nEvents > minEvtsCut):
                fit.Draw("same")
            canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
            bin_center = info_entry.th1.GetXaxis().GetBinCenter(i)
            msg_binres = "Bin: %i (x center = %.3f)"%(i, bin_center)
            msg_binres+= " -> Resolution: %.3f +/- %.3f"%(value, error)
            print(msg_binres)

        # Remove tracker contribution for one- and two-channel resolutions
        if rm_tracker and (value > trkr_value):
            new_value = TMath.Sqrt(value**2 - trkr_value**2)
            new_error = value / new_value * error
            value, error = new_value, new_error
        # Mark bins with resolution smaller than tracker
        elif (trkr_value > value) and (value > 0.0):
            print("  WARNING: Bin %i got method 1 resolution smaller than tracker (%.3f)"%(i, value))
            value = 2.0
            # error = 2.0

        # Fill only when inside limits
        if not mf.is_inside_limits(i, info_entry.th1, xmax=plot_xlimit):
            continue

        # Alert that statistical RMS value is used for two-ch position resolution if no enough events for fit
        if(nEvents < minEvtsCut) and (value>0) and ("twoStrip" in info_entry.outHistoName):
            print(" (!) Using RMS in bin %i of %s due to lack of stats"%(i, info_entry.outHistoName))

        info_entry.th1.SetBinContent(i, value)
        info_entry.th1.SetBinError(i, error)


Combinedhist = all_histoInfos[1].th1.Clone("CombinedPosRes")
nbins = all_histoInfos[1].th2.GetXaxis().GetNbins()
tmpHistOne = all_histoInfos[0].th1
tmpHistTwo = all_histoInfos[1].th1
for i in range(1, nbins+1):
    # Apply weights    
    binPos = tmpHistTwo.GetXaxis().GetBinCenter(i)
    oneEff = hOneEff.GetBinContent(hOneEff.GetXaxis().FindBin(binPos))
    onePR = tmpHistOne.GetBinContent(tmpHistOne.GetXaxis().FindBin(binPos))
    onePRError = tmpHistOne.GetBinError(tmpHistOne.GetXaxis().FindBin(binPos))
    twoEff = hTwoEff.GetBinContent(hTwoEff.GetXaxis().FindBin(binPos))
    twoPR = tmpHistTwo.GetBinContent(tmpHistTwo.GetXaxis().FindBin(binPos))
    twoPRError = tmpHistTwo.GetBinError(tmpHistTwo.GetXaxis().FindBin(binPos))
    # # print("{:.2f} -> oneEff {:.3f} (onePR {:.2f}), twoEff {:.3f} (twoPR {:.2f})".format(tmpHistTwo.GetXaxis().GetBinCenter(i), oneEff, onePR, twoEff, twoPR))
    # print("{:.2f} -> onePR {:.3f} (onePRE {:.2f}), twoPR {:.3f} (twoPRE {:.2f})".format(tmpHistTwo.GetXaxis().GetBinCenter(i), onePR, onePRError, twoPR, twoPRError))

    # Ensure sum of efficiencies is not 0 and it's no negative
    if ((oneEff*onePR*onePR + twoEff*twoPR*twoPR!=0) and (oneEff + twoEff > 0)):
        # Set to zero two-strip bins with eff < 0.05 (5%) and use one-strip value for combined in those cases
        if (twoEff < 0.05):
            value = onePR
            error = onePRError
            print(" (!!!) Bin %i efficiency lower than 0.05. Using only oneStrip reco value in Combined!"%(i))
        else:
            resOne2 = onePR * onePR
            resOne_err2 = onePRError * onePRError
            resTwo2 = twoPR * twoPR
            resTwo_err2 = twoPRError * twoPRError
            value = TMath.Sqrt((oneEff*resOne2 + twoEff*resTwo2)/(oneEff + twoEff))

            effOne2 = oneEff * oneEff
            effTwo2 = twoEff * twoEff
            error_num = effOne2*resOne2*resOne_err2 + effTwo2*resTwo2*resTwo_err2
            error_den = (oneEff + twoEff) * (oneEff*resOne2 + twoEff*resTwo2)
            error = TMath.Sqrt(error_num/error_den)
    else:
        value = 0
        error = 0

    # Tracker contribution already removed for one- and two-channel contribution
    # if rm_tracker and (value > trkr_value):
    #     new_value = TMath.Sqrt(value**2 - trkr_value**2)
    #     new_error = value / new_value * error
    #     value, error = new_value, new_error

    Combinedhist.SetBinContent(i, value)
    Combinedhist.SetBinError(i, error)

# Define output file
output_path = "%sCombinedPositionResVsX"%(outdir)

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
boxes = getStripBox(inputfile, ymax=ylength, shift=position_center, pitch=pitch)

# Create legend
legend = TLegend(pad_center-0.25, 1-pad_margin-0.3, pad_center+0.25, 1-pad_margin-0.055)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
# Draw gray bars in the background (Position of metallic sections)
for box in boxes:
    box.Draw()
for i,info_entry in enumerate(all_histoInfos):
    hist = info_entry.th1
    hist.SetLineColor(colors[i])
    hist.SetLineWidth(3)
    gPad.RedrawAxis("g")

    this_legend = info_entry.outHistoName.replace("track_", "")

    # Add this entry histogram
    hist.Draw("HIST e SAME")
    legend.AddEntry(hist, this_legend, "l")
    hist.Write()

Combinedhist.Draw("hist e same")
Combinedhist.SetLineColor(colors[len(all_histoInfos)])
Combinedhist.SetLineWidth(3)
Combinedhist.Write()
legend.AddEntry(Combinedhist, "Combined Resolution", "l")

htemp.Draw("AXIS same")
legend.Draw()

myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset, isPaperPlot=True)

save_path = "%sPosRes-Method1"%(outdir)
if (is_tight):
    save_path+= "_tight"
canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)

canvas.Clear()

outputfile.Close()
