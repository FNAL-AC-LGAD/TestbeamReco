from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TH1D,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite
import os
import optparse
from stripBox import getStripBox,getStripBoxY
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.th2 = self.getTH2(f, inHistoName, 'zx')
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift())
        # self.th1Mean = self.getTH1(self.th2, outHistoName, self.shift())
        
        self.th2Y = self.getTH2(f, inHistoName, 'zy')
        self.th1Y = self.getTH1(self.th2Y, outHistoName+"Y", self.shiftY())
        # self.th1MeanY = self.getTH1(self.th2Y, outHistoName, self.shiftY())

    def getTH2(self, f, name, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)
        th2.RebinX(2)
        return th2

    def getTH1(self, th2, name, centerShift):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift,th2.GetXaxis().GetXmax()-centerShift)
        return th1_temp
    
    def shift(self):
        return (self.f.Get("stripBoxInfo00").GetMean(1)+self.f.Get("stripBoxInfo01").GetMean(1))/2.

    def shiftY(self):
        return (self.f.Get("stripBoxInfoY00").GetMean(1)+self.f.Get("stripBoxInfoY10").GetMean(1))/2.

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "HPK C2", help="Type of sensor (HPK C2, HPK B2, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 180, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file)

all_histoInfos = [
    HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_00"),
    HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_01"),
    HistoInfo("timeDiff_vs_xy_channel10",inputfile, "channel_10"),
    HistoInfo("timeDiff_vs_xy_channel11",inputfile, "channel_11"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    # HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    # HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
    HistoInfo("weighted2_timeDiff_vs_xy", inputfile, "weighted2_time_diff"),
    # HistoInfo("weighted_timeDiff_goodSig_vs_xy", inputfile, "weighted_time_goodSig"),
    # HistoInfo("weighted2_timeDiff_goodSig_vs_xy", inputfile, "weighted2_time_goodSig"),
]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, all_histoInfos[0].th2.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
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

        #Do fit 
        if(nEvents > 50):
            tmpHist.Rebin(2)

            fit = TF1('fit','gaus',fitlow,fithigh)
            tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
            myFitMean = fit.GetParameter(1)
            myFitMeanError = fit.GetParError(1)
            mySigma = fit.GetParameter(2)
            mySigmaError = fit.GetParError(2)
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
            valueMean = abs(1000.0*myFitMean)
            errorMean = 1000.0*myFitMeanError

            ##For Debugging
            #tmpHist.Draw("hist")
            #fit.Draw("same")
            #canvas.SaveAs("q_"+str(i)+".gif")
            #
            #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
        else:
            value = 0.0
            valueMean = 0.0

        if i<=info.th1.FindBin(-0.25) or i>=info.th1.FindBin(0.25):
            value = 0.0
            error = 0.0

        # Removing telescope contribution
        if value!=0.0:
            error = error*value/TMath.Sqrt(value*value - 10*10)
            value = TMath.Sqrt(value*value - 10*10)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
        # info.th1Mean.SetBinContent(i,valueMean)
        # info.th1Mean.SetBinError(i,errorMean)

# Plot 2D histograms
outputfile = TFile("timeDiffVsXandY.root","RECREATE")
for info in all_histoInfos:
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    info.th1.SetTitle(info.outHistoName)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(70.0)
    info.th1.SetLineColor(kBlack)
    info.th1.GetXaxis().SetTitle("Track x position [mm]")
    info.th1.GetXaxis().SetRangeUser(-0.55, 0.55)
    info.th1.GetYaxis().SetTitle("Time resolution [ps]")

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
    boxes = getStripBox(inputfile,ymin,ymax,False,18,False,info.shift())
    for box in boxes:
        box.Draw()

    # boxes2 = getStripBox(inputfile,ymin,ymax,True,kRed,False,info.shift())
    # for box in boxes2:
    #     box.Draw()
    
    gPad.RedrawAxis("g")

    # info.th1Mean.SetLineColor(880)
    # info.th1Mean.Draw("hist e same")
    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()

hTimeRes = all_histoInfos[4].th1
hTimeResW2 = all_histoInfos[6].th1
hTimeRes.SetLineColor(kBlack)
hTimeResW2.SetLineColor(416+2) #kGreen+2 #(TColor.GetColor(136,34,85))

hTimeRes.SetMinimum(0.0001)
hTimeRes.SetMaximum(70.0)
hTimeRes.Draw("hist e")

ymin = hTimeRes.GetMinimum()
ymax = hTimeRes.GetMaximum()
boxes = getStripBox(inputfile,ymin,ymax,False,18,False,all_histoInfos[4].shift())
for box in boxes:
    box.Draw()

gPad.RedrawAxis("g")

hTimeRes.Draw("hist e same")
hTimeRes.Draw("AXIS same")
hTimeResW2.Draw("hist e same")

legend = TLegend(myStyle.GetPadCenter()-0.33,0.70,myStyle.GetPadCenter()+0.33,0.90)
legend.SetFillColor(kWhite)
legend.AddEntry(hTimeRes, "Single-channel timestamp")
legend.AddEntry(hTimeResW2, "Multi-channel timestamp")
legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

canvas.SaveAs("TimeRes_vs_x_BothMethods.gif")
canvas.SaveAs("TimeRes_vs_x_BothMethods.pdf")

outputfile.Close()

