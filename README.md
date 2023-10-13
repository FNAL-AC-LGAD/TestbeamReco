# TestbeamReco

## Setup
This initial setup must be done once only
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
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -E 100001
```
In this example, `-A` selects the analyzer among a pre-defined list, `-D` is the dataset name (can be found in [`sampleCollections.cfg`](./test/sampleCollections.cfg) and  [`sampleSets.cfg`](./test/sampleSets.cfg)), and `-E` is the number of entries to analyze from the dataset (if it is not given or higher than the total, it will stop at the final entry automatically).


## Making plots

The analyzer returns a rough version of the plots of interest. To obtain the final plots with a defined style we use a set of python macros.

Using a sensor as reference (HPK_W5_17_2_50T_1P0_500P_50M_E600_190V), the recipe to make some plots of interest is:
```
cd <WorkingArea>/TestbeamReco/test
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
cd ../macros

python DoPositionRecoFit.py       -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -A --xmax 0.85 --fitOrder 5
python Plot_AmplitudeVsX.py       -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V --xlength 2.7 --ylength 170.0
python Plot_SimpleXYMaps.py       -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python Plot_CutFlow.py            -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python Plot_Resolution1D.py       -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t
python Plot_Efficiency.py         -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7
python Plot_ResolutionXRecoVsX.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7
python Plot_ResolutionTimeVsX.py  -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V -t -x 2.7 -y 100
```

The whole analysis for a specific set of sensors can be obtained by using one of the bash scripts found [`here`](./test/sh/).
Example:
```
cd <WorkingArea>/TestbeamReco/test/sh/
./runEverything2023_MayStrips.sh
```
Feel free to edit the lists in the scripts to run a subset only if required.
