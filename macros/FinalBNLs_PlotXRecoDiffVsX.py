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

class HistoInfo:
    def __init__(self, inHistoName, f, outHistoName, doFits=True, yMax=30.0, title="", xlabel="", ylabel="Position resolution [#mum]", sensor=""):
        self.inHistoName = inHistoName
        self.f = f
        self.outHistoName = outHistoName
        self.doFits = doFits
        self.yMax = yMax
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.th2 = self.getTH2(f, inHistoName, sensor)
        self.th1 = self.getTH1(self.th2, outHistoName, self.shift(), self.fine_tuning(sensor))
        # self.sensor = sensor

    def getTH2(self, f, name, sensor):
        th2 = f.Get(name)
        # th2_temp = TH2D(outHist,"",42,-0.210,0.210,th2.GetYaxis().GetNbins(),th2.GetYaxis().GetXmin(),th2.GetYaxis().GetXmax())
        # for i in range(th2.GetXaxis().FindBin(-0.210+centerShift),th2.GetXaxis().FindBin(0.210+centerShift)+1,1):
        #     th2_temp.Fill()
        if sensor=="BNL2020": th2.RebinX(7)
        elif sensor=="BNL2021": th2.RebinX(10)
        return th2

    def getTH1(self, th2, name, centerShift, fine_value):
        th1_temp = TH1D(name,"",th2.GetXaxis().GetNbins(),th2.GetXaxis().GetXmin()-centerShift-fine_value,th2.GetXaxis().GetXmax()-centerShift-fine_value)
        return th1_temp

    def shift(self):
        return (self.f.Get("stripBoxInfo02").GetMean(1)+self.f.Get("stripBoxInfo03").GetMean(1))/2.

    def fine_tuning(self, sensor):
        value = 0.0
        if sensor=="BNL2020": value = 0.0075
        return value

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-f','--file', dest='file', default = "myoutputfile.root", help="File name (or path from ../test/)")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL, HPK, ...)")
parser.add_option('-b','--biasvolt', dest='biasvolt', default = 220, help="Bias Voltage value in [V]")
parser.add_option('--pitch', dest='pitch', type='float', default = 100, help="Set the pitch for the fit")
options, args = parser.parse_args()

file = options.file
sensor = options.sensor
bias = options.biasvolt

inputfile = TFile("../test/"+file,"READ")

all_histoInfos = [
    HistoInfo("deltaX_vs_Xtrack",   inputfile, "track", True,  200.0, "", "Track x position [mm]","Position resolution [#mum]",sensor),
    #HistoInfo("deltaX_vs_Xreco",    inputfile, "reco",  True,  35.0, "", "Reconstructed x position [mm]","Position resolution [#mum]",sensor),
]

canvas = TCanvas("cv","cv",1000,800)
canvas.SetGrid(0,1)
# gPad.SetTicks(1,1)
TH1.SetDefaultSumw2()
gStyle.SetOptStat(0)

print("Finished setting up langaus fit class")

#loop over X bins
for i in range(0, all_histoInfos[0].th2.GetXaxis().GetNbins()+1):
    ##For Debugging
    #if not (i==46 and j==5):
    #    continue

    for info in all_histoInfos:
        tmpHist = info.th2.ProjectionY("py",i,i)
        myMean = tmpHist.GetMean()
        myRMS = tmpHist.GetRMS()
        myRMSError = tmpHist.GetRMSError()
        nEvents = tmpHist.GetEntries()
        fitlow = myMean - 1.5*myRMS
        fithigh = myMean + 1.5*myRMS
        value = myRMS
        error = myRMSError

        #Do fit 
        if(nEvents > 50):
            if(info.doFits):
                tmpHist.Rebin(2)
                
                fit = TF1('fit','gaus',fitlow,fithigh)
                tmpHist.Fit(fit,"Q", "", fitlow, fithigh)
                myMPV = fit.GetParameter(1)
                mySigma = fit.GetParameter(2)
                mySigmaError = fit.GetParError(2)
                value = 1000.0*mySigma
                error = 1000.0*mySigmaError
            
                ##For Debugging
                #tmpHist.Draw("hist")
                #fit.Draw("same")
                #canvas.SetLogy()
                #canvas.SaveAs("q_"+str(i)+".gif")
                
                #print ("Bin : " + str(i) + " -> " + str(value) + " +/- " + str(error))
            else:
                value *= 1000.0
                error *= 1000.0
        else:
            value = 0.0
            error = 0.0

        # Removing telescope contribution
        if value>6.0:
            error = error*value/TMath.Sqrt(value*value - 6*6)
            value = TMath.Sqrt(value*value - 6*6)
        else:
            value = 0.0 # 20.0 to check if there are strange resolution values
            error = 0.0
        if i<=info.th1.FindBin(-0.2) and sensor=="BNL2020":
            value = 0.0
            error = 0.0

        info.th1.SetBinContent(i,value)
        info.th1.SetBinError(i,error)
                        
