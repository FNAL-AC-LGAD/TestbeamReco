cd ../../test

# HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
echo "Running over HPK_W8_18_2_50T_1P0_500P_100M_C600_208V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
cd ../macros
python FindDelayCorrections.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python FindInputHistos4YReco.py -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -A --xmax 0.70 --fitOrder 4
python PlotAmplitudeVsX.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python PlotAmpChargeVsXY.py         -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python PlotRecoDiffVsXY.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7
python plot1DRes.py                 -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python PlotRecoDiffVsY.py           -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V

# Paper plots
python Paper_1DRes.py               -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V
python Paper_Efficiency.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7
python Paper_XRes.py                -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -t
python Paper_Efficiency.py          -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7 -t
python Paper_XRes.py                -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V -x 2.7 -y 100 -t


# HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
echo "Running over HPK_W8_17_2_50T_1P0_500P_50M_C600_200V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
cd ../macros
python FindDelayCorrections.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python FindInputHistos4YReco.py -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -A --xmax 0.71 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python PlotAmpChargeVsXY.py         -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python PlotRecoDiffVsXY.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7
python plot1DRes.py                 -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python PlotRecoDiffVsY.py           -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V

# Paper plots
python Paper_1DRes.py               -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V
python Paper_Efficiency.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7
python Paper_XRes.py                -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -t
python Paper_Efficiency.py          -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7 -t
python Paper_XRes.py                -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V -x 2.7 -y 100 -t


# HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
echo "Running over HPK_W4_17_2_50T_1P0_500P_50M_C240_204V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
cd ../macros
python FindDelayCorrections.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python FindInputHistos4YReco.py -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -A --xmax 0.70 --fitOrder 4
python PlotAmplitudeVsX.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python PlotAmpChargeVsXY.py         -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python PlotRecoDiffVsXY.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7
python plot1DRes.py                 -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python PlotRecoDiffVsY.py           -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V

# Paper plots
python Paper_1DRes.py               -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V
python Paper_Efficiency.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7
python Paper_XRes.py                -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -t
python Paper_Efficiency.py          -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7 -t
python Paper_XRes.py                -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V -x 2.7 -y 100 -t


# HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
echo "Running over HPK_W5_17_2_50T_1P0_500P_50M_E600_190V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
cd ../macros
python FindDelayCorrections.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python FindInputHistos4YReco.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -A --xmax 0.85 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 2.7 --ylength 170.0
python PlotAmplitudeVsXY.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 20.0 --zmax 170.0
python PlotTimeDiffVsX.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python PlotAmpChargeVsXY.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python PlotRecoDiffVsXY.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7
python plot1DRes.py                 -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python PlotRecoDiffVsY.py           -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V

# Paper plots
python Paper_1DRes.py               -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python Paper_Efficiency.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7
python Paper_XRes.py                -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t
python Paper_Efficiency.py          -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7 -t
python Paper_XRes.py                -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -x 2.7 -y 100 -t


# HPK_W2_3_2_50T_1P0_500P_50M_E240_180V
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


# HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
echo "Running over HPK_W9_15_2_20T_1P0_500P_50M_E600_114V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
cd ../macros
python FindDelayCorrections.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python FindInputHistos4YReco.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -A --xmax 0.85 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python PlotAmpChargeVsXY.py         -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python PlotRecoDiffVsXY.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7
python plot1DRes.py                 -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python PlotRecoDiffVsY.py           -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V

# Paper plots
python Paper_1DRes.py               -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python Paper_Efficiency.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7
python Paper_XRes.py                -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -t
python Paper_Efficiency.py          -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7 -t
python Paper_XRes.py                -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V -x 2.7 -y 100 -t


# HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
echo "Running over HPK_W9_14_2_20T_1P0_500P_100M_E600_112V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
cd ../macros
python FindDelayCorrections.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python FindInputHistos4YReco.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python PlotAmpChargeVsXY.py         -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python PlotRecoDiffVsXY.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7
python plot1DRes.py                 -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python PlotRecoDiffVsY.py           -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V

# Paper plots
python Paper_1DRes.py               -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python Paper_Efficiency.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7
python Paper_XRes.py                -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -t
python Paper_Efficiency.py          -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7 -t
python Paper_XRes.py                -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V -x 2.7 -y 100 -t


# HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
echo "Running over HPK_W9_15_4_20T_0P5_500P_50M_E600_110V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
cd ../macros
python FindDelayCorrections.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python FindInputHistos4YReco.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
cd ../macros

python DoPositionRecoFit.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -A --xmax 0.93 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 2.7 --ylength 140.0
python PlotAmplitudeVsXY.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 20.0 --zmax 140.0
python PlotTimeDiffVsX.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 2.7 --ylength 100.0
python PlotTimeDiffVsXY.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 13.5 --ylength 100.0
python PlotTimeMeanVsXY.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python PlotAmpChargeVsXY.py         -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python PlotRecoDiffVsXY.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 2.7 --ylength 150.0
python PlotEfficiency.py            -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7
python plot1DRes.py                 -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python PlotRecoDiffVsY.py           -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V --xlength 13.5 --ylength 4.0
python PlotCutFlow.py               -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V

# Paper plots
python Paper_1DRes.py               -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python Paper_Efficiency.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7
python Paper_XRes.py                -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7 -y 100

python Paper_1DRes.py               -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -t
python Paper_Efficiency.py          -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7 -t
python Paper_XRes.py                -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7 -t
python Paper_PlotTimeDiffVsX.py     -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V -x 2.7 -y 100 -t



# HPK_KOJI_50T_1P0_80P_60M_E240_190V
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


# HPK_KOJI_20T_1P0_80P_60M_E240_112V
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

