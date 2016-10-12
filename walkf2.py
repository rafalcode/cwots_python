#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

PATH=sys.argv[1]
FLEXT='.fastq.gz' # file extension of interest
FLEXT='.txt' # file extension of interest
r=regex.compile(r'(?:([/_.])+)')

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
print LLSZ
for K in DL:    
    print "%s (%d): " % (K, len(DL[K]))
    for J in DL[K]:
        print " ".join([I for I in J])
    print

    # print "%s: %s" % (K, " ".join([I for I in DL[K]]))
