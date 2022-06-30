from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kRed,kWhite,TH1
import os
import optparse
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
        self.th1 = self.getTH1(self.th2, outHistoName)
        # self.th1Mean = self.getTH1(self.th2, outHistoName)

    def getTH2(self, f, name, axis='zy'):
        th3 = f.Get(name)
        th2 = th3.Project3D(axis)
        #if sensor=="BNL2020": th2.RebinX(5)
        #elif sensor=="BNL2021": th2.RebinX(10)
        return th2

    def getTH1(self, th2, name):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin(),th2.GetXaxis().GetXmax())
        return th1_temp
    

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="Limit x-axis in final plot")
parser.add_option('-y','--ylength', dest='ylength', default = 200.0, help="Max TimeResolution value in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-d', dest='debugMode', action='store_true', default = False, help="Run debug mode")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else:
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "TimeRes/")

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']
xlength = float(options.xlength)
ylength = float(options.ylength)
debugMode = options.debugMode

all_histoInfos = [
    # HistoInfo("timeDiff_vs_xy_channel00",inputfile, "channel_1"),
    # HistoInfo("timeDiff_vs_xy_channel01",inputfile, "channel_2"),
    # HistoInfo("timeDiff_vs_xy_channel02",inputfile, "channel_3"),
    # HistoInfo("timeDiff_vs_xy_channel03",inputfile, "channel_4"),
    # HistoInfo("timeDiff_vs_xy_channel04",inputfile, "channel_5"),
    # HistoInfo("timeDiff_vs_xy_channel05",inputfile, "channel_6"),
    HistoInfo("timeDiff_vs_xy", inputfile, "time_diff"),
    HistoInfo("timeDiffTracker_vs_xy", inputfile, "time_diffTracker"),
    # HistoInfo("timeDiff_vs_xy_amp2", inputfile, "time_diff_amp2"),
    # HistoInfo("timeDiff_vs_xy_amp3", inputfile, "time_diff_amp3"),
    # HistoInfo("weighted_timeDiff_vs_xy", inputfile, "weighted_time_diff"),
    HistoInfo("weighted2_timeDiff_tracker_vs_xy", inputfile, "weighted2_time_diffTracker"),
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
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)
print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = myStyle.CreateFolder(outdir, "q_resTimeY0/")

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()
# print(nXBins)
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

        minEvtsCut = 0.25*totalEvents/nXBins
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
            value = 1000.0*mySigma
            error = 1000.0*mySigmaError
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
outputfile = TFile(outdir+"timeDiffVsY.root","RECREATE")
for info in all_histoInfos:
    info.th1.Draw("hist e")
    info.th1.SetStats(0)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(ylength)
    info.th1.SetLineColor(kBlack)
    info.th1.GetXaxis().SetTitle("Track y position [mm]")
    info.th1.GetXaxis().SetRangeUser(-xlength,xlength)
    info.th1.GetYaxis().SetTitle("Time resolution [ps]")

    ymin = info.th1.GetMinimum()
    ymax = ylength
    
    gPad.RedrawAxis("g")

    info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    # myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    canvas.SaveAs(outdir+"TimeRes_vs_y_"+info.outHistoName+".gif")
    canvas.SaveAs(outdir+"TimeRes_vs_y_"+info.outHistoName+".pdf")
    info.th1.Write()


hTimeRes = all_histoInfos[0].th1 # 6
hTimeResCorr = all_histoInfos[1].th1
hTimeResW2 = all_histoInfos[2].th1 #7
hTimeRes.SetLineColor(28)
hTimeResCorr.SetLineColor(kBlack)
hTimeResW2.SetLineColor(416+2) #kGreen+2 #(TColor.GetColor(136,34,85))

hTimeRes.Draw("hist e")

ymin = hTimeRes.GetMinimum()
ymax = ylength

gPad.RedrawAxis("g")

hTimeRes.Draw("hist e same")
hTimeRes.Draw("AXIS same")
hTimeResCorr.Draw("hist e same")
hTimeResW2.Draw("hist e same")

legend = TLegend(myStyle.GetPadCenter()-0.4,0.70,myStyle.GetPadCenter()+0.4,0.90)
legend.SetFillColor(kWhite)
#legend.SetFillStyle(4050)
legend.AddEntry(hTimeRes, "Single-channel (w/o TrackerCorrection)")
legend.AddEntry(hTimeResCorr, "Single-channel (w/ TrackerCorrection)")
legend.AddEntry(hTimeResW2, "Multi-channel (w/ TrackerCorrection)")
legend.Draw();

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"TimeRes_vs_y_BothMethods.gif")
canvas.SaveAs(outdir+"TimeRes_vs_y_BothMethods.pdf")

outputfile.Close()
