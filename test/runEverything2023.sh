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

python PlotAmplitudeVsXY.py -D  BNL_20um_1cm_400um_W3074_1_4_95V --zmin 10.0 --zmax 50.0


##  BNL_20um_1cm_400um_W3075_1_2_80V
echo "Running over  BNL_20um_1cm_400um_W3075_1_2_80V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_20um_1cm_400um_W3075_1_2_80V
cd ../macros
python FindDelayCorrections.py -D BNL_20um_1cm_400um_W3075_1_2_80V
python FindInputHistos4YReco.py -D  BNL_20um_1cm_400um_W3075_1_2_80V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_20um_1cm_400um_W3075_1_2_80V
cd ../macros

python PlotAmplitudeVsXY.py -D  BNL_20um_1cm_400um_W3075_1_2_80V --zmin 10.0 --zmax 50.0


##  BNL_20um_1cm_450um_W3074_2_1_95V
echo "Running over  BNL_20um_1cm_450um_W3074_2_1_95V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_20um_1cm_450um_W3074_2_1_95V
cd ../macros
python FindDelayCorrections.py -D BNL_20um_1cm_450um_W3074_2_1_95V
python FindInputHistos4YReco.py -D  BNL_20um_1cm_450um_W3074_2_1_95V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_20um_1cm_450um_W3074_2_1_95V
cd ../macros

python PlotAmplitudeVsXY.py -D  BNL_20um_1cm_450um_W3074_2_1_95V --zmin 10.0 --zmax 50.0


##  BNL_20um_1cm_450um_W3074_2_1_95V
echo "Running over  BNL_20um_1cm_450um_W3075_2_4_80V sensor"
cd ../test
./MyAnalysis -A InitialAnalyzer -D  BNL_20um_1cm_450um_W3075_2_4_80V
cd ../macros
python FindDelayCorrections.py -D BNL_20um_1cm_450um_W3075_2_4_80V
python FindInputHistos4YReco.py -D  BNL_20um_1cm_450um_W3075_2_4_80V -I
cd ../test
./MyAnalysis -A Analyze -D  BNL_20um_1cm_450um_W3075_2_4_80V
cd ../macros

python PlotAmplitudeVsXY.py -D  BNL_20um_1cm_450um_W3075_2_4_80V --zmin 10.0 --zmax 50.0
