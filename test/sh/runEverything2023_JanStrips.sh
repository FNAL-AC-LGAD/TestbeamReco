cd ../../test

# BNL strip sensors
# -----------------------

# BNL_strips=('BNL_50um_1cm_450um_W3052_2_4_185V') # 'BNL_20um_1cm_450um_W3075_2_4_80V')
BNL_strips=('BNL_50um_1cm_450um_W3051_2_2_170V' 'BNL_50um_1cm_400um_W3051_1_4_160V')

for sensor in "${BNL_strips[@]}"; do
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
    python Plot_RisetimeVsX.py          -D ${sensor} -x 2.6
    python Plot_JitterVsX.py            -D ${sensor} -x 2.6
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 2.6 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 2.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 2.6
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 2.6 -y 100

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 2.6
    python Plot_JitterVsX.py            -D ${sensor} -t -x 2.6
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 2.6 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 2.6
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 2.6
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 2.6 -y 100
done

for sensor in "${BNL_strips[@]}"; do
    cd ../macros
    python Print_Resolution.py          -D ${sensor}
done
