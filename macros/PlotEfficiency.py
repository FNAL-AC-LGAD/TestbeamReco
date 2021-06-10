from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors,TLegend,gROOT
import os
import EfficiencyUtils

gROOT.SetBatch( True )


#inputfile = TFile("/afs/cern.ch/work/s/sixie/public/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.20210412.root")
inputfile = TFile("/uscms/home/amolnar/work/TestbeamReco/test/myoutputfile.root")    


efficiency_lowThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator")
efficiency_highThreshold_numerator_global = inputfile.Get("efficiency_vs_xy_highThreshold_numerator")
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_global, efficiency_denominator_global, "efficiency_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_global, efficiency_denominator_global, "efficiency_highThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.


efficiency_lowThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel00")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel01")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Strip 1", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel02 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel02")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel02, efficiency_denominator_global, "efficiency_channel02", "Efficiency Strip 2", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel03 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel03")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel03, efficiency_denominator_global, "efficiency_channel03", "Efficiency Strip 3", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel04 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel04")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel04, efficiency_denominator_global, "efficiency_channel04", "Efficiency Strip 4", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_lowThreshold_numerator_channel05 = inputfile.Get("efficiency_vs_xy_lowThreshold_numerator_channel05")
EfficiencyUtils.Plot2DEfficiency( efficiency_lowThreshold_numerator_channel05, efficiency_denominator_global, "efficiency_channel05", "Efficiency Strip 5", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel00 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel00")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel01 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel01")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Strip 1", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel02 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel02")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel02, efficiency_denominator_global, "efficiency_channel02", "Efficiency Strip 2", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel03 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel03")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel03, efficiency_denominator_global, "efficiency_channel03", "Efficiency Strip 3", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel04 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel04")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel04, efficiency_denominator_global, "efficiency_channel04", "Efficiency Strip 4", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_highThreshold_numerator_channel05 = inputfile.Get("efficiency_vs_xy_highThreshold_numerator_channel05")
EfficiencyUtils.Plot2DEfficiency( efficiency_highThreshold_numerator_channel05, efficiency_denominator_global, "efficiency_channel05", "Efficiency Strip 5", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )



#1D efficiency vs X
binY_lowEdge = efficiency_denominator_global.GetYaxis().FindFixBin(10.0)
binY_highEdge = efficiency_denominator_global.GetYaxis().FindFixBin(11.4)

efficiency_vs_x_denominator_global = efficiency_denominator_global.ProjectionX("efficiency_vs_x_denominator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_global = efficiency_lowThreshold_numerator_global.ProjectionX("efficiency_vs_x_lowThreshold_numerator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel00 = efficiency_lowThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel00",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel01 = efficiency_lowThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel01",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel02 = efficiency_lowThreshold_numerator_channel02.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel02",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel03 = efficiency_lowThreshold_numerator_channel03.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel03",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel04 = efficiency_lowThreshold_numerator_channel04.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel04",binY_lowEdge,binY_highEdge)
efficiency_vs_x_lowThreshold_numerator_channel05 = efficiency_lowThreshold_numerator_channel05.ProjectionX("efficiency_vs_x_lowThreshold_numerator_channel05",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_global = efficiency_highThreshold_numerator_global.ProjectionX("efficiency_vs_x_highThreshold_numerator_global",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel00 = efficiency_highThreshold_numerator_channel00.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel00",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel01 = efficiency_highThreshold_numerator_channel01.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel01",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel02 = efficiency_highThreshold_numerator_channel02.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel02",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel03 = efficiency_highThreshold_numerator_channel03.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel03",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel04 = efficiency_highThreshold_numerator_channel04.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel04",binY_lowEdge,binY_highEdge)
efficiency_vs_x_highThreshold_numerator_channel05 = efficiency_highThreshold_numerator_channel05.ProjectionX("efficiency_vs_x_highThreshold_numerator_channel05",binY_lowEdge,binY_highEdge)


efficiency_vs_x_lowThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel01", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel02 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel02, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel02", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel03 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel03, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel03", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel04 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel04, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel04", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_lowThreshold_channel05 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_lowThreshold_numerator_channel05, efficiency_vs_x_denominator_global, "efficiency_vs_x_lowThreshold_channel05", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)

efficiency_vs_x_highThreshold_global = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_global, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_global", "Efficiency Global", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel00 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel00, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel01 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel01, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel01", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel02 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel02, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel02", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel03 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel03, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel03", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel04 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel04, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel04", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)
efficiency_vs_x_highThreshold_channel05 = EfficiencyUtils.Make1DEfficiency(efficiency_vs_x_highThreshold_numerator_channel05, efficiency_vs_x_denominator_global, "efficiency_vs_x_highThreshold_channel05", "Efficiency Strip 0", "X [mm]", -0.5, 1.5)





canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
efficiency_vs_x_lowThreshold_global.Draw("ALP")
efficiency_vs_x_lowThreshold_channel00.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel01.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel02.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel03.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel04.Draw("LPsame")
efficiency_vs_x_lowThreshold_channel05.Draw("LPsame")

efficiency_vs_x_lowThreshold_global.GetXaxis().SetRangeUser(-0.2,1.0)
efficiency_vs_x_lowThreshold_global.GetYaxis().SetRangeUser(0.0,1.5)
efficiency_vs_x_lowThreshold_global.GetYaxis().SetTitle("Efficiency @ 10mV Threshold")


efficiency_vs_x_lowThreshold_global.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel00.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel01.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel02.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel03.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel04.SetLineWidth(2)
efficiency_vs_x_lowThreshold_channel05.SetLineWidth(2)

efficiency_vs_x_lowThreshold_global.SetLineColor(1)
efficiency_vs_x_lowThreshold_channel00.SetLineColor(416+2) #kGreen+2
efficiency_vs_x_lowThreshold_channel01.SetLineColor(432+2) #kCyan+2
efficiency_vs_x_lowThreshold_channel02.SetLineColor(600) #kBlue
efficiency_vs_x_lowThreshold_channel03.SetLineColor(880) #kViolet
efficiency_vs_x_lowThreshold_channel04.SetLineColor(632) #kRed
efficiency_vs_x_lowThreshold_channel05.SetLineColor(400+2) #kYellow+2

legend = TLegend(0.4,0.65,0.7,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(efficiency_vs_x_lowThreshold_global, "Any Strip")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel00, "Strip 1")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel01, "Strip 2")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel02, "Strip 3")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel03, "Strip 4")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel04, "Strip 5")
legend.AddEntry(efficiency_vs_x_lowThreshold_channel05, "Strip 6")
legend.Draw();

