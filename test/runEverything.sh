./MyAnalysis -A Analyze -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xmax 0.85 --pitch 500 --fitOrder 7 
python plot1DRes.py         -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotAmplitudeVsX.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --xlength 3.0 --ylength 130.0
python PlotTimeDiffVsX.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotRecoDiffVsX.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --xlength 3.0
python PlotSimpleXYMaps.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotAmplitudeVsXY.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 0.0 --zmax 120.0
python PlotTimeDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 0.0 --zmax 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin -0.2 --zmax 0.2
python PlotRecoDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --zmin 0.0 --zmax 100.0

cd ../test
./MyAnalysis -A Analyze -D HPK_strips_Eb_45um_170V
cd ../macros
python DoPositionRecoFit.py -D HPK_strips_Eb_45um_170V --xmax 0.62 --pitch 80 --fitOrder 3 
python plot1DRes.py         -D HPK_strips_Eb_45um_170V
python PlotAmplitudeVsX.py  -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --xlength 0.3 --ylength 90.0
python PlotTimeDiffVsX.py   -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --pitch 80 --xlength 0.3 --ylength 150.0
python PlotRecoDiffVsX.py   -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --pitch 80 --xlength 0.3 --ylength 40.0
python PlotEfficiency.py    -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --xlength 0.3
python PlotSimpleXYMaps.py  -D HPK_strips_Eb_45um_170V
python PlotAmplitudeVsXY.py -D HPK_strips_Eb_45um_170V --zmin 0.0 --zmax 80.0
python PlotTimeDiffVsXY.py  -D HPK_strips_Eb_45um_170V --zmin 20.0 --zmax 130.0
python PlotTimeMeanVsXY.py  -D HPK_strips_Eb_45um_170V --zmin -0.2 --zmax 0.2
python PlotRecoDiffVsXY.py  -D HPK_strips_Eb_45um_170V --zmin 0.0 --zmax 30.0

cd ../test
./MyAnalysis -A Analyze -D BNL2021_2022_medium_285V
cd ../macros
python DoPositionRecoFit.py -D BNL2021_2022_medium_285V --xmax 0.82 --pitch 150 --fitOrder 4 
python plot1DRes.py         -D BNL2021_2022_medium_285V
python PlotAmplitudeVsX.py  -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --xlength 0.6 --ylength 180.0
python PlotTimeDiffVsX.py   -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --pitch 150 --xlength 0.6 --ylength 80.0
python PlotRecoDiffVsX.py   -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --pitch 150 --xlength 0.6 --ylength 60.0
python PlotEfficiency.py    -D BNL2021_2022_medium_285V -s BNL_2021 -b 285 --xlength 0.6
python PlotSimpleXYMaps.py  -D BNL2021_2022_medium_285V
python PlotAmplitudeVsXY.py -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 150.0
python PlotTimeDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 50.0
python PlotTimeMeanVsXY.py  -D BNL2021_2022_medium_285V --zmin -0.2 --zmax 0.2
python PlotRecoDiffVsXY.py  -D BNL2021_2022_medium_285V --zmin 0.0 --zmax 20.0

cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_255V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_255V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_255V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_1cm_255V --xmax 0.8 --pitch 500 --fitOrder 7 
python plot1DRes.py         -D EIC_W1_1cm_255V
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_255V -s EIC_W1_1cm -b 255 --xlength 3.0 --ylength 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_255V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_255V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_255V -s EIC_W1_1cm -b 255 --xlength 3.0
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_255V
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_255V --zmin 20.0 --zmax 100.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_255V --zmin 0.0 --zmax 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_255V --zmin -0.5 --zmax 0.5
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_255V --zmin 0.0 --zmax 100.0

cd ../test
./MyAnalysis -A Analyze -D EIC_W1_2p5cm_UCSC_330V 
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_2p5cm_UCSC_330V --xmax 0.85 --pitch 500 --fitOrder 2 
python plot1DRes.py         -D EIC_W1_2p5cm_UCSC_330V
python PlotAmplitudeVsX.py  -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --xlength 3.0 --ylength 60.0
python PlotTimeDiffVsX.py   -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotRecoDiffVsX.py   -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_2p5cm_UCSC_330V -s EIC_W1_25mm_UCSC -b 330 --xlength 3.0
python PlotSimpleXYMaps.py  -D EIC_W1_2p5cm_UCSC_330V
python PlotAmplitudeVsXY.py -D EIC_W1_2p5cm_UCSC_330V --zmin 10.0 --zmax 50.0
python PlotTimeDiffVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin 0.0 --zmax 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin -0.5 --zmax 0.5
python PlotRecoDiffVsXY.py  -D EIC_W1_2p5cm_UCSC_330V --zmin 0.0 --zmax 100.0

cd ../test
./MyAnalysis -A Analyze -D EIC_W1_2p5cm_215V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_2p5cm_215V --xmax 0.75 --pitch 500 --fitOrder 4 
python plot1DRes.py         -D EIC_W1_2p5cm_215V
python PlotAmplitudeVsX.py  -D EIC_W1_2p5cm_215V -s EIC_W1_25mm -b 330 --xlength 3.0 --ylength 40.0
python PlotTimeDiffVsX.py   -D EIC_W1_2p5cm_215V -s EIC_W1_25mm -b 330 --pitch 500 --xlength 3.0 --ylength 350.0
python PlotRecoDiffVsX.py   -D EIC_W1_2p5cm_215V -s EIC_W1_25mm -b 330 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_2p5cm_215V -s EIC_W1_25mm -b 330 --xlength 3.0
python PlotSimpleXYMaps.py  -D EIC_W1_2p5cm_215V
python PlotAmplitudeVsXY.py -D EIC_W1_2p5cm_215V --zmin 10.0 --zmax 50.0
python PlotTimeDiffVsXY.py  -D EIC_W1_2p5cm_215V --zmin 0.0 --zmax 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_2p5cm_215V --zmin -0.5 --zmax 0.5
python PlotRecoDiffVsXY.py  -D EIC_W1_2p5cm_215V --zmin 0.0 --zmax 100.0

cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_all_multiPitch_240V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_1cm_all_multiPitch_240V --xmax 0.8 --pitch 500 --fitOrder 7 
python plot1DRes.py         -D EIC_W1_1cm_all_multiPitch_240V
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --xlength 3.0 --ylength 70.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --pitch 500 --xlength 3.0 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_all_multiPitch_240V -s EIC_W1_1cm -b 255 --xlength 3.0
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_all_multiPitch_240V
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_all_multiPitch_240V --zmin 25.0 --zmax 50.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin 0.0 --zmax 120.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin -0.5 --zmax 0.5
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_all_multiPitch_240V --zmin 0.0 --zmax 100.0


