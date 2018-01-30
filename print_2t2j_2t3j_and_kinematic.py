#!/usr/bin/env python

import os
import subprocess
import glob

if __name__ == '__main__':

    with open("reader11.out", "rt") as fin:
        with open("2t2j_2t3j_event_number_kinematic_more.output", "wt") as fout:
            for line in fin:
                if "peilong: ======WhfSR tagcatExcl nJet slection======" in line:
                   linestring = fin.next().replace('peilong: Event number ', ':').replace(' has passed ', '').replace('-tag ', 't').replace('-jet selection\n', 'j')
                   tagstring = linestring[-4:]
                   fout.write(linestring.replace(':', tagstring + ':')[:-4])

                if "peilong: lepton pt is" in line:
                    fout.write(' leptonPt:' + line[22:].replace('\n', ' '))
                if "peilong: lepton eta is " in line:
                    fout.write('leptonEta:' + line[23:].replace('\n', ' '))
                if "peilong: lepton phi is " in line:
                    fout.write('leptonPhi:' + line[23:].replace('\n', ' '))
                if "peilong: lepton Mass is " in line:
                    fout.write('leptonMass:' + line[24:].replace('\n', ' '))
                if "peilong: pTV is " in line:
                    fout.write('ptV:' + line[16:].replace('\n', ' '))
                if "peilong: MET is " in line:
                    fout.write('MET:' + line[16:])
