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


## Example Code

Recipe to make plots for:
* BNL 5mm long strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
cd ../macros
python DoPositionRecoFit.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V --xmax 0.85 --pitch 500 --fitOrder 7 
python plot1DRes.py         -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotAmplitudeVsX.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --xlength 4.0 --ylength 150.0
python PlotAmplitudeVsXY.py -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotTimeDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotTimeMeanVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotRecoDiffVsX.py   -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --pitch 500 --xlength 4.0 --ylength 150.0
python PlotRecoDiffVsXY.py  -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V
python PlotEfficiency.py    -D EIC_W1_0p5cm_500um_300um_gap_1_4_245V -s EIC_W1_5mm -b 245 --xlength 4.0
```
* HPK Eb strip sensor
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -D HPK_strips_Eb_45um_170V
cd ../macros
python DoPositionRecoFit.py -D HPK_strips_Eb_45um_170V --xmax 0.65 --pitch 80 --fitOrder 2 
python plot1DRes.py         -D HPK_strips_Eb_45um_170V
python PlotAmplitudeVsX.py  -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --xlength 0.5 --ylength 100.0
python PlotAmplitudeVsXY.py -D HPK_strips_Eb_45um_170V
python PlotTimeDiffVsXY.py  -D HPK_strips_Eb_45um_170V
python PlotTimeMeanVsXY.py  -D HPK_strips_Eb_45um_170V
python PlotRecoDiffVsX.py   -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --pitch 80 --xlength 0.5 --ylength 40.0
python PlotRecoDiffVsXY.py  -D HPK_strips_Eb_45um_170V
python PlotEfficiency.py    -D HPK_strips_Eb_45um_170V -s HPK_Eb -b 170 --xlength 0.5
```
