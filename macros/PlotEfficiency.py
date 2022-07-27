from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
organized_mode=True
colors = myStyle.GetColors()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-o', dest='Overall', action='store_true', default = False, help="Draw Overall efficiency (from Global) in 1DProjection")
options, args = parser.parse_args()

draw_overall = options.Overall
dataset = options.Dataset

outdir=""
if organized_mode: 
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else: 
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "Eff/")

xlength = float(options.xlength)
shift = inputfile.Get("stripBoxInfo03").GetMean(1)

list_thresholds = ["_lowThreshold", "_highThreshold"]
list_recoMethod = ["", "_noNeighb", "_highFrac", "_oneStrip", "_twoStrips"]

list_efficiency_numerator_global = []

####################################
#### Make and Save 2D Histograms
####################################
### Get 2D efficiency numerator Global Histograms
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")
for t in list_thresholds:
    for m in list_recoMethod:
        list_efficiency_numerator_global.append(inputfile.Get("efficiency_vs_xy%s%s_numerator"%(t,m)))
efficiency_fullReco_numerator_global = inputfile.Get("efficiency_vs_xy_fullReco_numerator")

#efficiency_lowThreshold_numerator_global.RebinX(3)
#efficiency_highThreshold_numerator_global.RebinX(3)
#efficiency_denominator_global.RebinX(3)

### Plot and save 2D efficiency Global Histograms
EfficiencyUtils.Plot2DEfficiency(efficiency_fullReco_numerator_global, efficiency_denominator_global, "%sEfficiencyFullReco"%(outdir), "Efficiency Full Reconstruction", "X [mm]", -10, 10, "Y [mm]", -20, 20, 0.0, 1.0)
EfficiencyUtils.Plot2DEfficiency(efficiency_fullReco_numerator_global, efficiency_denominator_global, "%sEfficiencyFullReco"%(outdir), "Efficiency Full Reconstruction", "X [mm]", -10, 10, "Y [mm]", -20, 20, 0.0, 1.0)
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        EfficiencyUtils.Plot2DEfficiency(list_efficiency_numerator_global[e], efficiency_denominator_global, "%sEfficiency%s%s_Global"%(outdir,t,m), "Efficiency%s%s"%(t,m), "X [mm]", -10, 10, "Y [mm]", -20, 20, 0.0, 1.0)
        e+=1


### Plot and save 2D Histograms per channel with fullReco
channel_good_index = []
list_efficiency_vs_xy_fullReco_numerator_ch = []
# th2_efficiency_vs_xy_fullReco_ch = []
for i in range(7):
    if inputfile.Get("efficiency_vs_xy_fullReco_numerator_channel0%i"%(i)):
        channel_good_index.append(i)
        list_efficiency_vs_xy_fullReco_numerator_ch.append(inputfile.Get("efficiency_vs_xy_fullReco_numerator_channel0%i"%(i)))
        EfficiencyUtils.Plot2DEfficiency(list_efficiency_vs_xy_fullReco_numerator_ch[-1], efficiency_denominator_global, "%sEfficiencyFullReco_ch0%i"%(outdir,i), "Efficiency Full Reconstruction Strip %i"%(i+1), "X [mm]", -10, 10, "Y [mm]", -20, 20, 0.0, 1.0)

### Get 2D efficiency Histograms per channel
list_efficiency_vs_xy_numerator_ch = []
# th2_efficiency_vs_xy_ch = []
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            hname = "efficiency_vs_xy%s%s_numerator_channel0%i"%(t,m, i)
            list_efficiency_vs_xy_numerator_ch.append(inputfile.Get(hname))


####################################
#### Make 1D X Projections
####################################
# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

efficiency_denominator_global_vs_x = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator")#,binY_lowEdge,binY_highEdge)

