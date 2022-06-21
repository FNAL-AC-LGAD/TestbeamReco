## EIC_W2_1cm_500up_300uw
echo "Running over EIC_W2_1cm_500up_300uw sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W2_1cm_500um_200um_gap_240V
cd ../macros
python FindDelayCorrections.py -D EIC_W2_1cm_500um_200um_gap_240V
cd ../test
./MyAnalysis -A RecoAnalyzer -D EIC_W2_1cm_500um_200um_gap_240V
cd ../macros
python FindInputHistos4YReco.py -D EIC_W2_1cm_500um_200um_gap_240V
cd ../test
./MyAnalysis -A Analyze -D EIC_W2_1cm_500um_200um_gap_240V
cd ../macros
python DoPositionRecoFit.py -D EIC_W2_1cm_500um_200um_gap_240V -A --xmax 0.74 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W2_1cm_500um_200um_gap_240V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W2_1cm_500um_200um_gap_240V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W2_1cm_500um_200um_gap_240V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W2_1cm_500um_200um_gap_240V --zmin 25.0 --zmax 75.0  ## --zmin 25.0 --zmax 75.0 For all fo the sensors! (2.5 cm uses 35. - 150.)
python PlotTimeDiffVsY.py   -D EIC_W2_1cm_500um_200um_gap_240V --xlength 6.0 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W2_1cm_500um_200um_gap_240V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W2_1cm_500um_200um_gap_240V
python PlotRecoDiffVsXY.py  -D EIC_W2_1cm_500um_200um_gap_240V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W2_1cm_500um_200um_gap_240V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W2_1cm_500um_200um_gap_240V -x 2.5 -r 0
python PlotEfficiency.py    -D EIC_W2_1cm_500um_200um_gap_240V -x 2.5 -r 1
python PlotEfficiency.py    -D EIC_W2_1cm_500um_200um_gap_240V -x 2.5 -r 2
python plot1DRes.py         -D EIC_W2_1cm_500um_200um_gap_240V

## EIC_W1_1cm_500up_200uw
echo "Running over EIC_W1_1cm_500up_200uw sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_255V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_255V
cd ../test
./MyAnalysis -A RecoAnalyzer -D EIC_W1_1cm_255V
cd ../macros
python FindInputHistos4YReco.py -D EIC_W1_1cm_255V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_255V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_1cm_255V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_255V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_255V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_255V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_255V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_255V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_255V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_255V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_255V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_255V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_255V -x 2.5 -r 0
python PlotEfficiency.py    -D EIC_W1_1cm_255V -x 2.5 -r 1
python PlotEfficiency.py    -D EIC_W1_1cm_255V -x 2.5 -r 2
python plot1DRes.py         -D EIC_W1_1cm_255V

## EIC_W2_1cm_500up_100uw
echo "Running over EIC_W2_1cm_500up_100uw sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W2_1cm_500um_400um_gap_220V
cd ../macros
python FindDelayCorrections.py -D EIC_W2_1cm_500um_400um_gap_220V
cd ../test
./MyAnalysis -A RecoAnalyzer -D EIC_W2_1cm_500um_400um_gap_220V
cd ../macros
python FindInputHistos4YReco.py -D EIC_W2_1cm_500um_400um_gap_220V
cd ../test
./MyAnalysis -A Analyze -D EIC_W2_1cm_500um_400um_gap_220V
cd ../macros

python DoPositionRecoFit.py -D EIC_W2_1cm_500um_400um_gap_220V -A --xmax 0.82 --fitOrder 4
python PlotAmplitudeVsX.py  -D EIC_W2_1cm_500um_400um_gap_220V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W2_1cm_500um_400um_gap_220V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W2_1cm_500um_400um_gap_220V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W2_1cm_500um_400um_gap_220V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W2_1cm_500um_400um_gap_220V --xlength 5.5 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W2_1cm_500um_400um_gap_220V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W2_1cm_500um_400um_gap_220V
python PlotRecoDiffVsXY.py  -D EIC_W2_1cm_500um_400um_gap_220V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W2_1cm_500um_400um_gap_220V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W2_1cm_500um_400um_gap_220V -x 2.5 -r 0
python PlotEfficiency.py    -D EIC_W2_1cm_500um_400um_gap_220V -x 2.5 -r 1
python PlotEfficiency.py    -D EIC_W2_1cm_500um_400um_gap_220V -x 2.5 -r 2
python plot1DRes.py         -D EIC_W2_1cm_500um_400um_gap_220V



