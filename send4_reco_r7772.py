#!/usr/bin/env python                                                                                                                                                           
#SBATCH -J Reco # job name                                                                                                                                                     
#SBATCH -o log_reco-%A_%a.out                                                                                                                                                  
#SBATCH -e log_reco-%A_%a.out                                                                                                                                                  
#SBATCH -p parallel-short


# submitted to highmem node

"""                                                                                                                                                                             
this script submits generation of a "huge" number of events using slurm arrays                                                                                                  
to submit just run this:                                                                                                                                                        
$ sbatch -a 1-N ./launch_slurm_array.py                                                                                                                                         
where N is the number of jobs you want to submit (has to be tuned with the variable 'numevents_pertask'                                                                         
in order to produce the total number of events you want                                                                                                                         
"""

import os
import subprocess

if __name__ == '__main__':
    # command template                                                                                      #parallel-medium
                                                                        
    # since we are generating events in chunks we need a different random seed for each chunk                                                                                   
    command_template ='export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase; source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh; source $AtlasSetup/scripts/asetup.sh --cmtconfig=x86_64-slc6-gcc49-opt AtlasProd1,20.7.5.1.1; export ATHENA_PROC_NUMBER=16; Reco_tf.py --inputHITSFile="/users/peilongw/Project/MC-Filter-Study/Derivation/aug_27_17/sim_%s/test_100k_%s.HITS.pool.root" --maxEvents="2000" --postExec "all:CfgMgr.MessageSvc().setError+=[\\"HepMcParticleLink\\"]" "ESDtoAOD:fixedAttrib=[s if \\"CONTAINER_SPLITLEVEL = \\\'99\\\'\\" not in s else \\"\\" for s in svcMgr.AthenaPoolCnvSvc.PoolAttributes];svcMgr.AthenaPoolCnvSvc.PoolAttributes=fixedAttrib" --postInclude "default:RecJobTransforms/UseFrontier.py" --preExec "all:rec.Commissioning.set_Value_and_Lock(True);from AthenaCommon.BeamFlags import jobproperties;jobproperties.Beam.numberOfCollisions.set_Value_and_Lock(20.0);from LArROD.LArRODFlags import larRODFlags;larRODFlags.NumberOfCollisions.set_Value_and_Lock(20);larRODFlags.nSamples.set_Value_and_Lock(4);larRODFlags.doOFCPileupOptimization.set_Value_and_Lock(True);larRODFlags.firstSample.set_Value_and_Lock(0);larRODFlags.useHighestGainAutoCorr.set_Value_and_Lock(True)" "RAWtoESD:from CaloRec.CaloCellFlags import jobproperties;jobproperties.CaloCellFlags.doLArCellEmMisCalib=False" "ESDtoAOD:TriggerFlags.AODEDMSet=\\"AODSLIM\\"" --preInclude "HITtoRDO:Digitization/ForceUseOfPileUpTools.py,SimulationJobOptions/preInclude.PileUpBunchTrainsMC15_2015_25ns_Config1.py,RunDependentSimData/configLumi_run284500_v2.py" "RDOtoRDOTrigger:RecExPers/RecoOutputMetadataList_jobOptions.py" --skipEvents="0" --autoConfiguration="everything" --conditionsTag "default:OFLCOND-MC15c-SDR-09" --geometryVersion="default:ATLAS-R2-2015-03-01-00" --runNumber="410501" --digiSeedOffset1="14694" --digiSeedOffset2="14694" --digiSteeringConf="StandardSignalOnlyTruth" --AMITag="r7772" --steering="doRDO_TRIG" --inputHighPtMinbiasHitsFile="HITS.05608152._002200.pool.root.1,HITS.05608152._002201.pool.root.1" --inputLowPtMinbiasHitsFile="HITS.05608147._000341.pool.root.1,HITS.05608147._000342.pool.root.1,HITS.05608147._000343.pool.root.1,HITS.05608147._000344.pool.root.1,HITS.05608147._000345.pool.root.1,HITS.05608147._000346.pool.root.1" --numberOfCavernBkg="0" --numberOfHighPtMinBias="0.12268057" --numberOfLowPtMinBias="39.8773194" --pileupFinalBunch="6" --outputAODFile="test_100k_%s.AOD.pool.root" --jobNumber="14694" --triggerConfig="RDOtoRDOTrigger=MCRECO:DBF:TRIGGERDBMC:2046,20,56" --ignorePatterns="Py:TrigConf2COOLLib.py.+ERROR.===================================+"'

    # rucio command

    command_rucio = 'ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000341.pool.root.1 ./HITS.05608147._000341.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000342.pool.root.1 ./HITS.05608147._000342.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000343.pool.root.1 ./HITS.05608147._000343.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000344.pool.root.1 ./HITS.05608147._000344.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000345.pool.root.1 ./HITS.05608147._000345.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608147._000346.pool.root.1 ./HITS.05608147._000346.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608152._002200.pool.root.1 ./HITS.05608152._002200.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.05608152._002201.pool.root.1 ./HITS.05608152._002201.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.10876973._060157.pool.root.1 ./HITS.10876973._060157.pool.root.1;ln -fs /users/peilongw/Project/MC-Filter-Study/Derivation/mc15_13TeV/HITS.10876973._061023.pool.root.1 ./HITS.10876973._061023.pool.root.1'

    # "build" the array                                                                                                                                                         
    SLURM_ARRAY_TASK_ID=os.environ["SLURM_ARRAY_TASK_ID"]

    actual_command = command_template % (SLURM_ARRAY_TASK_ID, SLURM_ARRAY_TASK_ID, SLURM_ARRAY_TASK_ID)

    dirname = 'reco_' + SLURM_ARRAY_TASK_ID

#    print('  Task ID: {}'.format(SLURM_ARRAY_TASK_ID))
#    print('  command: {}'.format(actual_command))

    os.system('cd /users/peilongw/Project/MC-Filter-Study/Derivation/aug_27_17')
    os.mkdir(dirname)
    os.system('cd {0}'.format(dirname))
    os.system('{0}'.format(command_rucio))
    os.system('{0}'.format(actual_command))
