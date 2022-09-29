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
        # self.sensor = sensor

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)
        # # th2_temp = TH2D(outHist,"",42,-0.210,0.210,th2.GetYaxis().GetNbins(),th2.GetYaxis().GetXmin(),th2.GetYaxis().GetXmax())
        # # for i in range(th2.GetXaxis().FindBin(-0.210+centerShift),th2.GetXaxis().FindBin(0.210+centerShift)+1,1):
        # #     th2_temp.Fill()
        # if sensor=="BNL2020": th2.RebinX(7)
        # elif sensor=="BNL2021": th2.RebinX(10)
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
parser.add_option('-x','--xlength', dest='xlength', default = 1.7, help="X axis range [-x, x]")
# parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Y axis upper limit")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")
options, args = parser.parse_args()

useShift = options.noShift
dataset = options.Dataset
outdir=""
outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "Paper_XRes/")

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']
strip_width  = sensor_Geometry['stripWidth']
strip_length  = sensor_Geometry['length']

xlength = float(options.xlength)
# ylength = 200.0
ylength = 160.0
debugMode = options.debugMode

all_histoInfos = [
    # HistoInfo("deltaX_vs_Xtrack",   inputfile, "track", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaY_vs_Xtrack",   inputfile, "track", True,  2500, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaXBasic_vs_Xtrack",   inputfile, "trackBasic", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaYBasic_vs_Xtrack",   inputfile, "trackBasic", True,  2500, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    # HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "track_oneStrip", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    HistoInfo("deltaX_vs_Xtrack_twoStrips",   inputfile, "track_twoStrips", True,  ylength, "", "Track x position [mm]","Position resolution [#mum]",dataset, useShift),
    # HistoInfo("deltaX_vs_Xtrack",   inputfile, "rms_track", False,  ylength, "", "Track x position [mm]","Position resolution RMS [#mum]",sensor),
    # HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "rms_track_oneStrip", False,  ylength, "", "Track x position [mm]","Position resolution_oneStrip RMS [#mum]",sensor),
    # HistoInfo("deltaX_vs_Xtrack_twoStrips",   inputfile, "rms_track_twoStrips", False,  ylength, "", "Track x position [mm]","Position resolution_twoStrips RMS [#mum]",sensor),
]


#### Get histograms for expected resolution
noise12_vs_x = inputfile.Get("BaselineRMS12_vs_x")
amp12_vs_x = inputfile.Get("Amp12_vs_x")
amp1_vs_x = inputfile.Get("Amp1_vs_x")
amp2_vs_x = inputfile.Get("Amp2_vs_x")
dXdFrac_vs_x = inputfile.Get("dXdFrac_vs_Xtrack")

mean_noise12_vs_x = noise12_vs_x.ProfileX()
mean_amp12_vs_x = amp12_vs_x.ProfileX()
mean_amp1_vs_x = amp1_vs_x.ProfileX()
mean_amp2_vs_x = amp2_vs_x.ProfileX()
mean_dXFrac_vs_x = dXdFrac_vs_x.ProfileX()

nbinsx = mean_amp12_vs_x.GetNbinsX()
low_x = mean_amp12_vs_x.GetBinLowEdge(1) # - all_histoInfos[0].shift() - all_histoInfos[0].fine_tune
high_x = mean_amp12_vs_x.GetBinLowEdge(nbinsx+1) # - all_histoInfos[0].shift() - all_histoInfos[0].fine_tune
if useShift:
    low_x -= all_histoInfos[0].fine_tune
    high_x -= all_histoInfos[0].fine_tune

expected_res_vs_x = ROOT.TH1F("h_exp","",nbinsx,low_x,high_x)
expected_res_vs_x.SetLineWidth(3)
expected_res_vs_x.SetLineStyle(7)
expected_res_vs_x.SetLineColor(colors[2])
for ibin in range(expected_res_vs_x.GetNbinsX()+1):
    if mean_amp12_vs_x.GetBinContent(ibin)>0:
        # With tracker's contribution of 5 microns
        # expected_res = math.sqrt(5.**2 + pow(abs(1000*mean_dXFrac_vs_x.GetBinContent(ibin) * (0.5*mean_noise12_vs_x.GetBinContent(ibin)) * pow(pow(mean_amp1_vs_x.GetBinContent(ibin),2)+pow(mean_amp2_vs_x.GetBinContent(ibin),2),0.5) /  (mean_amp12_vs_x.GetBinContent(ibin))**2),2))

        # Without tracker's contribution of 5 microns
        expected_res = abs(1000*mean_dXFrac_vs_x.GetBinContent(ibin) * (0.5*mean_noise12_vs_x.GetBinContent(ibin)) * pow(pow(mean_amp1_vs_x.GetBinContent(ibin),2)+pow(mean_amp2_vs_x.GetBinContent(ibin),2),0.5) /  (mean_amp12_vs_x.GetBinContent(ibin))**2)
    else:
        expected_res=-10.0

    #print("Bin %i, res %0.2f"%(ibin,expected_res))
    expected_res_vs_x.SetBinContent(ibin,expected_res)

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_res0/")


