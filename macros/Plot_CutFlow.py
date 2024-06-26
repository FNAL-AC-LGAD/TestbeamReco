from ROOT import TFile,TTree,TCanvas,TH1D,TH2F,TLatex,TMath,TEfficiency,\
    TGraphAsymmErrors,TLegend,gROOT,gStyle, kWhite
import os
import EfficiencyUtils
import langaus
import optparse
import time
from stripBox import getStripBox
import myStyle

gROOT.SetBatch( True )
gStyle.SetOptFit(1011)

## Defining Style
myStyle.ForceStyle()
gStyle.SetPadBottomMargin(4*myStyle.GetMargin())
# gStyle.SetPadRightMargin(2*myStyle.GetMargin())
gStyle.SetLabelSize(myStyle.GetSize()-12,"x")
gROOT.ForceStyle()
# gStyle.SetTitleYOffset(1.1)
organized_mode=True

def draw_reco_method_percentage(hist, denominator_bin_name):
    # Get values
    bin_pass = hist.GetXaxis().FindBin(denominator_bin_name)
    bin_one = hist.GetXaxis().FindBin("OneStripReco")
    bin_two = hist.GetXaxis().FindBin("TwoStripReco")

    value_pass = hist.GetBinContent(bin_pass)
    value_one = hist.GetBinContent(bin_one)
    value_two = hist.GetBinContent(bin_two)

    # Get right limit to draw text
    r_limit = bin_two

    if not value_pass:
        str_recoinfo = "Empty denominator"
    else:
        percent_one = 100*value_one/value_pass
        percent_two = 100*value_two/value_pass
        str_recoinfo = "One strip: %3.1f%%   "%(percent_one)
        str_recoinfo+= "Two strip: %3.1f%%"%(percent_two)
    txt_recoinfo = TLatex()
    txt_recoinfo.SetTextAlign(33)
    txt_recoinfo.SetTextSize(myStyle.GetSize()-4)
    txt_recoinfo.DrawLatex(r_limit-0.4, 1.05, str_recoinfo)

    print("\n%s efficiency --> %s"%(denominator_bin_name, str_recoinfo))

# Define function to extract numbers from graph and draw plots
def draw_cut_flow(evt_name, evt_graph, list_cuts):
    canvas = TCanvas("cv","cv",1000,800)
    canvas.SetGrid(0,1)
    # gPad.SetTicks(1,1)
    gStyle.SetOptStat(0)

    # Create 1D histogram
    hname = "cut_flow_%s"%evt_name
    htitle = "Cut flow %s;;Events normalized"%evt_name
    nbins = len(list_cuts)
    hist = TH1D(hname, htitle, nbins, 0, nbins)
    hist.GetYaxis().SetRangeUser(0.0, 1.1)
    l_txt_percentage = []

    # Extract efficiency values from evt_graph and normalize wrt first bin
    draw_percent = False
    for c,cut in enumerate(list_cuts):
        efficiency_value = evt_graph.GetEfficiency(c+1)/evt_graph.GetEfficiency(1)
        hist.Fill(cut, efficiency_value)
        hist.SetBinError(c+1, 0)

        # Save percentage to be explicitly written later
        if draw_percent:
            str_percentage = "%3.2f%%"%(efficiency_value*100)
            txt_percentage = TLatex(c+0.5, efficiency_value+0.01, str_percentage)
            txt_percentage.SetTextAlign(21)
            txt_percentage.SetTextSize(myStyle.GetSize()-4)
            l_txt_percentage.append(txt_percentage)
        draw_percent = True

    hist.LabelsOption("u")
    hist.Draw()

    # Define and draw top left label
    top_left_text = TLatex()
    top_left_text.SetTextSize(myStyle.GetSize()-4)
    lpos = 2*myStyle.GetMargin()+0.005
    bpos = 1-myStyle.GetMargin()+0.01
    top_left_text.DrawLatexNDC(lpos, bpos, "#bf{%s}"%evt_name)

    for perc in l_txt_percentage:
    	perc.Draw()

    # Loop over the bin labels
    label_exists = False
    for bin in range(1, nbins + 1):
        bin_label = hist.GetXaxis().GetBinLabel(bin)
        denominator_bin_name = ""
        if "tight" in evt_name:	
            denominator_bin_name = "Pass_tight"
        else:
            denominator_bin_name = "Pass"
	    
        if bin_label == denominator_bin_name:
            label_exists = True
            break


    # Draw one and two strip reco efficiency in this region
    if (label_exists):
        draw_reco_method_percentage(hist, denominator_bin_name)

    # myStyle.BeamInfo()
    myStyle.SensorInfoSmart(dataset)

    canvas.SaveAs("%sPlot_cutflow_%s.gif"%(outdir, evt_name))
    canvas.SaveAs("%sPlot_cutflow_%s.pdf"%(outdir, evt_name))

    canvas.Clear()

    return hist


# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-D', dest='Dataset', default = "", help="Dataset, which determines filepath")
options, args = parser.parse_args()

dataset = options.Dataset
outdir=""
if organized_mode:
    outdir = myStyle.getOutputDir(dataset)
    inputfile = TFile("%s%s_Analyze.root"%(outdir,dataset))
else:
    inputfile = TFile("../test/myoutputfile.root")

outdir = myStyle.GetPlotsDir(outdir, "Cutflow/")
colors = myStyle.GetColors(True)

sensor_Geometry = myStyle.GetGeometry(dataset)
sensor = sensor_Geometry['sensor']

# Add name of cut implemented in each bin of the cut flow
list_cuts_oneStrip = ["Pass", "Signal over Noise", "OneStripReco",
                      "High fraction", "High fraction & Good neighbour",
                      "No good neighbour", "High fraction & No neighbour",
                      "OneStripReco & OnMetal"]
list_cuts_twoStrip = ["Pass", "Signal over highThreshold", "Good neighbour",
                      "Good Amp fraction", "TwoStripReco",
                      "TwoStripReco & OnMetal"]
list_cuts_Overall = ["Pass", "No edge strip", "Overall",
                   "OneStripReco", "TwoStripReco"]
list_cuts_Overall_tight = ["Pass_tight", "No edge strip", "Overall",
                   "OneStripReco", "TwoStripReco"]
list_cuts_Metal = ["Pass", "No edge strip", "Over noise", "Metal",
                   "OneStripReco", "TwoStripReco"]
list_cuts_Gap = ["Pass", "No edge strip", "Over noise", "Gap",
                 "OneStripReco", "TwoStripReco"]
list_cuts_MidGap = ["Pass", "No edge strip", "Over noise", "MidGap",
                    "OneStripReco", "TwoStripReco"]

# Retrieve event graphs
event_oneStripReco = inputfile.Get("event_oneStripReco")
event_twoStripReco = inputfile.Get("event_twoStripReco")
event_Overall = inputfile.Get("event_Overall")
event_Overall_tight = inputfile.Get("event_Overall_tight")
event_Metal = inputfile.Get("event_Metal")
event_Gap = inputfile.Get("event_Gap")
event_MidGap = inputfile.Get("event_MidGap")

# Create histograms
h_oneStrip = draw_cut_flow("oneStrip", event_oneStripReco, list_cuts_oneStrip)
h_twoStrip = draw_cut_flow("twoStrip", event_twoStripReco, list_cuts_twoStrip)
h_Overall = draw_cut_flow("Overall", event_Overall, list_cuts_Overall)
h_Overall_tight = draw_cut_flow("Overall_tight", event_Overall_tight, list_cuts_Overall_tight)
h_Metal = draw_cut_flow("Metal", event_Metal, list_cuts_Metal)
h_Gap = draw_cut_flow("Gap", event_Gap, list_cuts_Gap)
h_MidGap = draw_cut_flow("MidGap", event_MidGap, list_cuts_MidGap)

# Save amplitude histograms
outputfile = TFile("%sPlot_cutflow.root"%(outdir),"RECREATE")

h_oneStrip.Write()
h_twoStrip.Write()
h_Overall.Write()
h_Overall_tight.Write()
h_Metal.Write()
h_Gap.Write()
h_MidGap.Write()

outputfile.Close()
