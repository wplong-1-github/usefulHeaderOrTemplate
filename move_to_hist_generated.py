#!/usr/bin/env python

import os
from glob import glob
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
inputDir = dir_path + "/" + "410*"

histFileList = sorted(glob(inputDir))

print histFileList

newLocation = dir_path + "/hist_generated"
os.system("mkdir {0}".format(newLocation))

for histFile in histFileList:
    histFileName = histFile + "/output_1Lep_" + histFile[-6:] + ".root"
    print histFileName
    print os.path.isfile(histFileName)
    os.system("cp {0} {1}".format(histFileName, newLocation))
    # print "cp {0} {1}".format(histFileName, newLocation)

