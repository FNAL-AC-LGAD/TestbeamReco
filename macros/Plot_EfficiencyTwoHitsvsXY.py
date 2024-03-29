from ROOT import TFile,TCutG,TBox,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle

gROOT.SetBatch(True)
colors = myStyle.GetColors()
myStyle.ForceStyle()
# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset

outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

# outdir = myStyle.getOutputDir("Paper2023")
outdir = myStyle.GetPlotsDir(outdir, "Efficiency/")

efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_fullReco_Denominator")
efficiency_fullReco_numerator_global = inputfile.Get("efficiency_vs_xy_TwoGoodHit_Numerator")
# efficiency_fullReco_numerator_global = inputfile.Get("efficiency_vs_xy_NoSum_twoStrip_numerator")

print("Entries : ", efficiency_fullReco_numerator_global.GetEntries())
print("Entries den: ", efficiency_denominator_global.GetEntries())

canvas = TCanvas("cv","cv",1000,800)
myStyle.ForceStyle()
gStyle.SetOptStat(0)

ratio = efficiency_fullReco_numerator_global.Clone("ratio")
ratio.Divide(efficiency_denominator_global)

#ratio.SetTitle("%sEfficiencyFullReco"%(outdir))
#ratio.SetTitleSize(0.05)
ratio.SetMaximum(1.0)
ratio.SetMinimum(0.0)

outputfile=TFile("%splotsEffvsXY.root"%outdir,"RECREATE")
ratio.Write()
outputfile.Close()


if "2x2pad" in dataset:
    cutg = TCutG("cutg",4)
    BoxHot = TBox(-9.25,-9.25,9.25,9.25)
    cutg.SetPoint(0,-0.53,-0.58)
    cutg.SetPoint(1,-0.53,0.53)
    cutg.SetPoint(2,0.75,0.53)
    cutg.SetPoint(3,0.75,-0.58)
    x_low = ratio.GetXaxis().FindBin(-0.8)
    x_high = ratio.GetXaxis().FindBin(0.8)
    ratio.GetXaxis().SetRange(x_low, x_high)
    y_low = ratio.GetYaxis().FindBin(-0.8)
    y_high = ratio.GetYaxis().FindBin(0.8)
    ratio.GetYaxis().SetRange(y_low, y_high)

elif "BNL" in dataset:
    cutg = TCutG("cutg",4)
    cutg.SetPoint(0,-0.5,-0.25)
    cutg.SetPoint(1,-0.5,0.25)
    cutg.SetPoint(2,0.5,0.25)
    cutg.SetPoint(3,0.5,-0.25)
    BoxHot = TBox(-0.51,-0.25,0.51,0.25)
    x_low = ratio.GetXaxis().FindBin(-0.75)
    x_high = ratio.GetXaxis().FindBin(0.75)
    ratio.GetXaxis().SetRange(x_low, x_high)
    y_low = ratio.GetYaxis().FindBin(-0.5)
    y_high = ratio.GetYaxis().FindBin(0.5)
    ratio.GetYaxis().SetRange(y_low, y_high)

else:
    cutg = TCutG("cutg",4)
    cutg.SetPoint(0,-0.5,-0.25)
    cutg.SetPoint(1,-0.5,0.25)
    cutg.SetPoint(2,0.5,0.25)
    cutg.SetPoint(3,0.5,-0.25)
    BoxHot = TBox(-0.5,-0.25,0.5,0.25)
    x_low = ratio.GetXaxis().FindBin(-0.95)
    x_high = ratio.GetXaxis().FindBin(0.95)
    ratio.GetXaxis().SetRange(x_low, x_high)
    y_low = ratio.GetYaxis().FindBin(-0.65)
    y_high = ratio.GetYaxis().FindBin(0.65)
    ratio.GetYaxis().SetRange(y_low, y_high)

BoxHot.SetLineColor(632)
BoxHot.SetFillStyle(0)
BoxHot.SetLineWidth(3)

ratio.GetZaxis().SetTitle("Two good pixel efficiency")
ratio.GetXaxis().SetTitle("Track x position [mm]")
ratio.GetYaxis().SetTitle("Track y position [mm]")
ratio.SetStats(0)
ratio.Draw("colz same [cutg]")
BoxHot.Draw("same")
# myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin())
canvas.SetRightMargin(3.0*myStyle.GetMargin())
name = "Eff_vs_xy"
myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin(), isPaperPlot = True)
myStyle.BeamInfo()
canvas.SaveAs(outdir+dataset+name+".gif")
canvas.SaveAs(outdir+dataset+name+".pdf")

outputfile=TFile("%splotsEffvsXY.root"%outdir,"RECREATE")
ratio.Write()
outputfile.Close()
