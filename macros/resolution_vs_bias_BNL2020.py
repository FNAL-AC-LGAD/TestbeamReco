import ROOT
import numpy as np
import myStyle

## Defining Style
myStyle.ForceStyle()

bias = np.array([               200,    210,    220,    225])
# OLD
# positionres = np.array([      13.37,  12.4,   11.66,  13.55])
# timingres = np.array([        41.04,  35.97,  32.56,  33.01])
# timingresweighted = np.array([37.91,  33.59,  29.81,  30.68])
# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionres = np.array([        10.45,  9.67,   8.60,   10.39])
# timingres = np.array([          39.36,  33.09,  31.26,  29.97])
# timingresweighted2 = np.array([ 41.53,  31.82,  28.02,  28.19])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
positionres = np.array([        10.43,  10.04,   8.75,  10.56])
timingres = np.array([          42.21,  35.17,  32.36,  32.8])
timingresweighted2 = np.array([ 38.71,  31.94,  30.49,  29.74])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionres = np.array([        10.81,  10.01,   9.32,  10.95])
# timingres = np.array([          42.53,  35.57,  31.59,  33.30])
# timingresweighted2 = np.array([ 38.43,  32.27,  30.46,  29.86])

for i in range(0,len(bias)):
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0,0])

# OLD
# positionresuncert = np.array([0.08, 0.1, 0.07, 0.07])
# timingresuncert = np.array([0.50, 0.43,0.27, 0.29])
# timingresweighteduncert = np.array([0.47, 0.36, 0.25, 0.28])
# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionresuncert = np.array([          0.14, 0.57, 0.19, 0.12])
# timingresuncert = np.array([            3.68, 2.54, 1.71, 1.40])
# timingresweighted2uncert = np.array([   6.00, 2.25, 1.89, 1.61])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
positionresuncert = np.array([          0.12, 0.19, 0.11, 0.11])
timingresuncert = np.array([            1.60, 1.00, 0.63, 0.70])
timingresweighted2uncert = np.array([   1.52, 0.92, 0.65, 0.66])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionresuncert = np.array([          0.12, 0.15, 0.10, 0.12])
# timingresuncert = np.array([            1.42, 1.05, 0.99, 0.90])
# timingresweighted2uncert = np.array([   1.54, 0.79, 0.87, 0.67])

for i in range(0,len(empty)):
    positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+36)/positionres[i]
    timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
    timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]


position_graph = ROOT.TGraphErrors(bias.size ,bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

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

c1 = ROOT.TCanvas( "c1", "c1",1000, 800)
# ROOT.gStyle.SetPadRightMargin(marg)
# ROOT.gPad.SetLeftMargin(0.12)
ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,0)
ROOT.gStyle.SetOptStat(0) 


# hdummy = ROOT.TH1D("","",1,bias.min()-10,bias.max()+10)
hdummy = ROOT.TH1D("","",1,bias.min()-5,bias.max()+5)
hdummy.GetXaxis().SetTitle("Bias Voltage [V]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

right_axis = ROOT.TGaxis(bias.max()+5,0.0001,bias.max()+5,70.0,0.0001,70.0,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Time resolution [ps]")
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())

right_axis.Draw()


# leg = ROOT.TLegend(0.4, 0.65, 0.8, 0.88)
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
# myStyle.SensorInfo("BNL2020", 220, False)
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-2*myStyle.GetMargin(),1-myStyle.GetMargin()+0.01,"#bf{BNL2020}")

leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_BNL2020.pdf")
