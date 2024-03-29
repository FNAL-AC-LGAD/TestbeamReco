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

# Define position of strip/pad centers to find nearest one-strip/pad position resolution
dict_one_strip_info = myStyle.GetResolutions(dataset, per_channel=True)
dict_resolution = dict_one_strip_info["resolution_onestrip"]
is_pad = len(dict_one_strip_info["resolution_onestrip"]) > 1
if(is_pad):
    stripcenterpos = [0.5, 0, -0.5]
else:
    stripcenterpos = [1.5, 1, 0.5, 0, -0.5, -1, -1.5]

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

outdir = myStyle.GetPlotsDir(outdir, "WeightedResolution_Pos/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["deltaX_vs_Xtrack_oneStrip", "track_oneStrip", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_twoStrip", "track_twoStrip", "Position resolution [#mum]"],
]
inName = outdirtemp+"Efficiency/EfficiencyVsX"+tight_postfix+".root"
inFile = TFile(inName,"READ")
hTwoEff = inFile.Get("hefficiency_vs_x_twoStrip_numerator_coarseBins"+tight_postfix)
hOneEff = inFile.Get("hefficiency_vs_x_oneStrip_numerator_coarseBins"+tight_postfix)
# Use of tight cut histograms not needed because will be weighted with the tight histograms which have value = 0 outside tight region
# if (is_tight):
#     print(" >> Using tight cuts!")
#     list_htitles = [["deltaX_vs_Xtrack_oneStrip_tight", "track_oneStrip_tight", "Position resolution [#mum]"],["deltaX_vs_Xtrack_twoStrip_tight", "track_twoStrip_tight", "Position resolution [#mum]"]]

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

# Get histograms for Expected Resolution of Two strip Reconstruction
# ------------------------------------------------------------------

# mean_noise12_vs_x = get_profX(inputfile, "BaselineRMS12_vs_x", is_tight)
# mean_amp12_vs_x = get_profX(inputfile, "Amp12_vs_x", is_tight)
# mean_amp1_vs_x = get_profX(inputfile, "Amp1_vs_x", is_tight)
# mean_amp2_vs_x = get_profX(inputfile, "Amp2_vs_x", is_tight)
# mean_dXFrac_vs_x = get_profX(inputfile, "dXdFrac_vs_Xtrack", is_tight)

# nbins = mean_amp12_vs_x.GetNbinsX()
# xmin, xmax = mf.get_shifted_limits(mean_amp12_vs_x, position_center)

# hist_expected = ROOT.TH1F("h_expected", "", nbins, xmin, xmax)
# hist_expected.SetLineWidth(3)
# hist_expected.SetLineStyle(7)
# hist_expected.SetLineColor(colors[2])

# # Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
# for ibin in range(1, hist_expected.GetNbinsX()+1):
#     if mean_amp12_vs_x.GetBinContent(ibin) > 0:
#         dXFrac = mean_dXFrac_vs_x.GetBinContent(ibin)
#         noise12 = mean_noise12_vs_x.GetBinContent(ibin)
#         amp1 = mean_amp1_vs_x.GetBinContent(ibin)
#         amp2 = mean_amp2_vs_x.GetBinContent(ibin)
#         amp12 = mean_amp12_vs_x.GetBinContent(ibin)

#         value_expected = abs(1000*dXFrac * (0.5*noise12) * pow(pow(amp1,2)+pow(amp2,2),0.5) / (amp12)**2)
#         if ("pad" in dataset) or ("500x500" in dataset):
#             value_expected = TMath.Sqrt(2)*value_expected

#     else:
#         value_expected = -10.0

#     # Adding tracker contribution
#     if (not rm_tracker) and (value_expected > 0.0):
#         value_expected = math.sqrt(trkr_value**2 + value_expected**2)

#     # Fill only when inside limits
#     if not mf.is_inside_limits(ibin, hist_expected, xmax=plot_xlimit):
#         continue

