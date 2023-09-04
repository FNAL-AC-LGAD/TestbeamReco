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

    min_bin = hist.FindBin(-0.615)
    max_bin = hist.FindBin( 0.615)

    hist_tmp = TH1F("relFracCh3_corr_"+str(number), hist.GetTitle(), nbins, hist.GetBinLowEdge(1), hist.GetBinLowEdge(nbins+1))
    for i in range(1,nbins+1):
        if  ((i < min_bin) or (max_bin <= i)):
            hist_tmp.SetBinContent(i, -1.0)
        else:
            hist_tmp.SetBinContent(i, hist.GetBinContent(i))
    return hist_tmp

outdir = myStyle.getOutputDir("Paper2022")

colors = myStyle.GetColors(True)

sensor_list = ["EIC_W1_1cm_500up_200uw_255V"]
ROI_list = ["", "hot_ySlice", "cold_ySlice"]
ROI_legend = ["All sensor", "Hot spot", "Cold spot"]
list_input = []
for name in sensor_list:
    file = TFile("../output/%s/%s_Analyze.root"%(name,name),"READ")
    list_input.append(file)

pitch = 0.500 #mm

xlim=0.75
ymin=0.00
ymax=1.19

# gStyle.SetOptFit(0)
# gROOT.ForceStyle()
canvas = TCanvas("cv","cv",1000,800)

# Save amplitude histograms
outputfile = TFile(outdir+"RelFracVsX_DiffROI.root","RECREATE")

temp_hist = TH1F("htemp","", 1, -xlim, xlim)
temp_hist.GetXaxis().SetTitle("Track x position [mm]")
temp_hist.GetYaxis().SetRangeUser(ymin, ymax)
temp_hist.GetYaxis().SetTitle("Amp. middle / Amp. max")
temp_hist.Draw("axis")

boxes = stripBox.getStripBox(list_input[0],ymin,1.0,False,18,True,list_input[0].Get("stripBoxInfo03").GetMean(1))
for b,box in enumerate(boxes):
    if b<5: box.DrawClone("same")

temp_hist.Draw("same axis")

legend = TLegend(myStyle.GetPadCenter()-0.35,1-myStyle.GetMargin()-0.12,myStyle.GetPadCenter()+0.35,1-myStyle.GetMargin()-0.02)
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(myStyle.GetFont())
legend.SetTextSize(myStyle.GetSize()-8)
legend.SetNColumns(3)
legend.SetFillStyle(0)

th1_list = []
for i,ROI in enumerate(ROI_list):
    th1_relFrac = list_input[0].Get("AmpOverMaxAmp_vs_x_channel03"+ROI).ProfileX()
    tmp_relFrac = CopyHist(th1_relFrac, i)

    tmp_relFrac.SetLineColor(colors[2*i])
    th1_list.append(tmp_relFrac)

    tmp_relFrac.Draw("hist same")

    legend.AddEntry(tmp_relFrac, ROI_legend[i],"L")
    tmp_relFrac.Write()

legend.Draw();

myStyle.BeamInfo()

TopRightText = ROOT.TLatex()
TopRightText.SetTextSize(myStyle.GetSize()-4)
TopRightText.SetTextAlign(31)
TopRightText.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying ROI}")

canvas.SaveAs(outdir+"RelFracVsX_DiffROI.gif")
canvas.SaveAs(outdir+"RelFracVsX_DiffROI.pdf")
outputfile.Close()

for e in list_input:
    e.Close()
