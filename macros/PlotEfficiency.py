from ROOT import TFile,TTree,TCanvas,TH1F,TH2F,TLatex,TMath,TEfficiency,TGraphAsymmErrors
import os
import EfficiencyUtils



inputfile = TFile("/uscms/home/sxie/work/releases/testbeam/CMSSW_11_2_0_pre5/src/TestbeamReco/test/BNL2020_220V.root")

efficiency_numerator_global = inputfile.Get("efficiency_vs_xy_numerator")
efficiency_denominator_global = inputfile.Get("efficiency_vs_xy_denominator")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_global, efficiency_denominator_global, "efficiency_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_global, efficiency_denominator_global, "efficiency_global", "Efficiency Global", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )
#For some reason the first time I call this function, the z-axis is not plotted in the right place. 
#So I call it twice.


efficiency_numerator_channel00 = inputfile.Get("efficiency_vs_xy_numerator_channel00")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel00, efficiency_denominator_global, "efficiency_channel00", "Efficiency Strip 0", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_numerator_channel01 = inputfile.Get("efficiency_vs_xy_numerator_channel01")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel01, efficiency_denominator_global, "efficiency_channel01", "Efficiency Strip 1", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_numerator_channel02 = inputfile.Get("efficiency_vs_xy_numerator_channel02")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel02, efficiency_denominator_global, "efficiency_channel02", "Efficiency Strip 2", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_numerator_channel03 = inputfile.Get("efficiency_vs_xy_numerator_channel03")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel03, efficiency_denominator_global, "efficiency_channel03", "Efficiency Strip 3", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_numerator_channel04 = inputfile.Get("efficiency_vs_xy_numerator_channel04")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel04, efficiency_denominator_global, "efficiency_channel04", "Efficiency Strip 4", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

efficiency_numerator_channel05 = inputfile.Get("efficiency_vs_xy_numerator_channel05")
EfficiencyUtils.Plot2DEfficiency( efficiency_numerator_channel05, efficiency_denominator_global, "efficiency_channel05", "Efficiency Strip 5", "X [mm]", -0.5, 1.5, "Y [mm]" , 9.5, 12.0 , 0.0, 1.0 )

