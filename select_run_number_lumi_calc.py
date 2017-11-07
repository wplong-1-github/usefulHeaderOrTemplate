#!/usr/bin/env python                                                                                                                                 

import os
import subprocess
import glob

if __name__ == '__main__':

    with open("lumitable.csv", "rt") as finLumi:
#        with open("data17_13tev_runnumber.txt", "rt") as finRunNumber:
 #           runNumber = finRunNumber.readline()
#            print runNumber
        with open("lumitable_runnumber.csv", "wt") as fout:
            for line in finLumi:
                if line[:6] in open('data17_13tev_runnumber.txt').read():
                    fout.write(line)
#                    print line
