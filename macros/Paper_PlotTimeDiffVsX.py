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
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0, ylabel="Time resolution [ps]", sensor="", addShift = False):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.ylabel = ylabel
        self.sensor = sensor
        self.th2 = self.getTH2(f, inHistoName, sensor)
        # self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor))
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor), addShift)
        # self.th1Mean = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name, sensor, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)
        if sensor=="BNL2020": th2.RebinX(5)
        elif sensor=="BNL2021": th2.RebinX(10)
        if "1cm_500up_300uw" in sensor: th2.RebinX(2)
        return th2

    def getTH1(self, th2, name, centerShift, fine_value, shift):
        if shift:
            th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-fine_value,th2.GetXaxis().GetXmax()-fine_value) # -centerShift
        else:
            th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin(),th2.GetXaxis().GetXmax()) # -centerShift
        return th1_temp

    def shift(self):
        if ("2x2pad" not in sensor):
            real_center = self.f.Get("stripBoxInfo03").GetMean(1)
            if not self.f.Get("stripBoxInfo06"):
                real_center = (self.f.Get("stripBoxInfo02").GetMean(1) + real_center)/2.
        else:
            real_center = 0.0

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

    # def shift(self):
    #     return self.f.Get("stripBoxInfo03").GetMean(1)

    # #def shift(self):
    #     #real_center = self.f.Get("stripBoxInfo03").GetMean(1)
    #     #if not self.f.Get("stripBoxInfo06"): real_center = (self.f.Get("stripBoxInfo02").GetMean(1) + real_center)/2.
    #     #return real_center


    # def getTH1(self, th2, name, centerShift, fine_value):
    #     th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift-fine_value,th2.GetXaxis().GetXmax()-centerShift-fine_value)
    #     return th1_temp   
    
    # def fine_tuning(self, sensor):
    #     value = 0.0
    #     if sensor=="BNL2020": value = 0.0025
    #     return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")
parser.add_option('-g', '--hot', dest='hotspot', action='store_true', default = False, help="Use hotspot")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")

options, args = parser.parse_args()
useShift = options.noShift
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

outdir = myStyle.GetPlotsDir(outdir, "Paper_Resolution_Time/")

# Save list with histograms to draw
list_htitles = [
    # [hist_input_name, short_output_name, y_axis_title]
    ["timeDiff_vs_xy", "time_diff", "Time resolution [ps]"],
    ["timeDiffTracker_vs_xy", "time_DiffTracker", "Time resolution [ps]"],
    ["weighted2_timeDiff_tracker_vs_xy", "weighted2_time_DiffTracker", "Time resolution [ps]"],
    ["weighted2_timeDiff_LGADXY_vs_xy", "weighted2_time_DiffLGADXY", "Time resolution [ps]"],
]

# Use tight cut histograms
if (is_tight):
    print("    Using tight cuts.")
    for titles in list_htitles:
        titles[0]+= "%s_tight"

# Use hotspot extension if required
if (is_hotspot):
    list_htitles = [["weighted2_timeDiff_tracker_vs_xy_hotspot", "weighted2_time_DiffTracker_hotspot", "Time resolution [ps]"]]


# List with histograms using HistoInfo class
all_histoInfos = []
for titles in list_htitles:
    hname, outname, ytitle = titles
    info_obj = HistoInfo(hname, inputfile, outname, True,  ylength, ytitle, dataset, useShift)
    all_histoInfos.append(info_obj)


# all_histoInfos = [
#     # HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
#     # HistoInfo("timeDiffTracker_vs_xy", inputfile, "time_DiffTracker"),
#     # #HistoInfo("timeDiffLGADXY_vs_xy", inputfile, "time_DiffLGADXY"),
#     # HistoInfo("weighted2_timeDiff_tracker_vs_xy", inputfile, "weighted2_time_DiffTracker"),
#     # HistoInfo("weighted2_timeDiff_LGADXY_vs_xy", inputfile, "weighted2_time_DiffLGADXY"),
#     # #HistoInfo("weighted2_timeDiff_LGADX_vs_xy_2Strip_Even", inputfile, "weighted2_time_DiffLGADX_Even"),
#     HistoInfo("timeDiff_vs_xy%s"%(tight_ext), inputfile, "time_diff", True,  ylength, "", "Track x position [mm]","Time resolution [ps]",dataset, useShift),
#     HistoInfo("timeDiffTracker_vs_xy%s"%(tight_ext), inputfile, "time_DiffTracker",True,  ylength, "", "Track x position [mm]","Time resolution [ps]",dataset, useShift),
#     HistoInfo("weighted2_timeDiff_tracker_vs_xy%s%s"%(pref_hotspot,tight_ext), inputfile, "weighted2_time_DiffTracker%s"%pref_hotspot,True,  ylength, "", "Track x position [mm]","Time resolution [ps]",dataset, useShift),
#     HistoInfo("weighted2_timeDiff_LGADXY_vs_xy%s"%(tight_ext), inputfile, "weighted2_time_DiffLGADXY",True,  ylength, "", "Track x position [mm]","Time resolution [ps]",dataset, useShift),
# ]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_ResTimeVsX0/")

