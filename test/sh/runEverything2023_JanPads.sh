cd ../../test

# # HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# echo "Running over HPK_20um_500x500um_2x2pad_E600_FNAL_105V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# cd ../macros
# python FindDelayCorrections.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# python FindInputHistos4YReco.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# # python Plot_AmpChargeVsXY.py        -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# python Plot_Efficiency.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 0.7
# # python Plot_XRes.py                 -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t
# python Plot_Efficiency.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t -x 0.7 -y 50


# # HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# echo "Running over HPK_30um_500x500um_2x2pad_E600_FNAL_140V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# cd ../macros
# python FindDelayCorrections.py -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# python FindInputHistos4YReco.py -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# # python Plot_AmpChargeVsXY.py        -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# python Plot_Efficiency.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 0.7
# # python Plot_XRes.py                 -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t
# python Plot_Efficiency.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t -x 0.7 -y 50


# # HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# echo "Running over HPK_50um_500x500um_2x2pad_E600_FNAL_190V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# cd ../macros
# python FindDelayCorrections.py -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# python FindInputHistos4YReco.py -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# cd ../macros


# # python DoPositionRecoFit.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# # python Plot_AmpChargeVsXY.py        -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# python Plot_Efficiency.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 0.7
# # python Plot_XRes.py                 -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t
# python Plot_Efficiency.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t -x 0.7 -y 50


# # Run Bias Scans
# echo "Running full bias scan results"
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_50um_500x500um_2x2pad_E600_FNAL
# ./MyAnalysis -A Analyze -D HPK_30um_500x500um_2x2pad_E600_FNAL
# ./MyAnalysis -A Analyze -D HPK_20um_500x500um_2x2pad_E600_FNAL
# cd ../macros
# python PlotBiasScans.py -D HPK_50um_500x500um_2x2pad_E600_FNAL

# <<commentout
# HPK_500x500um_2x2pad_E600
# -------------------------

HPK_2x2pad=('HPK_20um_500x500um_2x2pad_E600_FNAL_105V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_140V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_190V')

for sensor in "${HPK_2x2pad[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindPadCenters.py -D ${sensor}
    python FindDelayCorrections.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    # python DoPositionRecoFit.py         -D ${sensor} --xmax 0.70 --fitOrder 4
    # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    python Plot_SimpleXYMaps.py         -D ${sensor}
    # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_RisetimeVsX.py          -D ${sensor} -x 0.7
    python Plot_JitterVsX.py            -D ${sensor} -x 0.7
    python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.7 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 0.7
    # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.7
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.7 -y 60

    python Plot_RisetimeVsX.py          -D ${sensor} -t -x 0.7
    python Plot_JitterVsX.py            -D ${sensor} -t -x 0.7
    python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.7 -y 200.0
    python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 0.7
    # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.7
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.7 -y 60

    python Plot_Efficiency.py           -D ${sensor} -n -x 0.7
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -n -x 0.7 -y 60
done
# commentout

<<commentout_bias_scan ## Uncomment to run Bias Scan
# HPK_50um_500x500um_2x2pad_E600 Bias Scan
# ----------------------------------------

# HPK_50um_500x500um_2x2pad_E600=('HPK_50um_500x500um_2x2pad_E600_FNAL_190V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_185V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_180V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_170V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_160V')
HPK_50um_500x500um_2x2pad_E600=('HPK_50um_500x500um_2x2pad_E600_FNAL_185V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_180V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_170V' 'HPK_50um_500x500um_2x2pad_E600_FNAL_160V')

for sensor in "${HPK_50um_500x500um_2x2pad_E600[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    # cd ../macros

    # # python DoPositionRecoFit.py         -D ${sensor} -A --xmax 0.70 --fitOrder 4
    # # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    # python Plot_SimpleXYMaps.py         -D ${sensor}
    # # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    # python Plot_CutFlow.py              -D ${sensor}

    # # Paper plots
    # python Plot_JitterVsX.py            -D ${sensor} -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -c
    # python Plot_Efficiency.py           -D ${sensor} -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.7 -y 60

    # python Plot_JitterVsX.py            -D ${sensor} -t -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -t
    # python Plot_Efficiency.py           -D ${sensor} -t -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.7 -y 60
done


# HPK_30um_500x500um_2x2pad_E600 Bias Scan
# ----------------------------------------

# HPK_30um_500x500um_2x2pad_E600=('HPK_30um_500x500um_2x2pad_E600_FNAL_144V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_140V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_135V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_130V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_120V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_110V')
HPK_30um_500x500um_2x2pad_E600=('HPK_30um_500x500um_2x2pad_E600_FNAL_144V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_135V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_130V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_120V' 'HPK_30um_500x500um_2x2pad_E600_FNAL_110V')

for sensor in "${HPK_30um_500x500um_2x2pad_E600[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    # cd ../macros

    # # python DoPositionRecoFit.py         -D ${sensor} -A --xmax 0.70 --fitOrder 4
    # # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    # python Plot_SimpleXYMaps.py         -D ${sensor}
    # # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    # python Plot_CutFlow.py              -D ${sensor}

    # # Paper plots
    # python Plot_JitterVsX.py            -D ${sensor} -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -c
    # python Plot_Efficiency.py           -D ${sensor} -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.7 -y 60

    # python Plot_JitterVsX.py            -D ${sensor} -t -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -t
    # python Plot_Efficiency.py           -D ${sensor} -t -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.7 -y 60
done



# HPK_20um_500x500um_2x2pad_E600 Bias Scan
# ----------------------------------------

# HPK_20um_500x500um_2x2pad_E600=('HPK_20um_500x500um_2x2pad_E600_FNAL_95V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_100V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_105V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_110V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_108V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_90V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_85V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_75V')
HPK_20um_500x500um_2x2pad_E600=('HPK_20um_500x500um_2x2pad_E600_FNAL_95V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_100V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_110V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_108V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_90V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_85V' 'HPK_20um_500x500um_2x2pad_E600_FNAL_75V')

for sensor in "${HPK_20um_500x500um_2x2pad_E600[@]}"; do
    printf "\nRunning over ${sensor} sensor\n"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    # cd ../macros

    # # python DoPositionRecoFit.py         -D ${sensor} -A --xmax 0.70 --fitOrder 4
    # # python Plot_AmplitudeVsX.py         -D ${sensor} --xlength 2.7 --ylength 140.0 # Needs to be updated
    # # python Plot_AmplitudeVsXY.py        -D ${sensor} --zmin 20.0 --zmax 140.0 # Needs to be updated
    # # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    # python Plot_SimpleXYMaps.py         -D ${sensor}
    # # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    # python Plot_CutFlow.py              -D ${sensor}

    # # Paper plots
    # python Plot_JitterVsX.py            -D ${sensor} -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -c
    # python Plot_Efficiency.py           -D ${sensor} -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 0.7 -y 60

    # python Plot_JitterVsX.py            -D ${sensor} -t -x 0.7
    # python Plot_AmplitudeVsX.py         -D ${sensor} -t -x 0.7 -y 200.0
    # python Plot_AmplitudeVsXY.py        -D ${sensor} -t -z 0.0 -Z 200.0
    # python Plot_Resolution1D.py         -D ${sensor} -t
    # python Plot_Efficiency.py           -D ${sensor} -t -x 0.7
    # # python Plot_ResolutionXRecoVsX.py   -D ${sensor} -t -x 0.7
    # python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 0.7 -y 60
done

cd ../macros
# Get characteristic values (say, jitter, resolutions, amplitudes, etc.) for all sensors
python Plot_AllQuantities_BiasScan.py
python Plot_BiasScan.py
commentout_bias_scan
