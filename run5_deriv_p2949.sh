#!/bin/bash

TIME_A=`date +%s`

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
source $AtlasSetup/scripts/asetup.sh 20.7.8.7,AtlasDerivation,here

#Reco_tf.py --inputEVNTFile evgen.root --outputDAODFile pool.root --reductionConf TRUTH1
Reco_tf.py --inputAODFile test_1k.AOD.pool.root --outputDAODFile test_1k.pool.root --reductionConf HIGG5D2

TIME_B=`date +%s`
PT=`expr ${TIME_B} - ${TIME_A}`
H=`expr ${PT} / 3600`
PT=`expr ${PT} % 3600`
M=`expr ${PT} / 60`
S=`expr ${PT} % 60`
echo "${H}:${M}:${S}"
