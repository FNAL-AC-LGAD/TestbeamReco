##  BNL_50um_1cm_450um_W3051_2_2_170V
echo "Running over  BNL_50um_1cm_450um_W3051_2_2_170V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_50um_1cm_450um_W3051_2_2_170V
cd ../macros
python FindDelayCorrections.py -D BNL_50um_1cm_450um_W3051_2_2_170V
python FindInputHistos4YReco.py -D  BNL_50um_1cm_450um_W3051_2_2_170V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_50um_1cm_450um_W3051_2_2_170V
cd ../macros

python PlotAmplitudeVsXY.py         -D  BNL_50um_1cm_450um_W3051_2_2_170V --zmin 7.0 --zmax 50.0


##  BNL_50um_1cm_450um_W3052_2_4_185V
echo "Running over  BNL_50um_1cm_450um_W3052_2_4_185V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_50um_1cm_450um_W3052_2_4_185V
cd ../macros
python FindDelayCorrections.py -D BNL_50um_1cm_450um_W3052_2_4_185V
python FindInputHistos4YReco.py -D  BNL_50um_1cm_450um_W3052_2_4_185V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_50um_1cm_450um_W3052_2_4_185V
cd ../macros

python PlotAmplitudeVsXY.py         -D  BNL_50um_1cm_450um_W3052_2_4_185V --zmin 7.0 --zmax 50.0


##  BNL_20um_1cm_400um_W3074_1_4_95V
echo "Running over  BNL_20um_1cm_400um_W3074_1_4_95V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_20um_1cm_400um_W3074_1_4_95V
cd ../macros
python FindDelayCorrections.py -D BNL_20um_1cm_400um_W3074_1_4_95V
python FindInputHistos4YReco.py -D  BNL_20um_1cm_400um_W3074_1_4_95V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_20um_1cm_400um_W3074_1_4_95V
cd ../macros

python PlotAmplitudeVsXY.py         -D  BNL_20um_1cm_400um_W3074_1_4_95V --zmin 7.0 --zmax 50.0


