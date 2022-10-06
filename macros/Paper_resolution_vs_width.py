import ROOT
import numpy as np
import myStyle

## Defining Style
ROOT.gROOT.SetBatch( True )
myStyle.ForceStyle()
colors = myStyle.GetColors(True)

dict_resolutions = myStyle.resolutions2022

outdir = myStyle.getOutputDir("Paper2022")

# Sensors with 1cm strip length and 500um pitch
list_of_sensors = ["EIC_W2_1cm_500up_300uw_240V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W2_1cm_500up_100uw_220V"]

width = []
empty = [0]*len(list_of_sensors)
# positionres_oneStrip  = np.array([78.65, 84.13, 53.97]) # Sigma from fit to oneStrip 1DPlot
positionres_oneStrip = [] # RMS from oneStrip onMetal 1DPlot
positionres_twoStrip = []
positionres_oneStripuncert = []
positionres_twoStripuncert = []
positionres_weighted = []
positionres_weighteduncert = [0.5]*len(list_of_sensors)

positionres_oneStrip_StdDev = [] # StdDev from oneStrip 1DPlot
positionres_weighted_StdDev = []

for name in list_of_sensors:
    width.append(myStyle.GetGeometry(name)['stripWidth'])
    sensor_info = dict_resolutions[name]
    positionres_oneStrip.append(sensor_info['position_oneStripRMS'])
    positionres_oneStripuncert.append(0.01)
    positionres_twoStrip.append(sensor_info['position_twoStrip'])
    positionres_twoStripuncert.append(sensor_info['position_twoStrip_E'])

    weighted_value = sensor_info['position_oneStripRMS']*sensor_info['efficiency_oneStrip'] + sensor_info['position_twoStrip']*sensor_info['efficiency_twoStrip']
    positionres_weighted.append(weighted_value)

    oneStrip_Res = sensor_info['position_oneStrip_StdDev']
    twoStrip_Res = sensor_info['position_twoStrip']
    oneStrip_Eff = sensor_info['efficiency_oneStrip']
    twoStrip_Eff = sensor_info['efficiency_twoStrip']

    positionres_oneStrip_StdDev.append(oneStrip_Res)
    weighted_value_StdDev = ROOT.TMath.Sqrt(oneStrip_Res*oneStrip_Res*oneStrip_Eff + twoStrip_Res*twoStrip_Res*twoStrip_Eff)
    positionres_weighted_StdDev.append(weighted_value_StdDev)

width = np.asarray(width)
empty = np.asarray(empty)
positionres_oneStrip = np.asarray(positionres_oneStrip)
positionres_oneStripuncert = np.asarray(positionres_oneStripuncert)
positionres_twoStrip = np.asarray(positionres_twoStrip)
positionres_twoStripuncert = np.asarray(positionres_twoStripuncert)
positionres_weighted = np.asarray(positionres_weighted)
positionres_weighteduncert = np.asarray(positionres_weighteduncert)

positionres_oneStrip_StdDev = np.asarray(positionres_oneStrip_StdDev)
positionres_weighted_StdDev = np.asarray(positionres_weighted_StdDev)

# positionres_oneStrip  = np.array([78.65, 84.13, 53.97]) # Sigma from fit to oneStrip 1DPlot
# positionres_oneStrip  = np.array([80.37, 54.87, 27.93]) # RMS from oneStrip onMetal 1DPlot
# positionres_twoStrip = np.array([15.38, 18.53, 18.73])
# timingres = np.array([          39.57,  37.34,  34.20,  32.95,  32.55,  35.18])
# timingresweighted2 = np.array([ 35.84,  35.71,  32.67,  31.89,  31.15,  34.11])

# for i in range(0,len(width)):
#     positionres_twoStrip[i] = ROOT.TMath.Sqrt(positionres_twoStrip[i]*positionres_twoStrip[i]-36)
#     # timingres[i] = ROOT.TMath.Sqrt(timingres[i]*timingres[i]-100)
#     # timingresweighted2[i] = ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]-100)

# empty = np.array([0,0,0])

# positionres_oneStripuncert  = np.array([0.18, 0.08, 0.21])
# positionres_oneStripuncert  = np.array([0.01, 0.01, 0.01])
# positionres_twoStripuncert = np.array([0.07, 0.02, 0.02])
# timingresuncert = np.array([            2.58, 0.72, 0.60, 0.52, 0.54, 1.50])
# timingresweighted2uncert = np.array([   1.96, 0.50, 0.52, 0.47, 0.48, 1.36])

# for i in range(0,len(empty)):
#     positionres_twoStripuncert[i] = positionres_twoStripuncert[i]*ROOT.TMath.Sqrt(positionres_twoStrip[i]*positionres_twoStrip[i]+36)/positionres_twoStrip[i]
#     # timingresuncert[i] = timingresuncert[i]*ROOT.TMath.Sqrt(timingres[i]*timingres[i]+100)/timingres[i]
#     # timingresweighted2uncert[i] = timingresweighted2uncert[i]*ROOT.TMath.Sqrt(timingresweighted2[i]*timingresweighted2[i]+100)/timingresweighted2[i]