#     hist_expected.SetBinContent(ibin, value_expected)


# Get TLine with binary readout
# -----------------------------

line_binary_readout = ROOT.TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
line_binary_readout.SetLineWidth(3)
line_binary_readout.SetLineStyle(7)
line_binary_readout.SetLineColor(colors[4])


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

        # Define minimum of bin's entries to be fitted
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

        #Do fit 
        if(nEvents > minEvtsCut):
            # tmpHist.Rebin(2)
            fit = TF1('fit','gaus',fitlow,fithigh)
            # if "twoStrip" in info_entry.inHistoName:
            #     fit.SetParameter(1, 0.0)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myMPV = fit.GetParameter(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            # Save sigma value of fit only for two-strip position resolution
            if("twoStrip" in info_entry.outHistoName):
                value = 1000.0*mySigma
                error = 1000.0*mySigmaError
        
            # For Debugging
            if (debugMode):
                gStyle.SetOptStat(1)
                tmpHist.Draw("hist")
                fit.Draw("same")
                canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
                bin_center = info_entry.th1.GetXaxis().GetBinCenter(i)
                msg_binres = "Bin: %i (x center = %.3f)"%(i, bin_center)
                msg_binres+= " -> Resolution: %.3f +/- %.3f"%(value, error)
                print(msg_binres)
        else:
            if("twoStrip" in info_entry.outHistoName):
                value = 0.0 # previously was set to -10 for plotting reasons, but needs to be set to 0 for weighted pos. res.

        # Fill only when inside limits
        if not mf.is_inside_limits(i, info_entry.th1, xmax=plot_xlimit):
            continue

        info_entry.th1.SetBinContent(i, value)
        # info_entry.th1.SetBinError(i, error)

weightedhist = all_histoInfos[0].th1.Clone("weighted_pos_res")

for i in range(1, nbins+1):
    # Apply weights
    tmpHistOne = all_histoInfos[0].th1
    tmpHistTwo = all_histoInfos[1].th1
    binPos = tmpHistOne.GetXaxis().GetBinCenter(i)
    nearest = min(stripcenterpos, key=lambda x:abs(x-binPos))
    nearest_index = stripcenterpos.index(nearest)
    onePR = dict_resolution[0][nearest_index]
    oneEff = hOneEff.GetBinContent(hOneEff.GetXaxis().FindBin(tmpHistOne.GetXaxis().GetBinCenter(i)))
    twoEff = hTwoEff.GetBinContent(hTwoEff.GetXaxis().FindBin(tmpHistOne.GetXaxis().GetBinCenter(i)))
    print("{:.2f} -> oneEff {:.3f} (onePR {:.2f}), twoEff {:.3f} (twoPR {:.2f})".format(tmpHistOne.GetXaxis().GetBinCenter(i), oneEff, onePR, twoEff, tmpHistTwo.GetBinContent(i)))
    if(oneEff+twoEff <= 0): #ensure sum of efficiencies is not 0. Cannot also be negative, but adding it just-in-case
        value = 0
    else:
        value = TMath.Sqrt((oneEff*onePR*onePR + twoEff*tmpHistTwo.GetBinContent(i)*tmpHistTwo.GetBinContent(i))/(oneEff+twoEff))
        
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

# Add binary readout
line_binary_readout.Draw("SAME")
legend.AddEntry(line_binary_readout, "Pitch / #sqrt{12}", "l")

# Draw all other elements with Two Strip Reconstructed histogram only
if "twoStrip" in info_entry.inHistoName:
    # Get correct legend for Two Strip Reco
    this_legend = "Weighted resolution, observed"

    # Add two strips expected resolution
    # hist_expected.Draw("HIST SAME")
    # entry_expected = "Two %s expected"%(legend_reco)
    # legend.AddEntry(hist_expected, entry_expected, "l")
    # hist_expected.Write()
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
