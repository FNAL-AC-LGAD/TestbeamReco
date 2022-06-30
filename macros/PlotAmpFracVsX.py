from ROOT import TFile,TTree,TCanvas,TH1D,TH1F,TH2D,TH2F,TLatex,TMath,TColor,TLegend,TEfficiency,TGraphAsymmErrors,gROOT,gPad,TF1,gStyle,kBlack,kWhite,TH1
import ROOT
import os
from stripBox import getStripBox
import optparse
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
organized_mode=True

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=1.0, title="", xlabel="", ylabel="Amp fraction"):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift())

    def getTH2(self, f, name):
        th2 = f.Get(name)
        return th2

    def getTH1(self, th2, name, centerShift):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift,th2.GetXaxis().GetXmax()-centerShift)
        return th1_temp

    def shift(self):
        return self.f.Get("stripBoxInfo03").GetMean(1)


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 4.0, help="X axis range [-x, x]")
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

sensor_Geometry = myStyle.GetGeometry(dataset)

sensor = sensor_Geometry['sensor']
pitch  = sensor_Geometry['pitch']
xlength = float(options.xlength)
debugMode = options.debugMode

colors = myStyle.GetColors(True)

all_histoInfos = []
#     HistoInfo("relFrac_vs_x_channel00",   inputfile, "track", True,  ylength, "", "Track x position [mm]"),
#     HistoInfo("deltaX_vs_Xtrack_oneStrip",   inputfile, "track_oneStrip", True,  ylength, "", "Track x position [mm]"),
# ]

for i in range(7):
    hfrac = inputfile.Get("relFrac_vs_x_channel0%i"%i)
    if hfrac:
        all_histoInfos.append(HistoInfo("relFrac_vs_x_channel0%i"%i,   inputfile, "aFrac_ch0%i"%i, True,  1.0, "", "Track x position [mm]"))


canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

print("Finished setting up langaus fit class")

if debugMode:
    outdir_q = os.path.join(outdir,"q_ampFrac0/")
    if not os.path.exists(outdir_q):
            print(outdir_q)
            os.mkdir(outdir_q)
    else:
        i = 1
        while(os.path.exists(outdir_q)):
                outdir_q = outdir_q[0:-2] + str(i) + outdir_q[-1]
                i+=1
        os.mkdir(outdir_q)

nXBins = all_histoInfos[0].th2.GetXaxis().GetNbins()
#loop over X bins
for i in range(0, nXBins+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for hist in all_histoInfos:
        totalEvents = hist.th2.GetEntries()
        tmpHist = hist.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myMeanError = tmpHist.GetMeanError()
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myMean
        error = myMeanError

        # minEvtsCut = totalEvents/nXBins

        # if i==0: print(hist.inHistoName,": nEvents >",minEvtsCut,"( total events:",totalEvents,")")
        #Do fit 
        if(nEvents > 500):
            if(hist.doFits):
                # tmpHist.Rebin(2)
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMPV = fit.GetParameter(1)
                myMPVError = fit.GetParError(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = myMPV
                error = myMPVError
            
                ##For Debugging
                if (debugMode):
                    tmpHist.Draw("hist")
                    fit.Draw("same")
                    canvas.SaveAs(outdir_q+"q_"+hist.outHistoName+str(i)+".gif")
                    print ("Bin : " + str(i) + " (x = %.3f"%(hist.th1.GetXaxis().GetBinCenter(i)) +") -> Rel Frac: %.3f +/- %.3f"%(value, error))
            # else:
                # value *= 1000.0
                # error *= 1000.0
                ##For Debugging
                # if (debugMode):
                #     tmpHist.Draw("hist")
                #     fit.Draw("same")
                #     canvas.SaveAs(outdir_q+"q_"+info.outHistoName+str(i)+".gif")
                #     print ("Bin : " + str(i) + " (x = %.3f"%(info.th1.GetXaxis().GetBinCenter(i)) +") -> Resolution_rms: %.3f +/- %.3f"%(value, error))
        else:
            value = 0.0
            error = 0.0

        # Removing telescope contribution
        #if value>6.0:
        #    error = error*value/TMath.Sqrt(value*value - 6*6)
        #    value = TMath.Sqrt(value*value - 6*6)
        #else:
        #    value = 0.0 # 20.0 to check if there are strange resolution values
        #    error = 0.0
        #if i<=info.th1.FindBin(-0.2) and sensor=="BNL2020":
        #    value = 0.0
        #    error = 0.0

        hist.th1.SetBinContent(i,value)
        hist.th1.SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile(outdir+"PlotAmpFracVsX.root","RECREATE")

htemp = TH1F("htemp","",1,-xlength,xlength)
htemp.SetStats(0)
htemp.SetMinimum(0.0001)
htemp.SetMaximum(1.3*all_histoInfos[0].yMax)
# htemp.SetLineColor(kBlack)
htemp.GetXaxis().SetTitle(all_histoInfos[0].xlabel)
htemp.GetYaxis().SetTitle(all_histoInfos[0].ylabel)
# info.th1.Draw("hist e")
# info.th1.SetStats(0)
# info.th1.SetMinimum(0.0001)
# info.th1.SetMaximum(info.yMax)
# all_histoInfos[0].th1.SetLineColor(kBlack)
# info.th1.SetTitle(info.title)
# info.th1.GetXaxis().SetTitle(info.xlabel)
# info.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
# info.th1.GetYaxis().SetTitle(info.ylabel)
htemp.Draw("AXIS")

ymin = all_histoInfos[0].th1.GetMinimum()
ymax = all_histoInfos[0].yMax

boxes = getStripBox(inputfile,ymin,ymax,False,18,True,all_histoInfos[0].shift())
for box in boxes:
    box.Draw()

htemp.Draw("same AXIS")

legend = TLegend(2*myStyle.GetMargin()+0.02,1-myStyle.GetMargin()-0.02-0.2,1-myStyle.GetMargin()-0.02,1-myStyle.GetMargin()-0.02)
legend.SetNColumns(3)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize())
legend.SetBorderSize(0)
legend.SetFillColor(kWhite)

for i,info in enumerate(all_histoInfos):
    # gPad.RedrawAxis("g")

    # htemp.Draw("AXIS same")
    # # info.th1.Draw("AXIS same")
    # info.th1.Draw("hist e same")

    # legend = TLegend(myStyle.GetPadCenter()-0.27,1-myStyle.GetMargin()-0.2,myStyle.GetPadCenter()+0.27,1-myStyle.GetMargin()-0.1)
    info.th1.SetMinimum(0.0001)
    info.th1.SetMaximum(info.yMax)
    info.th1.SetLineWidth(2)
    info.th1.SetLineColor(colors[i])
    canvas.SetGrid(0,1)
    info.th1.Draw("hist same")
    legend.AddEntry(info.th1, "Channel %i"%(i))

legend.Draw();
myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs(outdir+"AmpFrac_vs_x.gif")
canvas.SaveAs(outdir+"AmpFrac_vs_x.pdf")

for info in all_histoInfos:
    info.th1.Write()

outputfile.Close()