# Plot 2D histograms
outputfile = TFile("PlotXRecoDiffVsX.root","RECREATE")
for info in all_histoInfos:
    if sensor=="BNL2020": xlimit = 0.32
    else: xlimit = 4.0
    htemp = TH1F("htemp","",1,-xlimit,xlimit)
    htemp.SetStats(0)
    htemp.SetMinimum(0.0001)
    htemp.SetMaximum(info.yMax)
    # htemp.SetLineColor(kBlack)
    htemp.GetXaxis().SetTitle(info.xlabel)
    htemp.GetYaxis().SetTitle(info.ylabel)
    # info.th1.Draw("hist e")
    # info.th1.SetStats(0)
    # info.th1.SetMinimum(0.0001)
    # info.th1.SetMaximum(info.yMax)
    info.th1.SetLineColor(kBlack)
    # info.th1.SetTitle(info.title)
    # info.th1.GetXaxis().SetTitle(info.xlabel)
    # info.th1.GetXaxis().SetRangeUser(-0.32, 0.32)
    # info.th1.GetYaxis().SetTitle(info.ylabel)
    htemp.Draw("AXIS")

    ymin = info.th1.GetMinimum()
    ymax = info.yMax

    boxes = getStripBox(inputfile,ymin,ymax,False,18,True,info.shift())
    for box in boxes:
        box.Draw()

    # boxes2 = getStripBox(inputfile,ymin,ymax,True,ROOT.kRed,True,info.shift())
    # for box in boxes2:
    #     box.Draw("same")

    default_res = ROOT.TLine(-xlimit,options.pitch/TMath.Sqrt(12),xlimit,options.pitch/TMath.Sqrt(12))
    default_res.SetLineWidth(4)
    default_res.SetLineStyle(9)
    default_res.SetLineColor(416+2) #kGreen+2 #(TColor.GetColor(136,34,85))
    default_res.Draw("same")

    gPad.RedrawAxis("g")

    htemp.Draw("AXIS same")
    # info.th1.Draw("AXIS same")
    info.th1.Draw("hist e same")

    legend = TLegend(myStyle.GetPadCenter()-0.27,1-myStyle.GetMargin()-0.2,myStyle.GetPadCenter()+0.27,1-myStyle.GetMargin()-0.1)
    # legend.SetBorderSize(0)
    # legend.SetFillColor(kWhite)
    # legend.SetTextFont(myStyle.GetFont())
    # legend.SetTextSize(myStyle.GetSize())
    #legend.SetFillStyle(0)
    legend.AddEntry(default_res, "Binary readout","l")
    legend.AddEntry(info.th1, "Two-strip reconstruction")
    legend.Draw();

    myStyle.BeamInfo()
    myStyle.SensorInfo(sensor, bias)

    canvas.SaveAs("PositionRes_vs_x_"+info.outHistoName+".gif")
    canvas.SaveAs("PositionRes_vs_x_"+info.outHistoName+".pdf")
    info.th1.Write()
    htemp.Delete()

outputfile.Close()

