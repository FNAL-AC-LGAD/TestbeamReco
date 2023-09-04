import ROOT
import numpy as np
import myStyle

## Defining Style
ROOT.gROOT.SetBatch( True )
myStyle.ForceStyle()
colors = myStyle.GetColors(True)

dict_resolutions = myStyle.resolutions2022

outdir = myStyle.getOutputDir("Paper2022")

# Sensors with 500um pitch and 200um metal width
list_of_sensors = ["EIC_W1_2p5cm_500up_200uw_215V", "EIC_W1_1cm_500up_200uw_255V", "EIC_W1_0p5cm_500up_200uw_1_4_245V"]

length = []
empty = [0]*len(list_of_sensors)

positionres_twoStrip = []
positionres_twoStripuncert = []

positionres_oneStrip_StdDev = [] # StdDev from oneStrip 1DPlot
positionres_oneStripuncert = []

positionres_weighted_StdDev = []
positionres_weighteduncert = [0.5]*len(list_of_sensors)

for name in list_of_sensors:
    length.append(myStyle.GetGeometry(name)['length'])
    sensor_info = dict_resolutions[name]

    oneStrip_Res = sensor_info['position_oneStrip_StdDev']
    twoStrip_Res = sensor_info['position_twoStrip']
    oneStrip_Eff = sensor_info['efficiency_oneStrip']
    twoStrip_Eff = sensor_info['efficiency_twoStrip']

    positionres_twoStrip.append(sensor_info['position_twoStrip'])
    positionres_twoStripuncert.append(sensor_info['position_twoStrip_E'])

    positionres_oneStrip_StdDev.append(oneStrip_Res)
    positionres_oneStripuncert.append(0.01)

    weighted_value_StdDev = ROOT.TMath.Sqrt(oneStrip_Res*oneStrip_Res*oneStrip_Eff + twoStrip_Res*twoStrip_Res*twoStrip_Eff)
    positionres_weighted_StdDev.append(weighted_value_StdDev)



length = np.asarray(length)
empty = np.asarray(empty)

positionres_twoStrip = np.asarray(positionres_twoStrip)
positionres_twoStripuncert = np.asarray(positionres_twoStripuncert)

positionres_oneStrip_StdDev = np.asarray(positionres_oneStrip_StdDev)
positionres_oneStripuncert = np.asarray(positionres_oneStripuncert)

positionres_weighted_StdDev = np.asarray(positionres_weighted_StdDev)
positionres_weighteduncert = np.asarray(positionres_weighteduncert)

print("Sensors             : ", list_of_sensors)
print("Two strip resolution: ", positionres_twoStrip)
print("Two strip error     : ", positionres_twoStripuncert)
print("One strip resolution: ", positionres_oneStrip_StdDev)
print("One strip error     : ", positionres_oneStripuncert)
print("Effective resolution: ", positionres_weighted_StdDev)
print("Effective res error : ", positionres_weighteduncert)

position_twoStrip_graph = ROOT.TGraphErrors(length.size ,length.astype(np.double), positionres_twoStrip.astype(np.double), empty.astype(np.double), positionres_twoStripuncert.astype(np.double))
position_oneStrip_StdDev_graph = ROOT.TGraphErrors(length.size ,length.astype(np.double), positionres_oneStrip_StdDev.astype(np.double), empty.astype(np.double), positionres_oneStripuncert.astype(np.double))
position_weighted_StdDev_graph = ROOT.TGraphErrors(length.size ,length.astype(np.double), positionres_weighted_StdDev.astype(np.double), empty.astype(np.double), positionres_weighteduncert.astype(np.double))

position_twoStrip_graph.SetMarkerColor(colors[2])
position_twoStrip_graph.SetMarkerStyle(20)
position_twoStrip_graph.SetMarkerSize(2)
position_twoStrip_graph.SetLineColor(colors[2])

position_oneStrip_StdDev_graph.SetMarkerColor(colors[0])
position_oneStrip_StdDev_graph.SetMarkerStyle(20) #47 cross
position_oneStrip_StdDev_graph.SetMarkerSize(2)
position_oneStrip_StdDev_graph.SetLineColor(colors[0])

position_weighted_StdDev_graph.SetMarkerColor(colors[1])
position_weighted_StdDev_graph.SetMarkerStyle(20)
position_weighted_StdDev_graph.SetMarkerSize(2)
position_weighted_StdDev_graph.SetLineColor(colors[1])

c1 = ROOT.TCanvas("c1","c1",1000,800)
c1.SetGrid(0,1)

ROOT.gPad.SetTicks(1,1)
ROOT.gStyle.SetOptStat(0) 


hdummy = ROOT.TH1D("","",1,length.min()-5,length.max()+5)
hdummy.GetXaxis().SetTitle("Strip length [mm]")
hdummy.GetYaxis().SetTitle("Position resolution [#mum]")
# hdummy.SetMaximum(90.0)
hdummy.SetMaximum(140.0)
hdummy.SetMinimum(0.0001)
hdummy.Draw("AXIS")

leg = ROOT.TLegend(2*myStyle.GetMargin()+0.01, 1-myStyle.GetMargin()-0.01-0.24, 2*myStyle.GetMargin()+0.01+0.35, 1-myStyle.GetMargin()-0.01)
leg.SetTextFont(myStyle.GetFont())
leg.SetTextSize(myStyle.GetSize()-4)

leg.AddEntry(position_oneStrip_StdDev_graph, "Exactly one strip reconstruction", "pl")
leg.AddEntry(position_weighted_StdDev_graph, "Effective resolution", "pl")

leg.AddEntry(position_twoStrip_graph, "Two strip reconstruction", "pl")

myStyle.BeamInfo()
text = ROOT.TLatex()
text.SetTextSize(myStyle.GetSize()-4)
text.SetTextAlign(31)
text.DrawLatexNDC(1-myStyle.GetMargin()-0.005,1-myStyle.GetMargin()+0.01,"#bf{Varying length}")

leg.Draw()
ROOT.gPad.RedrawAxis("g")

position_oneStrip_StdDev_graph.Draw("epl same")
position_weighted_StdDev_graph.Draw("epl same")

position_twoStrip_graph.Draw("epl same")

c1.SaveAs("%sresolution_vs_length_EIC.pdf"%(outdir))
