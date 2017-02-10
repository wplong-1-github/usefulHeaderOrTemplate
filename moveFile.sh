#!/bin/bash

for (( i=20; i<36; i=i+1 ))
do

    downloadName="AOD.07265714._0000"$i".pool.root.1" 
#    echo $downloadName
    mv ./mc15_13TeV/$downloadName ./mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.AOD.e3698_s2608_s2183_r6765_r6282/

