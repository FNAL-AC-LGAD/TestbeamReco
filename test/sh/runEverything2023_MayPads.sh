cd ../../test

# # HPK_W9_22_3_20T_500x500_150M_E600_112V
# echo "Running over HPK_W9_22_3_20T_500x500_150M_E600_112V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_22_3_20T_500x500_150M_E600_112V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W9_22_3_20T_500x500_150M_E600_112V
# python FindInputHistos4YReco.py -D HPK_W9_22_3_20T_500x500_150M_E600_112V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W9_22_3_20T_500x500_150M_E600_112V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_W9_22_3_20T_500x500_150M_E600_112V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_W9_22_3_20T_500x500_150M_E600_112V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V
# # python Plot_AmpChargeVsXY.py        -D HPK_W9_22_3_20T_500x500_150M_E600_112V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_W9_22_3_20T_500x500_150M_E600_112V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W9_22_3_20T_500x500_150M_E600_112V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V
# python Plot_Efficiency.py           -D HPK_W9_22_3_20T_500x500_150M_E600_112V -x 0.7
# # python Plot_XRes.py                 -D HPK_W9_22_3_20T_500x500_150M_E600_112V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_22_3_20T_500x500_150M_E600_112V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_W9_22_3_20T_500x500_150M_E600_112V -t
# python Plot_Efficiency.py           -D HPK_W9_22_3_20T_500x500_150M_E600_112V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_W9_22_3_20T_500x500_150M_E600_112V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_22_3_20T_500x500_150M_E600_112V -t -x 0.7 -y 50


# # HPK_W9_23_3_20T_500x500_300M_E600_112V
# echo "Running over HPK_W9_23_3_20T_500x500_300M_E600_112V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W9_23_3_20T_500x500_300M_E600_112V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W9_23_3_20T_500x500_300M_E600_112V
# python FindInputHistos4YReco.py -D HPK_W9_23_3_20T_500x500_300M_E600_112V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W9_23_3_20T_500x500_300M_E600_112V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_W9_23_3_20T_500x500_300M_E600_112V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_W9_23_3_20T_500x500_300M_E600_112V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V
# # python Plot_AmpChargeVsXY.py        -D HPK_W9_23_3_20T_500x500_300M_E600_112V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_W9_23_3_20T_500x500_300M_E600_112V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W9_23_3_20T_500x500_300M_E600_112V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V
# python Plot_Efficiency.py           -D HPK_W9_23_3_20T_500x500_300M_E600_112V -x 0.7
# # python Plot_XRes.py                 -D HPK_W9_23_3_20T_500x500_300M_E600_112V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_23_3_20T_500x500_300M_E600_112V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_W9_23_3_20T_500x500_300M_E600_112V -t
# python Plot_Efficiency.py           -D HPK_W9_23_3_20T_500x500_300M_E600_112V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_W9_23_3_20T_500x500_300M_E600_112V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W9_23_3_20T_500x500_300M_E600_112V -t -x 0.7 -y 50


# # HPK_W11_22_3_20T_500x500_150M_C600_116V
# echo "Running over HPK_W11_22_3_20T_500x500_150M_C600_116V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W11_22_3_20T_500x500_150M_C600_116V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W11_22_3_20T_500x500_150M_C600_116V
# python FindInputHistos4YReco.py -D HPK_W11_22_3_20T_500x500_150M_C600_116V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W11_22_3_20T_500x500_150M_C600_116V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_W11_22_3_20T_500x500_150M_C600_116V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_W11_22_3_20T_500x500_150M_C600_116V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V
# # python Plot_AmpChargeVsXY.py        -D HPK_W11_22_3_20T_500x500_150M_C600_116V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_W11_22_3_20T_500x500_150M_C600_116V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W11_22_3_20T_500x500_150M_C600_116V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V
# python Plot_Efficiency.py           -D HPK_W11_22_3_20T_500x500_150M_C600_116V -x 0.7
# # python Plot_XRes.py                 -D HPK_W11_22_3_20T_500x500_150M_C600_116V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W11_22_3_20T_500x500_150M_C600_116V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_W11_22_3_20T_500x500_150M_C600_116V -t
# python Plot_Efficiency.py           -D HPK_W11_22_3_20T_500x500_150M_C600_116V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_W11_22_3_20T_500x500_150M_C600_116V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W11_22_3_20T_500x500_150M_C600_116V -t -x 0.7 -y 50


# # HPK_W8_1_1_50T_500x500_150M_C600_200V
# echo "Running over HPK_W8_1_1_50T_500x500_150M_C600_200V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W8_1_1_50T_500x500_150M_C600_200V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W8_1_1_50T_500x500_150M_C600_200V
# python FindInputHistos4YReco.py -D HPK_W8_1_1_50T_500x500_150M_C600_200V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W8_1_1_50T_500x500_150M_C600_200V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_W8_1_1_50T_500x500_150M_C600_200V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_W8_1_1_50T_500x500_150M_C600_200V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V
# # python Plot_AmpChargeVsXY.py        -D HPK_W8_1_1_50T_500x500_150M_C600_200V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_W8_1_1_50T_500x500_150M_C600_200V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W8_1_1_50T_500x500_150M_C600_200V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V
# python Plot_Efficiency.py           -D HPK_W8_1_1_50T_500x500_150M_C600_200V -x 0.7
# # python Plot_XRes.py                 -D HPK_W8_1_1_50T_500x500_150M_C600_200V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_1_1_50T_500x500_150M_C600_200V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_W8_1_1_50T_500x500_150M_C600_200V -t
# python Plot_Efficiency.py           -D HPK_W8_1_1_50T_500x500_150M_C600_200V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_W8_1_1_50T_500x500_150M_C600_200V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W8_1_1_50T_500x500_150M_C600_200V -t -x 0.7 -y 50


