#!/usr/bin/env python2.7
# PArse MODule AVailable
# Prime example of how difficult regexes can be. Take the output of "module available"
# notoriously difficult to get rid of the header .. though starting - is a clue.
from __future__ import with_statement
import sys, regex

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: input filename"
    sys.exit(2)

RGX=regex.compile(r' +') # this is the separator
with open(sys.argv[1]) as x: FL = x.read().splitlines()

FLSZ=len(FL)
FL2=[]
for I in xrange(FLSZ):
    # m=RGX.findall(FL[I])
    m=RGX.split(FL[I])
    msz=len(m)
    if msz != 0:
        for J in xrange(msz):
            ssz=len(m[J])
            for K in xrange(46-ssz):
                # oh boy, this really is hideous: needed to keep text left justified.
                m[J] = m[J]+" "
            FL2.append(m[J])

FL2.sort()
FL2SZ=len(FL2)
FZ=FL2SZ/3
for I in xrange(FZ):
    fs= " %s%s%s" % (FL2[I*3], FL2[I*3+1], FL2[I*3+2])
    print fs
