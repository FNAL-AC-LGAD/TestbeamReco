import ROOT
import numpy as np

empty = np.array([0,0,0,0,0,0])
bias = np.array([260,265,275,280,285,290])
timingres = np.array([37.65, 36.07, 32.99, 32.55, 30.99, 31.32])
positionres = np.array([14.91, 16.07, 15.11, 15.28, 15.5, 14.73])
timingweightres= np.array([35.19, 34.3, 30.93, 31.12, 30.16, 30.97])

timingresuncert = np.array([1.01, 0.4, 0.29, 0.36, 0.33, 0.4])
positionresuncert = np.array([0.23, 0.11, 0.08, 0.10, 0.10, 0.09])
timingweightresuncert = np.array([1.0, 0.3, 0.29, 0.31, 0.25, 0.32])

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


leg = ROOT.TLegend(0.4, 0.65, 0.8, 0.88)
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
