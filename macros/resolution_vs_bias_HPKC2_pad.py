import ROOT
import numpy as np

## Defining Style
ROOT.gStyle.SetPadTopMargin(0.05)    #0.05
ROOT.gStyle.SetPadRightMargin(0.05)  #0.05
ROOT.gStyle.SetPadBottomMargin(0.1)  #0.16
ROOT.gStyle.SetPadLeftMargin(0.1)   #0.16

ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)

font=43 # Helvetica
tsize=28
ROOT.gStyle.SetTextFont(font)
ROOT.gStyle.SetLabelFont(font,"x")
ROOT.gStyle.SetTitleFont(font,"x")
ROOT.gStyle.SetLabelFont(font,"y")
ROOT.gStyle.SetTitleFont(font,"y")
ROOT.gStyle.SetLabelFont(font,"z")
ROOT.gStyle.SetTitleFont(font,"z")

ROOT.gStyle.SetTextSize(tsize)
ROOT.gStyle.SetLabelSize(tsize,"x")
ROOT.gStyle.SetTitleSize(tsize,"x")
ROOT.gStyle.SetLabelSize(tsize,"y")
ROOT.gStyle.SetTitleSize(tsize,"y")
ROOT.gStyle.SetLabelSize(tsize,"z")
ROOT.gStyle.SetTitleSize(tsize,"z")

ROOT.gStyle.SetTitleXOffset(1.0)
ROOT.gStyle.SetTitleYOffset(1.25)
ROOT.gStyle.SetOptTitle(0)
# ROOT.gStyle.SetOptStat(0)

ROOT.gStyle.SetMarkerStyle(20)

ROOT.gROOT.ForceStyle()

bias = np.array([160,170,180,190])
timingres = np.array([58.07,31.95,31.41,36.79])
positionres = np.array([22.76,21.35,20.05,24.72])
timingresweighted2 = np.array([29.82,28.00,27.14,38.14])

for i in range(0,len(bias)):
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-49)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0,0])

timingresuncert = np.array([18.65,3.31,2.39,4.29])
positionresuncert = np.array([3.27,2.06,0.72,1.0])
timingresweighted2uncert = np.array([2.64,3.0,1.53,3.43])

for i in range(0,len(empty)):
    timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
    positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+49)/positionres[i]
    timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))


position_graph.SetMarkerColor(ROOT.kRed)
position_graph.SetMarkerSize(1)
position_graph.SetLineColor(ROOT.kRed)

time_graph.SetMarkerColor(ROOT.kBlack)
time_graph.SetMarkerSize(1)
time_graph.SetLineColor(ROOT.kBlack)

time_weight_graph.SetMarkerColor(ROOT.kBlue)
time_weight_graph.SetMarkerSize(1)
time_weight_graph.SetLineColor(ROOT.kBlue)

c1 = ROOT.TCanvas( "c1", "c1", 800, 800)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(0.15)
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,bias.min()-10,bias.max()+10)
hdummy.GetXaxis().SetTitle("Bias Voltage (V)")
hdummy.GetYaxis().SetTitle("Resolution (ps/microns)")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw()


leg = ROOT.TLegend(0.4, 0.65, 0.8, 0.88)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
# leg.SetLineWidth(1)
leg.SetNColumns(1)
# leg.SetTextFont(42)
leg.AddEntry(time_graph, "Time Resolution", "pl")
leg.AddEntry(position_graph, "Position Resolution", "pl")
leg.AddEntry(time_weight_graph, "Weight squared Time Resolution", "pl")


leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_HPKC2.pdf")