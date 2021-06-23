import ROOT
import numpy as np

bias = np.array([260,265,275,285,290])
timingres = np.array([37.7,36.1,33.0,31.0,31.7])
positionres = np.array([16.9,18.4,17.5,17.9,17.2])
timingweightres= np.array([37.8,36.5,33.3,35.2,36.4])

empty = np.array([0,0,0,0,0])

timingresuncert = np.array([1.0,0.4,1.0,0.33,0.34])
positionresuncert = np.array([0.3,0.13,0.12,0.14,0.13])
timingweightresuncert = np.array([0.13,0.30,0.25,0.17,0.22 ])

position_graph = ROOT.TGraphErrors(bias.size ,bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingweightres.astype(np.double), empty.astype(np.double), timingweightresuncert.astype(np.double))

time_weight_graph.SetMarkerColor(ROOT.kBlue)
time_weight_graph.SetMarkerStyle(20)
time_weight_graph.SetMarkerSize(1)
time_weight_graph.SetLineColor(ROOT.kBlue)

position_graph.SetMarkerColor(ROOT.kRed)
position_graph.SetMarkerStyle(20)
position_graph.SetMarkerSize(1)
position_graph.SetLineColor(ROOT.kRed)

time_graph.SetMarkerColor(ROOT.kBlack)
time_graph.SetMarkerStyle(20)
time_graph.SetMarkerSize(1)
time_graph.SetLineColor(ROOT.kBlack)

c1 = ROOT.TCanvas( "c1", "c1", 0, 0, 800, 800)
ROOT.gPad.SetLeftMargin(0.12)
ROOT.gPad.SetRightMargin(0.15)
ROOT.gPad.SetTopMargin(0.08)
ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,bias.min()-10,bias.max()+10)
hdummy.GetXaxis().SetTitle("Bias Voltage (V)")
hdummy.GetYaxis().SetTitle("Resolution (ps/microns)")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0)
hdummy.Draw()


leg = ROOT.TLegend(0.6, 0.65, 0.9, 0.88)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetLineWidth(1)
leg.SetNColumns(1)
leg.SetTextFont(42)
leg.AddEntry(time_graph, "Time Resolution", "pl")
leg.AddEntry(position_graph, "Position Resolution", "pl")
leg.AddEntry(time_weight_graph, "Weighted Time Resolution", "pl")


leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_BNL2021_Medium.pdf")
