cd ../../test

# BNL_500x500um Cross sensors
# ---------------------------

BNL_CrossPads=('BNL_30um_500x500_Cross_W3104_115V')

for sensor in "${BNL_CrossPads[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    # cd ../test
    # ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    # cd ../macros
    # python FindPadCenters.py -D ${sensor}
    # python FindDelayCorrections.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    python DoPositionRecoFit.py         -D ${sensor} --xmax 0.85 --fitOrder 5
    # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    python Plot_SimpleXYMaps.py         -D ${sensor}
    # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_RisetimeVsX.py          -D ${sensor} -x 0.8
    python Plot_JitterVsX.py            -D ${sensor} -x 0.8
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.8 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 0.8
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.8
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.8 -y 80
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.8 -y 80 -Y

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 0.8
    python Plot_JitterVsX.py            -D ${sensor} -t -x 0.8
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.8 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 0.8
    python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.8
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.8 -y 80

    python Plot_Efficiency.py           -D ${sensor} -n -x 0.8
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -n -x 0.8 -y 80
done

for sensor in "${BNL_CrossPads[@]}"; do
    cd ../macros
    python Print_Resolution.py          -D ${sensor}
done
