from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite
import os
import optparse
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, xlabel="Tracker Position [mm]", ylabel="Resolution [ps]"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift())
        # self.th1Mean = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name, axis='zx'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)
        th2.RebinX(2)
        return th2

    def getTH1(self, th2, name, centerShift):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift,th2.GetXaxis().GetXmax()-centerShift)
        return th1_temp
    
    def shift(self):
        return (self.f.Get("stripBoxInfo02").GetMean(1)+self.f.Get("stripBoxInfo03").GetMean(1))/2.

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file)

all_histoInfos = [
    HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_1"),
    HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_2"),
    HistoInfo("timeDiff_vs_xy_channel02",inputfile, "channel_3"),
    HistoInfo("timeDiff_vs_xy_channel03",inputfile, "channel_4"),
    HistoInfo("timeDiff_vs_xy_channel04",inputfile, "channel_5"),
    HistoInfo("timeDiff_vs_xy_channel05",inputfile, "channel_6"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    # HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    # HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    # HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
    HistoInfo("weighted2_timeDiff_vs_xy", inputfile, "weighted2_time_diff"),
    # HistoInfo("weighted_timeDiff_goodSig_vs_xy", inputfile, "weighted_time_goodSig"),
    # HistoInfo("weighted2_timeDiff_goodSig_vs_xy", inputfile, "weighted2_time_goodSig"),
]

canvas = TCanvas("cv","cv",800,800)
# gPad.SetLeftMargin(0.12)
# gPad.SetRightMargin(0.15)
# gPad.SetTopMargin(0.08)
# gPad.SetBottomMargin(0.12)
# gPad.SetTicks(1,1)
#gPad.SetLogy()
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

        # Removing telescope contribution
        if value!=0.0:
            error = error*value/TMath.Sqrt(value*value - 10*10)
            value = TMath.Sqrt(value*value - 10*10)

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
        # info.th1Mean.SetBinContent(i,valueMean)
        # info.th1Mean.SetBinError(i,errorMean)
                        
# Plot 2D histograms
outputfile = TFile("BNL_timeDiffVsXandY.root","RECREATE")
for info in all_histoInfos:
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(60.0)
    info.th1.SetLineColor(kBlack)
    info.th1.GetXaxis().SetTitle("Track x position [mm]")
    # info.th1.GetXaxis().SetRangeUser(-0.43, 0.43)
    info.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
    info.th1.GetYaxis().SetTitle("Resolution [ps]")

    ymin = info.th1.GetMinimum()
    ymax = info.th1.GetMaximum()
    boxes = getStripBox(inputfile,ymin,ymax,False,18,True,info.shift())
    for box in boxes:
        box.Draw()

    gPad.RedrawAxis("g")

    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs("TimeRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()

hTimeRes = all_histoInfos[6].th1
hTimeResW2 = all_histoInfos[7].th1
hTimeRes.SetLineColor(kBlack)
hTimeResW2.SetLineColor(TColor.GetColor(136,34,85))

hTimeRes.Draw("hist e")

ymin = hTimeRes.GetMinimum()
ymax = hTimeRes.GetMaximum()
boxes = getStripBox(inputfile,ymin,ymax,False,18,True,all_histoInfos[6].shift())
for box in boxes:
    box.Draw()

gPad.RedrawAxis("g")

hTimeRes.Draw("hist e same")
hTimeRes.Draw("AXIS same")
hTimeResW2.Draw("hist e same")

legend = TLegend(myStyle.GetPadCenter()-0.31,0.70,myStyle.GetPadCenter()+0.31,0.90)
legend.SetFillColor(kWhite)
#legend.SetFillStyle(4050)
legend.AddEntry(hTimeRes, "Single-channel timestamp")
legend.AddEntry(hTimeResW2, "Multi-channel timestamp")
legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

canvas.SaveAs("TimeRes_vs_x_BothMethods.gif")
canvas.SaveAs("TimeRes_vs_x_BothMethods.pdf")

outputfile.Close()

