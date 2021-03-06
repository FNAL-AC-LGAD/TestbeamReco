# TestbeamReco

Setup
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

Can find all dataset options in the `sampleCollections.cfg` and  `sampleSets.cfg ` inside the `test` directory

Recipe to make plots
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

