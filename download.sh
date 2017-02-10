#!/bin/bash

#for (( i=86; i<100; i=i+1 ))
#do

#    downloadName="mc15_13TeV:AOD.07265714._0000"$i".pool.root.1" 
#    echo $downloadName
#    rucio download $downloadName

#done

rucio download mc15_13TeV:AOD.07265714._000036.pool.root.1
rucio download mc15_13TeV:AOD.07265714._000047.pool.root.1
rucio download mc15_13TeV:AOD.07265714._000055.pool.root.1
rucio download mc15_13TeV:AOD.07265714._000097.pool.root.1
rucio download mc15_13TeV:AOD.07265714._000100.pool.root.1
