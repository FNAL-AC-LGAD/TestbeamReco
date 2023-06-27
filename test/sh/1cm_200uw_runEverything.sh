#!/bin/bash
## EIC_W1_1cm_500up_200uw_255V

cd ../../test
if [ $# == 0 ]
then
echo "Running over EIC_W1_1cm_500up_200uw_255V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_500up_200uw_255V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_500up_200uw_255V
python FindInputHistos4YReco.py -D EIC_W1_1cm_500up_200uw_255V -I
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_500up_200uw_255V
echo "Analyzer finished"
fi

if [ $# == 0 ] || [ "$1" == "-q" ]
then
cd ../macros
#python DoPositionRecoFit.py -D EIC_W1_1cm_500up_200uw_255V -A --xmax 0.88 --fitOrder 5
#python PlotAmplitudeVsX.py  -D EIC_W1_1cm_500up_200uw_255V --xlength 2.5 --ylength 120.0
#python PlotAmplitudeVsXY.py -D EIC_W1_1cm_500up_200uw_255V --zmin 20.0 --zmax 120.0
python PlotTimeDiffVsX.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 5.2 --ylength 4000.0
#python PlotTimeDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin 25.0 --zmax 75.0
python PlotTimeDiffVsY.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 5.2 --ylength 4000.0
#python PlotTimeMeanVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin -0.5 --zmax 0.5
#python PlotSimpleXYMaps.py  -D EIC_W1_1cm_500up_200uw_255V
#python PlotRecoDiffVsXY.py  -D EIC_W1_1cm_500up_200uw_255V --zmin 0.0 --zmax 100.0
python PlotRecoDiffVsX.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 5.2 --ylength 4000.0
python PlotRecoDiffVsY.py   -D EIC_W1_1cm_500up_200uw_255V --xlength 5.2 --ylength 4000.0
#python PlotEfficiency.py    -D EIC_W1_1cm_500up_200uw_255V -x 2.5
#python plot1DRes.py         -D EIC_W1_1cm_500up_200uw_255V
fi

if [ $# == 0 ] || [ "$1" == "-q" ] || [ "$1" == "-d" ]
then
root -e "TFile *f = new TFile(\"../output/EIC_W1_1cm_500up_200uw_255V/EIC_W1_1cm_500up_200uw_255V_Analyze.root\",\"r\");\
TCanvas *c1 = new TCanvas(\"c1\",\"c1\",1400,500);\
c1->Divide(2);\
c1->cd(1);\
Yreco_vs_Ytrack->Draw(\"colz\");\
c1->cd(2);\
Yreco_vs_Ytrack->Draw();"
fi