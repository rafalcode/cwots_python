#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed"
    sys.exit(2)

# Primarily we expected absolute paths .. but this conditional will take care of relative paths too.
lc1=sys.argv[1][0]
a1sz = len(sys.argv[1])
if a1sz > 1:
    lc2=sys.argv[1][1]
    # OK. now argv1 has more than one character
    if lc1 == '/':
        PATH=os.getcwd()
    elif lc1 == '.' and lc2 == '/':
        PATH=os.getcwd() +sys.argv[1][1:]
    else:
        PATH=os.getcwd() +"/"+ sys.argv[1]
else:
    if lc1 == '.':
        PATH=os.getcwd()
    else:
        print "If argument is a single character, only the dot, i.e. CWD, is accepted."
        sys.exit(2)

print PATH

FLEXT='.fastq.gz' # file extension of interest
r=regex.compile(r'(?:([/_.])+)')

DL= { dp: [r.split(f) for f in fnz if f.endswith(FLEXT)] for dp, dn, fnz in os.walk(PATH)}
# if there are no fastq.gz files in there, the dictionary will be empty.
if not DL or not DL[PATH]:
    print "The specified directory does not contain any fastq.gz files in its root"
    sys.exit(2)

LLSZ=len(DL) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# We creat two containers, one a set of unique names, prefixes for each readpair, which will be iterated over, and then a dict based n thse unique names which will be appended to.
UIST=set()
DL2={}
print len(DL[PATH])
for J in DL[PATH]:
    UIST.add(J[0])
    DL2[J[0]]=[]
print len(UIST)
# we're going to go by threes: DIRNAME, PAIR1FNAME, PAIR2FNAME, repeat. Unfortunately P1 and P2 may not be in the right order.
# attach the main directory
for J in DL2:
    DL2[J].append(PATH)

for I in DL[PATH]:
    for J in UIST:
        if J == I[0]:
            DL2[J].append("".join([K for K in I]))

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

for J in DL2:
    print "%s_R1=%s" % (J, DL2[J][0] + "/" + DL2[J][1])
    print "%s_R2=%s" % (J, DL2[J][0] + "/" + DL2[J][2])
# 
# # NDL={} # new dict of lists
# # for M in UIST:
# #     # now float through root directory
# #     NDL[M]=[]
# #     for RD in DL[PATH]:
# #         print len(RD)
# #         if RD[0] == M:
# #             NDL[M].append("%s/%s" % (PATH,"".join([I for I in RD])))
# 
# # for K in NDL:
# #     print "%s: " % K,
# #     for J in NDL[K]:
# #        print len(J)
#         # print " ".join([I for I in J])
# #    print
# 
# #     NDL[M]=[]
# #     if(
# #     NDL[M].append(
# # for K in DL:
# #     PF=r.split(K)[-3]
# #     NDL[PF]=[]
# #     for M in UIST:
# #         if M == PF:
# #             NDL[PF].append("".joinDL[K]
# #     
# #     NDL{)[-3]
# #     print "%s now" % r.split(K)[-3]
