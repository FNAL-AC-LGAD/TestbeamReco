cd ../../test
# HPK_20um_500x500um_2x2pad_E600_FNAL_105V
echo "Running over HPK_20um_500x500um_2x2pad_E600_FNAL_105V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
cd ../macros
python FindDelayCorrections.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
python FindInputHistos4YReco.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
cd ../macros

# python DoPositionRecoFit.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -A --xmax 0.79 --fitOrder 5
# python PlotAmplitudeVsX.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 2.5 --ylength 100.0
# python PlotAmplitudeVsXY.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 20.0 --zmax 100.0
# python PlotTimeDiffVsX.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 10.0 --zmax 50.0
# python PlotTimeDiffVsY.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 6.0 --ylength 150.0
# python PlotTimeMeanVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# python PlotRecoDiffVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --zmin 0.0 --zmax 100.0
# python PlotRecoDiffVsX.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 2.5 --ylength 150.0
# python PlotEfficiency.py            -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 2.5
# python plot1DRes.py                 -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
# python PlotRecoDiffVsY.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xlength 5.6 --ylength 4.0
# python PlotCutFlow.py               -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V

# Paper plots
python Paper_1DRes.py     --runPad  -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V
python Paper_Efficiency.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 0.7 -y 50.0
# python Paper_Efficiency.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V --xLow 0.0 --xHigh 2.0
# python Paper_XRes.py                -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -x 2.5

python Paper_1DRes.py     --runPad  -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t
python Paper_Efficiency.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_20um_500x500um_2x2pad_E600_FNAL_105V -t -x 0.7 -y 50.0


# HPK_30um_500x500um_2x2pad_E600_FNAL_140V
echo "Running over HPK_30um_500x500um_2x2pad_E600_FNAL_140V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
cd ../macros
python FindDelayCorrections.py -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
python FindInputHistos4YReco.py -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
cd ../macros

# python DoPositionRecoFit.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -A --xmax 0.79 --fitOrder 5
# python PlotAmplitudeVsX.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 2.5 --ylength 100.0
# python PlotAmplitudeVsXY.py         -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 20.0 --zmax 100.0
# python PlotTimeDiffVsX.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 10.0 --zmax 50.0
# python PlotTimeDiffVsY.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 6.0 --ylength 150.0
# python PlotTimeMeanVsXY.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# python PlotRecoDiffVsXY.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --zmin 0.0 --zmax 100.0
# python PlotRecoDiffVsX.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 2.5 --ylength 150.0
# python PlotEfficiency.py            -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 2.5
# python plot1DRes.py                 -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
# python PlotRecoDiffVsY.py           -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xlength 5.6 --ylength 4.0
# python PlotCutFlow.py               -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V

# Paper plots
python Paper_1DRes.py     --runPad  -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V
python Paper_Efficiency.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 0.7 -y 50.0
# python Paper_Efficiency.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V --xLow 0.0 --xHigh 2.0
# python Paper_XRes.py                -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -x 2.5

python Paper_1DRes.py     --runPad  -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t
python Paper_Efficiency.py          -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_30um_500x500um_2x2pad_E600_FNAL_140V -t -x 0.7 -y 50.0


# HPK_50um_500x500um_2x2pad_E600_FNAL_190V
echo "Running over HPK_50um_500x500um_2x2pad_E600_FNAL_190V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
cd ../macros
python FindDelayCorrections.py -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
python FindInputHistos4YReco.py -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
cd ../macros

# python DoPositionRecoFit.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -A --xmax 0.79 --fitOrder 5
# python PlotAmplitudeVsX.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 2.5 --ylength 100.0
# python PlotAmplitudeVsXY.py         -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 20.0 --zmax 100.0
# python PlotTimeDiffVsX.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 10.0 --zmax 50.0
# python PlotTimeDiffVsY.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 6.0 --ylength 150.0
# python PlotTimeMeanVsXY.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# python PlotRecoDiffVsXY.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --zmin 0.0 --zmax 100.0
# python PlotRecoDiffVsX.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 2.5 --ylength 150.0
# python PlotEfficiency.py            -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 2.5
# python plot1DRes.py                 -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
# python PlotRecoDiffVsY.py           -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xlength 5.6 --ylength 4.0
# python PlotCutFlow.py               -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V

# Paper plots
python Paper_1DRes.py     --runPad  -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V
python Paper_Efficiency.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 0.7 -y 50.0
# python Paper_Efficiency.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V --xLow 0.0 --xHigh 2.0
# python Paper_XRes.py                -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -x 2.5

python Paper_1DRes.py     --runPad  -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t
python Paper_Efficiency.py          -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t -x 0.7
python Paper_PlotTimeDiffVsX.py     -D HPK_50um_500x500um_2x2pad_E600_FNAL_190V -t -x 0.7 -y 50.0



# # Run Bias Scans
# echo "Running full bias scan results"
# cd ../test
# ./MyAnalysis -A Analyze -D HPK_50um_500x500um_2x2pad_E600_FNAL
# ./MyAnalysis -A Analyze -D HPK_30um_500x500um_2x2pad_E600_FNAL
# ./MyAnalysis -A Analyze -D HPK_20um_500x500um_2x2pad_E600_FNAL
# cd ../macros
# python PlotBiasScans.py -D HPK_50um_500x500um_2x2pad_E600_FNAL