### WIP

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()

#loop over X bins
for i in range(1, nXBins+1):
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
        minEvtsCut = totalEvents/nXBins
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

            value = math.sqrt((valueRaw*valueRaw) - (10.0*10.0))
            value = math.sqrt((valueRaw*valueRaw) - (res_photek*res_photek))
            error  = errorRaw*(valueRaw/value)

            
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
                        
# Plot 2D histograms
outputfile = TFile("%stimeDiffVsX%s%s.root"%(outdir,pref_hotspot,tight_ext),"RECREATE")
for info in all_histoInfos:
    #info.th1.Draw("hist e")
    info.th1.SetStats(0)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(ylength)
    info.th1.SetLineWidth(3)
    info.th1.SetLineColor(kBlack)
    #info.th1.GetXaxis().SetTitle("Track x position [mm]")
    info.th1.GetXaxis().SetRangeUser(-xlength,xlength)
    #info.th1.GetYaxis().SetTitle("Time resolution [ps]")

    ymin = info.th1.GetMinimum()
    ymax = ylength    

htemp = TH1F("htemp","",1,-xlength,xlength)
htemp.SetStats(0)
htemp.GetYaxis().SetRangeUser(0.0, ylength)
htemp.GetXaxis().SetTitle("Track x position [mm]")
htemp.GetYaxis().SetTitle("Time resolution [ps]")  
htemp.SetLineColor(colors[2])
htemp.Draw("AXIS")
#boxes = getStripBox(inputfile,0.0,ymax,False,18,True,this_shift)
#for i,box in enumerate(boxes):
    #if (i!=0 and i!=(len(boxes)-1)): box.Draw()

gPad.RedrawAxis("g")

#info.th1.Draw("AXIS same")
#info.th1.Draw("hist e same")
#myStyle.BeamInfo()
#myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"TimeRes_vs_x%s%s_"%(pref_hotspot,tight_ext)+info.outHistoName+".gif")
canvas.SaveAs(outdir+"TimeRes_vs_x%s%s_"%(pref_hotspot,tight_ext)+info.outHistoName+".pdf")
info.th1.Write()

hTimeRes =  all_histoInfos[0].th1
hTimeTracker = all_histoInfos[1].th1 
hTimeW2Tracker = all_histoInfos[2].th1
hTimeW2LGADXY = all_histoInfos[3].th1

hTimeRes.SetLineColor(colors[5])
hTimeTracker.SetLineColor(kBlack)
hTimeW2Tracker.SetLineColor(colors[2])
hTimeW2LGADXY.SetLineColor(colors[1])

#hTimeRes.SetLineStyle(2)
#hTimeTracker.SetLineStyle(2)
#hTimeW2LGADXY.SetLineStyle(2)

hTimeRes.SetLineWidth(2)
hTimeTracker.SetLineWidth(2)
hTimeW2Tracker.SetLineWidth(4)
hTimeW2LGADXY.SetLineWidth(2)

ymin = hTimeRes.GetMinimum()
ymax = ylength

boxes = getStripBox(inputfile,ymin,ymax,False,18,True,info.shift())
for box in boxes:
    box.Draw()

hTimeRes.Draw("hist e same")
hTimeW2LGADXY.Draw("hist e same")
hTimeTracker.Draw("hist e same")
hTimeW2Tracker.Draw("hist e same")
htemp.Draw("AXIS same")
gPad.RedrawAxis("g")
# legend = TLegend(myStyle.GetPadCenter()-0.15,1-myStyle.GetMargin()-0.80,myStyle.GetPadCenter()+0.25,1-myStyle.GetMargin()-0.60)
legend = TLegend(myStyle.GetPadCenter()-0.20,2*myStyle.GetMargin()+0.01,myStyle.GetPadCenter()+0.20,2*myStyle.GetMargin()+0.16)
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-20)
#legend.SetFillStyle(0)

legend.AddEntry(hTimeRes, "Single-channel, no delay correction","lep")
legend.AddEntry(hTimeTracker, "Single-channel, tracker delay correction","lep")
legend.AddEntry(hTimeW2LGADXY, "Multi-channel, LGAD delay correction","lep")
legend.AddEntry(hTimeW2Tracker, "Multi-channel, tracker delay correction","lep")
#legend.AddEntry(hTimeW2LGADXY, "Multi-channel, LGAD delay correction","lep")

htemp.Draw("AXIS same")
legend.Draw();


# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("%sTimeRes_vs_x%s%s_BothMethods.gif"%(outdir,pref_hotspot,tight_ext))
canvas.SaveAs("%sTimeRes_vs_x%s%s_BothMethods.pdf"%(outdir,pref_hotspot,tight_ext))

hTimeW2Tracker.Clone("h_time").Write()

outputfile.Close()
