cd ../../test

# ## BNL_50um_1cm_450um_W3051_2_2_170V
# echo "Running over BNL_50um_1cm_450um_W3051_2_2_170V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_50um_1cm_450um_W3051_2_2_170V
# cd ../macros
# python FindDelayCorrections.py -D BNL_50um_1cm_450um_W3051_2_2_170V
# python FindInputHistos4YReco.py -D BNL_50um_1cm_450um_W3051_2_2_170V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_50um_1cm_450um_W3051_2_2_170V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_50um_1cm_450um_W3051_2_2_170V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_50um_1cm_450um_W3051_2_2_170V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_50um_1cm_450um_W3051_2_2_170V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_50um_1cm_450um_W3051_2_2_170V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_50um_1cm_450um_W3051_2_2_170V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_50um_1cm_450um_W3051_2_2_170V
# python Plot_AmpChargeVsXY.py        -D BNL_50um_1cm_450um_W3051_2_2_170V
# python Plot_RecoDiffVsXY.py         -D BNL_50um_1cm_450um_W3051_2_2_170V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_50um_1cm_450um_W3051_2_2_170V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_50um_1cm_450um_W3051_2_2_170V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_50um_1cm_450um_W3051_2_2_170V
# python Plot_Efficiency.py           -D BNL_50um_1cm_450um_W3051_2_2_170V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_450um_W3051_2_2_170V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_450um_W3051_2_2_170V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_50um_1cm_450um_W3051_2_2_170V -t
# python Plot_Efficiency.py           -D BNL_50um_1cm_450um_W3051_2_2_170V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_450um_W3051_2_2_170V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_450um_W3051_2_2_170V -t -x 2.5 -y 150


# ## BNL_50um_1cm_400um_W3051_1_4_160V
# echo "Running over BNL_50um_1cm_400um_W3051_1_4_160V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_50um_1cm_400um_W3051_1_4_160V
# cd ../macros
# python FindDelayCorrections.py -D BNL_50um_1cm_400um_W3051_1_4_160V
# python FindInputHistos4YReco.py -D BNL_50um_1cm_400um_W3051_1_4_160V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_50um_1cm_400um_W3051_1_4_160V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_50um_1cm_400um_W3051_1_4_160V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_50um_1cm_400um_W3051_1_4_160V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_50um_1cm_400um_W3051_1_4_160V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_50um_1cm_400um_W3051_1_4_160V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_50um_1cm_400um_W3051_1_4_160V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_50um_1cm_400um_W3051_1_4_160V
# python Plot_AmpChargeVsXY.py        -D BNL_50um_1cm_400um_W3051_1_4_160V
# python Plot_RecoDiffVsXY.py         -D BNL_50um_1cm_400um_W3051_1_4_160V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_50um_1cm_400um_W3051_1_4_160V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_50um_1cm_400um_W3051_1_4_160V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_50um_1cm_400um_W3051_1_4_160V
# python Plot_Efficiency.py           -D BNL_50um_1cm_400um_W3051_1_4_160V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_400um_W3051_1_4_160V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_400um_W3051_1_4_160V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_50um_1cm_400um_W3051_1_4_160V -t
# python Plot_Efficiency.py           -D BNL_50um_1cm_400um_W3051_1_4_160V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_400um_W3051_1_4_160V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_400um_W3051_1_4_160V -t -x 2.5 -y 150


