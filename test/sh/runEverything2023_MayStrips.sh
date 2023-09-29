cd ../../test

# # HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# echo "Running over HPK_W8_18_2_50T_1P0_500P_100M_C600_208V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# python FindInputHistos4YReco.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -A --xmax 0.70 --fitOrder 4
# python Plot_AmplitudeVsX.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# python Plot_AmpChargeVsXY.py        -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# python Plot_RecoDiffVsXY.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -c
# python Plot_Efficiency.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -t
# python Plot_Efficiency.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V


# # HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# echo "Running over HPK_W8_17_2_50T_1P0_500P_50M_C600_200V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# python FindInputHistos4YReco.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -A --xmax 0.71 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# python Plot_AmpChargeVsXY.py        -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# python Plot_RecoDiffVsXY.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -c
# python Plot_Efficiency.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -t
# python Plot_Efficiency.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V


# # HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# echo "Running over HPK_W4_17_2_50T_1P0_500P_50M_C240_204V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# python FindInputHistos4YReco.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -A --xmax 0.70 --fitOrder 4
# python Plot_AmplitudeVsX.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# python Plot_AmpChargeVsXY.py        -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# python Plot_RecoDiffVsXY.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -c
# python Plot_Efficiency.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -t
# python Plot_Efficiency.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V


# # HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# echo "Running over HPK_W5_17_2_50T_1P0_500P_50M_E600_190V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# python FindInputHistos4YReco.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -A --xmax 0.85 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 2.7 --ylength 170.0
# python Plot_AmplitudeVsXY.py        -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 20.0 --zmax 170.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# python Plot_AmpChargeVsXY.py        -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# python Plot_RecoDiffVsXY.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -c
# python Plot_Efficiency.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t
# python Plot_Efficiency.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V

# # Get summary for best performance sensors only
# python Plot_Summary_XRes_Time.py    -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7


# # HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# echo "Running over HPK_W2_3_2_50T_1P0_500P_50M_E240_180V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# python FindInputHistos4YReco.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -A --xmax 0.84 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# python Plot_AmpChargeVsXY.py        -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# python Plot_RecoDiffVsXY.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -c
# python Plot_Efficiency.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -t
# python Plot_Efficiency.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V

# # Get summary for best performance sensors only
# python Plot_Summary_XRes_Time.py    -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7


# # HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# echo "Running over HPK_W9_15_2_20T_1P0_500P_50M_E600_114V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# python FindInputHistos4YReco.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -A --xmax 0.85 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# python Plot_AmpChargeVsXY.py        -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# python Plot_RecoDiffVsXY.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -c
# python Plot_Efficiency.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -t
# python Plot_Efficiency.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V


# # HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# echo "Running over HPK_W9_14_2_20T_1P0_500P_100M_E600_112V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# python FindInputHistos4YReco.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -A --xmax 0.81 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# python Plot_AmpChargeVsXY.py        -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# python Plot_RecoDiffVsXY.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -c
# python Plot_Efficiency.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -t
# python Plot_Efficiency.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V


# # HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# echo "Running over HPK_W9_15_4_20T_0P5_500P_50M_E600_110V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# python FindInputHistos4YReco.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -A --xmax 0.93 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 2.7 --ylength 140.0
# python Plot_AmplitudeVsXY.py        -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 20.0 --zmax 140.0
# # python Plot_TimeDiffVsXY.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# python Plot_AmpChargeVsXY.py        -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
# python Plot_RecoDiffVsXY.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -c
# python Plot_Efficiency.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7 -y 100

# python Plot_Resolution1D.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -t
# python Plot_Efficiency.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -t -x 2.7 -y 100

# python Print_Resolution.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V


# # HPK_KOJI_50T_1P0_80P_60M_E240_190V
# echo "Running over HPK_KOJI_50T_1P0_80P_60M_E240_190V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# cd ../macros
# python FindDelayCorrections.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# python FindInputHistos4YReco.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -A --xmax 0.62 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 0.6 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 20.0 --zmax 100.0
# # python Plot_TimeDiffVsXY.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# python Plot_AmpChargeVsXY.py        -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# python Plot_RecoDiffVsXY.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_KOJI_50T_1P0_80P_60M_E240_190V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -c
# python Plot_Efficiency.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6
# python Plot_ResolutionXRecoVsX.py   -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 50
# python Plot_ResolutionTimeVsX.py    -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 100

# python Plot_Resolution1D.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -t
# python Plot_Efficiency.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -t -x 0.6
# python Plot_ResolutionXRecoVsX.py   -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -t -x 0.6 -y 50
# python Plot_ResolutionTimeVsX.py    -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -t -x 0.6 -y 100

