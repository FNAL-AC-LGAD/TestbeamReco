import ROOT
import numpy as np
import myStyle

## Defining Style
myStyle.ForceStyle()

bias = np.array([               160,    170,    180,    190])

# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionres = np.array([        22.76,  21.35,  20.05,  24.72])
# timingres = np.array([          58.07,  31.95,  31.41,  36.79])
# timingresweighted2 = np.array([ 29.82,  28.00,  27.14,  38.14])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
positionres = np.array([        22.16,  21.36,  22.76,  24.72]) # 30.98])
timingres = np.array([          39.43,  36.10,  32.31,  34.96])
timingresweighted2 = np.array([ 35.30,  32.59,  31.54,  33.61])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionres = np.array([        23.42,  21.44,  22.77,  26.48]) # Last BV with [-0.7,0.7] fit range
# timingres = np.array([          38.75,  37.30,  32.86,  35.20])
# timingresweighted2 = np.array([ 35.98,  33.43,  32.68,  33.87])

for i in range(0,len(bias)):
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0,0])

# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionresuncert = np.array([          3.27,   2.06,   0.72,   1.0])
# timingresuncert = np.array([            18.65,  3.31,   2.39,   4.29])
# timingresweighted2uncert = np.array([   2.64,   3.0,    1.53,   3.43])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
positionresuncert = np.array([          0.76,   0.85,   0.51,   1.0]) # 0.89])
timingresuncert = np.array([            1.82,   1.90,   0.85,   1.01])
timingresweighted2uncert = np.array([   1.70,   1.33,   1.01,   0.96])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionresuncert = np.array([          1.10,   0.88,   0.52,   0.99]) # Last BV with [-0.7,0.7] fit range
# timingresuncert = np.array([            1.79,   1.70,   1.52,   1.20])
# timingresweighted2uncert = np.array([   1.49,   1.19,   0.95,   0.88])

for i in range(0,len(empty)):
    positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+36)/positionres[i]
    timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
    timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size, bias.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

print("For Nominal Voltage")
print("Position resolution: "+"{:.1f}".format(positionres[2])+" #pm "+"{:.1f}".format(positionresuncert[2]))
print("Time W2 resolution: "+"{:.1f}".format(timingresweighted2[2])+" #pm "+"{:.1f}".format(timingresweighted2uncert[2]))

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

c1 = ROOT.TCanvas( "c1", "c1", 1000, 800)
# ROOT.gPad.SetLeftMargin(0.12)
ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,0)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,bias.min()-4,bias.max()+4)
hdummy.GetXaxis().SetTitle("Bias Voltage [V]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

right_axis = ROOT.TGaxis(bias.max()+4,0.0001,bias.max()+4,70.0,0.0001,70.0,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Time resolution [ps]")
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())
right_axis.Draw()


leg = ROOT.TLegend(myStyle.GetPadCenter()-0.25, 1-myStyle.GetMargin()-0.01-0.30, myStyle.GetPadCenter()+0.25, 1-myStyle.GetMargin()-0.01)
# leg.SetFillStyle(0)
# leg.SetBorderSize(0)
# leg.SetLineWidth(1)
# leg.SetNColumns(1)
# leg.SetTextFont(42)
leg.AddEntry(time_graph, "#splitline{Single-channel Time}{Resolution}", "pl")
leg.AddEntry(time_weight_graph, "#splitline{Multi-channel Time}{Resolution}", "pl")
leg.AddEntry(position_graph, "Position Resolution", "pl")

myStyle.BeamInfo()
# myStyle.SensorInfo("HPK C2", 180, False)
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-2*myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{HPK C2}")

leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_HPKC2.pdf")