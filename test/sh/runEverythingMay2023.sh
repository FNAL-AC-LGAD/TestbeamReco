cd ../../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# ##./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# ##./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

# cd ../macros
# ##python FindStripCenters.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# ##python FindStripCenters.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# ##python FindStripCenters.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# ##python FindStripCenters.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# ##python FindStripCenters.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# ##python FindStripCenters.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# ##python FindStripCenters.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# ##python FindStripCenters.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# ##python FindStripCenters.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V


# python FindDelayCorrections.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# python FindDelayCorrections.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# python FindDelayCorrections.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# python FindDelayCorrections.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# python FindDelayCorrections.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# python FindDelayCorrections.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# python FindDelayCorrections.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# #python FindDelayCorrections.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# #python FindDelayCorrections.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V


# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
# ./MyAnalysis -A Analyze -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
# ./MyAnalysis -A Analyze -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
# ./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
# ./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
# ./MyAnalysis -A Analyze -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
# ./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
# ./MyAnalysis -A Analyze -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
# ./MyAnalysis -A Analyze -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

# cd ../macros
# python PlotAmplitudeVsXY.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 15.0 --zmax 80.0
# python PlotAmplitudeVsXY.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 15.0 --zmax 80.0
# python PlotAmplitudeVsXY.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 15.0 --zmax 80.0
# python PlotAmplitudeVsXY.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 15.0 --zmax 120.0
# python PlotAmplitudeVsXY.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 7.0 --zmax 60.0
# python PlotAmplitudeVsXY.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 15.0 --zmax 120.0
# python PlotAmplitudeVsXY.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 7.0 --zmax 60.0
# python PlotAmplitudeVsXY.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 15.0 --zmax 80.0
# python PlotAmplitudeVsXY.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 7.0 --zmax 60.0

# cd ../test


## HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
echo "Running over HPK_W2_3_2_50T_1P0_500P_50M_E240_180V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
cd ../macros
python FindDelayCorrections.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python FindInputHistos4YReco.py -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -A --xmax 0.84 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python PlotAmpChargeVsXY.py         -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python PlotRecoDiffVsXY.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7
python plot1DRes.py                 -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python PlotRecoDiffVsY.py           -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V

# Paper plots
python Paper_1DRes.py               -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
python Paper_Efficiency.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7
python Paper_XRes.py                -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -t
python Paper_Efficiency.py          -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7 -t
python Paper_XRes.py                -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V -x 2.7 -y 100 -t


## HPK_KOJI_50T_1P0_80P_60M_E240_190V
echo "Running over HPK_KOJI_50T_1P0_80P_60M_E240_190V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
cd ../macros
python FindDelayCorrections.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
python FindInputHistos4YReco.py -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
cd ../macros

python DoPositionRecoFit.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -A --xmax 0.62 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 0.6 --ylength 100.0
python PlotAmplitudeVsXY.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 20.0 --zmax 100.0
python PlotTimeDiffVsX.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 0.6 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
python PlotAmpChargeVsXY.py         -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
python PlotRecoDiffVsXY.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 0.6 --ylength 100.0
python PlotEfficiency.py            -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6
python plot1DRes.py                 -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
python PlotRecoDiffVsY.py           -D HPK_KOJI_50T_1P0_80P_60M_E240_190V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_KOJI_50T_1P0_80P_60M_E240_190V

# Paper plots
python Paper_1DRes.py               -D HPK_KOJI_50T_1P0_80P_60M_E240_190V
python Paper_Efficiency.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6
python Paper_XRes.py                -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 50
python Paper_PlotTimeDiffVsX.py     -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 100

python Paper_1DRes.py               -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -t
python Paper_Efficiency.py          -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -t
python Paper_XRes.py                -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 50 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_KOJI_50T_1P0_80P_60M_E240_190V -x 0.6 -y 100 -t


## HPK_KOJI_20T_1P0_80P_60M_E240_112V
echo "Running over HPK_KOJI_20T_1P0_80P_60M_E240_112V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
cd ../macros
python FindDelayCorrections.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
python FindInputHistos4YReco.py -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
cd ../macros

python DoPositionRecoFit.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -A --xmax 0.62 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 0.6 --ylength 100.0
python PlotAmplitudeVsXY.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 20.0 --zmax 100.0
python PlotTimeDiffVsX.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 0.6 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
python PlotAmpChargeVsXY.py         -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
python PlotRecoDiffVsXY.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 0.6 --ylength 100.0
python PlotEfficiency.py            -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6
python plot1DRes.py                 -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
python PlotRecoDiffVsY.py           -D HPK_KOJI_20T_1P0_80P_60M_E240_112V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_KOJI_20T_1P0_80P_60M_E240_112V

# Paper plots
python Paper_1DRes.py               -D HPK_KOJI_20T_1P0_80P_60M_E240_112V
python Paper_Efficiency.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6
python Paper_XRes.py                -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 50
python Paper_PlotTimeDiffVsX.py     -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 100

python Paper_1DRes.py               -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -t
python Paper_Efficiency.py          -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -t
python Paper_XRes.py                -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 50 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_KOJI_20T_1P0_80P_60M_E240_112V -x 0.6 -y 100 -t
