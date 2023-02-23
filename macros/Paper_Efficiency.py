from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
organized_mode=True
colors = myStyle.GetColors(True)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('--xHigh', dest='xHigh', default = None, help="Limit x-axis in final plot")
parser.add_option('--xLow',  dest='xLow',  default = None, help="Limit x-axis in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-o', dest='Overall', action='store_true', default = False, help="Draw Overall efficiency (from Global) in 1DProjection")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
options, args = parser.parse_args()

dataset = options.Dataset
draw_overall = options.Overall
useTight = options.useTight

outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "Paper_Eff/")

xHigh = float(options.xHigh) if options.xHigh else  float(options.xlength)
xLow  = float(options.xLow)  if options.xLow  else -float(options.xlength)
shift = 0.0
if inputfile.Get("stripBoxInfo03"):
    shift = inputfile.Get("stripBoxInfo03").GetMean(1)
if not inputfile.Get("stripBoxInfo06") and inputfile.Get("stripBoxInfo02"):
    shift = (inputfile.Get("stripBoxInfo02").GetMean(1) + shift)/2.

# list_thresholds = ["_lowThreshold", "_highThreshold"]
tight_ext = "_tight" if useTight else ""
list_thresholds = [""]
list_recoMethod = ["", "_noNeighb", "_highFrac", "_oneStrip", "_twoStrips"]

list_efficiency_numerator_global = []

####################################
#### Make and Save 2D Histograms
####################################
### Get 2D efficiency numerator Global Histograms
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator%s"%(tight_ext))
for t in list_thresholds:
    for m in list_recoMethod:
        list_efficiency_numerator_global.append(inputfile.Get("efficiency_vs_xy%s%s_numerator%s"%(t,m,tight_ext)))
efficiency_fullReco_numerator_global = inputfile.Get("efficiency_vs_xy_fullReco_numerator%s"%(tight_ext))

### Plot and save 2D efficiency Global Histograms
EfficiencyUtils.Plot2DEfficiency(efficiency_fullReco_numerator_global, efficiency_denominator_global, "%sEfficiencyFullReco%s"%(outdir,tight_ext), "Efficiency Full Reconstruction", "X [mm]", xLow, xHigh, "Y [mm]", -20, 20, 0.0, 1.0, True)
EfficiencyUtils.Plot2DEfficiency(efficiency_fullReco_numerator_global, efficiency_denominator_global, "%sEfficiencyFullReco%s"%(outdir,tight_ext), "Efficiency Full Reconstruction", "X [mm]", xLow, xHigh, "Y [mm]", -20, 20, 0.0, 1.0, True)
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        EfficiencyUtils.Plot2DEfficiency(list_efficiency_numerator_global[e], efficiency_denominator_global, "%sEfficiency%s%s_Global%s"%(outdir,t,m,tight_ext), "Efficiency%s%s"%(t,m), "X [mm]", xLow, xHigh, "Y [mm]", -20, 20, 0.0, 1.0)
        e+=1


### Plot and save 2D Histograms per channel with fullReco
channel_good_index = []
list_efficiency_vs_xy_fullReco_numerator_ch = []
# th2_efficiency_vs_xy_fullReco_ch = []
for i in range(7):
    for j in range(7):
        if inputfile.Get("efficiency_vs_xy_fullReco_numerator%s_channel%i%i"%(tight_ext,i,j)):
            channel_good_index.append("%i%i"%(i,j))
            list_efficiency_vs_xy_fullReco_numerator_ch.append(inputfile.Get("efficiency_vs_xy_fullReco_numerator%s_channel%i%i"%(tight_ext,i,j)))
            EfficiencyUtils.Plot2DEfficiency(list_efficiency_vs_xy_fullReco_numerator_ch[-1], efficiency_denominator_global, "%sEfficiencyFullReco%s_ch%i%i"%(outdir,tight_ext,i,j), "Efficiency Full Reconstruction Strip %i%i"%(i+1,j), "X [mm]", xLow, xHigh, "Y [mm]", -20, 20, 0.0, 1.0)

### Get 2D efficiency Histograms per channel
list_efficiency_vs_xy_numerator_ch = []
# th2_efficiency_vs_xy_ch = []
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            hname = "efficiency_vs_xy%s%s_numerator%s_channel%s"%(t,m, tight_ext,i)
            list_efficiency_vs_xy_numerator_ch.append(inputfile.Get(hname))


####################################
#### Make 1D X Projections
####################################
# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

efficiency_denominator_global_vs_x = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator")#,binY_lowEdge,binY_highEdge)

fine_tune = efficiency_denominator_global_vs_x.GetBinWidth(2)/2.

