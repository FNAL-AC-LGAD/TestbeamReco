./MyAnalysis -A InitialAnalyzer -D EIC_W1_1cm_255V
cd ../macros
python FindDelayCorrections.py -D EIC_W1_1cm_255V
cd ../test
./MyAnalysis -A Analyze -D EIC_W1_1cm_255V

