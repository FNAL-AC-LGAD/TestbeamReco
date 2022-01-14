# TestbeamReco

## Setup
```
cd <WorkingArea>
git clone git@github.com:FNAL-AC-LGAD/TestbeamReco.git
cd TestbeamReco/test
source setup.sh
./configure
make clean
make -j4
```

Example of running MyAnalysis interactively
```
cd <WorkingArea>/TestbeamReco/test
source setup.sh
./MyAnalysis -A Analyze -H myoutputfile.root -D BNL2020_220V -E 100001
```

Can find all dataset options in the [`sampleCollections.cfg`](./test/sampleCollections.cfg) and  [`sampleSets.cfg`](./test/sampleSets.cfg) inside the `test` directory.

## Final plots

Almost all of the 'Final' files have three common options:
  - f : Input file name (**with** `.root` extension) from [test directory](./test/).
  - s : Sensor name (BNL2020, 'HPK C2', ...) for the top header label.
  - b : Bias voltage of the data set (220, 285, ...) for the top header label.

Recreate final plots for:
* BNL strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H <file_name>.root -D BNL2020_220V
cd ../macros
python WavePlot.py -f <file_name>.root
python plot1DRes.py -f <file_name>.root
python Final_1dAmplitude.py -f <file_name>.root -s BNL2020 -b 220
python FinalBNLs_PlotEfficiency.py -f <file_name>.root -s BNL2020 -b 220
python FinalBNLs_PlotAmplitudeVsX.py -f <file_name>.root -s BNL2020 -b 220
python FinalBNLs_DoPositionRecoFit.py -f <file_name>.root --xmax 0.77 --pitch 100 --fitOrder 4
python FinalBNLs_PlotXRecoDiffVsX.py -f <file_name>.root -s BNL2020 -b 220
python FinalBNLs_PlotTimeDiffVsX.py -f <file_name>.root -s BNL2020 -b 220
```

* HPK pad sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H <file_name>.root -D HPK_pad_C2_180V 
cd ../macros
python plot1DRes.py -f <file_name>.root -m 0.7 -M 0.7
python FinalHPKp_PlotAmplitudeVsXandY_Pad.py -f <file_name>.root -s 'HPK C2' -b 180
python FinalHPKp_DoPositionRecoFit_Pad.py -f <file_name>.root -s 'HPK C2' -b 180
python FinalHPKp_PlotXRecoDiffVsX.py -f <file_name>.root -s 'HPK C2' -b 180
python FinalHPKp_PlotTimeDiffVsXandY_Pad.py -f <file_name>.root -s 'HPK C2' -b 180
```

* HPK strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H <file_name>.root -D HPK_strips_C2_45um_170V 
cd ../macros
python Final_1dAmplitude.py -f <file_name>.root -s 'HPK C2 45#mum' -b 170
```

* Resolution summary plots
```
python resolution_vs_bias.py -s BNL2020
python resolution_vs_bias.py -s BNL2021
python resolution_vs_bias_HPKB2_pad.py
python resolution_vs_bias_HPKC2_pad.py
```

## Old test plots

Recipe to make plots for:
* BNL strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H myoutputfile.root -D BNL2020_220V
cd ../macros
python DoPositionRecoFit.py --xmax 0.75 --pitch 100 --fitOrder 4
python plot1DRes.py
python PlotAmplitudeVsX.py --run
python PlotAmplitudeVsX.py --run -t
python PlotEfficiency.py
python PlotTimeDiffVsXY.py
python PlotTimeDiffVsX.py
python PlotXRecoDiffVsX.py
```
* HPK pad sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H myoutputfile.root -D HPK_pad_C2_180V 
cd ../macros
python DoPositionRecoFit_Pad.py
python plot1DRes.py --runPad 
python PlotBaselineRMSvsXandY_Pad.py 
python PlotAmplitudeVsXandY_Pad.py 
python PlotAmplitudeVsXandY_Pad.py -t
python PlotTimeDiffVsXandY_Pad.py
python PlotXRecoDiffVsX.py --runPad 
python PlotYRecoDiffVsY.py
```
* HPK strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -H myoutputfile.root -D HPK_strips_C2_45um_170V 
cd ../macros
python Final_1dAmplitude.py
python plot1DRes.py
python PlotAmplitudeVsX.py --run
python PlotAmplitudeVsX.py --run -t
```
