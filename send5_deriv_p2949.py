#!/usr/bin/env python                                                                                                                                                           
#SBATCH -J AOD # job name                                                                                                                                                     
#SBATCH -o log_aod-%A_%a.out                                                                                                                                                  
#SBATCH -e log_aod-%A_%a.error                                                                                                                                                  
#SBATCH -p medium-mem-1-m

#htc

# htc

# medium-mem-1-l

# standard-mem-s



# submitted to highmem node

"""                                                                                                                                                                             
this script submits generation of a "huge" number of events using slurm arrays                                                                                                  
to submit just run this:                                                                                                                                                        
$ sbatch -a 1-N ./launch_slurm_array.py                                                                                                                                         
where N is the number of jobs you want to submit (has to be tuned with the variable 'numevents_pertask'                                                                         
in order to produce the total number of events you want                                                                                              



medium-mem-1-m    up 7-00:00:00      6   idle m[025-030]
medium-mem-1-l    up 30-00:00:0      5   idle m[031-035]
medium-mem-2      up 14-00:00:0      4   idle m1m[001-004]
high-mem-1        up 14-00:00:0      6   idle h[001-005],th001
high-mem-2        up 14-00:00:0      6   idle m1h[001-006]



                           
"""

import os
import subprocess

if __name__ == '__main__':
    # command template                                                                                      #parallel-medium
                                                                        
    # since we are generating events in chunks we need a different random seed for each chunk                                                                                   
    command_template = 'export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase; source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh; source $AtlasSetup/scripts/asetup.sh 20.7.8.7,AtlasDerivation,here; Reco_tf.py --inputAODFile /users/peilongw/Project/MC-Filter-Study/Production/aug_27_17/reco_%s/test_100k_%s.AOD.pool.root --outputDAODFile test_1k_%s.pool.root --reductionConf HIGG5D2'

    # "build" the array                                                                                                                                                         
    SLURM_ARRAY_TASK_ID=os.environ["SLURM_ARRAY_TASK_ID"]

    actual_command = command_template % (SLURM_ARRAY_TASK_ID, SLURM_ARRAY_TASK_ID, SLURM_ARRAY_TASK_ID)

    dirname = 'recoToAOD_' + SLURM_ARRAY_TASK_ID

#    print('  Task ID: {}'.format(SLURM_ARRAY_TASK_ID))
    print('  command: {0}'.format(actual_command))

    os.system('cd /users/peilongw/Project/MC-Filter-Study/Production/aug_27_17; mkdir {0}'.format(dirname))

    os.system('cd /users/peilongw/Project/MC-Filter-Study/Production/aug_27_17/{0}; {1}'.format(dirname, actual_command))
