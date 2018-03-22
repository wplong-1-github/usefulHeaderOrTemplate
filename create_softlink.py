#!/usr/bin/env python

import os
from glob import glob

# list=[410441,410442,410470,410472,410480,410482,410557,410558]

dir_path = os.path.dirname(os.path.realpath(__file__))

print dir_path

inputDir = '/eos/user/a/abell/TruthTuples_v07/*1_Lep*'

# get the ntuple list from inputDir
ntupleList = sorted(glob(inputDir))

# mkdir for each of the item in the list
for ntupleName in ntupleList:
    os.system('mkdir {0}'.format(dir_path + "/" + ntupleName[34:]))
    os.system('cd {0}'.format(dir_path + "/" + ntupleName[34:]))
    # for each mkdir, create a softlink
    os.system('ln -s {0} {1}'.format(ntupleName, dir_path + "/" + ntupleName[34:]))

