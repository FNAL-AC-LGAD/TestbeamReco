from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT,gStyle, TLine, kGray
import os
import optparse
import EfficiencyUtils
from stripBox import getStripBox
import myStyle
import myFunctions as mf

gROOT.SetBatch( True )
colors = myStyle.GetColors(True)

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-x','--xlength', dest='xlength', default = 2.5, help="Limit x-axis in final plot")
parser.add_option('--xHigh', dest='xHigh', default = None, help="Limit x-axis in final plot")
parser.add_option('--xLow',  dest='xLow',  default = None, help="Limit x-axis in final plot")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
parser.add_option('-c', dest='each_channel', action='store_true', default = False, help="Draw efficiency for each channel")
parser.add_option('-Y', '--alongY',dest='centerAlongY', action='store_true', default = False, help="Center plots in Y direction (for pads only)")
parser.add_option('-t', dest='useTight', action='store_true', default = False, help="Use tight cut for pass")
parser.add_option('-n', dest='useNoSum', action='store_true', default = False, help="Use no sum column")
options, args = parser.parse_args()

dataset = options.Dataset
use_center_y = options.centerAlongY
use_each_channel = options.each_channel
is_tight = options.useTight
noSum = options.useNoSum

outdir = myStyle.getOutputDir(dataset)
inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))

outdir = myStyle.GetPlotsDir(outdir, "EfficiencyVsXReco/")

xmin = float(options.xLow) if options.xLow else -float(options.xlength)
xmax = float(options.xHigh) if options.xHigh else float(options.xlength)

# Get position of the central channel in the direction requested
# (x is default and y should be useful for pads only)
direction = "x" if not use_center_y else "y"
position_center = mf.get_central_channel_position(inputfile, direction)

# Get 2D efficiency maps
list_hnames2d = [
    # [hist_input_name, short_output_name]
    ["efficiency_vs_xrecoy_denominator_coarseBins", ""]
]

for cut in ["", "_oneStrip", "_twoStrip"]:
    pair_name = ["efficiency_vs_xrecoy%s_numerator_coarseBins"%cut, "Efficiency_vs_xrecoy%s"%cut]
    list_hnames2d.append(pair_name)

# Use tight cut histograms
if (is_tight):
    print(" >> Using tight cuts!")
    for i, name in enumerate(list_hnames2d):
        list_hnames2d[i][0]+= "_tight"
        list_hnames2d[i][1]+= "-tight"

hname_denominator,_ = list_hnames2d.pop(0)
th2_efficiency_denominator = inputfile.Get(hname_denominator)

# Use NoSum efficiency instead!
if (noSum):
    for cut in ["", "_oneStrip", "_twoStrip"]:
        pair_name_nosum = ["efficiency_vs_xrecoy_NoSum%s_numerator"%cut, "Efficiency_vs_xrecoy_NoSum%s"%cut]
        list_hnames2d.append(pair_name_nosum)


list_th2_efficiency = []
list_th2_efficiency_channel = []
indices = []

for hname, outname in list_hnames2d:
    outpath = "%s%s"%(outdir,outname)
    htitle = outname.replace("_", " ")

    th2_efficiency = inputfile.Get(hname)
    EfficiencyUtils.Plot2DEfficiency(th2_efficiency, th2_efficiency_denominator, outpath, htitle,
                                     "X [mm]", xmin, xmax, "Y [mm]", -20, 20, 0.0, 1.0)
    list_th2_efficiency.append(th2_efficiency)

    # Run over each channel
    if (not use_each_channel) or (noSum):
        continue

    if not indices:
        indices = mf.get_existing_indices(inputfile, "efficiency_vs_xy_numerator_channel")

    for idx in indices:
        hname_ch = "%s_channel%s"%(hname, idx)
        outpath_ch = "%s-Ch%s"%(outpath, idx)
        htitle_ch = "%s - Channel %s"%(htitle, idx)

        th2_efficiency = inputfile.Get(hname_ch)
        if not th2_efficiency:
            continue
        EfficiencyUtils.Plot2DEfficiency(th2_efficiency, th2_efficiency_denominator, outpath_ch, htitle_ch,
                                         "X [mm]", xmin, xmax, "Y [mm]", -20, 20, 0.0, 1.0)
        list_th2_efficiency_channel.append(th2_efficiency)

# Define output file
output_path = "%sEfficiencyVsXreco"%(outdir)
if (noSum):
    output_path+= "_NoSum"
elif (is_tight):
    output_path+= "_tight"
output_path+= ".root"

outputfile = TFile(output_path,"RECREATE")

# Make 1D projection
projX_efficiency_denominator = th2_efficiency_denominator.ProjectionX()

# list_legend_overall = ["One or more strips reconstruction", "Exactly one strip reconstruction", "Two strip reconstruction"]
list_legend_overall = ["Exactly one channel reconstruction", "Two channels reconstruction"]
list_names_overall = ["_oneStrip_numerator", "_twoStrip_numerator"]
sub_colors = [colors[0], colors[2]]
list_th1_overall = [0, 0]
list_test_overall = []

