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
python PlotAmplitudeVsXY.py -D HPK_strips_Eb_45um_170V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D HPK_strips_Eb_45um_170V --xlength 0.6 --ylength 150.0
python PlotTimeDiffVsXY.py  -D HPK_strips_Eb_45um_170V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D HPK_strips_Eb_45um_170V --xlength 5.5 --ylength 150.0
