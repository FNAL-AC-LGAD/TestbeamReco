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
        self.sensor = sensor
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor), addShift)
        self.fine_tune = self.fine_tuning(sensor)

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
        if not self.f.Get("stripBoxInfo06"):
            real_center = (self.f.Get("stripBoxInfo02").GetMean(1) + real_center)/2.

        if ("2p5cm_mixConfig1_W3051" in self.sensor):
            real_center = self.f.Get("stripBoxInfo02").GetMean(1)

        elif ("2p5cm_mixConfig2_W3051" in self.sensor):
            real_center = self.f.Get("stripBoxInfo04").GetMean(1)

        return real_center

    def fine_tuning(self, sensor):
        # value = 0.0
        value = self.th2.GetXaxis().GetBinWidth(2)/2.
        if "1cm_500up_300uw" in sensor: value = 0.0
        elif "1cm_500up_100uw" in sensor: value = self.shift()
        elif "0p5cm_500up_200uw_1_4" in sensor: value = -value
        # if sensor=="BNL2020": value = 0.0075

        if ("2p5cm_mixConfig" in sensor):
            value = self.shift()

        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="X axis range [-x, x]")
parser.add_option('-y','--ylength', dest='ylength', default = 160.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
parser.add_option('-o', dest='showOneStrip', action='store_false', default = True, help="Draw marker with oneStrip resolution per channel")
options, args = parser.parse_args()

useShift = options.noShift
dataset = options.Dataset
outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']
strip_width  = sensor_Geometry['stripWidth']
strip_length  = sensor_Geometry['length']

xlength = float(options.xlength)
ylength = float(options.ylength)
# ylength = 160.0
# ylength = 80.0
debugMode = options.debugMode
is_hotspot = options.hotspot
pref_hotspot = "_hotspot" if (is_hotspot) else ""

# Define tracker contribution
# rm_tracker True shows expected and measured curves without tracker component
rm_tracker = True
trkr_value = 5 # um

useTight = options.useTight
tight_ext = "_tight" if useTight else ""
showOneStrip = options.showOneStrip

all_histoInfos = [
    # HistoInfo("deltaX_vs_Xtrack",   inputfile, "track", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaY_vs_Xtrack",   inputfile, "track", True,  2500, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "track_oneStrip", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    HistoInfo("deltaX_vs_Xtrack_twoStrips%s"%pref_hotspot,   inputfile, "track_twoStrips%s"%pref_hotspot, True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",dataset, useShift),
    # HistoInfo("deltaX_vs_Xtrack",   inputfile, "rms_track", False,  ylength, "", "Track x position [mm]","Position resolution RMS [#mum]",sensor),
]

if useTight:
    all_histoInfos = [
        HistoInfo("deltaX_vs_Xtrack_twoStrips_tight",   inputfile, "track_twoStrips%s"%pref_hotspot, True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",dataset, useShift),
    ]

hist_info_twoStrip = all_histoInfos[0]

#### Get histograms for expected resolution
noise12_vs_x = inputfile.Get("BaselineRMS12_vs_x%s"%tight_ext)
amp12_vs_x = inputfile.Get("Amp12_vs_x%s"%tight_ext)
amp1_vs_x = inputfile.Get("Amp1_vs_x%s"%tight_ext)
amp2_vs_x = inputfile.Get("Amp2_vs_x%s"%tight_ext)
dXdFrac_vs_x = inputfile.Get("dXdFrac_vs_Xtrack%s"%tight_ext)

mean_noise12_vs_x = noise12_vs_x.ProfileX()
mean_amp12_vs_x = amp12_vs_x.ProfileX()
mean_amp1_vs_x = amp1_vs_x.ProfileX()
mean_amp2_vs_x = amp2_vs_x.ProfileX()
mean_dXFrac_vs_x = dXdFrac_vs_x.ProfileX()

nbinsx = mean_amp12_vs_x.GetNbinsX()
low_x = mean_amp12_vs_x.GetBinLowEdge(1)
high_x = mean_amp12_vs_x.GetBinLowEdge(nbinsx+1)
if useShift:
    low_x -= hist_info_twoStrip.fine_tune
    high_x -= hist_info_twoStrip.fine_tune

expected_res_vs_x = ROOT.TH1F("h_exp","",nbinsx,low_x,high_x)
expected_res_vs_x.SetLineWidth(3)
expected_res_vs_x.SetLineStyle(7)
expected_res_vs_x.SetLineColor(colors[2])

# Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
for ibin in range(1,expected_res_vs_x.GetNbinsX()+1):
    if mean_amp12_vs_x.GetBinContent(ibin)>0:
        dXFrac = mean_dXFrac_vs_x.GetBinContent(ibin)
        noise12 = mean_noise12_vs_x.GetBinContent(ibin)
        amp1 = mean_amp1_vs_x.GetBinContent(ibin)
        amp2 = mean_amp2_vs_x.GetBinContent(ibin)
        amp12 = mean_amp12_vs_x.GetBinContent(ibin)
        # Without tracker's contribution
        expected_res = abs(1000*dXFrac * (0.5*noise12) * pow(pow(amp1,2)+pow(amp2,2),0.5) / (amp12)**2)
        # With tracker's contribution of 5 microns
        if not rm_tracker:
            # expected_res = math.sqrt(5.**2 + pow(abs(1000*dXFrac * (0.5*noise12) * pow(pow(amp1,2)+pow(amp2,2),0.5) / (amp12)**2),2))
            expected_res = math.sqrt(trkr_value**2 + pow(expected_res,2))
    else:
        expected_res=-10.0
    if ("1cm_500up_300uw" in hist_info_twoStrip.sensor) and (mean_amp12_vs_x.GetBinContent(ibin)>0) and (mean_amp12_vs_x.GetBinContent(ibin+1)<=0):
        expected_res=-10.0

    #print("Bin %i, res %0.2f"%(ibin,expected_res))
    expected_res_vs_x.SetBinContent(ibin,expected_res)

# ### Get Efficiency for weighted average curve
# in_efficiency = TFile("%sPaper_Eff/EfficiencyPlots.root"%(outdir), "READ")
# eff_OneStrip = in_efficiency.Get("efficiency_vs_x_oneStrip_coarseBins") # Remember that these Eff plots have the double of bins in x!!
# eff_TwoStrip = in_efficiency.Get("efficiency_vs_x_twoStrip_coarseBins")

### Draw canvas
canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

print("Finished setting up langaus fit class")

outdir = myStyle.GetPlotsDir(outdir, "Paper_XRes/")
if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_res0/")

if (is_hotspot):
    input_fullSnsr = TFile("%sPlotXRes.root"%(outdir), "READ")
    hist_twoStrip_fullSnsr = input_fullSnsr.Get("h_twoStrip")

# oneStripResValue = myStyle.resolutions2022[dataset]['position_oneStripRMS']
l_resolution_dicts = [myStyle.resolutions2022OneStripChannel, myStyle.resolutions2023OneStripChannel]
for r_dict in l_resolution_dicts:
    if dataset in r_dict:
        oneStripResValue_list = r_dict[dataset]['resOneStrip']

max_strip_edge = hist_info_twoStrip.f.Get("stripBoxInfo01").GetMean(1) + strip_width/2000.
if useShift: max_strip_edge -= hist_info_twoStrip.shift()

# ### Create Weighted Average histogram
# weighted_hist = ROOT.TH1F("Weighted_average","",nbinsx,low_x,high_x)

# weighted_hist.SetLineWidth(3)
# # weighted_hist.SetLineStyle(1)
# weighted_hist.SetLineColor(colors[1])

nXBins = hist_info_twoStrip.th2.GetXaxis().GetNbins()

# Get boxes (channel drawn in the background)
this_shift = hist_info_twoStrip.shift() if useShift else 0
boxes = getStripBox(inputfile,0.0,hist_info_twoStrip.yMax,False,18,True,this_shift)

# Run across X-bins. ROOT convention: bin 0 - underflow, nbins+1 - overflow bin
for i in range(1, nXBins+1):
    for info in all_histoInfos:
        totalEvents = info.th2.GetEntries()
        tmpHist = info.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = myRMSError

        minEvtsCut = totalEvents/nXBins

        if i==0:
            print("%s: nEvents > %.2f (Total events: %i; N bins: %i)"%(info.inHistoName,minEvtsCut,totalEvents,nXBins))
        #Do fit 
        if(nEvents > minEvtsCut):
            if(info.doFits):
                # tmpHist.Rebin(2)
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMPV = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                error = 1000.0*mySigmaError
            
                ##For Debugging
                if (debugMode):
                   tmpHist.Draw("hist")
                   fit.Draw("same")
                   canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                   print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution: %.3f +/- %.3f"%(value, error))
            else:
                value *= 1000.0
                error *= 1000.0
                ##For Debugging
                # if (debugMode):
                #     tmpHist.Draw("hist")
                #     fit.Draw("same")
                #     canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                #     print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution_rms: %.3f +/- %.3f"%(value, error))

            # ## Remove bins when twoStrip is used
            # oneStripHist.SetBinContent(i, -10.0)
        else:
            ## Add oneStripReco value
            # value = TMath.Sqrt(oneStripRes*oneStripRes - 5*5)
            value = -10.0
            error = 0
            # if "track_twoStrips" in info.outHistoName:
            #     ## Add metal width/sqrt(12) as expected resolution in metal region
            #     # expected_res_vs_x.SetBinContent(i,strip_width/TMath.Sqrt(12))
            #     expected_res_vs_x.SetBinContent(i,-10.0)

            # if (info.th1.FindBin(-max_strip_edge)<i and i<info.th1.FindBin(max_strip_edge)):
            #     oneStripHist.SetBinContent(i, 30)
            # if (("300uw" in dataset) and ((i == (info.th1.FindBin(-max_strip_edge)+1)) or (i == (info.th1.FindBin(max_strip_edge)-1)))):
            #     oneStripHist.SetBinContent(i, -10.0)

        # Removing tracker's contribution
        if (value > trkr_value) and rm_tracker:
            error = error*value/TMath.Sqrt(value*value - trkr_value**2)
            value = TMath.Sqrt(value*value - trkr_value**2)
        # Get track of bins with resolution smaller than tracker
        elif value > 0.0:
            value = 2.0
            error = 2.0
        # if info.f.Get("stripBoxInfo06") and (i<=info.th1.FindBin(-1.1) or info.th1.FindBin(1.1)<=i):
        #     value = -10.0
        #     error = 0.0
        #     expected_res_vs_x.SetBinContent(i,-10)

        # elif not info.f.Get("stripBoxInfo06") and (i<=info.th1.FindBin(-0.9) or info.th1.FindBin(0.9)<=i):
        #     value = -10.0
        #     error = 0.0
        #     expected_res_vs_x.SetBinContent(i,-10)

        if (is_hotspot and hist_twoStrip_fullSnsr.GetBinContent(i)<2.0):
            value = -10.0
            error = 0

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)

        # ### Fill WeightedAverage
        # x_value = info.th1.GetBinCenter(i)

        # eff_OneStrip_value = eff_OneStrip.GetBinContent(i)
        # eff_TwoStrip_value = eff_TwoStrip.GetBinContent(i)

        # res_OneStrip_value = oneStripHist.GetBinContent(oneStripHist.FindBin(x_value))
        # res_TwoStrip_value = value

        # weighted_value = TMath.Sqrt(res_OneStrip_value*res_OneStrip_value*eff_OneStrip_value + res_TwoStrip_value*res_TwoStrip_value*eff_TwoStrip_value)

        # if res_TwoStrip_value<5.0:
        #     weighted_value = res_OneStrip_value #*eff_OneStrip_value

        # # Remove unwanted bins outside the expected curve
        # if expected_res_vs_x.GetBinContent(i)<0:
        #     weighted_value = 0.0

        # weighted_hist.SetBinContent(i, weighted_value)

# Get lines with binary readout in the sensor, binary readout in the strip, and oneStripReco

binary_readout_res_sensor = ROOT.TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
binary_readout_res_sensor.SetLineWidth(3)
binary_readout_res_sensor.SetLineStyle(7)
binary_readout_res_sensor.SetLineColor(colors[4]) #kGreen+2 #(TColor.GetColor(136,34,85))

# Plot 2D histograms
outputfile = TFile("%sPlotXRes%s.root"%(outdir,pref_hotspot),"RECREATE")
# for info in all_histoInfos:
htemp = TH1F("htemp","",1,-xlength,xlength)
htemp.SetStats(0)
# htemp.SetMinimum(0.0)
# htemp.SetMaximum(info.yMax)
htemp.GetYaxis().SetRangeUser(0.0, hist_info_twoStrip.yMax)
# htemp.SetLineColor(kBlack)
htemp.GetXaxis().SetTitle(hist_info_twoStrip.xlabel)
htemp.GetYaxis().SetTitle(hist_info_twoStrip.ylabel)
# hist_info_twoStrip.th1.Draw("hist e")
# hist_info_twoStrip.th1.SetStats(0)
# hist_info_twoStrip.th1.SetMinimum(0.0001)
# hist_info_twoStrip.th1.SetMaximum(hist_info_twoStrip.yMax)
hist_info_twoStrip.th1.SetLineWidth(3)
hist_info_twoStrip.th1.SetLineColor(colors[2])
# hist_info_twoStrip.th1.SetTitle(hist_info_twoStrip.title)
# hist_info_twoStrip.th1.GetXaxis().SetTitle(hist_info_twoStrip.xlabel)
# hist_info_twoStrip.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
# hist_info_twoStrip.th1.GetYaxis().SetTitle(hist_info_twoStrip.ylabel)
htemp.Draw("AXIS")

ymin = hist_info_twoStrip.th1.GetMinimum()
ymax = hist_info_twoStrip.yMax

this_shift = hist_info_twoStrip.shift() if useShift else 0

for i,box in enumerate(boxes):
    # if (i!=0 and i!=(len(boxes)-1)):
    box.Draw()

# Draw lines
binary_readout_res_sensor.Draw("same")
# binary_readout_res_strip.Draw("same")

# weighted_hist.Draw("hist same")

# tracker_res = ROOT.TLine(-xlength,5.,xlength,5.)
# tracker_res.SetLineWidth(4)
# tracker_res.SetLineStyle(5)
# tracker_res.SetLineColor(880) #kViolet
# tracker_res.Draw("same")

gPad.RedrawAxis("g")

# Create oneStripRes curve (per channel)
# oneStripBins = [-1.00, -0.50, 0.00, 0.50, 1.00] if strip_width!=300 else [-1.25, -0.75, -0.25, 0.25, 0.75, 1.25]
if showOneStrip:
    oneStripBins = [-0.75, -0.25, 0.25, 0.75] if strip_width==300 else [-1.00, -0.50, 0.00, 0.50, 1.00]
    oneStripValues = []
    for i,box in enumerate(boxes):
        if (i!=0 and i!=(len(boxes)-1)):
            oneStripValues.append(oneStripResValue_list[i])

    oneStripHist = ROOT.TGraph(len(oneStripBins), array('f',oneStripBins), array('f',oneStripValues))
    oneStripHist.SetName("h_oneStrip")
    # oneStripHist.SetLineWidth(3)
    oneStripHist.SetLineStyle(1)
    oneStripHist.SetMarkerStyle(33)
    oneStripHist.SetMarkerSize(3)
    oneStripHist.SetMarkerColor(colors[0])

    oneStripHist.Draw("P same")

hist_info_twoStrip.th1.Draw("hist e same")

# Create and fill legend
legend = TLegend(myStyle.GetPadCenter()-0.25,1-myStyle.GetMargin()-0.385, myStyle.GetPadCenter()+0.25,1-myStyle.GetMargin()-0.095)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetBorderSize(0)
# legend.SetFillColor(kWhite)
# legend.SetFillStyle(0)

legend.AddEntry(binary_readout_res_sensor, "Pitch / #sqrt{12}","l")
if showOneStrip:
    legend.AddEntry(oneStripHist, "Exactly one strip observed","P")
# legend.AddEntry(tracker_res, "Tracker resolution","l")

if ('twoStrips' in info.outHistoName):
    expected_res_vs_x.Draw("hist same")
    legend.AddEntry(expected_res_vs_x,"Two strip expected","l")
    legend.AddEntry(hist_info_twoStrip.th1, "Two strip observed","l")

# legend.AddEntry(weighted_hist, "Effective resolution","l")
    
htemp.Draw("AXIS same")
legend.Draw();

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

save_name = "%sPositionRes_vs_x%s"%(outdir,pref_hotspot) if not useTight else "%sPositionRes_vs_x_tight"%(outdir)

# ("../output/PositionResolution/%s_xPosition.gif"%(dataset))
canvas.SaveAs("%s.gif"%(save_name))
canvas.SaveAs("%s.pdf"%(save_name))
expected_res_vs_x.Write()
hist_info_twoStrip.th1.Clone("h_twoStrip").Write()
if showOneStrip:
    oneStripHist.Write()

htemp.Delete()
binary_readout_res_sensor.Write("l_sqrt12")

print()
outputfile.Close()
if (is_hotspot):
    input_fullSnsr.Close()
