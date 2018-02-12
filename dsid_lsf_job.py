#!/usr/bin/env python

import os

list=[410501,410511,410512,410225,410525]

print list

jobCommand = 'bsub -q 1nd NtupleToHist 1 /afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis/VHbbTruthFramework/macros/NtupleToHist/%s %s /afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis2/run'


for listName in list:
    print listName
    job = jobCommand % (listName, listName)
    print job
    
    os.system('cd /afs/cern.ch/user/p/pewang/public/Project/VHbbTruthAnalysis2/run')
    os.system('{0}'.format(job))