# ## BNL_50um_1cm_450um_W3052_2_4_185V
# echo "Running over BNL_50um_1cm_450um_W3052_2_4_185V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_50um_1cm_450um_W3052_2_4_185V
# cd ../macros
# python FindDelayCorrections.py -D BNL_50um_1cm_450um_W3052_2_4_185V
# python FindInputHistos4YReco.py -D BNL_50um_1cm_450um_W3052_2_4_185V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_50um_1cm_450um_W3052_2_4_185V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_50um_1cm_450um_W3052_2_4_185V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_50um_1cm_450um_W3052_2_4_185V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_50um_1cm_450um_W3052_2_4_185V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_50um_1cm_450um_W3052_2_4_185V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_50um_1cm_450um_W3052_2_4_185V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_50um_1cm_450um_W3052_2_4_185V
# python Plot_AmpChargeVsXY.py        -D BNL_50um_1cm_450um_W3052_2_4_185V
# python Plot_RecoDiffVsXY.py         -D BNL_50um_1cm_450um_W3052_2_4_185V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_50um_1cm_450um_W3052_2_4_185V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_50um_1cm_450um_W3052_2_4_185V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_50um_1cm_450um_W3052_2_4_185V
# python Plot_Efficiency.py           -D BNL_50um_1cm_450um_W3052_2_4_185V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_450um_W3052_2_4_185V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_450um_W3052_2_4_185V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_50um_1cm_450um_W3052_2_4_185V -t
# python Plot_Efficiency.py           -D BNL_50um_1cm_450um_W3052_2_4_185V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_1cm_450um_W3052_2_4_185V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_1cm_450um_W3052_2_4_185V -t -x 2.5 -y 150


# ## BNL_20um_1cm_400um_W3074_1_4_95V
# echo "Running over BNL_20um_1cm_400um_W3074_1_4_95V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_20um_1cm_400um_W3074_1_4_95V
# cd ../macros
# python FindDelayCorrections.py -D BNL_20um_1cm_400um_W3074_1_4_95V
# python FindInputHistos4YReco.py -D BNL_20um_1cm_400um_W3074_1_4_95V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_20um_1cm_400um_W3074_1_4_95V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_20um_1cm_400um_W3074_1_4_95V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_20um_1cm_400um_W3074_1_4_95V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_20um_1cm_400um_W3074_1_4_95V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_20um_1cm_400um_W3074_1_4_95V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_20um_1cm_400um_W3074_1_4_95V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_20um_1cm_400um_W3074_1_4_95V
# python Plot_AmpChargeVsXY.py        -D BNL_20um_1cm_400um_W3074_1_4_95V
# python Plot_RecoDiffVsXY.py         -D BNL_20um_1cm_400um_W3074_1_4_95V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_20um_1cm_400um_W3074_1_4_95V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_20um_1cm_400um_W3074_1_4_95V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_20um_1cm_400um_W3074_1_4_95V
# python Plot_Efficiency.py           -D BNL_20um_1cm_400um_W3074_1_4_95V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_400um_W3074_1_4_95V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_400um_W3074_1_4_95V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_20um_1cm_400um_W3074_1_4_95V -t
# python Plot_Efficiency.py           -D BNL_20um_1cm_400um_W3074_1_4_95V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_400um_W3074_1_4_95V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_400um_W3074_1_4_95V -t -x 2.5 -y 150


# ## BNL_20um_1cm_400um_W3075_1_2_80V
# echo "Running over BNL_20um_1cm_400um_W3075_1_2_80V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_20um_1cm_400um_W3075_1_2_80V
# cd ../macros
# python FindDelayCorrections.py -D BNL_20um_1cm_400um_W3075_1_2_80V
# python FindInputHistos4YReco.py -D BNL_20um_1cm_400um_W3075_1_2_80V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_20um_1cm_400um_W3075_1_2_80V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_20um_1cm_400um_W3075_1_2_80V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_20um_1cm_400um_W3075_1_2_80V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_20um_1cm_400um_W3075_1_2_80V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_20um_1cm_400um_W3075_1_2_80V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_20um_1cm_400um_W3075_1_2_80V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_20um_1cm_400um_W3075_1_2_80V
# python Plot_AmpChargeVsXY.py        -D BNL_20um_1cm_400um_W3075_1_2_80V
# python Plot_RecoDiffVsXY.py         -D BNL_20um_1cm_400um_W3075_1_2_80V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_20um_1cm_400um_W3075_1_2_80V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_20um_1cm_400um_W3075_1_2_80V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_20um_1cm_400um_W3075_1_2_80V
# python Plot_Efficiency.py           -D BNL_20um_1cm_400um_W3075_1_2_80V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_400um_W3075_1_2_80V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_400um_W3075_1_2_80V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_20um_1cm_400um_W3075_1_2_80V -t
# python Plot_Efficiency.py           -D BNL_20um_1cm_400um_W3075_1_2_80V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_400um_W3075_1_2_80V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_400um_W3075_1_2_80V -t -x 2.5 -y 150


