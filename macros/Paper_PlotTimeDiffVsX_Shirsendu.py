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
    def __init__(self, inHistoName, f, outHistoName, xlabel="Tracker Position [mm]", ylabel="Time resolution [ps]"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor))
        # self.th1Mean = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name, axis='zx'):
        th3 = f.Get(name)
        #th3.RebinX(2)
        th2 = th3.Project3D(axis)
        if sensor=="BNL2020": th2.RebinX(5)
        elif sensor=="BNL2021": th2.RebinX(10)
        return th2

    def shift(self):
        return self.f.Get("stripBoxInfo03").GetMean(1)

    #def shift(self):
        #real_center = self.f.Get("stripBoxInfo03").GetMean(1)
        #if not self.f.Get("stripBoxInfo06"): real_center = (self.f.Get("stripBoxInfo02").GetMean(1) + real_center)/2.
        #return real_center


    def getTH1(self, th2, name, centerShift, fine_value):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift-fine_value,th2.GetXaxis().GetXmax()-centerShift-fine_value)
        return th1_temp   
    
    def fine_tuning(self, sensor):
        value = 0.0
        if sensor=="BNL2020": value = 0.0025
        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
parser.add_option('-n', dest='noShift', action='store_false', default = True, help="Do not apply shift (this gives an asymmetric distribution in general)")

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
pitch  = sensor_Geometry['pitch']
strip_width  = sensor_Geometry['stripWidth']
strip_length  = sensor_Geometry['length']

xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

#outdir = myStyle.GetPlotsDir(outdir, "TimeRes/")
outdir = myStyle.getOutputDir("Paper2022")
all_histoInfos = [
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    HistoInfo("timeDiffTracker_vs_xy", inputfile, "time_DiffTracker"),
    #HistoInfo("timeDiffLGADXY_vs_xy", inputfile, "time_DiffLGADXY"),
    HistoInfo("weighted2_timeDiff_tracker_vs_xy", inputfile, "weighted2_time_DiffTracker"),
    HistoInfo("weighted2_timeDiff_LGADXY_vs_xy", inputfile, "weighted2_time_DiffLGADXY"),
    #HistoInfo("weighted2_timeDiff_LGADX_vs_xy_2Strip_Even", inputfile, "weighted2_time_DiffLGADX_Even"),
]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
canvas.SetGrid(0,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_resTimeX0/")

#max_strip_edge = all_histoInfos[0].f.Get("stripBoxInfo03").GetMean(1) + strip_width/2000.
#if useShift: max_strip_edge -= all_histoInfos[0].shift()

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()

#loop over X bins
for i in range(0, nXBins+1):
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

        minEvtsCut = totalEvents/nXBins
        if i==0: print(info.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")


        #Do fit 
        if(nEvents > minEvtsCut):
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myFitMean = fit.GetParameter(1)
            myFitMeanError = fit.GetParError(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            valueRaw = 1000.0*mySigma
            value = math.sqrt((valueRaw*valueRaw) - (10.0*10.0))
            errorRaw = 1000.0*mySigmaError
            error  = errorRaw*(valueRaw/value)
            valueMean = abs(1000.0*myFitMean)
            errorMean = 1000.0*myFitMeanError

            ##For Debugging
            #tmpHist.Draw("hist")
            #fit.Draw("same")
            #canvas.SaveAs(outdir+"q"+info.outHistoName +"_"+str(i)+".gif")
            
            if (debugMode):
                tmpHist.Draw("hist")
                fit.Draw("same")
                canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution: %.3f +/- %.3f"%(value, error))


            # print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
        else:
            value = 0.0
            valueMean = 0.0

        ## Removing telescope contribution
        #if value!=0.0:
        #    error = error*value/TMath.Sqrt(value*value - 10*10)
        #    value = TMath.Sqrt(value*value - 10*10)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
        # info.th1Mean.SetBinContent(i,valueMean)
        # info.th1Mean.SetBinError(i,errorMean)
                        
# Plot 2D histograms
outputfile = TFile(outdir+"timeDiffVsXandY.root","RECREATE")
for info in all_histoInfos:
    #info.th1.Draw("hist e")
    info.th1.SetStats(0)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
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

canvas.SaveAs(outdir+"TimeRes_vs_x_"+info.outHistoName+".gif")
canvas.SaveAs(outdir+"TimeRes_vs_x_"+info.outHistoName+".pdf")
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
legend = TLegend(myStyle.GetPadCenter()-0.15,1-myStyle.GetMargin()-0.80,myStyle.GetPadCenter()+0.25,1-myStyle.GetMargin()-0.60)
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


#myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"TimeRes_vs_x_BothMethods.gif")
canvas.SaveAs(outdir+"TimeRes_vs_x_BothMethods.pdf")

outputfile.Close()

