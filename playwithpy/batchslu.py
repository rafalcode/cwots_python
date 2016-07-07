#!/usr/bin/env python2
import sys, re

# we accept one argument, which is a file listing. BEware that, if you use "find" the first entry will be the directory
argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: 1) numscripts"
    sys.exit(2)

NSCRPS = int(sys.argv[1])

CW=os.getcwd()  # CW for current working directory
CZ=os.listdir(CW) # CZ for "contentz (of the CW)"

RG=re.compile(r'GSL_.+_R1\.fq')
LOP=[] # list of pairs
for I in CZ: # loops through each file in the current directory.
    MA=RG.match(I)
    if(MA):
        LOI=I.split('_')
        LOP.append( "_".join(LOI[0:4]))

P1SFX="_R1.fq"
P2SFX="_R2.fq"
LOPSZ=len(LOP)
CMDA=[]
for I in range(LOPSZ):
    CMDA.append("stampy.py -t 16 -g ArcGaz -h ArcGaz --substitutionrate="+SBR+" -o "+LOP[I]+".sam -M "+LOP[I]+P1SFX+" "+LOP[I]+P2SFX+" >/dev/null 2>&1")

CSZ=len(CMDA)

linesz=len(lines)
cppack=CSZ/NSCRPS # minimum lines per pack
packsw1x=CSZ%NSCRPS # number of packs with 1 extra because of leftover

LOL=[]
TTA="4:00:00"

S1='''#!/bin/bash -l
#SBATCH -A b2012209
#SBATCH -p node -n 16
#SBATCH -t '''

S2='''module load python'''

for i in xrange(0,NSCRPS):
    tfnam="./slurmstampy_%02d.sh" % i # temporary filename.
    tf=open(tfnam, "w")
    if i < packsw1x:
    	start=(lppack+1)*i
    	end=(lppack+1)*(i+1)
    else:
    	start=lppack*i+packsw1x
    	end=lppack*(i+1)+packsw1x
    tf.write(S1+TTA+"\n"+S2+"\n")
    for j in xrange(start, end):
    	tf.write(CMDA[j]+"\n")
    tf.close()