### Make and save 1D projections (vs X) fullReco Global
eff_num_tmp = efficiency_fullReco_numerator_global.ProjectionX("efficiency_vs_x_fullReco_numerator_global")
efficiency_vs_x_project_fullReco_global = EfficiencyUtils.Make1DEfficiencyHist(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x_fullReco", "Efficiency Full Reconstruction", "X [mm]", xLow, xHigh, shift, fine_tune)

### Make and save 1D projections (vs X) fullReco per channel
list_efficiency_vs_x_project_fullReco_ch = []
for i,index in enumerate(channel_good_index):
    eff_num_tmp = list_efficiency_vs_xy_fullReco_numerator_ch[i].ProjectionX("efficiency_vs_x_fullReco_numerator_channel%s"%(i))
    list_efficiency_vs_x_project_fullReco_ch.append( EfficiencyUtils.Make1DEfficiencyHist(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x_fullReco_channel%i"%(i), "Efficiency Full Reconstruction Strip %i"%(i+1), "X [mm]", xLow, xHigh, shift, fine_tune) )

### Make and save 1D projections (vs X) Global
list_efficiency_vs_x_project_global = []
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        eff_num_tmp = list_efficiency_numerator_global[e].ProjectionX("efficiency_vs_x%s%s_numerator"%(t,m))
        list_efficiency_vs_x_project_global.append( EfficiencyUtils.Make1DEfficiencyHist(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x%s%s"%(t,m), "Efficiency%s%s"%(t,m), "X [mm]", xLow, xHigh, shift, fine_tune) )
        e+=1

### Make and save 1D projections (vs X) per channel
list_efficiency_vs_x_project_ch = []
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            eff_num_tmp = list_efficiency_vs_xy_numerator_ch[e].ProjectionX("efficiency_vs_x%s%s_numerator_channel%s"%(t,m, i))
            list_efficiency_vs_x_project_ch.append( EfficiencyUtils.Make1DEfficiencyHist(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x%s%s_channel%s"%(t,m,i), "Efficiency%s%s Strip %s"%(t,m,i), "X [mm]", xLow, xHigh, shift, fine_tune) )
            e+=1


# Save efficiency plots
outputfile = TFile("%sEfficiencyPlots.root"%(outdir),"RECREATE")

####################################
#### Draw only global x projections all together
####################################
canvas = TCanvas("cv","cv",1000,800)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1, xLow,xHigh)
htemp.GetYaxis().SetRangeUser(0.00,1.49)
htemp.Fill(0,-2)

htemp.Draw()

boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for i,box in enumerate(boxes):
    if (i!=0 and i!=(len(boxes)-1)): box.Draw()

legend = TLegend(myStyle.GetPadCenter()-0.36,1-myStyle.GetMargin()-0.01-0.23,myStyle.GetPadCenter()+0.36,1-myStyle.GetMargin()-0.01);
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetNColumns(3)

index_RecoOne = list_recoMethod.index("_oneStrip")
index_RecoTwo = list_recoMethod.index("_twoStrips")

list_efficiency_vs_x_project_global[index_RecoOne].Write("Full_OneStripReco")
list_efficiency_vs_x_project_global[index_RecoTwo].Write("Full_TwoStripReco")

# Draw OneStripReco Global
hist_Global_OneStrip = list_efficiency_vs_x_project_global[index_RecoOne]
hist_Global_OneStrip.Draw("hist same")
hist_Global_OneStrip.SetLineWidth(3)
hist_Global_OneStrip.SetLineColor(colors[0])

# Draw TwoStripsReco Global
hist_Global_TwoStrips = list_efficiency_vs_x_project_global[index_RecoTwo]
hist_Global_TwoStrips.Draw("hist same")
hist_Global_TwoStrips.SetLineWidth(3)
hist_Global_TwoStrips.SetLineColor(colors[2])

# Draw FullReco Global
hist_Global_FullReco = efficiency_vs_x_project_fullReco_global
hist_Global_FullReco.Draw("hist same")
hist_Global_FullReco.SetLineWidth(3)
hist_Global_FullReco.SetLineColor(colors[4])

legend.AddEntry(hist_Global_FullReco, "One or more strips reconstruction")
legend.AddEntry(hist_Global_OneStrip, "Exactly one strip reconstruction")
legend.AddEntry(hist_Global_TwoStrips, "Two strip reconstruction")
legend.Draw()
htemp.Draw("AXIS same")

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

canvas.SaveAs("%sEfficiencyAll_vs_x%s"%(outdir, tight_ext)+".gif")
canvas.SaveAs("%sEfficiencyAll_vs_x%s"%(outdir, tight_ext)+".pdf")

list_hist_coarse_bin = ["efficiency_vs_xy_numerator_coarseBins%s"%tight_ext, "efficiency_vs_xy_oneStrip_numerator_coarseBins%s"%tight_ext, "efficiency_vs_xy_twoStrips_numerator_coarseBins%s"%tight_ext]
list_name_coarse_bin = ["efficiency_vs_x_coarseBins", "efficiency_vs_x_oneStrip_coarseBins", "efficiency_vs_x_twoStrip_coarseBins"]
list_good_hists = []

this_denom = inputfile.Get("efficiency_vs_xy_denominator_coarseBins").ProjectionX()
for n,name in enumerate(list_hist_coarse_bin):
    this_hist = inputfile.Get(name).ProjectionX()
    good_hist = EfficiencyUtils.Make1DEfficiencyHist(this_hist, this_denom, list_name_coarse_bin[n], list_name_coarse_bin[n], "X [mm]", xLow, xHigh, 0.0, 0.0)
    list_good_hists.append(good_hist)

for h,hist in enumerate(list_good_hists):
    hist.Write(list_name_coarse_bin[h])

e=0
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            list_efficiency_vs_x_project_ch[e].Write("efficiency_vs_x%s%s_channel%s"%(t,m,i))
            e+=1

for i in range(len(channel_good_index)):
    list_efficiency_vs_x_project_fullReco_ch[i].Write("efficiency_vs_x_fullReco_channel%s"%(channel_good_index[i]))

outputfile.Close()


