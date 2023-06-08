cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
./MyAnalysis -A InitialAnalyzer -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
./MyAnalysis -A InitialAnalyzer -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
./MyAnalysis -A InitialAnalyzer -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
./MyAnalysis -A InitialAnalyzer -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
./MyAnalysis -A InitialAnalyzer -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
##./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
##./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

cd ../macros
##python FindStripCenters.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
##python FindStripCenters.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
##python FindStripCenters.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
##python FindStripCenters.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
##python FindStripCenters.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
##python FindStripCenters.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
##python FindStripCenters.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
##python FindStripCenters.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
##python FindStripCenters.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V


python FindDelayCorrections.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python FindDelayCorrections.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python FindDelayCorrections.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python FindDelayCorrections.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python FindDelayCorrections.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python FindDelayCorrections.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python FindDelayCorrections.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
#python FindDelayCorrections.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
#python FindDelayCorrections.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V


cd ../test
./MyAnalysis -A Analyze -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
./MyAnalysis -A Analyze -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
./MyAnalysis -A Analyze -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
./MyAnalysis -A Analyze -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
./MyAnalysis -A Analyze -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
./MyAnalysis -A Analyze -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

cd ../macros
python PlotAmplitudeVsXY.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 15.0 --zmax 80.0
python PlotAmplitudeVsXY.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 15.0 --zmax 80.0
python PlotAmplitudeVsXY.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 15.0 --zmax 80.0
python PlotAmplitudeVsXY.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 15.0 --zmax 120.0
python PlotAmplitudeVsXY.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 7.0 --zmax 60.0
python PlotAmplitudeVsXY.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 15.0 --zmax 120.0
python PlotAmplitudeVsXY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 7.0 --zmax 60.0
python PlotAmplitudeVsXY.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 15.0 --zmax 80.0
python PlotAmplitudeVsXY.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 7.0 --zmax 60.0

cd ../test