# ## BNL_20um_1cm_450um_W3074_2_1_95V
# echo "Running over BNL_20um_1cm_450um_W3074_2_1_95V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_20um_1cm_450um_W3074_2_1_95V
# cd ../macros
# python FindDelayCorrections.py -D BNL_20um_1cm_450um_W3074_2_1_95V
# python FindInputHistos4YReco.py -D BNL_20um_1cm_450um_W3074_2_1_95V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_20um_1cm_450um_W3074_2_1_95V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_20um_1cm_450um_W3074_2_1_95V -A --xmax 0.79 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_20um_1cm_450um_W3074_2_1_95V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_20um_1cm_450um_W3074_2_1_95V --zmin 20.0 --zmax 100.0
# python Plot_TimeDiffVsXY.py         -D BNL_20um_1cm_450um_W3074_2_1_95V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_20um_1cm_450um_W3074_2_1_95V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_20um_1cm_450um_W3074_2_1_95V
# python Plot_AmpChargeVsXY.py        -D BNL_20um_1cm_450um_W3074_2_1_95V
# python Plot_RecoDiffVsXY.py         -D BNL_20um_1cm_450um_W3074_2_1_95V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_20um_1cm_450um_W3074_2_1_95V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_20um_1cm_450um_W3074_2_1_95V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_20um_1cm_450um_W3074_2_1_95V
# python Plot_Efficiency.py           -D BNL_20um_1cm_450um_W3074_2_1_95V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_450um_W3074_2_1_95V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_450um_W3074_2_1_95V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_20um_1cm_450um_W3074_2_1_95V -t
# python Plot_Efficiency.py           -D BNL_20um_1cm_450um_W3074_2_1_95V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_450um_W3074_2_1_95V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_450um_W3074_2_1_95V -t -x 2.5 -y 150


# ## BNL_20um_1cm_450um_W3075_2_4_80V
# echo "Running over BNL_20um_1cm_450um_W3075_2_4_80V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_20um_1cm_450um_W3075_2_4_80V
# cd ../macros
# python FindDelayCorrections.py -D BNL_20um_1cm_450um_W3075_2_4_80V
# python FindInputHistos4YReco.py -D BNL_20um_1cm_450um_W3075_2_4_80V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_20um_1cm_450um_W3075_2_4_80V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_20um_1cm_450um_W3075_2_4_80V -A --xmax 0.75 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_20um_1cm_450um_W3075_2_4_80V --xlength 2.5 --ylength 100.0
# python Plot_AmplitudeVsXY.py        -D BNL_20um_1cm_450um_W3075_2_4_80V --zmin 10.0 --zmax 40.0
# python Plot_TimeDiffVsXY.py         -D BNL_20um_1cm_450um_W3075_2_4_80V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_20um_1cm_450um_W3075_2_4_80V --xlength 6.0 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_20um_1cm_450um_W3075_2_4_80V
# python Plot_AmpChargeVsXY.py        -D BNL_20um_1cm_450um_W3075_2_4_80V
# python Plot_RecoDiffVsXY.py         -D BNL_20um_1cm_450um_W3075_2_4_80V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_20um_1cm_450um_W3075_2_4_80V --xlength 5.6 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_20um_1cm_450um_W3075_2_4_80V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_20um_1cm_450um_W3075_2_4_80V
# python Plot_Efficiency.py           -D BNL_20um_1cm_450um_W3075_2_4_80V -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_450um_W3075_2_4_80V -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_450um_W3075_2_4_80V -x 2.5 -y 150

