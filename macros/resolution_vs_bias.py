import ROOT
import numpy as np
import myStyle
import optparse

## Defining Style
myStyle.ForceStyle()

# Construct the argument parser
parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s','--sensor', dest='sensor', default = "BNL2020", help="Type of sensor (BNL2020, BNL2021, HPKB2, HPKC2)")
options, args = parser.parse_args()

sensor = options.sensor

# Sensor resolution values

if (sensor=="BNL2020"):
    bias = np.array([               200,    210,    220,    225])
    nominal_pos = 2
    positionres = np.array([        10.43,  10.04,   8.75,  10.56])
    timingres = np.array([          42.21,  35.17,  32.36,  32.8])
    timingresweighted2 = np.array([ 38.71,  31.94,  30.49,  29.74])
elif (sensor=="BNL2021"):
    bias = np.array([               260,    265,    275,    280,    285,    290])
    nominal_pos = 4
    positionres = np.array([        12.40,  12.12,  12.20,  11.79,  12.47,   9.99])
    timingres = np.array([          39.57,  37.34,  34.20,  32.95,  32.55,  35.18])
    timingresweighted2 = np.array([ 35.84,  35.71,  32.67,  31.89,  31.15,  34.11])
elif (sensor=="HPKB2"):
    bias = np.array([               210,    220,    230,    250,    310,    360])
    nominal_pos = 2
    positionres = np.array([        33.34,  27.85,  24.94,  28.01,  30.52,  32.69])
    timingres = np.array([          41.99,  37.54,  34.57,  35.53,  37.24,  35.44])
    timingresweighted2 = np.array([ 35.31,  32.14,  29.21,  30.50,  31.93,  32.35])
elif (sensor=="HPKC2"):
    bias = np.array([               160,    170,    180,    190])
    nominal_pos = 2
    positionres = np.array([        22.16,  21.36,  22.76,  24.72])
    timingres = np.array([          39.43,  36.10,  32.31,  34.96])
    timingresweighted2 = np.array([ 35.30,  32.59,  31.54,  33.61])
else:
    print("Enter a valid sensor name (BNL2020, BNL2021, HPKB2, HPKC2)!")

for i in range(0,len(bias)):
    positionres[i] = ROOT.TMath.Sqrt(positionres[i]*positionres[i]-36)
    timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
    timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

# Resolution error values

if (sensor=="BNL2020"):
    empty = np.array([0,0,0,0])
    positionresuncert = np.array([          0.12, 0.19, 0.11, 0.11])
    timingresuncert = np.array([            1.60, 1.00, 0.63, 0.70])
    timingresweighted2uncert = np.array([   1.52, 0.92, 0.65, 0.66])
elif (sensor=="BNL2021"):
    empty = np.array([0,0,0,0,0,0])
    positionresuncert = np.array([          0.30, 0.15, 0.20, 0.14, 0.17, 0.23])
    timingresuncert = np.array([            2.58, 0.72, 0.60, 0.52, 0.54, 1.50])
    timingresweighted2uncert = np.array([   1.96, 0.50, 0.52, 0.47, 0.48, 1.36])
elif (sensor=="HPKB2"):
    empty = np.array([0,0,0,0,0,0])
    positionresuncert =         np.array([0.93, 0.68,   1.06,   0.90,   1.32,   1.09])
    timingresuncert =           np.array([1.12, 0.80,   0.93,   1.93,   2.08,   1.42])
    timingresweighted2uncert =  np.array([0.84, 0.68,   0.65,   1.30,   1.14,   1.17])
elif (sensor=="HPKC2"):
    empty = np.array([0,0,0,0])
    positionresuncert = np.array([          0.76,   0.85,   0.51,   1.00])
    timingresuncert = np.array([            1.82,   1.90,   0.85,   1.01])
    timingresweighted2uncert = np.array([   1.70,   1.33,   1.01,   0.96])

for i in range(0,len(empty)):
    positionresuncert[i] = positionresuncert[i]*ROOT.TMath.Sqrt(positionres[i]*positionres[i]+36)/positionres[i]
    timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
    timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_ymax = 30.0
time_ymax = 70.0

position_graph = ROOT.TGraphErrors(bias.size ,bias.astype(np.double), (time_ymax/position_ymax)*positionres.astype(np.double), empty.astype(np.double), positionresuncert.astype(np.double))
time_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
time_weight_graph = ROOT.TGraphErrors(bias.size , bias.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

print("For Nominal Voltage in "+sensor+" sensor:")
print("Position resolution: "+"{:.1f}".format(positionres[nominal_pos])+" #pm "+"{:.1f}".format(positionresuncert[nominal_pos]))
print("Time W2 resolution: "+"{:.1f}".format(timingresweighted2[nominal_pos])+" #pm "+"{:.1f}".format(timingresweighted2uncert[nominal_pos]))

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
hdummy.GetYaxis().SetTitle("Time resolution [ps]")
hdummy.SetMaximum(time_ymax)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

right_axis = ROOT.TGaxis(bias.max()+5,0.0001,bias.max()+5,time_ymax,0.0001,position_ymax,510,"+L")
right_axis.UseCurrentStyle()
right_axis.SetTitle("Position resolution [#mum]")
right_axis.SetLabelSize(myStyle.GetSize()-4)
right_axis.SetTitleSize(myStyle.GetSize())
right_axis.SetLabelFont(myStyle.GetFont())
right_axis.SetTitleFont(myStyle.GetFont())
right_axis.SetLineColor(ROOT.kRed)
right_axis.SetLabelColor(ROOT.kRed)
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
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-2*myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{"+str(sensor)+"}")

leg.Draw()
position_graph.Draw("epl same")
time_graph.Draw("epl same")
time_weight_graph.Draw("epl same")

c1.SaveAs("resolution_plot_"+sensor+".pdf")