canvas.SaveAs("Efficiency_LowThreshold_vs_x.gif")





canvas = TCanvas("cv","cv",800,800)
canvas.SetLeftMargin(0.12)
efficiency_vs_x_highThreshold_global.Draw("ALP")
efficiency_vs_x_highThreshold_channel00.Draw("LPsame")
efficiency_vs_x_highThreshold_channel01.Draw("LPsame")
efficiency_vs_x_highThreshold_channel02.Draw("LPsame")
efficiency_vs_x_highThreshold_channel03.Draw("LPsame")
efficiency_vs_x_highThreshold_channel04.Draw("LPsame")
efficiency_vs_x_highThreshold_channel05.Draw("LPsame")

efficiency_vs_x_highThreshold_global.GetXaxis().SetRangeUser(-0.2,1.0)
efficiency_vs_x_highThreshold_global.GetYaxis().SetRangeUser(0.0,1.5)
efficiency_vs_x_highThreshold_global.GetYaxis().SetTitle("Efficiency @ 30mV Threshold")


efficiency_vs_x_highThreshold_global.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel00.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel01.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel02.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel03.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel04.SetLineWidth(2)
efficiency_vs_x_highThreshold_channel05.SetLineWidth(2)

efficiency_vs_x_highThreshold_global.SetLineColor(1)
efficiency_vs_x_highThreshold_channel00.SetLineColor(416+2) #kGreen+2
efficiency_vs_x_highThreshold_channel01.SetLineColor(432+2) #kCyan+2
efficiency_vs_x_highThreshold_channel02.SetLineColor(600) #kBlue
efficiency_vs_x_highThreshold_channel03.SetLineColor(880) #kViolet
efficiency_vs_x_highThreshold_channel04.SetLineColor(632) #kRed
efficiency_vs_x_highThreshold_channel05.SetLineColor(400+2) #kYellow+2

legend = TLegend(0.4,0.65,0.7,0.88);
legend.SetBorderSize(0)
legend.SetTextSize(0.04)
legend.AddEntry(efficiency_vs_x_highThreshold_global, "Any Strip")
legend.AddEntry(efficiency_vs_x_highThreshold_channel00, "Strip 1")
legend.AddEntry(efficiency_vs_x_highThreshold_channel01, "Strip 2")
legend.AddEntry(efficiency_vs_x_highThreshold_channel02, "Strip 3")
legend.AddEntry(efficiency_vs_x_highThreshold_channel03, "Strip 4")
legend.AddEntry(efficiency_vs_x_highThreshold_channel04, "Strip 5")
legend.AddEntry(efficiency_vs_x_highThreshold_channel05, "Strip 6")
legend.Draw();

canvas.SaveAs("Efficiency_HighThreshold_vs_x.gif")



# Save efficiency plots
outputfile = TFile("EfficiencyPlots.root","RECREATE")
efficiency_vs_x_lowThreshold_global.Write("efficiency_vs_x_lowThreshold_global")
efficiency_vs_x_lowThreshold_channel00.Write("efficiency_vs_x_lowThreshold_channel00")
efficiency_vs_x_lowThreshold_channel01.Write("efficiency_vs_x_lowThreshold_channel01")
efficiency_vs_x_lowThreshold_channel02.Write("efficiency_vs_x_lowThreshold_channel02")
efficiency_vs_x_lowThreshold_channel03.Write("efficiency_vs_x_lowThreshold_channel03")
efficiency_vs_x_lowThreshold_channel04.Write("efficiency_vs_x_lowThreshold_channel04")
efficiency_vs_x_lowThreshold_channel05.Write("efficiency_vs_x_lowThreshold_channel05")
efficiency_vs_x_highThreshold_global.Write("efficiency_vs_x_highThreshold_global")
efficiency_vs_x_highThreshold_channel00.Write("efficiency_vs_x_highThreshold_channel00")
efficiency_vs_x_highThreshold_channel01.Write("efficiency_vs_x_highThreshold_channel01")
efficiency_vs_x_highThreshold_channel02.Write("efficiency_vs_x_highThreshold_channel02")
efficiency_vs_x_highThreshold_channel03.Write("efficiency_vs_x_highThreshold_channel03")
efficiency_vs_x_highThreshold_channel04.Write("efficiency_vs_x_highThreshold_channel04")
efficiency_vs_x_highThreshold_channel05.Write("efficiency_vs_x_highThreshold_channel05")
outputfile.Close()


