#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

PATH=sys.argv[1]
FLEXT='.fastq.gz' # file extension of interest
# FLEXT='.txt' # file extension of interest
r=regex.compile(r'(?:([/_.])+)')
r2=regex.compile(r'_paired') # trimmomatic particularity

# what follows is a list comprehension of a loop over the files in a subdirectory
# and a loop over the subdirectories of the path, with the path and filename finally being joined together
# the code follows the english in reverse: i.e. looping over files comes last.
# fqz = [os.path.join(dp, f) for dp, dn, fnz in os.walk(PATH) for f in fnz ]
# LL= [dp for dp, dn, fnz in os.walk(PATH)]
# LL= [dp for dp, dn, fnz in os.walk(PATH) [f for f in fnz]]
# LL= [[f for f in fnz if rx.match(f) is not None] for dp, dn, fnz in os.walk(PATH)]
# LL= [[f for f in fnz if f[-1] == 't'] for dp, dn, fnz in os.walk(PATH)] # works
# LL= [[f for f in fnz if f[-3:-1] == 'lst'] for dp, dn, fnz in os.walk(PATH)] # disna
# LL= [[f for f in fnz if f.endswith('txt')] for dp, dn, fnz in os.walk(PATH)]
# DL= { dp: [f for f in fnz if f.endswith('.txt')] for dp, dn, fnz in os.walk(PATH)} # works!
DL= { dp: [r.split(f) for f in fnz if f.endswith(FLEXT)] for dp, dn, fnz in os.walk(PATH)}
# LL= [dp for dp, dn, fnz in os.walk(PATH) for f in fnz ]
# LL= [dp [f for dp, dn, fnz in os.walk(PATH) for f in fnz ]]

LLSZ=len(DL) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# OK lets sort each LofL
# for D in DL:
#     for I in DL[D]:
# 
#     DLLSZ=len(DL[D]for D in DL:
#     if DL[D
#     DL[D].sort(key= lambda col
# developer output
# print LLSZ
# for K in DL:    
#     print "%s (%d): " % (K, len(DL[K]))
#     for J in DL[K]:
#         print "".join([I for I in J])
#     print
    # Template
    # print "%s: %s" % (K, " ".join([I for I in DL[K]]))

# NOTES: DL is the dictionary wiht the full path, its value is a list of of file names split up

# this will print out the prefixes. Easy enough to add the next token, if necessary.
# print ">>> fastq.gz prefixes in root directory:"
# print "%s (%d): " % (PATH, len(DL[PATH]))
# for J in DL[PATH]:
#     print "%s "% J[0],
# print

# We creat two containers, one a set of unique names, prefixes for each readpair, which will be iterated over, and then a dict based n thse unique names which will be appended to.
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

# again we want to make sure those pairs are in correct order. Actually above re-ordering can be done in one shot here
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

