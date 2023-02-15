## HPK_20um_500x500um_2x2pad_E600_FNAL_100V
echo "Running over HPK_20um_500x500um_2x2pad_E600_FNAL_100V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
cd ../macros
python FindDelayCorrections.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
python FindInputHistos4YReco.py -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V -I
cd ../test
./MyAnalysis -A Analyze -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
cd ../macros

python DoPositionRecoFit.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V -A --xmax 0.79 --fitOrder 5
python PlotAmplitudeVsX.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --xlength 2.5 --ylength 100.0
python PlotAmplitudeVsXY.py         -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --zmin 20.0 --zmax 100.0
python PlotTimeDiffVsX.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --xlength 6.0 --ylength 150.0
python PlotTimeMeanVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
python PlotRecoDiffVsXY.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py            -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V -x 2.5
python plot1DRes.py                 -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
python PlotRecoDiffVsY.py           -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V --xlength 5.6 --ylength 4.0
python PlotCutFlow.py               -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V

# Paper plots
python Paper_1DRes.py               -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V
python Paper_Efficiency.py          -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V -x 2.5
python Paper_XRes.py                -D HPK_20um_500x500um_2x2pad_E600_FNAL_100V -x 2.5
