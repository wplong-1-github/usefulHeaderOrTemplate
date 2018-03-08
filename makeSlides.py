#!/usr/bin/env python

import sys
from optparse import OptionParser
import os
import glob
import subprocess

def main():
    print "name: ", sys.argv[0]
    print "number of arguments: ", len(sys.argv)
    print "arguments are: ", str(sys.argv)

    parser = OptionParser()
    # parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")

    parser.add_option("-s", "--slides", dest="slidesName", help="generate a new slides folder with given name", metavar="FILE")

    parser.add_option("-t", "--section", dest="nOfSection", help="how many section will this slides have", metavar="FILE")

    parser.add_option("-q","--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")

    (options, args) = parser.parse_args()

    print options
    # print options.filename
    # print options.slidesName
    # print options.nOfSection
    print args

    newSlidesName = options.slidesName
    numberOfSection = options.nOfSection

    if newSlidesName == None:
        print "makeSlides.py: please input the slides name by -s name"
    elif os.path.isdir("./slides/{0}/".format(newSlidesName)):
        print "makeSlides.py: this slides name already exits"
    else:
        os.system('mkdir ./slides/{0}'.format(newSlidesName))
        os.system('ln -s /home/peilong/Documents/talks_latex/latex ./slides/{0}/'.format(newSlidesName))
        # generate new Makefile for newSlidesName
        print "making Makefile"
        with open("./MakefileTemplate", "rt") as fin:
            with open("./slides/{0}/Makefile".format(newSlidesName), "wr") as fout:
                for line in fin:
                    fout.write( line.replace('presentationTemplate.tex', newSlidesName + '.tex') )

        # handle the number of section inside the slides
        os.system('cp ./presentationTemplate.tex ./slides/{0}/{0}.tex'.format(newSlidesName))
        with open("./presentationTemplate.tex", "rt") as fin:
            with open("./slides/{0}/{0}.tex".format(newSlidesName), "wr") as fout:
                for line in fin:
                    if 'sectionTemplate.tex' in line:
                        if numberOfSection != None:
                            for i in range(0, int(numberOfSection)):
                                fout.write( line.replace('Template.tex}', str(i) + '.tex}') )
                        else:
                            fout.write(line)
                    else:
                        fout.write(line)

        # generate sectioni.tex file in src/
        os.system('cp -r ./src ./slides/{0}/'.format(newSlidesName))
        if numberOfSection != None:
            for i in range(0, int(numberOfSection)):
                newSectionName = 'section' + str(i) + '.tex'
                os.system( 'cp ./slides/{0}/src/sectionTemplate.tex ./slides/{0}/src/{1}'.format(newSlidesName, newSectionName) )
            os.system('rm ./slides/{0}/src/sectionTemplate.tex'.format(newSlidesName))

        # tell user it's the end of the program
        print "makeSlides.py: location of the new slides -> ./slides/{0}/".format(newSlidesName)

if __name__ == '__main__':
    main()
