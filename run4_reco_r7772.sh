#!/bin/bash

TIME_A=`date +%s`

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
source $AtlasSetup/scripts/asetup.sh --cmtconfig=x86_64-slc6-gcc49-opt AtlasProd1,20.7.5.1.1
export ATHENA_PROC_NUMBER=16

Reco_tf.py --inputHITSFile="test_1k.HITS.pool.root" --maxEvents="2" --postExec "all:CfgMgr.MessageSvc().setError+=[\"HepMcParticleLink\"]" "ESDtoAOD:fixedAttrib=[s if \"CONTAINER_SPLITLEVEL = \'99\'\" not in s else \"\" for s in svcMgr.AthenaPoolCnvSvc.PoolAttributes];svcMgr.AthenaPoolCnvSvc.PoolAttributes=fixedAttrib" --postInclude "default:RecJobTransforms/UseFrontier.py" --preExec "all:rec.Commissioning.set_Value_and_Lock(True);from AthenaCommon.BeamFlags import jobproperties;jobproperties.Beam.numberOfCollisions.set_Value_and_Lock(20.0);from LArROD.LArRODFlags import larRODFlags;larRODFlags.NumberOfCollisions.set_Value_and_Lock(20);larRODFlags.nSamples.set_Value_and_Lock(4);larRODFlags.doOFCPileupOptimization.set_Value_and_Lock(True);larRODFlags.firstSample.set_Value_and_Lock(0);larRODFlags.useHighestGainAutoCorr.set_Value_and_Lock(True)" "RAWtoESD:from CaloRec.CaloCellFlags import jobproperties;jobproperties.CaloCellFlags.doLArCellEmMisCalib=False" "ESDtoAOD:TriggerFlags.AODEDMSet=\"AODSLIM\"" --preInclude "HITtoRDO:Digitization/ForceUseOfPileUpTools.py,SimulationJobOptions/preInclude.PileUpBunchTrainsMC15_2015_25ns_Config1.py,RunDependentSimData/configLumi_run284500_v2.py" "RDOtoRDOTrigger:RecExPers/RecoOutputMetadataList_jobOptions.py" --skipEvents="0" --autoConfiguration="everything" --conditionsTag "default:OFLCOND-MC15c-SDR-09" --geometryVersion="default:ATLAS-R2-2015-03-01-00" --runNumber="410501" --digiSeedOffset1="14694" --digiSeedOffset2="14694" --digiSteeringConf='StandardSignalOnlyTruth' --AMITag="r7772" --steering="doRDO_TRIG" --inputHighPtMinbiasHitsFile="HITS.05608152._002200.pool.root.1,HITS.05608152._002201.pool.root.1" --inputLowPtMinbiasHitsFile="HITS.05608147._000341.pool.root.1,HITS.05608147._000342.pool.root.1,HITS.05608147._000343.pool.root.1,HITS.05608147._000344.pool.root.1,HITS.05608147._000345.pool.root.1,HITS.05608147._000346.pool.root.1" --numberOfCavernBkg="0" --numberOfHighPtMinBias="0.12268057" --numberOfLowPtMinBias="39.8773194" --pileupFinalBunch="6" --outputAODFile="test_1k.AOD.pool.root" --jobNumber="14694" --triggerConfig="RDOtoRDOTrigger=MCRECO:DBF:TRIGGERDBMC:2046,20,56" --ignorePatterns="Py:TrigConf2COOLLib.py.+ERROR.===================================+"



TIME_B=`date +%s`
PT=`expr ${TIME_B} - ${TIME_A}`
H=`expr ${PT} / 3600`
PT=`expr ${PT} % 3600`
M=`expr ${PT} / 60`
S=`expr ${PT} % 60`
echo "${H}:${M}:${S}"
