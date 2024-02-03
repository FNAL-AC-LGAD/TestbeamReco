make clean
make -j4
./MyAnalysis -A Analyze -D HPK_W11_22_3_20T_500x500_150M_C600_116V
./MyAnalysis -A Analyze -D HPK_W9_22_3_20T_500x500_150M_E600_112V
./MyAnalysis -A Analyze -D HPK_W5_1_1_50T_500x500_150M_E600_185V
./MyAnalysis -A Analyze -D HPK_W9_23_3_20T_500x500_300M_E600_112V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_186V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_188V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_192V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_194V
./MyAnalysis -A Analyze -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
./MyAnalysis -A Analyze -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V

python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W11_22_3_20T_500x500_150M_C600_116V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W9_22_3_20T_500x500_150M_E600_112V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W5_1_1_50T_500x500_150M_E600_185V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W9_23_3_20T_500x500_300M_E600_112V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W9_14_2_20T_1P0_500P_100M_E600_112V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python ../macros/Plot_AmplitudeVsXY_Metal.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
python ../macros/Plot_AllQuantities.py

HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
make clean
make -j4
./MyAnalysis -A Analyze -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
cd ../output/HPK_W9_15_4_20T_0P5_500P_50M_E600_110V/
mkdir waveforms
cd ../../test/
mv ./waveform* ../output/HPK_W9_15_4_20T_0P5_500P_50M_E600_110V/waveforms/
python ../macros/PlotWaveformsFromCSV.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
./MyAnalysis -A Analyze -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
cd ../output/HPK_W5_17_2_50T_1P0_500P_50M_E600_190V/
mkdir waveforms
cd ../../test/
mv ./waveform* ../output/HPK_W5_17_2_50T_1P0_500P_50M_E600_190V/waveforms/
python ../macros/PlotWaveformsFromCSV.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
./MyAnalysis -A Analyze -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
cd ../output/HPK_W9_15_2_20T_1P0_500P_50M_E600_114V/
mkdir waveforms
cd ../../test/
mv ./waveform* ../output/HPK_W9_15_2_20T_1P0_500P_50M_E600_114V/waveforms/
python ../macros/PlotWaveformsFromCSV.py -D HPK_W9_15_2_20T_1P0_500P_50M_E600_114V
python ../macros/PlotWaveformsFromCSV.py -D HPK_W5_17_2_50T_1P0_500P_50M_E600_190V
python ../macros/PlotWaveformsFromCSV.py -D HPK_W9_15_4_20T_0P5_500P_50M_E600_110V