# ## MultiPitch
# ## EIC_W1_1cm_100up_50uw
# ## EIC_W1_1cm_200up_100uw
# ## EIC_W1_1cm_300up_150uw
# cd ../test
# ./MyAnalysis -A Analyze -D EIC_W1_1cm_all_multiPitch_240V
# cd ../macros
# python DoPositionRecoFit.py -D EIC_W1_1cm_all_multiPitch_240V --xmax 0.8 --pitch 500 --fitOrder 7 
# python plot1DRes.py         -D EIC_W1_1cm_all_multiPitch_240V
# python PlotAmplitudeVsX.py  -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --xlength 3.0 --ylength 70.0
# python PlotTimeDiffVsX.py   -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
# python PlotRecoDiffVsX.py   -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
# python PlotEfficiency.py    -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --xlength 3.0
# python PlotSimpleXYMaps.py  -D EIC_W1_1cm_all_multiPitch_240V
# python PlotAmplitudeVsXY.py -D EIC_W1_1cm_all_multiPitch_240V --zmin 25.0 --zmax 50.0
# python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin 0.0 --zmax 120.0
# python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin -0.5 --zmax 0.5
# python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin 0.0 --zmax 100.0



# ## EIC_UCSC_2p5cm_500up_200uw
# cd ../test
# ./MyAnalysis -A Analyze -D EIC_W1_2p5cm_UCSC_330V 
# cd ../macros
# python DoPositionRecoFit.py -D EIC_W1_2p5cm_UCSC_330V --xmax 0.85 --pitch 500 --fitOrder 2 
# python plot1DRes.py         -D EIC_W1_2p5cm_UCSC_330V
# python PlotAmplitudeVsX.py  -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --xlength 3.0 --ylength 60.0
# python PlotTimeDiffVsX.py   -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --pitch 500 --xlength 3.0 --ylength 150.0
# python PlotRecoDiffVsX.py   -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --pitch 500 --xlength 3.0 --ylength 150.0
# python PlotEfficiency.py    -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --xlength 3.0
# python PlotSimpleXYMaps.py  -D EIC_W1_2p5cm_UCSC_330V
# python PlotAmplitudeVsXY.py -D EIC_W1_2p5cm_UCSC_330V --zmin 10.0 --zmax 50.0
# python PlotTimeDiffVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin 0.0 --zmax 120.0
# python PlotTimeMeanVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin -0.5 --zmax 0.5
# python PlotRecoDiffVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin 0.0 --zmax 100.0

## EIC_2p5cm_500up_200uw
echo "Running over EIC_W1_2p5cm_215V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_2p5cm_215V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_2p5cm_215V
cd ../test
./MyAnalysis -A RecoAnalyzer -D EIC_W1_2p5cm_215V
cd ../macros
python FindInputHistos4YReco.py -D EIC_W1_2p5cm_215V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_2p5cm_215V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_2p5cm_215V -A --xmax 0.73 --fitOrder 4
python PlotAmplitudeVsX.py  -D EIC_W1_2p5cm_215V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_2p5cm_215V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_2p5cm_215V --xlength 2.5 --ylength 350.0
python PlotTimeDiffVsXY.py  -D EIC_W1_2p5cm_215V --zmin 35.0 --zmax 150.0
python PlotTimeDiffVsY.py   -D EIC_W1_2p5cm_215V --xlength 15.0 --ylength 350.0
python PlotTimeMeanVsXY.py  -D EIC_W1_2p5cm_215V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_2p5cm_215V
python PlotRecoDiffVsXY.py  -D EIC_W1_2p5cm_215V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_2p5cm_215V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_2p5cm_215V -x 2.5 -r 0
python PlotEfficiency.py    -D EIC_W1_2p5cm_215V -x 2.5 -r 1
python PlotEfficiency.py    -D EIC_W1_2p5cm_215V -x 2.5 -r 2
python plot1DRes.py         -D EIC_W1_2p5cm_215V



## HPK_1cm_80up_45uw
echo "Running over HPK_strips_Eb_45um_170V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_strips_Eb_45um_170V
cd ../macros
python FindDelayCorrections.py -D HPK_strips_Eb_45um_170V
cd ../test
./MyAnalysis -A RecoAnalyzer -D HPK_strips_Eb_45um_170V
cd ../macros
python FindInputHistos4YReco.py -D HPK_strips_Eb_45um_170V
cd ../test
./MyAnalysis -A Analyze -D HPK_strips_Eb_45um_170V
cd ../macros

