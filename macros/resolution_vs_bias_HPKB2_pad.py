import ROOT
import numpy as np
import myStyle

## Defining Style
myStyle.ForceStyle()

bias = np.array([               210,    220,    230,    250,    310,    360])

# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# timingres =                 np.array([31.47,36.71,32.22,40.54,37.75,38.35])
# positionres =               np.array([30.02,25.72,24.96,26.49,28.48,31.29])
# timingresweighted2 =        np.array([40.44,23.43,23.69,29.82,31.08,47.06])
# Range [myMean - 0.8*myRMS , myMean + 0.6*myRMS]
# timingres =                 np.array([36.64,36.08,31.67,34.65,33.58,36.41])
# positionres =               np.array([29.67,28.13,26.84,26.96,30.22,32.33])
# timingresweighted2 =        np.array([39.26,26.89,25.47,29.01,29.91,39.03])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
# positionres = np.array([        27.56,  25.22,  27.47,  29.25,  31.92,  38.36])
# timingres = np.array([          36.84,  35.17,  33.00,  33.48,  35.10,  42.08])
# timingresweighted2 = np.array([ 32.89,  30.72,  27.32,  30.37,  33.06,  42.28])
# Range [myMean - 1.3*myRMS , myMean + 1.3*myRMS] + Rebin(2) first half
# Range [myMean - 0.7*myRMS , myMean + 0.7*myRMS] + Rebin(2) second half
# positionres = np.array([        30.51,  26.53,  28.93,  29.25,  31.92,  38.36])
# timingres = np.array([          40.73,  34.81,  34.57,  33.48,  35.10,  42.08])
# timingresweighted2 = np.array([ 33.12,  31.32,  29.21,  30.37,  33.06,  42.28])
# Range variable + Rebin(2) ???
positionres = np.array([        33.34,  27.85,  24.94,  28.01,  30.52,  32.69])
timingres = np.array([          41.99,  37.54,  34.57,  35.53,  37.24,  35.44])
timingresweighted2 = np.array([ 35.31,  32.14,  29.21,  30.50,  31.93,  32.35])

for i in range(0,len(bias)):
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

empty = np.array([0,0,0,0,0,0])

# Range [myMean - 0.65*myRMS , myMean + 0.6*myRMS]
# timingresuncert =           np.array([4.81,6.51,3.25,5.95,4.26,2.54])
# positionresuncert =         np.array([5.67,5.17,1.73,1.33,1.36,1.12])
# timingresweighted2uncert =  np.array([9.48,2.58,1.23,2.46,2.09,4.41])
# Range [myMean - 0.8*myRMS , myMean + 0.6*myRMS]
# timingresuncert =           np.array([5.12,4.27,2.10,2.77,2.27,1.80])
# positionresuncert =         np.array([4.33,5.06,1.46,1.27,1.36,1.03])
# timingresweighted2uncert =  np.array([5.75,2.52,1.11,1.68,1.45,2.24])
# Range [myMean - 1*myRMS , myMean + 1*myRMS]
# positionresuncert =         np.array([1.78, 1.35,   0.75,   0.94,   0.96,   1.07])
# timingresuncert =           np.array([2.35, 2.23,   1.00,   1.13,   1.40,   1.55])
# timingresweighted2uncert =  np.array([1.59, 1.53,   0.72,   1.06,   1.43,   1.86])
# Range [myMean - 1.3*myRMS , myMean + 1.3*myRMS] + Rebin(2) first half
# Range [myMean - 0.7*myRMS , myMean + 0.7*myRMS] + Rebin(2) second half
# positionresuncert =         np.array([1.41, 1.00,   0.54,   0.94,   0.96,   1.07])
# timingresuncert =           np.array([1.68, 1.26,   0.93,   1.13,   1.40,   1.55])
# timingresweighted2uncert =  np.array([1.27, 0.97,   0.65,   1.06,   1.43,   1.86])
# Different Range per channel + Rebin(2) (see plot1DRes.py)
positionresuncert =         np.array([0.93, 0.68,   1.06,   0.90,   1.32,   1.09])
timingresuncert =           np.array([1.12, 0.80,   0.93,   1.93,   2.08,   1.42])
timingresweighted2uncert =  np.array([0.84, 0.68,   0.65,   1.30,   1.14,   1.17])

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

c1 = ROOT.TCanvas( "c1", "c1", 1000, 800)
# ROOT.gPad.SetLeftMargin(0.12)
# ROOT.gPad.SetRightMargin(0.15)
# ROOT.gPad.SetTopMargin(0.08)
# ROOT.gPad.SetBottomMargin(0.12)
ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,bias.min()-10,bias.max()+10)
hdummy.GetXaxis().SetTitle("Bias Voltage [V]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
hdummy.SetMaximum(70.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

right_axis = ROOT.TGaxis(bias.max()+10,0.0001,bias.max()+10,70.0,0.0001,70.0,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Time resolution [ps]")
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())


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
myStyle.SensorInfo("HPK B2", 230, False)

leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_HPKB2.pdf")