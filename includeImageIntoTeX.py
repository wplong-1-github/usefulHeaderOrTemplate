#!/usr/bin/env python

import sys
import os
from glob import glob
import subprocess

def getValueNames():
    regions = ['WhfSR']
    values = ['mBB', 'pTV', 'MET', 'Mtop', 'dRBB', 'pTB1', 'pTB2', 'mTW', 'dPhiVBB', 'dPhiLBmin', 'dYWH','BDT']
    valueNames = []
    for i0, i1 in [(i0, i1) for i0 in regions for i1 in values]:
        valueNames.append(i0 + '_' + i1)
    print valueNames

    return valueNames

def getImgNames(oneValueName):
    imgFiles='/home/peilong/Documents/talks_latex/image/Hbb/VHbbModeling/*' + oneValueName + '*'
    imgNames=[os.path.basename(x) for x in glob(imgFiles)]

    # for i,imgName in enumerate(sorted(glob(imgFiles))):
    #     print imgName
    
    return imgNames

def insertImagesIntoTeX(valueName, imageNames, fout):
    
    fout.write( '%% insert ' + valueName + ' into slides by includeImageIntoTeX.py\n' )
    fout.write( '\\begin{frame}\n' )
    fout.write( '  \\frametitle{' + valueName.replace('_', '\_') + '}\n' )
    fout.write( '  \\centering\n' )
    fout.write( '  \\begin{tabular}{c@{}c}\n' )

    for i,imageName in enumerate(imageNames):
        if (i == 1 or i == 3):
            fout.write( '&\n' )
        if i == 2:
            fout.write( '\\\\[-1.5mm]\n' )
        fout.write( '    \\includegraphics[width=0.5\\textwidth]{'+ imageName[:-4] + '}\n' )
    fout.write( '  \\end{tabular}\n' )
    fout.write( ' \\end{frame}\n' )
    fout.write( '%------------------------------------------------\n' )



def main():
# open the section1.tex file
    with open("./src/section1.tex", "rt") as fin:
        with open("./src/section1Temp.tex", "wt") as fout:
            # for loop
            for line in fin:
                # where to insert the line
                if 'use_includeImageIntoTeX_py=true' in line:
                    # get one valueName
                    fout.write(line)
                    fout.write('%% beginning of operation of includeImageIntoTeX.py\n')
                    fout.write( '%------------------------------------------------\n' )

                    for valueName in getValueNames():
                        imgNames = getImgNames(valueName)
                        insertImagesIntoTeX(valueName, imgNames, fout)
                    fout.write('%% end of operation of includeImageIntoTeX.py\n')
                    fout.write( '%------------------------------------------------\n' )

                else:
                    fout.write(line)

    os.system('mv ./src/section1.tex ./src/section1_old.tex')
    os.system('mv ./src/section1Temp.tex ./src/section1.tex')
    print 'includeImageIntoTeX done!'

if __name__ == '__main__':
    main()