### Make and save 1D projections (vs X) fullReco Global
eff_num_tmp = efficiency_fullReco_numerator_global.ProjectionX("efficiency_vs_x_fullReco_numerator_global")
efficiency_vs_x_project_fullReco_global = EfficiencyUtils.Make1DEfficiency(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x_fullReco", "Efficiency Full Reconstruction", "X [mm]", -xlength, xlength, False, shift)

### Make and save 1D projections (vs X) fullReco per channel
list_efficiency_vs_x_project_fullReco_ch = []
for i,index in enumerate(channel_good_index):
    eff_num_tmp = list_efficiency_vs_xy_fullReco_numerator_ch[i].ProjectionX("efficiency_vs_x_fullReco_numerator_channel0%i"%(i))
    list_efficiency_vs_x_project_fullReco_ch.append( EfficiencyUtils.Make1DEfficiency(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x_fullReco_channel%i"%(i), "Efficiency Full Reconstruction Strip %i"%(i+1), "X [mm]", -xlength, xlength, False, shift) )

### Make and save 1D projections (vs X) Global
list_efficiency_vs_x_project_global = []
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        eff_num_tmp = list_efficiency_numerator_global[e].ProjectionX("efficiency_vs_x%s%s_numerator"%(t,m))
        list_efficiency_vs_x_project_global.append( EfficiencyUtils.Make1DEfficiency(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x%s%s"%(t,m), "Efficiency%s%s"%(t,m), "X [mm]", -xlength, xlength, False, shift) )
        e+=1

### Make and save 1D projections (vs X) per channel
list_efficiency_vs_x_project_ch = []
e = 0
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            eff_num_tmp = list_efficiency_vs_xy_numerator_ch[e].ProjectionX("efficiency_vs_x%s%s_numerator_channel0%i"%(t,m, i))
            list_efficiency_vs_x_project_ch.append( EfficiencyUtils.Make1DEfficiency(eff_num_tmp, efficiency_denominator_global_vs_x, "efficiency_vs_x%s%s_channel0%i"%(t,m,i), "Efficiency%s%s Strip %i"%(t,m,i+1), "X [mm]", -xlength, xlength, False, shift) )
            e+=1

####################################
#### Draw 1D X Projections
####################################
canvas = TCanvas("cv","cv",1000,800)
htemp = TH1F("htemp",";Track x position [mm];Efficiency",1,-xlength,xlength)
htemp.GetYaxis().SetRangeUser(0.0001,1.5)

### Draw 1D projection per channel
e = 0
eG = 0
for t in list_thresholds:
    for m in list_recoMethod:
        htemp.Draw()

        boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
        for box in boxes:
            box.Draw()

        legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
        legend.SetNColumns(3)
        legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);

        for i,ch in enumerate(channel_good_index):
            list_efficiency_vs_x_project_ch[e].Draw("LPsame")
            list_efficiency_vs_x_project_ch[e].SetLineWidth(2)
            list_efficiency_vs_x_project_ch[e].SetLineColor(colors[i])
            legend.AddEntry(list_efficiency_vs_x_project_ch[e], "Strip %i"%(ch+1))

            e+=1
        
        legend.Draw()

        if draw_overall:
            list_efficiency_vs_x_project_global[eG].Draw("LPsame")
            list_efficiency_vs_x_project_global[eG].SetLineWidth(2)
            list_efficiency_vs_x_project_global[eG].SetLineColor(1)
            legend2.AddEntry(list_efficiency_vs_x_project_global[eG], "Overall")
            legend2.Draw()

        # myStyle.BeamInfo()
        myStyle.SensorInfoSmart(dataset)

        htemp.Draw("AXIS same")
        canvas.SaveAs("%sEfficiency%s%s_vs_x"%(outdir,t,m)+".gif")
        canvas.SaveAs("%sEfficiency%s%s_vs_x"%(outdir,t,m)+".pdf")
        canvas.Clear()
        eG+=1


### Draw 1D projection per channel with fullReco

htemp.Draw()

boxes = getStripBox(inputfile,0.0,1.0,False,18,True,shift)
for box in boxes:
    box.Draw()

legend = TLegend(myStyle.GetPadCenter()-0.3,1-myStyle.GetMargin()-0.01-0.16,myStyle.GetPadCenter()+0.3,1-myStyle.GetMargin()-0.01);
legend.SetNColumns(3)
legend2 = TLegend(myStyle.GetPadCenter()-0.2,1-myStyle.GetMargin()-0.01-0.24,myStyle.GetPadCenter()+0.2,1-myStyle.GetMargin()-0.01-0.16);

for i,ch in enumerate(channel_good_index):
    list_efficiency_vs_x_project_fullReco_ch[i].Draw("LPsame")
    list_efficiency_vs_x_project_fullReco_ch[i].SetLineWidth(2)
    list_efficiency_vs_x_project_fullReco_ch[i].SetLineColor(colors[i])
    legend.AddEntry(list_efficiency_vs_x_project_fullReco_ch[i], "Strip %i"%(ch+1))

legend.Draw()

if draw_overall:
    efficiency_vs_x_project_fullReco_global.Draw("LPsame")
    efficiency_vs_x_project_fullReco_global.SetLineWidth(2)
    efficiency_vs_x_project_fullReco_global.SetLineColor(1)
    legend2.AddEntry(efficiency_vs_x_project_fullReco_global, "Overall")
    legend2.Draw()

# myStyle.BeamInfo()
myStyle.SensorInfoSmart(dataset)

htemp.Draw("AXIS same")

canvas.SaveAs("%sEfficiencyFullReco_vs_x"%(outdir)+".gif")
canvas.SaveAs("%sEfficiencyFullReco_vs_x"%(outdir)+".pdf")
canvas.Clear()


# Save efficiency plots
outputfile = TFile("%sEfficiencyPlots.root"%(outdir),"RECREATE")

e=0
for t in list_thresholds:
    for m in list_recoMethod:
        for i in channel_good_index:
            list_efficiency_vs_x_project_ch[e].Write("efficiency_vs_x%s%s_channel0%i"%(t,m,i))
            e+=1

for i in channel_good_index:
    list_efficiency_vs_x_project_fullReco_ch[i].Write("efficiency_vs_x_fullReco_channel%i"%(i))

outputfile.Close()


