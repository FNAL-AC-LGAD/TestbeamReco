cd ../../test
## EIC_W1_1cm_500up_200uw_205V
echo "Running over EIC_W1_1cm_500up_200uw_205V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_205V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_205V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_205V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_205V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_205V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_205V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_205V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_205V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_205V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_205V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_205V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_205V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_205V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_205V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_205V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_205V

## EIC_W1_1cm_500up_200uw_215V
echo "Running over EIC_W1_1cm_500up_200uw_215V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_215V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_215V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_215V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_215V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_215V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_215V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_215V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_215V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_215V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_215V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_215V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_215V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_215V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_215V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_215V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_215V

## EIC_W1_1cm_500up_200uw_225V
echo "Running over EIC_W1_1cm_500up_200uw_225V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_225V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_225V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_225V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_225V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_225V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_225V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_225V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_225V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_225V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_225V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_225V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_225V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_225V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_225V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_225V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_225V

## EIC_W1_1cm_500up_200uw_235V
echo "Running over EIC_W1_1cm_500up_200uw_235V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_235V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_235V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_235V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_235V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_235V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_235V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_235V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_235V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_235V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_235V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_235V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_235V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_235V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_235V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_235V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_235V

## EIC_W1_1cm_500up_200uw_245V
echo "Running over EIC_W1_1cm_500up_200uw_245V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_245V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_245V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_245V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_245V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_245V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_245V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_245V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_245V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_245V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_245V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_245V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_245V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_245V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_245V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_245V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_245V

# ## EIC_W1_1cm_500up_200uw_250V
# echo "Running over EIC_W1_1cm_500up_200uw_250V sensor"
# cd ../test
# ./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_250V
# cd ../macros
# python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_250V
# python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_250V -I
# cd ../test
# ./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_250V
# cd ../macros

# python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_250V -A --xmax 0.81 --fitOrder 5
# python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_250V --xlength 2.5 --ylength 90.0
# python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_250V --zmin 20.0 --zmax 90.0
# python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_250V --xlength 2.5 --ylength 150.0
# python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_250V --zmin 25.0 --zmax 75.0
# python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_250V --xlength 5.2 --ylength 150.0
# python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_250V --zmin -0.5 --zmax 0.5
# python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_250V
# python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_250V --zmin 0.0 --zmax 100.0
# python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_250V --xlength 2.5 --ylength 150.0
# python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_250V -x 2.5
# python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_250V

## EIC_W1_1cm_500up_200uw_265V
echo "Running over EIC_W1_1cm_500up_200uw_265V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_265V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_265V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_265V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_265V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_265V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_265V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_265V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_265V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_265V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_265V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_265V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_265V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_265V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_265V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_265V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_265V
