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
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-n','--name', dest='hist2plot', default = "AmpOverMaxAmp", help="Histogram to draw w/o _vs_x_channel")
parser.add_option('-c','--cut', dest='histCut', default = "", help="Cut used, can be _NearHit, or none, WITH _")
options, args = parser.parse_args()

histName = options.hist2plot
histCut  = options.histCut

outdir = myStyle.getOutputDir("Paper2022")

colors = myStyle.GetColors(True)
# colors = [ROOT.kRed, ROOT.kRed, ROOT.kGreen, ROOT.kGreen, ROOT.kBlue, ROOT.kBlue, ROOT.kMagenta, ROOT.kMagenta,]

sensor_list = ["EIC_W2_1cm_500up_300uw_240V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W2_1cm_500up_100uw_220V"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)

pitch = 0.500 #mm

# xlim=2.5
# xlim=1.1
xlim=0.75
ymin=0.001
ymax=1.2

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",1000,800)

# Save amplitude histograms
outputfile = TFile(outdir+"RelFracVsX_DiffWidth_"+histName+histCut+".root","RECREATE")

temp_hist = TH1F("htemp","", 1, -xlim, xlim)
temp_hist.GetXaxis().SetTitle("X_{wrtCenter} [mm]")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.GetYaxis().SetTitle("RelAmp in Ch3")
temp_hist.Draw("axis")

boxes = stripBox.getStripBox(list_input[0],ymin,1.0,False,18,True,list_input[0].Get("stripBoxInfo03").GetMean(1))
for b,box in enumerate(boxes):
    if b<5: box.DrawClone("same")

for i,item in enumerate(sensor_list):
    sensor_Geometry = myStyle.GetGeometry(item)
    width = sensor_Geometry['stripWidth']
    for k in range(-1,2,2):
        horizontal_lineL = ROOT.TLine(-width/2000.+0.5*k, ymin, -width/2000.+0.5*k, 1.0)
        horizontal_lineL.SetLineWidth(3)
        horizontal_lineL.SetLineStyle(9)
        horizontal_lineL.SetLineColorAlpha(colors[2*i],0.4)
        horizontal_lineL.DrawClone("same")

        horizontal_lineR = ROOT.TLine(width/2000.+0.5*k, ymin, width/2000.+0.5*k, 1.0)
        horizontal_lineR.SetLineWidth(3)
        horizontal_lineR.SetLineStyle(9)
        horizontal_lineR.SetLineColorAlpha(colors[2*i],0.4)
        horizontal_lineR.DrawClone("same")

temp_hist.Draw("same axis")

# legend = TLegend(2*myStyle.GetMargin()+0.2,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.2,1-myStyle.GetMargin()-0.02)
legend = TLegend(myStyle.GetPadCenter()-0.35,1-myStyle.GetMargin()-0.12,myStyle.GetPadCenter()+0.35,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(3)
legend.SetFillStyle(0)

th1_list = []
for i,item in enumerate(sensor_list):
    th1_relFrac = list_input[i].Get(histName+"_vs_x_channel03"+histCut).ProfileX()
    tmp_relFrac = CopyHist(th1_relFrac, i)

    tmp_relFrac.SetLineColor(colors[2*i])
    th1_list.append(tmp_relFrac)

    tmp_relFrac.Draw("hist same")

    legend.AddEntry(tmp_relFrac, myStyle.GetGeometry(item)["sensor"],"L")
    tmp_relFrac.Write()

legend.Draw();

# myStyle.BeamInfo()

TopLeftText = ROOT.TLatex()
TopLeftText.SetTextSize(myStyle.GetSize()-4)
TopLeftText.SetTextAlign(11)
TopLeftText.DrawLatexNDC(2*myStyle.GetMargin()+0.005,1-myStyle.GetMargin()+0.01,"#bf{"+histName+histCut+"}")

TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Diff Width}")

canvas.SaveAs(outdir+"RelFracVsX_DiffWidth_"+histName+histCut+".gif")
canvas.SaveAs(outdir+"RelFracVsX_DiffWidth_"+histName+histCut+".pdf")
outputfile.Close()

for e in list_input:
    e.Close()