# oneStripResValue = myStyle.resolutions2022[dataset]['position_oneStripRMS']
oneStripResValue_list = myStyle.resolutions2022OneStripChannel[dataset]['resOneStrip']
# oneStripHist = all_histoInfos[0].th1.Clone("oneStripRes")
# oneStripHist.SetLineWidth(3)
# # oneStripHist.SetLineStyle(1)
# oneStripHist.SetLineColor(colors[0])

max_strip_edge = all_histoInfos[0].f.Get("stripBoxInfo01").GetMean(1) + strip_width/2000.
if useShift: max_strip_edge -= all_histoInfos[0].shift()

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()
#loop over X bins
for i in range(0, nXBins+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

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

        if i==0: print("%s: nEvents > %.2f (Total events: %i; N bins: %i)"%(info.inHistoName,minEvtsCut,totalEvents,nXBins))
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
            if "track_twoStrips" in info.outHistoName:
                ## Add metal width/sqrt(12) as expected resolution in metal region
                # expected_res_vs_x.SetBinContent(i,strip_width/TMath.Sqrt(12))
                expected_res_vs_x.SetBinContent(i,-10.0)

            # if (info.th1.FindBin(-max_strip_edge)<i and i<info.th1.FindBin(max_strip_edge)):
            #     oneStripHist.SetBinContent(i, 30)
            # if (("300uw" in dataset) and ((i == (info.th1.FindBin(-max_strip_edge)+1)) or (i == (info.th1.FindBin(max_strip_edge)-1)))):
            #     oneStripHist.SetBinContent(i, -10.0)

        # Removing tracker's contribution of 5 microns
        if value>5.0:
            error = error*value/TMath.Sqrt(value*value - 5*5)
            value = TMath.Sqrt(value*value - 5*5)
        elif value>0.0:
            value = 2.0 # to check if there are strange resolution values
            error = 2.0
        # if info.f.Get("stripBoxInfo06") and (i<=info.th1.FindBin(-1.1) or info.th1.FindBin(1.1)<=i):
        #     value = -10.0
        #     error = 0.0
        #     expected_res_vs_x.SetBinContent(i,-10)
        
        # elif not info.f.Get("stripBoxInfo06") and (i<=info.th1.FindBin(-0.9) or info.th1.FindBin(0.9)<=i):
        #     value = -10.0
        #     error = 0.0
        #     expected_res_vs_x.SetBinContent(i,-10)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)

# Get lines with binary readout in the sensor, binary readout in the strip, and oneStripReco

# sqrt_12 = TLatex("#sqrt(12)")

binary_readout_res_sensor = ROOT.TLine(-xlength,pitch/TMath.Sqrt(12), xlength,pitch/TMath.Sqrt(12))
binary_readout_res_sensor.SetLineWidth(3)
binary_readout_res_sensor.SetLineStyle(7)
binary_readout_res_sensor.SetLineColor(colors[4]) #kGreen+2 #(TColor.GetColor(136,34,85))

# Get OneStripReco observed histogram
# indexOneStrip = 1
# change=False
# for i in range(oneStripHist.GetNbinsX(), 0, -1):
#     if oneStripResValue_list[indexOneStrip]<0.0: break
#     if oneStripHist.GetBinContent(i) > 0.0:
#         oneStripHist.SetBinContent(i,oneStripResValue_list[indexOneStrip])
#         if oneStripHist.GetBinContent(i-1) < 0.0:
#             change = True
#     if change:
#         indexOneStrip+=1
#         change=False

# Plot 2D histograms
outputfile = TFile(outdir+"PlotXRes.root","RECREATE")
for info in all_histoInfos:
    htemp = TH1F("htemp","",1,-xlength,xlength)
    htemp.SetStats(0)
    # htemp.SetMinimum(0.0)
    # htemp.SetMaximum(info.yMax)
    htemp.GetYaxis().SetRangeUser(0.0, info.yMax)
    # htemp.SetLineColor(kBlack)
    htemp.GetXaxis().SetTitle(info.xlabel)
    htemp.GetYaxis().SetTitle(info.ylabel)
    # info.th1.Draw("hist e")
    # info.th1.SetStats(0)
    # info.th1.SetMinimum(0.0001)
    # info.th1.SetMaximum(info.yMax)
    info.th1.SetLineWidth(3)
    info.th1.SetLineColor(colors[2])
    # info.th1.SetTitle(info.title)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    htemp.Draw("AXIS")

    ymin = info.th1.GetMinimum()
    ymax = info.yMax

    this_shift = info.shift() if useShift else 0

    binary_readout_res_strip_4legend = []
    boxes = getStripBox(inputfile,0.0,ymax,False,18,True,this_shift)

    oneStripBins = [-1.00, -0.50, 0.00, 0.50, 1.00] if strip_width==300 else [-1.25, -0.75, -0.25, 0.25, 0.75, 1.25]
    oneStripHist = TH1F("oneStripRes","", len(oneStripBins)-1, array('f',oneStripBins)) # all_histoInfos[0].th1.Clone("oneStripRes")
    oneStripHist.SetLineWidth(3)
    # oneStripHist.SetLineStyle(1)
    oneStripHist.SetLineColor(colors[0])

    for i,box in enumerate(boxes):
        if (i!=0 and i!=(len(boxes)-1)):
            box.Draw()
            xl = box.GetX1()
            xr = box.GetX2()
            binary_readout_res_strip = ROOT.TLine(xl,strip_width/TMath.Sqrt(12), xr,strip_width/TMath.Sqrt(12))
            binary_readout_res_strip.SetLineWidth(3)
            binary_readout_res_strip.SetLineStyle(7)
            binary_readout_res_strip.SetLineColor(colors[0]) #kGreen+2 #(TColor.GetColor(136,34,85))
            binary_readout_res_strip_4legend.append(binary_readout_res_strip)
            binary_readout_res_strip_4legend[-1].Draw("same")

            oneStripHist.Fill(xl, oneStripResValue_list[i])

    # Draw lines
    binary_readout_res_sensor.Draw("same")
    # binary_readout_res_strip.Draw("same")
    oneStripHist.Draw("hist same")
    
    # tracker_res = ROOT.TLine(-xlength,5.,xlength,5.)
    # tracker_res.SetLineWidth(4)
    # tracker_res.SetLineStyle(5)
    # tracker_res.SetLineColor(880) #kViolet
    # tracker_res.Draw("same")

    gPad.RedrawAxis("g")

    # info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    legend = TLegend(myStyle.GetPadCenter()-0.25,1-myStyle.GetMargin()-0.385, myStyle.GetPadCenter()+0.25,1-myStyle.GetMargin()-0.095)
    # legend.SetBorderSize(0)
    # legend.SetFillColor(kWhite)
    legend.SetTextFont(myStyle.GetFont())
    legend.SetTextSize(myStyle.GetSize()-4)
    #legend.SetFillStyle(0)

    legend.AddEntry(binary_readout_res_sensor, "Pitch / #sqrt{12}","l")
    legend.AddEntry(binary_readout_res_strip_4legend[0], "Width / #sqrt{12}","l")
    legend.AddEntry(oneStripHist, "Exactly one strip observed","l")
    # legend.AddEntry(tracker_res, "Tracker resolution","l")

    # if ('oneStrip' in info.outHistoName):
    #     legend.AddEntry(info.th1, "One strip reconstruction")
    if ('twoStrips' in info.outHistoName):
        expected_res_vs_x.Draw("hist same")
        legend.AddEntry(expected_res_vs_x,"Two strip expected","l")
        legend.AddEntry(info.th1, "Two strip observed","l")
    # else:
    #     legend.AddEntry(info.th1, "Full reconstruction")
        
    htemp.Draw("AXIS same")
    legend.Draw();

    myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    canvas.SaveAs(outdir+"PositionRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"PositionRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()
    htemp.Delete()

outputfile.Close()

