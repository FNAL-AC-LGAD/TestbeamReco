#!/bin/bash

#########
# ./plotAnalyze.sh <sensor_name> <x_axis_limits>
#
# EG: ./plotAnalyze.sh EIC_W1_1cm_255V 3.0
#########

INPUTARRAY=("$@")

SENSORNAME=${INPUTARRAY[0]}
XLIM=${INPUTARRAY[1]}

python PlotRecoDiffVsX.py -D ${SENSORNAME} -x ${XLIM} -y 150 -d
python PlotEfficiency.py -D ${SENSORNAME} -x ${XLIM} -r 0
python PlotEfficiency.py -D ${SENSORNAME} -x ${XLIM} -r 1
python PlotEfficiency.py -D ${SENSORNAME} -x ${XLIM} -r 2
python plot1DRes.py -D ${SENSORNAME}
