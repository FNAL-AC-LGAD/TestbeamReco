import ROOT
import numpy as np
import myStyle

## Defining Style
myStyle.ForceStyle()

bias = np.array([               260,    265,    275,    280,    285,    290])
# OLD
# positionres = np.array([        14.83,  16.0,   14.99,  15.21,  15.41,  14.62])
# timingres = np.array([          37.65,  36.07,  32.99,  32.55,  30.99,  31.32])
# timingresweighted2 = np.array([ 35.19,  34.16,  30.91,  31.13,  30.09,  30.94])
# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionres = np.array([        12.04,  13.34,  16.72,  13.25,  12.58,  9.44])
# timingres = np.array([          45.30,  30.73,  31.55,  27.71,  29.15,  33.09])
# timingresweighted2 = np.array([ 60.53,  39.35,  29.87,  28.11,  26.75,  53.31])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
# positionres = np.array([        12.09,  12.05,  12.14,  12.33,  13.05,  9.21])
# timingres = np.array([          42.87,  38.05,  32.82,  31.41,  31.00,  36.96])
# timingresweighted2 = np.array([ 34.39,  34.37,  31.00,  31.8,   30.76,  35.74])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionres = np.array([        12.34,  12.58,  13.47,  12.59,  12.92,  9.57])
# timingres = np.array([          39.94,  38.25,  32.52,  31.14,  31.22,  34.61])
# timingresweighted2 = np.array([ 35.83,  35.29,  31.33,  31.52,  30.48,  34.41])
# Range [myMean - 1.4*myRMS , myMean + 1.4*myRMS] + Rebin(2)
positionres = np.array([        12.40,  12.12,  12.20,  11.79,  12.47,  9.99]) # 9.99...
timingres = np.array([          39.57,  37.34,  34.20,  32.95,  32.55,  35.18])
timingresweighted2 = np.array([ 35.84,  35.71,  32.67,  31.89,  31.15,  34.11])

for i in range(0,len(bias)):
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0,0,0,0])

# OLD
# positionresuncert = np.array([          0.22, 0.5,  0.08, 0.10, 0.10, 0.09])
# timingresuncert = np.array([            1.01, 0.4,  0.29, 0.36, 0.33, 0.4])
# timingresweighted2uncert = np.array([   1.01, 0.34, 0.29, 0.31, 0.25, 0.31])
# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# positionresuncert = np.array([          1.14, 1.41, 2.78, 0.77, 1.28, 0.66])
# timingresuncert = np.array([            17.0, 2.95, 3.09, 2.04, 1.61, 5.39])
# timingresweighted2uncert = np.array([   55.1, 5.97, 2.54, 2.10, 1.91, 35.63])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
# positionresuncert = np.array([          0.47, 0.28, 0.38, 0.29, 0.37, 0.26])
# timingresuncert = np.array([            4.51, 1.37, 0.88, 0.99, 1.00, 3.02])
# timingresweighted2uncert = np.array([   2.94, 1.00, 1.00, 1.00, 0.76, 2.68])
# Range [myMean - 1*myRMS , myMean + 1*myRMS] + Rebin(2)
# positionresuncert = np.array([          0.47, 0.52, 0.65, 0.25, 0.61, 0.29])
# timingresuncert = np.array([            6.77, 1.17, 1.21, 1.01, 1.10, 3.48])
# timingresweighted2uncert = np.array([   4.80, 0.91, 1.05, 1.04, 1.01, 3.37])
# Range [myMean - 1.4*myRMS , myMean + 1.4*myRMS] + Rebin(2)
positionresuncert = np.array([          0.30, 0.15, 0.20, 0.14, 0.17, 0.23])
timingresuncert = np.array([            2.58, 0.72, 0.60, 0.52, 0.54, 1.50])
timingresweighted2uncert = np.array([   1.96, 0.50, 0.52, 0.47, 0.48, 1.36])

for i in range(0,len(empty)):
    positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+36)/positionres[i]
    timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
    timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_graph = ROOT.TGraphErrors(bias.size ,bias.astype(np.double), positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

print("For Nominal Voltage")
print("Position resolution: "+"{:.1f}".format(positionres[4])+" #pm "+"{:.1f}".format(positionresuncert[4]))
print("Time W2 resolution: "+"{:.1f}".format(timingresweighted2[4])+" #pm "+"{:.1f}".format(timingresweighted2uncert[4]))

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

# c1 = ROOT.TCanvas( "c1", "c1", 0, 0, 800, 800)
c1 = ROOT.TCanvas("c1","c1",1000,800)
# ROOT.gPad.SetLeftMargin(0.12)
ROOT.gPad.SetRightMargin(2*myStyle.GetMargin())
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,0)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,bias.min()-5,bias.max()+5)
hdummy.GetXaxis().SetTitle("Bias Voltage [V]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

right_axis = ROOT.TGaxis(bias.max()+5,0.0001,bias.max()+5,70.0,0.0001,70.0,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Time resolution [ps]")
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
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
# myStyle.SensorInfo("BNL2021", 285, False)
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-2*myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{BNL2021}")

leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_BNL2021_Medium.pdf")