position_oneStrip_graph  = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres_oneStrip.astype(np.double), empty.astype(np.double), positionres_oneStripuncert.astype(np.double))
position_twoStrip_graph = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres_twoStrip.astype(np.double), empty.astype(np.double), positionres_twoStripuncert.astype(np.double))
position_weighted_graph = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres_weighted.astype(np.double), empty.astype(np.double), positionres_weighteduncert.astype(np.double))

position_oneStrip_StdDev_graph = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres_oneStrip_StdDev.astype(np.double), empty.astype(np.double), positionres_oneStripuncert.astype(np.double))
position_weighted_StdDev_graph = ROOT.TGraphErrors(width.size ,width.astype(np.double), positionres_weighted_StdDev.astype(np.double), empty.astype(np.double), positionres_weighteduncert.astype(np.double))

# time_graph = ROOT.TGraphErrors(width.size , width.astype(np.double), timingres.astype(np.double), empty.astype(np.double), timingresuncert.astype(np.double))
# time_weight_graph = ROOT.TGraphErrors(width.size , width.astype(np.double), timingresweighted2.astype(np.double), empty.astype(np.double), timingresweighted2uncert.astype(np.double))

# print("For Nominal Voltage")
# print("Position resolution: "+"{:.1f}".format(positionres_twoStrip[4])+" #pm "+"{:.1f}".format(positionres_twoStripuncert[4]))
# print("Time W2 resolution: "+"{:.1f}".format(timingresweighted2[4])+" #pm "+"{:.1f}".format(timingresweighted2uncert[4]))

position_twoStrip_graph.SetMarkerColor(colors[2])
position_twoStrip_graph.SetMarkerStyle(20)
position_twoStrip_graph.SetMarkerSize(2)
position_twoStrip_graph.SetLineColor(colors[2])

# Using OnMetal cut
# position_oneStrip_graph.SetMarkerColor(colors[0])
# position_oneStrip_graph.SetMarkerStyle(20)
# position_oneStrip_graph.SetMarkerSize(2)
# position_oneStrip_graph.SetLineColor(colors[0])

# position_weighted_graph.SetMarkerColor(colors[4])
# position_weighted_graph.SetMarkerStyle(20)
# position_weighted_graph.SetMarkerSize(2)
# position_weighted_graph.SetLineColor(colors[4])

# Without OnMetal cut
position_oneStrip_StdDev_graph.SetMarkerColor(colors[0])
position_oneStrip_StdDev_graph.SetMarkerStyle(20) # 47
position_oneStrip_StdDev_graph.SetMarkerSize(2)
position_oneStrip_StdDev_graph.SetLineColor(colors[0])

position_weighted_StdDev_graph.SetMarkerColor(colors[1])
position_weighted_StdDev_graph.SetMarkerStyle(20)
position_weighted_StdDev_graph.SetMarkerSize(2)
position_weighted_StdDev_graph.SetLineColor(colors[1])

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
c1.SetGrid(0,1)

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,width.min()-50,width.max()+50)
hdummy.GetXaxis().SetTitle("Metal width [#mum]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
# hdummy.SetMaximum(90.0)
hdummy.SetMaximum(140.0)
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

# leg = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin()-0.01-0.20, 2*myStyle.GetMargin()+0.01+0.35, 1-myStyle.GetMargin()-0.01)
leg = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin()-0.01-0.24, 2*myStyle.GetMargin()+0.01+0.35, 1-myStyle.GetMargin()-0.01)
leg.SetTextFont(myStyle.GetFont())
leg.SetTextSize(myStyle.GetSize()-4)
# leg.AddEntry(time_graph, "#splitline{Single-channel Time}{Resolution}", "pl")
# leg.AddEntry(time_weight_graph, "#splitline{Multi-channel Time}{Resolution}", "pl")

# Using OnMetal cut
# leg.AddEntry(position_oneStrip_graph, "Exactly one strip reconstruction, OnMetal", "pl")
# leg.AddEntry(position_weighted_graph, "Weighted average, OnMetal", "pl")

# Without OnMetal cut
leg.AddEntry(position_oneStrip_StdDev_graph, "Exactly one strip reconstruction", "pl")
leg.AddEntry(position_weighted_StdDev_graph, "Effective resolution", "pl")

leg.AddEntry(position_twoStrip_graph, "Two strip reconstruction", "pl")

myStyle.BeamInfo()
# myStyle.SensorInfo("BNL2021", 285, False)
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying width}")

leg.Draw()
ROOT.gPad.RedrawAxis("g")

# Using OnMetal cut
# position_oneStrip_graph.Draw("epl same")
# position_weighted_graph.Draw("epl same")

# Without OnMetal cut
position_oneStrip_StdDev_graph.Draw("epl same")
position_weighted_StdDev_graph.Draw("epl same")

position_twoStrip_graph.Draw("epl same")

# time_graph.Draw("epl same")
# time_weight_graph.Draw("epl same")

c1.SaveAs("%sresolution_vs_width_EIC.pdf"%(outdir))
