#!/usr/bin/env python2.7
import os, regex, sys
import os, sys, subprocess		
from subprocess import call, check_output, CalledProcessError, STDOUT

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

PATH=sys.argv[1]
FLEXT='.fastq.gz' # file extension of interest
r=regex.compile(r'(?:([/_.])+)')
r2=regex.compile(r'_paired') # trimmomatic particularity

DL= { dp: [r.split(f) for f in fnz if f.endswith(FLEXT)] for dp, dn, fnz in os.walk(PATH)}

LLSZ=len(DL) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# We now create two containers, one a set of unique names, prefixes for each readpair, which will be iterated over,
# and then a dict based on these unique names which will be appended to.
UIST=set()
DL2={}
for J in DL[PATH]:
    UIST.add(J[0])
    DL2[J[0]]=[]

# we're going to go by threes: DIRNAME, PAIR1FNAME, PAIR2FNAME, repeat. Unfortunately P1 and P2 may not be in the right order.
# attach the main directory
for J in DL2:
    DL2[J].append(PATH)

for I in DL[PATH]:
    for J in UIST:
        if J == I[0]:
            DL2[J].append("".join([K for K in I]))
            break # found this particular unique prefix in DL[PATH] want to travel through the others now.

# Procedure: Ensure right pair order
# So unfortunately we cannot depend on the pairs being sorted in relation to each other.
# So, we'll go through every second and third entry, compare them lexicographically, and switch their positions
# we are a bit stuck if lexicographically it doesn't work that way i.e. left shoul dbe econd, and right first.
# using pythons well-known ability to do this, i.e.
# mylist[1],mylist[0] = mylist[0, mylist[1]
for J in DL2:
    JLEN=len(DL2[J])
    J3L=JLEN/3
    for I in xrange(J3L):
        if(DL2[J][I*3+1]>DL2[J][I*3+2]):
            DL2[J][I*3+2], DL2[J][I*3+1] = DL2[J][I*3+1], DL2[J][I*3+2]

# OK now we want to add the directories that are named after the samplepair.
for D in DL:
    if D == PATH:
        continue # done already.
    PF=r.split(D)[-3]
    for J in UIST:
        if J == PF:
            DL2[J].append(D)
            for K in DL[D]:
                print " ".join([I for I in K])
                if K[4] == 'paired':
                    DL2[J].append("".join([I for I in K]))
            break
            # DL2[J].append("".join([K for K in I]))

# Make sure the pairs of reads (every secodn and third entry of our dict of lists) are in the right lexicographic order.
for J in DL2:
    JLEN=len(DL2[J])
    J3L=JLEN/3
    for I in xrange(J3L):
        if(DL2[J][I*3+1] > DL2[J][I*3+2]):
            DL2[J][I*3+2], DL2[J][I*3+1] = DL2[J][I*3+1], DL2[J][I*3+2]

for J in DL2:
    print "%s: %s" % (J, " ".join([I for I in DL2[J]]))

# So at the end of this we have a dict whose keys are the prefix to each sample.
# The dict consists of a list for each key, arranged in groups of three. The first group is
# the root directory and the two readsamples, then the directory in which the trimmomatic reads are kept.

# SAPF, sample prefix ... it's what our dict DL2 is based on:
for SAPF in DL2:
		cmd = "#!/bin/bash"
		cmd += "\n#$ -V"
		cmd += "\n#$ -cwd"
		cmd += "\n#$ -j y"
		cmd += "\n#$ -S /bin/bash"
		cmd += "\n#$ -q all.q"
		cmd += "\n#$ -pe multi 8"
		cmd += "\nmodule load SPAdes"
		cmd += "\nR1=" +DL2[SAPF][3]+ DL2[SAPF][4]
		cmd += "\nR2=" +DL2[SAPF][3]+ DL2[SAPF][5]
		cmd += "\nON=" +DL2[SAPF][3]
		cmd += "\nspades.py -t $NSLOTS -o $ON --pe1-1 $R1 --pe1-2 $R2"
		
		# print and run command
		# print cmd
		echo_for_cmd = ["echo", "-e", "%s" % cmd] # we need this for the Popen pipe
		echocmdproc = subprocess.Popen(echo_for_cmd, stdout=subprocess.PIPE)
		out = subprocess.check_output("qsub", stdin=echocmdproc.stdout)
		echocmdproc.wait()
