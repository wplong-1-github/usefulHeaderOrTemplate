#!/usr/bin/env python

import os
import subprocess
import glob

if __name__ == '__main__':

    dir_std_output='/afs/cern.ch/user/p/pewang/public/Project/CxAODrun_master/CxAODFramework_test/'

    os.system('cd {0}; cat reader7.output| grep "2-tag 2-jet" > 2t2j_event_number.output'.format(dir_std_output))
    os.system('cd {0}; cat reader7.output| grep "2-tag 3-jet" > 2t3j_event_number.output'.format(dir_std_output))

    with open("2t2j_event_number.output", "rt") as fin:
        with open("2t2j_event_number_rename.output", "wt") as fout:
            for line in fin:
                fout.write( (line.replace('peilong: Event number ', '2t2j:')).replace(' has passed 2-tag 2-jet selection', '') )

    with open("2t3j_event_number.output", "rt") as fin:
        with open("2t3j_event_number_rename.output", "wt") as fout:
            for line in fin:
                fout.write( (line.replace('peilong: Event number ', '2t3j:')).replace(' has passed 2-tag 3-jet selection', '') )
