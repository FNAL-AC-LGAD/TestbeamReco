cd ../../test

# BNL_500x500um pads with different shapes
# ----------------------------------------

BNL_PadShapes=("BNL_30um_500x500_SmallSquare_W3104_115V" "BNL_30um_500x500_LargeSquare_W3104_115V" "BNL_30um_500x500_SquaredCircle_W3104_110V" "BNL_30um_500x500_Cross_W3104_115V")

for sensor in "${BNL_PadShapes[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python Plot_MeanAmplitudeVsXY.py        -D ${sensor}
    python Plot_EfficiencyTwoHitsvsXY.py    -D ${sensor}
    python Plot_EfficiencyTwoHitsvsXY.py    -D ${sensor} -F
    python Plot_RiseTimeVsXY.py             -D ${sensor} -z 350 -Z 450
done