# python Plot_Resolution1D.py         -D BNL_20um_1cm_450um_W3075_2_4_80V -t
# python Plot_Efficiency.py           -D BNL_20um_1cm_450um_W3075_2_4_80V -t -x 2.5
# python Plot_ResolutionXRecoVsX.py   -D BNL_20um_1cm_450um_W3075_2_4_80V -t -x 2.5
# python Plot_ResolutionTimeVsX.py    -D BNL_20um_1cm_450um_W3075_2_4_80V -t -x 2.5 -y 150


# ## BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# echo "Running over BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# cd ../macros
# python FindDelayCorrections.py -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# python FindInputHistos4YReco.py -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -A --xmax 0.72 --fitOrder 5
# python Plot_AmplitudeVsX.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --xlength 2.7 --ylength 40.0
# python Plot_AmplitudeVsXY.py        -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --zmin 20.0 --zmax 40.0
# python Plot_TimeDiffVsXY.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --xlength 13.5 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# python Plot_AmpChargeVsXY.py        -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# python Plot_RecoDiffVsXY.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V
# python Plot_Efficiency.py           -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -x 2.7 -y 150

# python Plot_Resolution1D.py         -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -t
# python Plot_Efficiency.py           -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V -t -x 2.7 -y 150


# ## BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# echo "Running over BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# cd ../macros
# python FindDelayCorrections.py -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# python FindInputHistos4YReco.py -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -I
# cd ../test
# ./MyAnalysis -A Analyze -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# cd ../macros

# python DoPositionRecoFit.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -A --xmax 0.72 --fitOrder 4
# python Plot_AmplitudeVsX.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --xlength 2.7 --ylength 40.0
# python Plot_AmplitudeVsXY.py        -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --zmin 20.0 --zmax 40.0
# python Plot_TimeDiffVsXY.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --zmin 25.0 --zmax 75.0
# python Plot_TimeDiffVsY.py          -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --xlength 13.5 --ylength 150.0
# python Plot_SimpleXYMaps.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# python Plot_AmpChargeVsXY.py        -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# python Plot_RecoDiffVsXY.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --zmin 0.0 --zmax 100.0
# python Plot_RecoDiffVsY.py          -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V --xlength 13.5 --ylength 4.0
# python Plot_CutFlow.py              -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V

# # Paper plots
# python Plot_Resolution1D.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V
# python Plot_Efficiency.py           -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -x 2.7
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -x 2.7 -y 150

# python Plot_Resolution1D.py         -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -t
# python Plot_Efficiency.py           -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -t -x 2.7
# python Plot_ResolutionXRecoVsX.py   -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -t -x 2.7
# python Plot_ResolutionTimeVsX.py    -D BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V -t -x 2.7 -y 150


# BNL strip sensors
# -----------------------

# BNL_strips=('BNL_50um_1cm_450um_W3051_2_2_170V' 'BNL_50um_1cm_400um_W3051_1_4_160V' 'BNL_50um_1cm_450um_W3052_2_4_185V' 'BNL_20um_1cm_400um_W3074_1_4_95V' 'BNL_20um_1cm_400um_W3075_1_2_80V' 'BNL_20um_1cm_450um_W3074_2_1_95V' 'BNL_20um_1cm_450um_W3075_2_4_80V' 'BNL_50um_2p5cm_mixConfig1_W3051_1_4_170V' 'BNL_50um_2p5cm_mixConfig2_W3051_1_4_170V')
BNL_strips=('BNL_50um_1cm_450um_W3051_2_2_170V' 'BNL_50um_1cm_400um_W3051_1_4_160V' 'BNL_50um_1cm_450um_W3052_2_4_185V') # 'BNL_20um_1cm_450um_W3075_2_4_80V')

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
    # python Plot_RecoDiffVsXY.py         -D ${sensor} --zmin 0.0 --zmax 100.0
    # python Plot_RecoDiffVsY.py          -D ${sensor} --xlength 13.5 --ylength 4.0
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
