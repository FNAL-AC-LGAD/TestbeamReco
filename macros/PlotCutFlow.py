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
    bin_two = hist.GetXaxis().FindBin("TwoStripsReco")

    value_pass = hist.GetBinContent(bin_pass)
    value_one = hist.GetBinContent(bin_one)
    value_two = hist.GetBinContent(bin_two)

    # Get right limit to draw text
    r_limit = hist.GetXaxis().GetNbins()

    str_oneStrip = "One strip: %3.2f"%(100*value_one/value_pass)
    txt_oneStrip = TLatex(r_limit-0.02, 1.05, str_oneStrip)
    txt_oneStrip.SetTextAlign(33)
    txt_oneStrip.SetTextSize(myStyle.GetSize()-4)
    txt_oneStrip.Draw()

    str_twoStrip = "Two strip: %3.2f"%(100*value_two/value_pass)
    txt_twoStrip = TLatex(r_limit-0.02, 0.90, str_twoStrip)
    txt_twoStrip.SetTextAlign(33)
    txt_twoStrip.SetTextSize(myStyle.GetSize()-4)
    txt_twoStrip.Draw()

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

    b1 = hist.GetXaxis().FindBin("Signal over Noise")
    b2 = hist.GetXaxis().FindBin("hi")
    b3 = hist.GetXaxis().FindBin(evt_name)
    print("Value b1", b1)
    print("Value b2", b2)
    print("Value b3", b3) # WIP

    # Draw one and two strip reco efficiency in this region
    if (hist.GetXaxis().FindBin(evt_name)<nbins):
        draw_reco_method_percentage(hist, evt_name)

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
list_cuts_oneStrip  = ["Pass", "Signal over Noise", "OneStripReco",
                       "High fraction", "High fraction & Good neighbour",
                       "No good neighbour", "High fraction & No neighbour",
                       "OneStripReco & OnMetal"]
list_cuts_twoStrips = ["Pass", "Signal over highThreshold", "Good neighbour",
                       "Good Amp fraction", "TwoStripsReco",
                       "TwoStripsReco & OnMetal"]
list_cuts_Metal = ["Pass", "No edge strip", "Metal",
                   "OneStripReco", "TwoStripsReco"]
list_cuts_Gap = ["Pass", "No edge strip", "Gap",
                 "OneStripReco", "TwoStripsReco"]
list_cuts_MidGap = ["Pass", "No edge strip", "MidGap",
                    "OneStripReco", "TwoStripsReco"]

# Retrieve event graphs
event_oneStripReco  = inputfile.Get("event_oneStripReco")
event_twoStripsReco = inputfile.Get("event_twoStripsReco")
event_Metal = inputfile.Get("event_Metal")
event_Gap = inputfile.Get("event_Gap")
event_MidGap = inputfile.Get("event_MidGap")

# Create histograms
h_oneStrip = draw_cut_flow("oneStrip", event_oneStripReco, list_cuts_oneStrip)
h_twoStrips = draw_cut_flow("twoStrips", event_twoStripsReco, list_cuts_twoStrips)
h_Metal = draw_cut_flow("Metal", event_Metal, list_cuts_Metal)
h_Gap = draw_cut_flow("Gap", event_Gap, list_cuts_Gap)
h_MidGap = draw_cut_flow("MidGap", event_MidGap, list_cuts_MidGap)

# Save amplitude histograms
outputfile = TFile("%sPlot_cutflow.root"%(outdir),"RECREATE")

h_oneStrip.Write()
h_twoStrips.Write()
h_Metal.Write()
h_Gap.Write()
h_MidGap.Write()

outputfile.Close()