# # HPK_W5_1_1_50T_500x500_150M_E600_185V
# echo "Running over HPK_W5_1_1_50T_500x500_150M_E600_185V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D HPK_W5_1_1_50T_500x500_150M_E600_185V
# cd ../macros
# python FindDelayCorrections.py -D HPK_W5_1_1_50T_500x500_150M_E600_185V
# python FindInputHistos4YReco.py -D HPK_W5_1_1_50T_500x500_150M_E600_185V -I
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_W5_1_1_50T_500x500_150M_E600_185V
# cd ../macros

# # python DoPositionRecoFit.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V -A --xmax 0.70 --fitOrder 4
# # python Plot_AmplitudeVsX.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V --xlength 2.7 --ylength 140.0 # Needs to be updated
# # python Plot_AmplitudeVsXY.py        -D HPK_W5_1_1_50T_500x500_150M_E600_185V --zmin 20.0 --zmax 140.0 # Needs to be updated
# # python Plot_TimeDiffVsXY.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V --zmin 10.0 --zmax 50.0
# # python Plot_TimeDiffVsY.py          -D HPK_W5_1_1_50T_500x500_150M_E600_185V --xlength 1.0 --ylength 100.0
# python Plot_SimpleXYMaps.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V
# # python Plot_AmpChargeVsXY.py        -D HPK_W5_1_1_50T_500x500_150M_E600_185V # Needs to be updated
# # python Plot_RecoDiffVsXY.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V --zmin 0.0 --zmax 100.0
# # python Plot_RecoDiffVsY.py          -D HPK_W5_1_1_50T_500x500_150M_E600_185V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D HPK_W5_1_1_50T_500x500_150M_E600_185V

# # Paper plots
# python Plot_Resolution1D.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V
# python Plot_Efficiency.py           -D HPK_W5_1_1_50T_500x500_150M_E600_185V -x 0.7
# # python Plot_XRes.py                 -D HPK_W5_1_1_50T_500x500_150M_E600_185V -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W5_1_1_50T_500x500_150M_E600_185V -x 0.7 -y 50

# python Plot_Resolution1D.py         -D HPK_W5_1_1_50T_500x500_150M_E600_185V -t
# python Plot_Efficiency.py           -D HPK_W5_1_1_50T_500x500_150M_E600_185V -t -x 0.7
# # python Plot_XRes.py                 -D HPK_W5_1_1_50T_500x500_150M_E600_185V -t -x 0.7
# python Plot_ResolutionTimeVsX.py    -D HPK_W5_1_1_50T_500x500_150M_E600_185V -t -x 0.7 -y 50



# HPK_2x3pad
# ----------

# NOTE: 'HPK_W9_23_3_20T_500x500_300M_E600_112V' has a missing channel
HPK_2x3pad=('HPK_W9_22_3_20T_500x500_150M_E600_112V' 'HPK_W11_22_3_20T_500x500_150M_C600_116V' 'HPK_W8_1_1_50T_500x500_150M_C600_200V' 'HPK_W5_1_1_50T_500x500_150M_E600_185V')

for sensor in "${HPK_2x3pad[@]}"; do
    echo "Running over ${sensor} sensor"
    cd ../test
    ./MyAnalysis -A InitialAnalyzer -D ${sensor}
    cd ../macros
    python FindDelayCorrections.py -D ${sensor}
    python FindPadCenters.py -D ${sensor}
    cd ../test
    ./MyAnalysis -A Analyze -D ${sensor}
    cd ../macros

    # python DoPositionRecoFit.py         -D ${sensor} -A --xmax 0.70 --fitOrder 4
    # python Plot_AmplitudeVsX.py         -D ${sensor} --xlength 2.7 --ylength 140.0 # Needs to be updated
    # python Plot_AmplitudeVsXY.py        -D ${sensor} --zmin 20.0 --zmax 140.0 # Needs to be updated
    # python Plot_TimeDiffVsXY.py         -D ${sensor} --zmin 10.0 --zmax 50.0
    # python Plot_TimeDiffVsY.py          -D ${sensor} --xlength 1.0 --ylength 100.0
    python Plot_SimpleXYMaps.py         -D ${sensor}
    # python Plot_AmpChargeVsXY.py        -D ${sensor} # Needs to be updated
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
    python Plot_CutFlow.py              -D ${sensor}

    # Paper plots
    python Plot_Resolution1D.py         -D ${sensor} -c
    python Plot_Efficiency.py           -D ${sensor} -x 1.1
    # python Plot_XRes.py                 -D ${sensor} -x 1.1
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -x 1.1 -y 50

    python Plot_Resolution1D.py         -D ${sensor} -t
    python Plot_Efficiency.py           -D ${sensor} -t -x 1.1
    # python Plot_XRes.py                 -D ${sensor} -t -x 1.1
    python Plot_ResolutionTimeVsX.py    -D ${sensor} -t -x 1.1 -y 50

    # python Print_Resolution.py          -D ${sensor}
done

