
#Setup env from cvmfs
source /cvmfs/sft.cern.ch/lcg/views/LCG_99cuda/x86_64-centos7-gcc8-opt/setup.sh

#Add scripts direcotry to path
SCRIPTSDIR=${PWD}/../scripts
if [[ $PATH != *"${SCRIPTSDIR}"* ]]
then
    export PATH=${SCRIPTSDIR}:${PATH}
    echo "adding ${SCRIPTSDIR} to the path"
fi

