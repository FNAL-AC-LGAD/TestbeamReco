cd ../../test

# HPK_2x3pad
# ----------

# NOTE: 'HPK_W9_23_3_20T_500x500_300M_E600_112V' has a missing channel
# HPK_2x3pad=("HPK_W9_22_3_20T_500x500_150M_E600_112V")
HPK_2x3pad=("HPK_W11_22_3_20T_500x500_150M_C600_116V" "HPK_W8_1_1_50T_500x500_150M_C600_200V" "HPK_W5_1_1_50T_500x500_150M_E600_185V" "HPK_W9_23_3_20T_500x500_300M_E600_112V")

for sensor in "${HPK_2x3pad[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindPadCenters.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python Plot_SimpleXYMaps.py         -D ${sensor}
    # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_RisetimeVsX.py          -D ${sensor} -x 1.1
    python Plot_JitterVsX.py            -D ${sensor} -x 1.1
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 1.1 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 1.1
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 1.1
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 1.1 -y 80

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 1.1
    python Plot_JitterVsX.py            -D ${sensor} -t -x 1.1
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 1.1 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 1.1
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 1.1
    python Plot_ResolutionCombinedPosMethod1.py   -D ${sensor} -t -x 1.1
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 1.1 -y 80

    python Plot_Efficiency.py           -D ${sensor} -n -x 1.1
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -n -x 1.1 -y 80

    python Plot_MeanAmplitudeVsXY.py        -D ${sensor}
    python Plot_EfficiencyTwoHitsvsXY.py    -D ${sensor}
    python Plot_EfficiencyTwoHitsvsXY.py    -D ${sensor} -F
    python Plot_RiseTimeVsXY.py             -D ${sensor} -z 280 -Z 450
done

cd ../macros
# DoPositionRecoFit
python DoPositionRecoFit.py     -D HPK_W11_22_3_20T_500x500_150M_C600_116V  --xmax 0.84 --fitOrder 5
# python DoPositionRecoFit.py     -D HPK_W9_22_3_20T_500x500_150M_E600_112V   --xmax 0.84 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W8_1_1_50T_500x500_150M_C600_200V    --xmax 0.82 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W5_1_1_50T_500x500_150M_E600_185V    --xmax 0.86 --fitOrder 5
python DoPositionRecoFit.py     -D HPK_W9_23_3_20T_500x500_300M_E600_112V   --xmax 0.87 --fitOrder 5

for sensor in "${HPK_2x3pad[@]}"; do
    cd ../macros
    python Print_Resolution.py          -D ${sensor}
    python Plot_Summary_XRes_Time.py    -D ${sensor} -x 0.9 -y 190
done
