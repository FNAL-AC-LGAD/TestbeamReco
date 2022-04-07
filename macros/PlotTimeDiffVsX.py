from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite
import os
import optparse
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

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
        th2 = th3.Project3D(axis)
        if sensor=="BNL2020": th2.RebinX(5)
        elif sensor=="BNL2021": th2.RebinX(10)
        return th2

    def getTH1(self, th2, name, centerShift, fine_value):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift-fine_value,th2.GetXaxis().GetXmax()-centerShift-fine_value)
        return th1_temp
    
    def shift(self):
        return self.f.Get("stripBoxInfo03").GetMean(1)
    
    def fine_tuning(self, sensor):
        value = 0.0
        if sensor=="BNL2020": value = 0.0025
        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="Bias Voltage value in [V]") 
parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Bias Voltage value in [V]") 
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath") 
options, args = parser.parse_args()

sensor = options.sensor
bias = options.biasvolt
xlength = float(options.xlength) 
ylength = float(options.ylength) 

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")   

all_histoInfos = [
    # HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_1"),
    # HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_2"),
    # HistoInfo("timeDiff_vs_xy_channel02",inputfile, "channel_3"),
    # HistoInfo("timeDiff_vs_xy_channel03",inputfile, "channel_4"),
    # HistoInfo("timeDiff_vs_xy_channel04",inputfile, "channel_5"),
    # HistoInfo("timeDiff_vs_xy_channel05",inputfile, "channel_6"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    # HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    # HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    # HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
    HistoInfo("weighted2_timeDiff_vs_xy", inputfile, "weighted2_time_diff"),
    # HistoInfo("weighted_timeDiff_goodSig_vs_xy", inputfile, "weighted_time_goodSig"),
    # HistoInfo("weighted2_timeDiff_goodSig_vs_xy", inputfile, "weighted2_time_goodSig"),
]

canvas = TCanvas("cv","cv",1000,800)
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
            # tmpHist.Draw("hist")
            # fit.Draw("same")
            # canvas.SaveAs(outdir+"q"+info.outHistoName +"_"+str(i)+".gif")
            
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
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(ylength)
    info.th1.SetLineColor(kBlack)
    info.th1.GetXaxis().SetTitle("Track x position [mm]")
    info.th1.GetXaxis().SetRangeUser(-xlength,xlength)
    info.th1.GetYaxis().SetTitle("Time resolution [ps]")

    ymin = info.th1.GetMinimum()
    ymax = ylength
    boxes = getStripBox(inputfile,ymin,ymax,False,18,True,info.shift())
    for box in boxes:
        box.Draw()

    gPad.RedrawAxis("g")

    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    canvas.SaveAs(outdir+"TimeRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"TimeRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()

hTimeRes = all_histoInfos[0].th1 # 6
hTimeResW2 = all_histoInfos[1].th1 #7
hTimeRes.SetLineColor(kBlack)
hTimeResW2.SetLineColor(416+2) #kGreen+2 #(TColor.GetColor(136,34,85))

hTimeRes.Draw("hist e")

ymin = hTimeRes.GetMinimum()
ymax = ylength
boxes = getStripBox(inputfile,ymin,ymax,False,18,True,all_histoInfos[0].shift()) # 6
for box in boxes:
    box.Draw()

gPad.RedrawAxis("g")

hTimeRes.Draw("hist e same")
hTimeRes.Draw("AXIS same")
hTimeResW2.Draw("hist e same")

legend = TLegend(myStyle.GetPadCenter()-0.33,0.70,myStyle.GetPadCenter()+0.33,0.90)
legend.SetFillColor(kWhite)
#legend.SetFillStyle(4050)
legend.AddEntry(hTimeRes, "Single-channel timestamp")
legend.AddEntry(hTimeResW2, "Multi-channel timestamp")
legend.Draw();

myStyle.BeamInfo()
myStyle.SensorInfo(sensor, bias)

canvas.SaveAs(outdir+"TimeRes_vs_x_BothMethods.gif")
canvas.SaveAs(outdir+"TimeRes_vs_x_BothMethods.pdf")

outputfile.Close()

