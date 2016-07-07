#!/usr/bin/env python2
import sys, subprocess, re
from multiprocessing import Process, Queue
from Queue import Empty

# we accept one argument, which is a file listing. BEware that, if you use "find" the first entry will be the directory
argquan=len(sys.argv)
if argquan != 3:
    print "This script requires two arguments: 1) input filelisting 2) numprocs"
    sys.exit(2)

fname = sys.argv[1]
NSCRPS = int(sys.argv[2])

# we read our file listing into a list.
with open(fname) as file:
    lines = [line.rstrip('\n') for line in file]
file.closed
# we close the file, its lines are in memory, it's not required anymore.

LASZ=len(lines)

linesz=len(lines)
lppack=linesz/NSCRPS # minimum lines per pack
packsw1x=linesz%NSCRPS # number of packs with 1 extra because of leftover

LOL=[]
for i in xrange(0,NSCRPS):
    tfnam="./slurmstampy_%02d.sh" % i # temporary filename.
    tf=open(tfnam, "w")
    if i < packsw1x:
    	start=(lppack+1)*i
    	end=(lppack+1)*(i+1)
    else:
    	start=lppack*i+packsw1x
    	end=lppack*(i+1)+packsw1x
    LOL.append( lines[start:end] )

TTA="4:00:00"


S1='''#!/bin/bash -l
#SBATCH -A b2012209
#SBATCH -p node -n 16
#SBATCH -t '''


S2='''module load python
python ./stamingrps.py'''
print S1+TTA+"\n"+S2


