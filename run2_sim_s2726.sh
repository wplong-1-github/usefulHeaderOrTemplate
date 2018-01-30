#!/bin/bash

TIME_A=`date +%s`

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
source $AtlasSetup/scripts/asetup.sh --cmtconfig=x86_64-slc6-gcc47-opt AtlasProduction 19.2.4.9 here


# --AMITag="a766" s2726
Sim_tf.py --inputEVNTFile="/users/peilongw/Project/MC-Filter-Study/Derivation/test_1k.EVNT.pool.root" --AMITag="s2726" --DBRelease="default:current" --DataRunNumber="222525" --conditionsTag "default:OFLCOND-RUN12-SDR-19" --firstEvent="1" --geometryVersion="default:ATLAS-R2-2015-03-01-00_VALIDATION" --maxEvents="2" --outputHITSFile="test_1k.HITS.pool.root" --physicsList="FTFP_BERT" --postInclude "default:PyJobTransforms/UseFrontier.py" --preInclude "EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py" --randomSeed="1" --runNumber="410501" --simulator="MC12G4" --skipEvents="0" --truthStrategy="MC15aPlus"



TIME_B=`date +%s`
PT=`expr ${TIME_B} - ${TIME_A}`
H=`expr ${PT} / 3600`
PT=`expr ${PT} % 3600`
M=`expr ${PT} / 60`
S=`expr ${PT} % 60`
echo "${H}:${M}:${S}"
