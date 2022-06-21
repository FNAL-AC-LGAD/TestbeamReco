import ROOT
import numpy as np
import myStyle

## Defining Style
ROOT.gROOT.SetBatch( True )
myStyle.ForceStyle()

outdir = myStyle.getOutputDir("Paper2022")

width = np.array([300, 200, 100])

positionres = np.array([15.38, 18.53, 18.73])
# timingres = np.array([          39.57,  37.34,  34.20,  32.95,  32.55,  35.18])
# timingresweighted2 = np.array([ 35.84,  35.71,  32.67,  31.89,  31.15,  34.11])

# for i in range(0,len(width)):
#     positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
#     # timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
#     # timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0])

positionresuncert = np.array([0.07, 0.02, 0.02])
# timingresuncert = np.array([            2.58, 0.72, 0.60, 0.52, 0.54, 1.50])
# timingresweighted2uncert = np.array([   1.96, 0.50, 0.52, 0.47, 0.48, 1.36])

# for i in range(0,len(empty)):
#     positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+36)/positionres[i]
#     # timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
#     # timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_graph = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
# time_graph = ROOT.TGraphErrors(width.size , width.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
# time_weight_graph = ROOT.TGraphErrors(width.size , width.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

# print("For Nominal Voltage")
# print("Position resolution: "+"{:.1f}".format(positionres[4])+" #pm "+"{:.1f}".format(positionresuncert[4]))
# print("Time W2 resolution: "+"{:.1f}".format(timingresweighted2[4])+" #pm "+"{:.1f}".format(timingresweighted2uncert[4]))

position_graph.SetMarkerColor(ROOT.kRed)
position_graph.SetMarkerStyle(20)
position_graph.SetMarkerSize(1)
position_graph.SetLineColor(ROOT.kRed)

# time_graph.SetMarkerColor(ROOT.kBlack)
# time_graph.SetMarkerStyle(20)
# time_graph.SetMarkerSize(1)
# time_graph.SetLineColor(ROOT.kBlack)

# time_weight_graph.SetMarkerColor(ROOT.kBlue)
# time_weight_graph.SetMarkerStyle(20)
# time_weight_graph.SetMarkerSize(1)
# time_weight_graph.SetLineColor(ROOT.kBlue)

# c1 = ROOT.TCanvas( "c1", "c1", 0, 0, 800, 800)
c1 = ROOT.TCanvas("c1","c1",1000,800)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,0)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,width.min()-50,width.max()+50)
hdummy.GetXaxis().SetTitle("Metal width [#mum]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
hdummy.SetMaximum(40.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

# right_axis = ROOT.TGaxis(width.max()+5,0.0001,width.max()+5,70.0,0.0001,70.0,510,"+L")
# right_axis.UseCurrentStyle()
# right_axis.SetTitle("Time resolution [ps]")
# right_axis.SetLabelFont(myStyle.GetFont())
# right_axis.SetTitleFont(myStyle.GetFont())
# right_axis.SetLabelSize(myStyle.GetSize()-4)
# right_axis.SetTitleSize(myStyle.GetSize())
# right_axis.Draw()

# leg = ROOT.TLegend(myStyle.GetPadCenter()-0.25, 1-myStyle.GetMargin()-0.01-0.30, myStyle.GetPadCenter()+0.25, 1-myStyle.GetMargin()-0.01)
# # leg.SetFillStyle(0)
# # leg.SetBorderSize(0)
# # leg.SetLineWidth(1)
# # leg.SetNColumns(1)
# # leg.SetTextFont(42)
# # leg.AddEntry(time_graph, "#splitline{Single-channel Time}{Resolution}", "pl")
# # leg.AddEntry(time_weight_graph, "#splitline{Multi-channel Time}{Resolution}", "pl")
# leg.AddEntry(position_graph, "Position Resolution", "pl")

# myStyle.BeamInfo()
# myStyle.SensorInfo("BNL2021", 285, False)
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-2*myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{EIC 1cm strip 500um pitch}")

# leg.Draw()
position_graph.Draw("epl same")
# time_graph.Draw("epl same")
# time_weight_graph.Draw("epl same")

c1.SaveAs("%sresolution_vs_width_EIC1cm.pdf"%(outdir))
