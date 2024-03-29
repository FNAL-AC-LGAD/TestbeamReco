from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT
import os
import EfficiencyUtils
from stripBox import getStripBox

gROOT.SetBatch( True )


#inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.20210412.root")
#inputfile = TFile("/uscms/home/amolnar/work/TestbeamReco/test/myoutputfile.root")    
inputfile = TFile("../test/myoutputfile.root")    


efficiency_lowThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator")
efficiency_highThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_highThreshold_numerator")
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, "efficiency_highThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.


efficiency_lowThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel00")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Pad 00", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel01")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Pad 01", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel10 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel10")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel10, efficiency_denominator_global, "efficiency_channel10", "Efficiency Pad 10", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel11 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel11")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel11, efficiency_denominator_global, "efficiency_channel11", "Efficiency Pad 11", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel00")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Pad 00", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel01")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Pad 01", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel10 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel10")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel10, efficiency_denominator_global, "efficiency_channel10", "Efficiency Pad 10", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel11 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel11")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel11, efficiency_denominator_global, "efficiency_channel11", "Efficiency Pad 11", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )



#1D efficiency vs X
binY_lowEdge = efficiency_denominator_global.GetYaxis().FindFixBin(10.0)
binY_highEdge = efficiency_denominator_global.GetYaxis().FindFixBin(11.4)

efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_global = efficiency_lowThreshold_numerator_global.ProjectionX("efficiency_vs_x_lowThreshold_numerator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel00 = efficiency_lowThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel00",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel01 = efficiency_lowThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel01",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel10 = efficiency_lowThreshold_numerator_channel10.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel10",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel11 = efficiency_lowThreshold_numerator_channel11.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel11",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_global = efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel00 = efficiency_highThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel00",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel01 = efficiency_highThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel01",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel10 = efficiency_highThreshold_numerator_channel10.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel10",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel11 = efficiency_highThreshold_numerator_channel11.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel11",binY_lowEdge,binY_highEdge)


efficiency_vs_x_lowThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel00", "Efficiency Pad 00", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel01", "Efficiency Pad 01", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel10 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel10, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel10", "Efficiency Pad 10", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel11 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel11, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel11", "Efficiency Pad 11", "X [mm]", -0.5, 1.5)

efficiency_vs_x_highThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel00", "Efficiency Pad 00", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel01", "Efficiency Pad 01", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel10 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel10, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel10", "Efficiency Pad 10", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel11 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel11, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel11", "Efficiency Pad 11", "X [mm]", -0.5, 1.5)



canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
efficiency_vs_x_lowThreshold_global.Draw("ALP")
efficiency_vs_x_lowThreshold_channel00.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel01.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel10.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel11.Draw("LPsame")

efficiency_vs_x_lowThreshold_global.GetXaxis().SetRangeUser(-0.2,1.0)
efficiency_vs_x_lowThreshold_global.GetYaxis().SetRangeUser(0.0,1.5)
efficiency_vs_x_lowThreshold_global.GetYaxis().SetTitle("Efficiency @ 10mV Threshold")


efficiency_vs_x_lowThreshold_global.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel00.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel01.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel10.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel11.SetLineWidth(2)

efficiency_vs_x_lowThreshold_global.SetLineColor(1)
efficiency_vs_x_lowThreshold_channel00.SetLineColor(416+2) #kGreen+2
efficiency_vs_x_lowThreshold_channel01.SetLineColor(432+2) #kCyan+2
efficiency_vs_x_lowThreshold_channel10.SetLineColor(600) #kBlue
efficiency_vs_x_lowThreshold_channel11.SetLineColor(880) #kViolet

legend = TLegend(0.4,0.65,0.7,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(efficiency_vs_x_lowThreshold_global, "Any Pad")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel00, "Pad 00")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel01, "Pad 01")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel10, "Pad 10")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel11, "Pad 11")
legend.Draw();

efficiency_vs_x_lowThreshold_global.Draw("LP same")
canvas.SaveAs("Efficiency_LowThreshold_vs_x.gif")





canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
efficiency_vs_x_highThreshold_global.Draw("ALP")


#ymin = efficiency_vs_x_highThreshold_global.GetMinimum()
#ymax = efficiency_vs_x_highThreshold_global.GetMaximum()
boxes = getStripBox(inputfile,0.0,1.0,False,18,False)
for box in boxes:
    box.Draw()

efficiency_vs_x_highThreshold_channel00.Draw("LPsame")
efficiency_vs_x_highThreshold_channel01.Draw("LPsame")
efficiency_vs_x_highThreshold_channel10.Draw("LPsame")
efficiency_vs_x_highThreshold_channel11.Draw("LPsame")

efficiency_vs_x_highThreshold_global.GetXaxis().SetRangeUser(-0.2,1.0)
efficiency_vs_x_highThreshold_global.GetYaxis().SetRangeUser(0.0,1.5)
efficiency_vs_x_highThreshold_global.GetYaxis().SetTitle("Efficiency @ 30mV Threshold")


efficiency_vs_x_highThreshold_global.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel00.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel01.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel10.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel11.SetLineWidth(2)

efficiency_vs_x_highThreshold_global.SetLineColor(1)
efficiency_vs_x_highThreshold_channel00.SetLineColor(416+2) #kGreen+2
efficiency_vs_x_highThreshold_channel01.SetLineColor(432+2) #kCyan+2
efficiency_vs_x_highThreshold_channel10.SetLineColor(600) #kBlue
efficiency_vs_x_highThreshold_channel11.SetLineColor(880) #kViolet

legend = TLegend(0.4,0.65,0.7,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(efficiency_vs_x_highThreshold_global, "Any Pad")
legend.AddEntry(efficiency_vs_x_highThreshold_channel00, "Pad 00")
legend.AddEntry(efficiency_vs_x_highThreshold_channel01, "Pad 01")
legend.AddEntry(efficiency_vs_x_highThreshold_channel10, "Pad 10")
legend.AddEntry(efficiency_vs_x_highThreshold_channel11, "Pad 11")
legend.Draw();

efficiency_vs_x_highThreshold_global.Draw("LP same")
canvas.SaveAs("Efficiency_HighThreshold_vs_x.gif")



# Save efficiency plots
outputfile = TFile("EfficiencyPlots.root","RECREATE")
efficiency_vs_x_lowThreshold_global.Write("efficiency_vs_x_lowThreshold_global")
efficiency_vs_x_lowThreshold_channel00.Write("efficiency_vs_x_lowThreshold_channel00")
efficiency_vs_x_lowThreshold_channel01.Write("efficiency_vs_x_lowThreshold_channel01")
efficiency_vs_x_lowThreshold_channel10.Write("efficiency_vs_x_lowThreshold_channel10")
efficiency_vs_x_lowThreshold_channel11.Write("efficiency_vs_x_lowThreshold_channel11")
efficiency_vs_x_highThreshold_global.Write("efficiency_vs_x_highThreshold_global")
efficiency_vs_x_highThreshold_channel00.Write("efficiency_vs_x_highThreshold_channel00")
efficiency_vs_x_highThreshold_channel01.Write("efficiency_vs_x_highThreshold_channel01")
efficiency_vs_x_highThreshold_channel10.Write("efficiency_vs_x_highThreshold_channel10")
efficiency_vs_x_highThreshold_channel11.Write("efficiency_vs_x_highThreshold_channel11")
outputfile.Close()


