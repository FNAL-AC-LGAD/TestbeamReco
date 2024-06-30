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
parser.add_option('-F', dest='FullReco', action='store_true', default = False, help="Show Full reco (one or more hit) instead of two")
options, args = parser.parse_args()

dataset = options.Dataset
use_fullreco = options.FullReco

outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "Efficiency/")

denominator_name = "efficiency_vs_xy_fullReco_Denominator"
numerator_name = "efficiency_vs_xy_fullReco_Numerator"
if not use_fullreco: numerator_name = "efficiency_vs_xy_TwoGoodHit_Numerator"
if "HPK_W11_22_3" in dataset:
    denominator_name+= "_thinBins"
    numerator_name+= "_thinBins"

efficiency_denominator_global = inputfile.Get(denominator_name)
efficiency_fullReco_numerator_global = inputfile.Get(numerator_name)

print("Entries : ", efficiency_fullReco_numerator_global.GetEntries())
print("Entries den: ", efficiency_denominator_global.GetEntries())

canvas = TCanvas("cv","cv",1000,800)
myStyle.ForceStyle()
gStyle.SetOptStat(0)

ratio = efficiency_fullReco_numerator_global.Clone("ratio")
ratio.Divide(efficiency_denominator_global)
ratio.SetMaximum(1.0)
ratio.SetMinimum(0.0)

# Define limits of cut and box position
if "2x2pad" in dataset:
    x1, y1 = -0.53, -0.58
    x2, y2 = 0.75, 0.53
elif "BNL" in dataset:
    x1, y1 = -0.50, -0.25
    x2, y2 = 0.50,0.25
else:
    x1, y1 = -0.50, -0.25
    x2, y2 = 0.50,0.25
cutg = TCutG("cutg", 4)
cutg.SetPoint(0, x1, y1)
cutg.SetPoint(1, x1, y2)
cutg.SetPoint(2, x2, y2)
cutg.SetPoint(3, x2, y1)
# Draw box in the limit of the map
x1_box, y1_box = -0.51, -0.25
x2_box, y2_box = 0.51, 0.25
if "2x2pad" in dataset:
    x1_box, y1_box = -9.25, -9.25
    x2_box, y2_box = 9.25, 9.25
elif "Cross" in dataset:
    x1_box, x2_box = -0.50, 0.50
elif "HPK_W11_22_3" in dataset:
    x1_box, x2_box = -0.50, 0.50

BoxHot = TBox(x1_box, y1_box, x2_box, y2_box)
BoxHot.SetLineColor(632)
BoxHot.SetFillStyle(0)
BoxHot.SetLineWidth(3)

x1_user, y1_user = -0.65, -0.32
x2_user, y2_user = 0.65, 0.32
if "2x2pad" in dataset:
    x1_user, y1_user = -0.75, -0.75
    x2_user, y2_user = 0.75, 0.75

ratio.GetZaxis().SetTitleOffset(1.3)
z_title = "One or more" if use_fullreco else "Two"
ratio.GetZaxis().SetTitle(z_title+" good pixel efficiency")
ratio.GetXaxis().SetTitle("Track x position [mm]")
ratio.GetYaxis().SetTitle("Track y position [mm]")
ratio.GetXaxis().SetRangeUser(x1_user, x2_user)
ratio.GetYaxis().SetRangeUser(y1_user, y2_user)
ratio.SetStats(0)
ratio.Draw("colz same [cutg]")
BoxHot.Draw("same")
canvas.SetRightMargin(3.0*myStyle.GetMargin())

myStyle.SensorInfoSmart(dataset,2.0*myStyle.GetMargin(), isPaperPlot = True)
myStyle.BeamInfo()
file_name = "OneOrMore" if use_fullreco else "TwoHits"
canvas.SaveAs("%sEff%s_vs_xy.gif"%(outdir, file_name))
canvas.SaveAs("%sEff%s_vs_xy.pdf"%(outdir, file_name))

outputfile=TFile("%sPlots_Eff%svsXY.root"%(outdir,file_name),"RECREATE")
ratio.Write()
outputfile.Close()
