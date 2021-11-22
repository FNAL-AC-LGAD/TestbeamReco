import ROOT
import numpy as np

bias = np.array([160,170,180,190])
timingres = np.array([58.07,31.95,31.41,36.79])
positionres = np.array([22.76,21.35,20.05,24.72])
timingresweighted = np.array([34.22,29.19,28.99,35.74])

empty = np.array([0,0,0,0])

timingresuncert = np.array([19,3.3,2.4,4.3])
positionresuncert = np.array([3.2,2.1,0.72,1.0])
timingresweighteduncert = np.array([3.9,3.7,1.9,3.0])

position_graph = ROOT.TGraphErrors(bias.size ,bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingresweighted.astype(np.double), empty.astype(np.double), timingresweighteduncert.astype(np.double))


position_graph.SetMarkerColor(ROOT.kRed)
position_graph.SetMarkerStyle(20)
position_graph.SetMarkerSize(1)
position_graph.SetLineColor(ROOT.kRed)

time_graph.SetMarkerColor(ROOT.kBlack)
time_graph.SetMarkerStyle(20)
time_graph.SetMarkerSize(1)
time_graph.SetLineColor(ROOT.kBlack)

time_weight_graph.SetMarkerColor(ROOT.kBlue)
time_weight_graph.SetMarkerStyle(20)
time_weight_graph.SetMarkerSize(1)
time_weight_graph.SetLineColor(ROOT.kBlue)

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

c1.SaveAs("resolution_plot.pdf")