# Overall + per channel
list_th2 = list_th2_efficiency + list_th2_efficiency_channel
for th2 in list_th2:
    hname = th2.GetName()
    new_hname = hname.replace("_xrecoy_", "_xreco_")
    projX_efficiency = th2.ProjectionX(new_hname)
    th1_efficiency = EfficiencyUtils.Make1DEfficiencyHist(projX_efficiency, projX_efficiency_denominator, new_hname, center=position_center)
    th1_efficiency.Write()

    if ("channel" in hname.lower()):
        continue

    for i, name_overall in enumerate(list_names_overall):
        if (name_overall in hname):
            list_th1_overall[i] = th1_efficiency
            list_test_overall.append(th1_efficiency)

# Defining Style
myStyle.ForceStyle()
gStyle.SetOptStat(0)

canvas = TCanvas("cv", "cv", 1000, 800)
htemp = TH1F("htemp","; X Reco position [mm];Efficiency",1, xmin,xmax)
htemp.GetYaxis().SetRangeUser(0.00,1.49)
htemp.Fill(0,-2)

htemp.Draw("AXIS")

boxes = getStripBox(inputfile, ymin=0.0, ymax=1.0, shift=position_center)
for i,box in enumerate(boxes):
    # if (i!=0 and i!=(len(boxes)-1)):
    box.Draw()

# Draw reference line at Efficiency = 1.0
reference_line = TLine(xmin, 1.0, xmax, 1.0)
reference_line.SetLineWidth(2)
reference_line.SetLineStyle(7)
reference_line.SetLineColor(kGray+2)
reference_line.Draw()

# Define legend
pad_center = myStyle.GetPadCenter()
pad_margin = myStyle.GetMargin()
legend = TLegend(pad_center-0.36, 1-pad_margin-0.01-0.23, pad_center+0.36, 1-pad_margin-0.01)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
# legend.SetNColumns(3)

# Draw overall histograms only
for i, th1_overall in enumerate(list_th1_overall):
    th1_overall.SetLineWidth(3)
    th1_overall.SetLineColor(sub_colors[i])
    th1_overall.Draw("hist same")
    legend.AddEntry(th1_overall, list_legend_overall[i])

htemp.Draw("AXIS same")
legend.Draw()

myStyle.BeamInfo()
# myStyle.SensorInfoSmart(dataset)

save_path = "%sEfficiencyAll_vs_xreco"%(outdir)
if (noSum):
    save_path+= "_NoSum"
elif (is_tight):
    save_path+= "_tight"
canvas.SaveAs("%s.gif"%save_path)
canvas.SaveAs("%s.pdf"%save_path)


# Coarse bins projections
# list_name_coarse = []
# for reco in ["denominator", "numerator", "oneStrip_numerator", "twoStrip_numerator"]:
#     hname = "efficiency_vs_xrecoy_%s_coarseBins"%(reco)
#     if (is_tight):
#         hname+= "_tight"
#     list_name_coarse.append(hname)

# hname_denominator = list_name_coarse.pop(0)
# th1_coarse_eff_denominator = inputfile.Get(hname_denominator).ProjectionX()

# legend = TLegend(pad_center-0.36, 1-pad_margin-0.01-0.23, pad_center+0.36, 1-pad_margin-0.01)
# legend.SetTextFont(myStyle.GetFont())
# legend.SetTextSize(myStyle.GetSize()-4)
# # legend.SetNColumns(3)

# canvas.Clear()
# htemp.Draw("AXIS")
# for i,box in enumerate(boxes):
#     # if (i!=0 and i!=(len(boxes)-1)):
#     box.Draw()
# reference_line.Draw()

# list_th1 = []
# for i, in_name in enumerate(list_name_coarse):
#     new_hname = in_name.replace("_xy_", "_x_")
#     projX_efficiency = inputfile.Get(in_name).ProjectionX()
#     th1_efficiency = EfficiencyUtils.Make1DEfficiencyHist(projX_efficiency, th1_coarse_eff_denominator, new_hname, center=position_center)
#     th1_efficiency.SetLineWidth(3)
#     th1_efficiency.SetLineColor(sub_colors[i])
#     th1_efficiency.Draw("hist same")
#     th1_efficiency.Write()

#     list_th1.append(th1_efficiency)
#     legend.AddEntry(th1_efficiency, list_legend_overall[i])

# # # Check adding oneStrip + twoStrip is equivalent to single numerator
# # hSum = list_th1[0].Clone("hsum")
# # hSum.Add(list_th1[1], list_th1[2])
# # hSum.SetLineWidth(3)
# # hSum.SetLineStyle(2)
# # hSum.SetLineColor(colors[3])
# # hSum.Draw("hist same")
# # legend.AddEntry(hSum, "Sum 1 + 2")

# htemp.Draw("AXIS same")
# legend.Draw()

# myStyle.BeamInfo()
# myStyle.SensorInfoSmart(dataset)

# save_path = "%sEfficiencyCoarse"%(outdir)
# if (is_tight):
#     save_path+= "_tight"
# # canvas.SaveAs("%s.gif"%(save_path))
# canvas.SaveAs("%s.pdf"%(save_path))

outputfile.Close()
