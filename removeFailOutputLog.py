#!/usr/bin/env python

import os
import subprocess
import glob

if __name__ == '__main__':
    # command template                                                                                                                                                          
    # since we are generating events in chunks we need a different random seed for each chunk                                                        

    for number in range(1, 2001):

        rootpathname='/users/peilongw/Project/MC-Filter-Study/Production/aug_27_17/reco_%d/test_100k_%d.AOD.pool.root'
        actual_rootpathname=  rootpathname % (number, number)
        fileexist=os.path.isfile(actual_rootpathname)
        
        dirpathname='/users/peilongw/Project/MC-Filter-Study/Production/aug_27_17/reco_%d'
        actual_dirpathname= dirpathname % number

        logfilename='/users/peilongw/Project/MC-Filter-Study/Production/*_%d.out'
        actual_logfilename= logfilename % number

        
        submit_template = 'sbatch -a %d /users/peilongw/Project/MC-Filter-Study/Production/send5_deriv_p2949.py'
        submit_command = submit_template % number

        name_template = '/users/peilongw/Project/MC-Filter-Study/Production/*.error'
        file_list = glob.glob(name_template)

        for entry in file_list:
            newentry=entry.replace('error','out')
#            print('{0}'.format(newentry))
            os.system('rm -f {0}'.format(newentry))

#            print('{0}'.format(newentry))

#        if fileexist:
#            print (' {0} exits'.format(actual_rootpathname))
#            print (' command submit: {0}'.format(submit_command))
#            os.system('{0}'.format(submit_command))

#        else:
#            print (' {0} does not exit'.format(actual_rootpathname))
#            print('dir  command: {0}'.format(actual_dirpathname))
#            print('log  command: {0}'.format(actual_logfilename))

#            os.system('rm -r {0}'.format(actual_dirpathname))
#            os.system('rm {0}'.format(actual_logfilename))
