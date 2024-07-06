cd ../../test

# HPK 500um Pitch sensors
# -----------------------

# HPK_500P=("HPK_W9_15_4_20T_0P5_500P_50M_E600_110V")
HPK_500P=("HPK_W9_15_2_20T_1P0_500P_50M_E600_114V" "HPK_W4_17_2_50T_1P0_500P_50M_C240_204V" "HPK_W8_17_2_50T_1P0_500P_50M_C600_200V" "HPK_W2_3_2_50T_1P0_500P_50M_E240_180V" "HPK_W5_17_2_50T_1P0_500P_50M_E600_190V" "HPK_W9_14_2_20T_1P0_500P_100M_E600_112V" "HPK_W8_18_2_50T_1P0_500P_100M_C600_208V")

for sensor in "${HPK_500P[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindInputHistos4YReco.py -D ${sensor} -I
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python Plot_SimpleXYMaps.py         -D ${sensor}
    python Plot_AmpChargeVsXY.py        -D ${sensor}
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_RisetimeVsX.py          -D ${sensor} -x 1.9
    python Plot_JitterVsX.py            -D ${sensor} -x 1.9
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 1.9 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 1.9
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 1.9
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 1.9 -y 100

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 1.9
    python Plot_JitterVsX.py            -D ${sensor} -t -x 1.9
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 1.9 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 1.9
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 1.9
    python Plot_ResolutionCombinedPosMethod1.py   -D ${sensor} -t -x 1.9
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 1.9 -y 100
done

cd ../macros
# DoPositionRecoFit
# python DoPositionRecoFit.py     -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V   --xmax 0.93 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V   --xmax 0.85 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W4_17_2_50T_1P0_500P_50M_C240_204V   --xmax 0.69 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W8_17_2_50T_1P0_500P_50M_C600_200V   --xmax 0.71 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W2_3_2_50T_1P0_500P_50M_E240_180V    --xmax 0.84 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V   --xmax 0.85 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V  --xmax 0.85 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W8_18_2_50T_1P0_500P_100M_C600_208V  --xmax 0.71 --fitOrder 5


# HPK narrow pitch sensors
# ------------------------

HPK_80P=("HPK_KOJI_20T_1P0_80P_60M_E240_112V" "HPK_KOJI_50T_1P0_80P_60M_E240_190V")

for sensor in "${HPK_80P[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindInputHistos4YReco.py -D ${sensor} -I
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python DoPositionRecoFit.py         -D ${sensor} --xmax 0.62 --fitOrder 5
    python Plot_SimpleXYMaps.py         -D ${sensor}
    python Plot_AmpChargeVsXY.py        -D ${sensor}
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_RisetimeVsX.py          -D ${sensor} -x 0.6
    python Plot_JitterVsX.py            -D ${sensor} -x 0.6
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.6 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 0.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.6 -y 50
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.6 -y 100

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 0.6
    python Plot_JitterVsX.py            -D ${sensor} -t -x 0.6
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.6 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 0.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.6 -y 50
    python Plot_ResolutionCombinedPosMethod1.py   -D ${sensor} -t -x 0.6 -y 50
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.6 -y 100
done

# Print resolution values at the end
for sensor in "${HPK_500P[@]}"; do
    cd ../macros
    python Print_Resolution.py          -D ${sensor}
    python Plot_Summary_XRes_Time.py    -D ${sensor} -x 1.5 -y 80
done

for sensor in "${HPK_80P[@]}"; do
    cd ../macros
    python Print_Resolution.py          -D ${sensor}
    python Plot_Summary_XRes_Time.py    -D ${sensor} -x 0.3 -y 60
done
