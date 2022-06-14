./MyAnalysis -A InitialAnalyzer -D EIC_W1_2p5cm_215V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_2p5cm_215V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_2p5cm_215V