# python Print_Resolution.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V


# # HPK_KOJI_20T_1P0_80P_60M_E240_112V
# echo "Running over HPK_KOJI_20T_1P0_80P_60M_E240_112V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
# cd ../macros
# python FindDelayCorrections.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
# python FindInputHistos4YReco.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
# cd ../macros

# python DoPositionRecoFit.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -A --xmax 0.62 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 0.6 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 20.0 --zmax 100.0
# # python Plot_TimeDiffVsXY.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 25.0 --zmax 75.0
# # python Plot_TimeDiffVsY.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 13.5 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
# python Plot_AmpChargeVsXY.py        -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
# python Plot_RecoDiffVsXY.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -c
# python Plot_Efficiency.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6
# python Plot_ResolutionXRecoVsX.py   -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 50
# python Plot_ResolutionTimeVsX.py    -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 100

# python Plot_Resolution1D.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -t
# python Plot_Efficiency.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -t -x 0.6
# python Plot_ResolutionXRecoVsX.py   -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -t -x 0.6 -y 50
# python Plot_ResolutionTimeVsX.py    -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -t -x 0.6 -y 100

# python Print_Resolution.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V



# HPK 500um Pitch sensors
# -----------------------

HPK_500P=('HPK_W8_18_2_50T_1P0_500P_100M_C600_208V' 'HPK_W8_17_2_50T_1P0_500P_50M_C600_200V' 'HPK_W4_17_2_50T_1P0_500P_50M_C240_204V' 'HPK_W5_17_2_50T_1P0_500P_50M_E600_190V' 'HPK_W2_3_2_50T_1P0_500P_50M_E240_180V' 'HPK_W9_15_2_20T_1P0_500P_50M_E600_114V' 'HPK_W9_14_2_20T_1P0_500P_100M_E600_112V' 'HPK_W9_15_4_20T_0P5_500P_50M_E600_110V')

for sensor in "${HPK_500P[@]}"; do
    echo "Running over ${sensor} sensor"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindInputHistos4YReco.py -D ${sensor} -I
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python Plot_AmplitudeVsX.py         -D ${sensor} --xlength 1.9 --ylength 170.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} --zmin 20.0 --zmax 170.0
    python Plot_SimpleXYMaps.py         -D ${sensor}
    python Plot_AmpChargeVsXY.py        -D ${sensor}
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 1.9
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 1.9
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 1.9 -y 100

    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 1.9
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 1.9
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 1.9 -y 100

    # python Print_Resolution.py          -D ${sensor}
done

cd ../macros
# DoPositionRecoFit
python DoPositionRecoFit.py     -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V  -A --xmax 0.70 --fitOrder 4
python DoPositionRecoFit.py     -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V   -A --xmax 0.71 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V   -A --xmax 0.70 --fitOrder 4
python DoPositionRecoFit.py     -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V   -A --xmax 0.85 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V    -A --xmax 0.84 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V   -A --xmax 0.85 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V  -A --xmax 0.81 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V   -A --xmax 0.93 --fitOrder 5

# Resolution summary
python Plot_Summary_XRes_Time.py    -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V   -x 1.9
python Plot_Summary_XRes_Time.py    -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V    -x 1.9


# HPK narrow pitch sensors
# ------------------------

HPK_80P=('HPK_KOJI_50T_1P0_80P_60M_E240_190V' 'HPK_KOJI_20T_1P0_80P_60M_E240_112V')

for sensor in "${HPK_80P[@]}"; do
    echo "Running over ${sensor} sensor"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindInputHistos4YReco.py -D ${sensor} -I
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python DoPositionRecoFit.py         -D ${sensor} -A --xmax 0.62 --fitOrder 5
    python Plot_AmplitudeVsX.py         -D ${sensor} --xlength 0.6 --ylength 100.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} --zmin 20.0 --zmax 100.0
    python Plot_SimpleXYMaps.py         -D ${sensor}
    python Plot_AmpChargeVsXY.py        -D ${sensor}
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 0.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.6 -y 50
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.6 -y 100

    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 0.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.6 -y 50
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.6 -y 100

    # python Print_Resolution.py          -D ${sensor}
done

# Print resolution values at the end
for sensor in "${HPK_500P[@]}"; do
    python Print_Resolution.py          -D ${sensor}
done

for sensor in "${HPK_80P[@]}"; do
    python Print_Resolution.py          -D ${sensor}
done
