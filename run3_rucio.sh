#!/bin/bash

TIME_A=`date +%s`

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup rucio
voms-proxy-init -voms atlas -hours 48; voms-proxy-info

#retrieve inputs

rucio download mc15_13TeV:HITS.05608147._000341.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000341.pool.root.1 ./HITS.05608147._000341.pool.root.1
rucio download mc15_13TeV:HITS.05608147._000342.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000342.pool.root.1 ./HITS.05608147._000342.pool.root.1
rucio download mc15_13TeV:HITS.05608147._000343.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000343.pool.root.1 ./HITS.05608147._000343.pool.root.1
rucio download mc15_13TeV:HITS.05608147._000344.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000344.pool.root.1 ./HITS.05608147._000344.pool.root.1
rucio download mc15_13TeV:HITS.05608147._000345.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000345.pool.root.1 ./HITS.05608147._000345.pool.root.1
rucio download mc15_13TeV:HITS.05608147._000346.pool.root.1
ln -fs mc15_13TeV/HITS.05608147._000346.pool.root.1 ./HITS.05608147._000346.pool.root.1
rucio download mc15_13TeV:HITS.05608152._002200.pool.root.1
ln -fs mc15_13TeV/HITS.05608152._002200.pool.root.1 ./HITS.05608152._002200.pool.root.1
rucio download mc15_13TeV:HITS.05608152._002201.pool.root.1
ln -fs mc15_13TeV/HITS.05608152._002201.pool.root.1 ./HITS.05608152._002201.pool.root.1
rucio download mc15_13TeV:HITS.10876973._060157.pool.root.1
ln -fs mc15_13TeV/HITS.10876973._060157.pool.root.1 ./HITS.10876973._060157.pool.root.1
rucio download mc15_13TeV:HITS.10876973._061023.pool.root.1
ln -fs mc15_13TeV/HITS.10876973._061023.pool.root.1 ./HITS.10876973._061023.pool.root.1


TIME_B=`date +%s`
PT=`expr ${TIME_B} - ${TIME_A}`
H=`expr ${PT} / 3600`
PT=`expr ${PT} % 3600`
M=`expr ${PT} / 60`
S=`expr ${PT} % 60`
echo "${H}:${M}:${S}"
