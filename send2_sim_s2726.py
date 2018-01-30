#!/usr/bin/env python                                                                                                                                                           
#SBATCH -J Sim # job name                                                                                                                                                     
#SBATCH -o log_sim-%A_%a.out                                                                                                                                                  
#SBATCH -e log_sim-%A_%a.out                                                                                                                                                  
#SBATCH -p parallel-short

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
    # command template                                                                                                                                                          
    # since we are generating events in chunks we need a different random seed for each chunk                                                                                   
    command_template = 'export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase; source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh; source $AtlasSetup/scripts/asetup.sh --cmtconfig=x86_64-slc6-gcc47-opt AtlasProduction 19.2.4.9 here; Sim_tf.py --inputEVNTFile="/users/flosterzo/public/evnt_files/split_50evPerFile_20170827/ttbar_410501_%s.EVNT.pool.root" --AMITag="s2726" --DBRelease="default:current" --DataRunNumber="222525" --conditionsTag "default:OFLCOND-RUN12-SDR-19" --firstEvent="%d" --geometryVersion="default:ATLAS-R2-2015-03-01-00_VALIDATION" --maxEvents="2000" --outputHITSFile="test_100k_%s.HITS.pool.root" --physicsList="FTFP_BERT" --postInclude "default:PyJobTransforms/UseFrontier.py" --preInclude "EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py" --randomSeed="1" --runNumber="410501" --simulator="MC12G4" --skipEvents="0" --truthStrategy="MC15aPlus"'
    
    # "build" the array                                                                                                                                                         
    SLURM_ARRAY_TASK_ID=os.environ["SLURM_ARRAY_TASK_ID"]
    taskid = int(SLURM_ARRAY_TASK_ID)     
    numevents_pertask = 50
    firstevent = numevents_pertask * (taskid - 1) + 1
    
    actual_command = command_template % (SLURM_ARRAY_TASK_ID, firstevent, SLURM_ARRAY_TASK_ID)

    dirname = 'sim_' + SLURM_ARRAY_TASK_ID

#    print('  Task ID: {}'.format(SLURM_ARRAY_TASK_ID))
#    print('  command: {}'.format(actual_command))

    os.system('cd /users/peilongw/Project/MC-Filter-Study/Derivation/aug_27_17')
    os.mkdir(dirname)
    os.system('cd {0}; {1}'.format(dirname, actual_command))
