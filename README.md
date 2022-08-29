# TestbeamReco

## Setup
This initial setup must be done only once
```
cd <WorkingArea>
git clone git@github.com:FNAL-AC-LGAD/TestbeamReco.git
cd TestbeamReco/test
source setup.sh
./configure
make clean
make -j4
```

Later, everytime you make a change, must run
```
cd <WorkingArea>/TestbeamReco/test
source setup.sh
make -j4
```

Example of running MyAnalysis interactively
```
cd <WorkingArea>/TestbeamReco/test
source setup.sh
./MyAnalysis -A Analyze -D EIC_W1_1cm_255V -E 100001
```

Can find all dataset names in [`sampleCollections.cfg`](./test/sampleCollections.cfg) and  [`sampleSets.cfg`](./test/sampleSets.cfg) inside the `test` directory.


## Making plots

Recipe to make plots for:
* EIC 1cm long strip 500um pitch 200um metal width (EIC_W1_1cm_500up_200uw_255V)
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -D EIC_W1_1cm_255V
cd ../macros

python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_255V -A --xmax 0.81 --fitOrder 5
python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_255V --xlength 2.5 --ylength 90.0
python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_255V --zmin 20.0 --zmax 90.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 2.5 --ylength 150.0
python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 5.2 --ylength 150.0
python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin -0.5 --zmax 0.5
python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_255V
python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 2.5 --ylength 150.0
python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_255V -x 2.5
python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_255V
python PlotRecoDiffVsY.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 10.0 --ylength 3500.0
```

To get all plots for all sensors, run:
```
cd <WorkingArea>/TestbeamReco/test
./runEverything.sh
```
