from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraph,TGraphErrors,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox
import array
import EfficiencyUtils
import numpy as np

myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode=True
gROOT.SetBatch( True )
tsize = myStyle.GetSize()

ROOT.gROOT.ForceStyle()

outdir = myStyle.getOutputDir("Paper2022")

colors = myStyle.GetColors(True)
# colors = [ROOT.kRed, ROOT.kRed, ROOT.kGreen, ROOT.kGreen, ROOT.kBlue, ROOT.kBlue, ROOT.kMagenta, ROOT.kMagenta,]

sensor_list = ["EIC_W1_0p5cm_500up_200uw_1_4_245V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W1_2p5cm_500up_200uw_215V"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)

pitch = 0.500 #mm

# xlim=2.5
# xlim=1.1
xmin=0.0
xmax=30.0
ymin=400.0
ymax=850.0

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",1000,800)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 
#canvas.SetLeftMargin(0.12)
# Minimum Function
def getMin(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res
 
# Maximum Function
def getMax(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res

NSensors, NStrips = (3, 4)

stripindexFirst = ["03hot","03cold","03gap","03"]
stripindexSecond = ["01hot","01cold","01gap","01"]
stripindexThird = ["02hot","02cold","02gap","02"]
stripindexTotal = ["03","01","02"]

VarMean = [[0]*NStrips]*NSensors
VarRMS = [[0]*NStrips]*NSensors
VarMeanHot = []
VarRMSHot = []
VarMeanCold = []
VarRMSCold = []
VarMeanGap = []
VarRMSGap = []
VarMeanTotal = []
VarRMSTotal = []

TH1DVar2 = []

for nSensor,item1 in enumerate(sensor_list):

    stripindex = [];
    TH1DVar =  [];
    TH1DVar2.append(list_input[nSensor].Get("baselineRMS%s"%(stripindexTotal[nSensor])))    
    for nstrip,item2 in enumerate(stripindexFirst):

        if (nSensor == 0): stripindex.append(stripindexFirst[nstrip])
        if (nSensor == 1): stripindex.append(stripindexSecond[nstrip])
        if (nSensor == 2): stripindex.append(stripindexThird[nstrip])
        
        TH1DVar.append(list_input[nSensor].Get("slewRateChargeRatio%s"%(stripindex[nstrip])))
        VarMean[nSensor][nstrip] = (1000*TH1DVar2[nSensor].GetMean())/(10*TH1DVar[nstrip].GetMean())
        VarRMS[nSensor][nstrip] = TH1DVar[nstrip].GetRMS()
        
        if(nstrip == 0): 
           VarMeanHot.append(VarMean[nSensor][nstrip]) 
           VarRMSHot.append(VarRMS[nSensor][nstrip])
        if(nstrip == 1): 
           VarMeanCold.append(VarMean[nSensor][nstrip]) 
           VarRMSCold.append(VarRMS[nSensor][nstrip])
        if(nstrip == 2): 
           VarMeanGap.append(VarMean[nSensor][nstrip]) 
           VarRMSGap.append(VarRMS[nSensor][nstrip])
        if(nstrip == 3): 
           VarMeanTotal.append(VarMean[nSensor][nstrip]) 
           VarRMSTotal.append(VarRMS[nSensor][nstrip])


xValue = [5.0,10.0,25.0]
#xValueBand = [4.0,10.0,26.0]
xValueError = [] 
VarValue = []
VarError = []
VarErrorUp = []
VarErrorDown = []
for nSensor,item1 in enumerate(sensor_list):
        
        arr = [VarMeanHot[nSensor], VarMeanCold[nSensor], VarMeanGap[nSensor]]
        min_value = getMin(arr, len(arr))
        max_value = getMax(arr, len(arr))
        VarValue.append((min_value + max_value)*0.5)
        VarError.append(max_value - VarValue[nSensor])
        VarErrorUp.append(max_value - VarMeanTotal[nSensor])
        VarErrorDown.append(VarMeanTotal[nSensor] - min_value)
        xValueError.append(0.0)


hdummy = ROOT.TH1D("","",1,0,30)
hdummy.GetXaxis().SetTitle("Strip length [mm]")
hdummy.GetYaxis().SetTitle("Expected jitter at 10 fC [ps]")
hdummy.SetMaximum(80.0)
hdummy.SetMinimum(0.1)
hdummy.Draw("AXIS")

xValueArr = array.array('f',xValue)
#xValueBandArr = array.array('f',xValueBand)
VarMeanTotalArr = array.array('f',VarMeanTotal)
VarValueArr = array.array('f',VarValue) 
xValueErrorArr = array.array('f',xValueError)
VarErrorArr = array.array('f',VarError)
VarErrorUpArr = array.array('f',VarErrorUp)
VarErrorDownArr = array.array('f',VarErrorDown)

grAsym = TGraphAsymmErrors(NSensors,xValueArr,VarMeanTotalArr,xValueErrorArr,xValueErrorArr,VarErrorDownArr,VarErrorUpArr)
grAsym.SetLineColor(1)
grAsym.SetMarkerColor(1)
grAsym.SetMarkerStyle(20)
grAsym.SetMarkerSize(1.75)

grBand = TGraphErrors(NSensors, xValueArr, VarValueArr, xValueErrorArr, VarErrorArr)
grBand.SetFillColor(1)
grBand.SetFillStyle(3005)

#grBand.SetTitle("")
#grBand.GetXaxis().SetTitle("Strip length [mm]")
#grBand.GetXaxis().SetTitleSize(0.05)
#grBand.GetXaxis().SetTitleOffset(1.0)
#grBand.GetXaxis().SetLabelSize(1)
#grBand.GetXaxis().SetRangeUser(xmin,xmax)
#grBand.GetYaxis().SetTitle("Risetime [ps]")
#grBand.GetYaxis().SetTitleSize(0.05)
#grBand.GetYaxis().SetTitleOffset(1.0)
#grBand.GetYaxis().SetLabelSize(0.04)
#grBand.SetMaximum(ymax)
#grBand.SetMinimum(ymin)

grBand.Draw("3 same")
grAsym.Draw("P same")

legend = TLegend(1-myStyle.GetMargin()-0.65,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.25,1-myStyle.GetMargin()-0.10)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
legend.SetFillStyle(0)
legend.AddEntry(grAsym,"Central value" ,"p")
legend.AddEntry(grBand,"Variation across surface" ,"f")
legend.Draw();


TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying length}")

myStyle.BeamInfo()

canvas.SaveAs(outdir+"ExpectedJitter_DiffLength.gif")
canvas.SaveAs(outdir+"ExpectedJitter_DiffLength.pdf")


for e in list_input:
    e.Close()
