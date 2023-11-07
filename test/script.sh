HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
HPK_KOJI_50T_1P0_80P_60M_E240_190V
HPK_KOJI_20T_1P0_80P_60M_E240_112V
BNL_50um_1cm_400um_W3051_1_4_160V
BNL_50um_1cm_450um_W3051_2_2_170V

./MyAnalysis -A InitialAnalyzer -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/FindStripCenters.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/FindDelayCorrections.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/DoPositionRecoFit.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -A --xmax 0.85 --fitOrder 5
python ../macros/Paper_XRes.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/Plot_AmplitudeVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -d true -t true
python ../macros/PlotChargeVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V 
python ../macros/PlotRisetimeVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V 
python ../macros/FitOverallJitter.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotJitterVsXY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotJitterVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotTimeDiffVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --ylength 100.0 -d True
python ../macros/BothTR_and_Jitter_vsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotJitterVsY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotTRvsY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/BothTR_and_Jitter_vsY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotAmpVsdT.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotAmpVsRes.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/PlotAmplitudeVsXY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 20.0 --zmax 150.0
python ../macros/PlotTimeDiffVsY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 0.8 --ylength 150.0


python ../macros/Plot_AmplitudeVsX.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D BNL_50um_1cm_400um_W3051_1_4_160V -d true -t true
python ../macros/Plot_AmplitudeVsX.py -D BNL_50um_1cm_450um_W3051_2_2_170V -d true -t true