python DoPositionRecoFit.py -D HPK_strips_Eb_45um_170V -A --xmax 0.63 --fitOrder 5
python PlotAmplitudeVsX.py  -D HPK_strips_Eb_45um_170V --xlength 0.6 --ylength 90.0
python PlotAmplitudeVsXY.py -D HPK_strips_Eb_45um_170V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D HPK_strips_Eb_45um_170V --xlength 0.6 --ylength 150.0
python PlotTimeDiffVsXY.py  -D HPK_strips_Eb_45um_170V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D HPK_strips_Eb_45um_170V --xlength 5.5 --ylength 150.0
python PlotTimeMeanVsXY.py  -D HPK_strips_Eb_45um_170V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D HPK_strips_Eb_45um_170V
python PlotRecoDiffVsXY.py  -D HPK_strips_Eb_45um_170V --zmin 0.0 --zmax 60.0
python PlotRecoDiffVsX.py   -D HPK_strips_Eb_45um_170V --xlength 0.6 --ylength 60.0
python PlotEfficiency.py    -D HPK_strips_Eb_45um_170V -x 0.6 -r 0
python PlotEfficiency.py    -D HPK_strips_Eb_45um_170V -x 0.6 -r 1
python PlotEfficiency.py    -D HPK_strips_Eb_45um_170V -x 0.6 -r 2
python plot1DRes.py         -D HPK_strips_Eb_45um_170V



## EIC_W1_0p5cm_500up_200uw_1_4
echo "Running over EIC_W1_0p5cm_500um_300um_gap_1_4_245V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../test
./MyAnalysis -A RecoAnalyzer -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../macros
python FindInputHistos4YReco.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -A --xmax 0.88 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xlength 2.5 --ylength 120.0
python PlotAmplitudeVsXY.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 20.0 --zmax 120.0
python PlotTimeDiffVsX.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xlength 2.5 --ylength 120.0
python PlotTimeDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xlength 2.5 --ylength 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotRecoDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -x 2.5 -r 0
python PlotEfficiency.py    -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -x 2.5 -r 1
python PlotEfficiency.py    -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -x 2.5 -r 2
python plot1DRes.py         -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V



## BNL2021_V2_?cm_150up_80uw
echo "Running over BNL2021_2022_medium_285V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D BNL2021_2022_medium_285V
cd ../macros
python FindDelayCorrections.py -D BNL2021_2022_medium_285V
cd ../test
./MyAnalysis -A RecoAnalyzer -D BNL2021_2022_medium_285V
cd ../macros
python FindInputHistos4YReco.py -D BNL2021_2022_medium_285V
cd ../test
./MyAnalysis -A Analyze -D BNL2021_2022_medium_285V
cd ../macros

python DoPositionRecoFit.py -D BNL2021_2022_medium_285V -A --xmax 0.82 --fitOrder 4
python PlotAmplitudeVsX.py  -D BNL2021_2022_medium_285V --xlength 0.8 --ylength 180.0
python PlotAmplitudeVsXY.py -D BNL2021_2022_medium_285V --zmin 20.0 --zmax 180.0
python PlotTimeDiffVsX.py   -D BNL2021_2022_medium_285V --xlength 0.8 --ylength 150.0
python PlotTimeDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D BNL2021_2022_medium_285V --xlength 1.5 --ylength 150.0
python PlotTimeMeanVsXY.py  -D BNL2021_2022_medium_285V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D BNL2021_2022_medium_285V
python PlotRecoDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 60.0
python PlotRecoDiffVsX.py   -D BNL2021_2022_medium_285V --xlength 0.8 --ylength 60.0
python PlotEfficiency.py    -D BNL2021_2022_medium_285V -x 0.8 -r 0
python PlotEfficiency.py    -D BNL2021_2022_medium_285V -x 0.8 -r 1
python PlotEfficiency.py    -D BNL2021_2022_medium_285V -x 0.8 -r 2
python plot1DRes.py         -D BNL2021_2022_medium_285V

# # # cd ../test
# # # ./MyAnalysis -A Analyze -D BNL2021_2022_medium_285V
# # # cd ../macros
# # # python DoPositionRecoFit.py -D BNL2021_2022_medium_285V --xmax 0.82 --pitch 150 --fitOrder 4 
# # # python plot1DRes.py         -D BNL2021_2022_medium_285V
# # # python PlotAmplitudeVsX.py  -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --xlength 0.6 --ylength 180.0
# # # python PlotTimeDiffVsX.py   -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --pitch 150 --xlength 0.6 --ylength 80.0
# # # python PlotRecoDiffVsX.py   -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --pitch 150 --xlength 0.6 --ylength 60.0
# # # python PlotEfficiency.py    -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --xlength 0.6
# # # python PlotSimpleXYMaps.py  -D BNL2021_2022_medium_285V
# # # python PlotAmplitudeVsXY.py -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 150.0
# # # python PlotTimeDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 50.0
# # # python PlotTimeMeanVsXY.py  -D BNL2021_2022_medium_285V --zmin -0.2 --zmax 0.2
# # # python PlotRecoDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 20.0

