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
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="X axis range [-x, x]")
parser.add_option('-y','--ylength', dest='ylength', default = 160.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch = sensor_Geometry['pitch']
strip_width = sensor_Geometry['stripWidth']
strip_length = sensor_Geometry['length']

# Define tracker contribution
# rm_tracker True shows expected and measured curves without tracker component
rm_tracker = True
trkr_value = 5 # um

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

is_tight = options.useTight
is_hotspot = options.hotspot

# Get position of the central channel in the "x" direction
position_center = mf.get_central_channel_position(inputfile, "x")

outdir = myStyle.GetPlotsDir(outdir, "Resolution_X/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["deltaX_vs_Xtrack_twoStrips", "track_twoStrips", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_noNeighb", "track_twoStrips_noNeighb", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_highFrac", "track_twoStrips_highFrac", "Position resolution [#mum]"],
    ["deltaX_vs_Xtrack_oneStrip", "track_oneStrip", "Position resolution [#mum]"],
]

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    list_htitles = [["deltaX_vs_Xtrack_twoStrips_tight", "track_twoStrips_tight", "Position resolution [#mum]"]]

# Use hotspot extension if required
if (is_hotspot):
    list_htitles = [["deltaX_vs_Xtrack_twoStrips_hotspot", "track_twoStrips_hotspot", "Position resolution [#mum]"]]

# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, yMax=ylength, ylabel=ytitle,
                         sensor=dataset, center_position=position_center)
    all_histoInfos.append(info_obj)


# Get histograms for Expected Resolution of Two strip Reconstruction
# ------------------------------------------------------------------

mean_noise12_vs_x = get_profX(inputfile, "BaselineRMS12_vs_x", is_tight)
mean_amp12_vs_x = get_profX(inputfile, "Amp12_vs_x", is_tight)
mean_amp1_vs_x = get_profX(inputfile, "Amp1_vs_x", is_tight)
mean_amp2_vs_x = get_profX(inputfile, "Amp2_vs_x", is_tight)
mean_dXFrac_vs_x = get_profX(inputfile, "dXdFrac_vs_Xtrack", is_tight)

nbins = mean_amp12_vs_x.GetNbinsX()
xmin, xmax = mf.get_shifted_limits(mean_amp12_vs_x, position_center)

hist_expected = ROOT.TH1F("h_expected", "", nbins, xmin, xmax)
hist_expected.SetLineWidth(3)
hist_expected.SetLineStyle(7)
hist_expected.SetLineColor(colors[2])

# Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
for ibin in range(1,hist_expected.GetNbinsX()+1):
    if mean_amp12_vs_x.GetBinContent(ibin) > 0:
        dXFrac = mean_dXFrac_vs_x.GetBinContent(ibin)
        noise12 = mean_noise12_vs_x.GetBinContent(ibin)
        amp1 = mean_amp1_vs_x.GetBinContent(ibin)
        amp2 = mean_amp2_vs_x.GetBinContent(ibin)
        amp12 = mean_amp12_vs_x.GetBinContent(ibin)

        value_expected = abs(1000*dXFrac * (0.5*noise12) * pow(pow(amp1,2)+pow(amp2,2),0.5) / (amp12)**2)

    else:
        value_expected = -10.0

    # Adding tracker contribution
    if (not rm_tracker) and (value_expected > 0.0):
        value_expected = math.sqrt(trkr_value**2 + value_expected**2)

    hist_expected.SetBinContent(ibin, value_expected)


# Get TGraph for One strip Reconstruction method's resolution
# -----------------------------------------------------------

boxes = getStripBox(inputfile, ymax=ylength, shift=position_center)

use_one_strip = True
dict_one_strip_resolutions = dict(myStyle.resolutions2022OneStripChannel)
dict_one_strip_resolutions.update(myStyle.resolutions2023OneStripChannel)

if dataset in dict_one_strip_resolutions:
    list_one_strip_values = dict_one_strip_resolutions[dataset]['resOneStrip']
else:
    print(" >> Sensor not found in One strip Reco dictionary. Please, add sensor with a default number if needed.")
    exit()

list_positions = []
list_values = []
for i, value in enumerate(list_one_strip_values):
    if value > 0.0:
        box = boxes[i]
        x_position = (box.GetX1() + box.GetX2())/2.
        list_positions.append(x_position)
        list_values.append(value)

if not list_values:
    use_one_strip = False
else:
    hist_one_strip = ROOT.TGraph(len(list_values), array('f',list_positions), array('f',list_values))
    hist_one_strip.SetName("h_one_strip")
    # hist_one_strip.SetLineWidth(3)
    hist_one_strip.SetLineStyle(1)
    hist_one_strip.SetMarkerStyle(33)
    hist_one_strip.SetMarkerSize(3)
    hist_one_strip.SetMarkerColor(colors[0])


# Get TLine with binary readout
# -----------------------------

line_binary_readout = ROOT.TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
line_binary_readout.SetLineWidth(3)
line_binary_readout.SetLineStyle(7)
line_binary_readout.SetLineColor(colors[4])


# Get histogram for Two strip Reconstruction's resolution
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
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = myRMSError

        # Define minimum of bin's entries to be fitted
        minEvtsCut = totalEvents/nbins

        if i==0:
            msg_nentries = "%s: nEvents > %.2f "%(info_entry.inHistoName, minEvtsCut)
            msg_nentries+= "(Total events: %i)"%(totalEvents)
            print(msg_nentries)

        #Do fit 
        if(nEvents > minEvtsCut):
            # tmpHist.Rebin(2)
            
            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myMPV = fit.GetParameter(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
        
            # For Debugging
            if (debugMode):
                tmpHist.Draw("hist")
                fit.Draw("same")
                canvas.SaveAs("%sq_%s%i.gif"%(outdir_q, info_entry.outHistoName, i))
                bin_center = info_entry.th1.GetXaxis().GetBinCenter(i)
                msg_binres = "Bin: %i (x center = %.3f)"%(i, bin_center)
                msg_binres+= " -> Resolution: %.3f +/- %.3f"%(value, error)
                print(msg_binres)
        else:
            value = -10.0
            error = 0

        # Removing tracker's contribution
        if rm_tracker and (value > trkr_value):
            error = error*value/TMath.Sqrt(value**2 - trkr_value**2)
            value = TMath.Sqrt(value**2 - trkr_value**2)
        # Mark bins with resolution smaller than tracker
        elif (trkr_value > value) and (value > 0.0):
            value = 2.0
            error = 2.0

        info_entry.th1.SetBinContent(i, value)
        info_entry.th1.SetBinError(i, error)

# Define output file
output_path = "%sPositionResVsX"%(outdir)
if (is_hotspot):
    output_path+= "_hotspot"
elif (is_tight):
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

pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
for i,info_entry in enumerate(all_histoInfos):
    htemp.Draw("AXIS")

    hist = info_entry.th1
    hist.SetLineColor(colors[2])
    hist.SetLineWidth(3)
    ymin = hist.GetMinimum()
    ymax = hist.GetMaximum()

    # Draw gray bars in the background (Position of metallic sections)
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
    if "twoStrips" in info_entry.inHistoName:
        # Get correct legend for Two Strip Reco
        this_legend = "Two strip observed"

        # Add one strip resolution
        if use_one_strip:
            hist_one_strip.Draw("P SAME")
            legend.AddEntry(hist_one_strip, "Exactly one strip observed", "P")
            hist_one_strip.Write()

        # Add two strips expected resolution
        hist_expected.Draw("HIST SAME")
        legend.AddEntry(hist_expected, "Two strip expected", "l")
        hist_expected.Write()
    # If not twoStrip, set a default title for the legend
    else:
        this_legend = info_entry.outHistoName.replace("track_", "")

    # Add this entry histogram
    hist.Draw("HIST E SAME")
    legend.AddEntry(hist, this_legend, "l")
    hist.Write()

    htemp.Draw("AXIS same")
    legend.Draw()

    # myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    save_path = "%sPositionResolution_vs_x"%(outdir)
    # Choose another name if not Two Strip Reconstructed histogram
    if "twoStrips" not in info_entry.inHistoName:
        save_path = "%sPosRes-%s"%(outdir, this_legend)
    if (is_hotspot):
        save_path+= "-hotspot"
    elif (is_tight):
        save_path+= "-tight"
    canvas.SaveAs("%s.gif"%save_path)
    canvas.SaveAs("%s.pdf"%save_path)
    
    canvas.Clear()

outputfile.Close()
