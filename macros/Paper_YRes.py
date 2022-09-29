from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,TF1,gStyle,gROOT
import ROOT
import os
import optparse
import myStyle
import stripBox

myStyle.ForceStyle()
gStyle.SetOptStat(0)
organized_mode=True
gROOT.SetBatch( True )
tsize = myStyle.GetSize()

ROOT.gROOT.ForceStyle()

def CopyHist(hist, number):
    nbins = hist.GetNbinsX()

    min_bin = hist.FindBin(-0.665)
    max_bin = hist.FindBin( 0.665)

    hist_tmp = TH1F("relFracCh3_corr_"+str(number), hist.GetTitle(), nbins, hist.GetBinLowEdge(1), hist.GetBinLowEdge(nbins+1))
    for i in range(1,nbins+1):
        if  ((i < min_bin) or (max_bin <= i)):
            hist_tmp.SetBinContent(i, -1.0)
        else:
            hist_tmp.SetBinContent(i, hist.GetBinContent(i))
    return hist_tmp

# Construct the argument parser
# parser = optparse.OptionParser("usage: %prog [options]\n")
# parser.add_option('-n','--name', dest='hist2plot', default = "AmpOverMaxAmp", help="Histogram to draw w/o _vs_x_channel")
# parser.add_option('-c','--cut', dest='histCut', default = "", help="Cut used, can be _NearHit, or none, WITH _")
# options, args = parser.parse_args()

# histName = options.hist2plot
# histCut  = options.histCut

outdir = myStyle.getOutputDir("Paper2022")

colors = myStyle.GetColors(True)
# colors = [ROOT.kRed, ROOT.kRed, ROOT.kGreen, ROOT.kGreen, ROOT.kBlue, ROOT.kBlue, ROOT.kMagenta, ROOT.kMagenta,]

sensor_list = ["EIC_W2_1cm_500up_300uw_240V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W2_1cm_500up_100uw_220V"]
list_input = []
for name in sensor_list:
    indir = myStyle.getOutputDir(name)
    indir = myStyle.GetPlotsDir(indir, "PositionResY/")
    infile = TFile(indir+"PlotRecoDiffVsY.root","READ")
    list_input.append(infile)

pitch = 0.500 #mm

# xlim=2.5
# xlim=1.1
xlim = 5.00
ymin = 0.00
ymax = 4.00

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",1000,800)

# Save amplitude histograms
# outputfile = TFile(outdir+"RelFracVsX_DiffWidth.root","RECREATE")

temp_hist = TH1F("htemp","", 1, -xlim, xlim)
temp_hist.GetXaxis().SetTitle("Track y position [mm]")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.GetYaxis().SetTitle("Position resolution [mm]")
temp_hist.Draw("axis")


legend = TLegend(myStyle.GetPadCenter()-0.27,1-myStyle.GetMargin()-0.24,myStyle.GetPadCenter()+0.27,1-myStyle.GetMargin()-0.02)

legend.SetBorderSize(0)
# legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-4)
#legend.SetFillStyle(0)
legend.SetNColumns(2)
legend.SetFillStyle(0)


default_res = ROOT.TLine(-xlim,10/TMath.Sqrt(12),xlim,10/TMath.Sqrt(12))
default_res.SetLineWidth(3)
default_res.SetLineStyle(7)
default_res.SetLineColor(colors[1])
default_res.Draw("same")

ROOT.gPad.RedrawAxis("g")

legend.AddEntry(default_res, "Length / #sqrt{12}","l")
# legend.AddEntry(info.th1, "Two strip reconstruction","l")

th1_list = []
for i,item in enumerate(sensor_list):
    # th1_YRes = list_input[i].Get("track").Clone(item) # Use original limits
    th1_YRes = list_input[i].Get("track_1cm").Clone(item) # Use paper limits (all three sensors with the same value)
    th1_YRes.SetLineColor(colors[2*i])
    th1_YRes.SetLineWidth(3)
    th1_list.append(th1_YRes)

    th1_YRes.Draw("hist e same")

    legend.AddEntry(th1_YRes, myStyle.GetGeometry(item)["sensor"],"L")
    # th1_YRes.Write()

legend.Draw();

myStyle.BeamInfo()

# TopLeftText = ROOT.TLatex()
# TopLeftText.SetTextSize(myStyle.GetSize()-4)
# TopLeftText.SetTextAlign(11)
# TopLeftText.DrawLatexNDC(2*myStyle.GetMargin()+0.005,1-myStyle.GetMargin()+0.01,"#bf{"+histName+"}")

TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying width}")

canvas.SaveAs(outdir+"ResolutionY_DiffWidth.gif")
canvas.SaveAs(outdir+"ResolutionY_DiffWidth.pdf")
# outputfile.Close()

for e in list_input:
    e.Close()
