#!/usr/bin/env python2.7
# Take a file with a name int he first olum, and a integer in the second.
# Render a histogram of the 2nd column values
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
    FL2.append(tuple(RGX.split(FL[I])))

for I in xrange(FLSZ):
    print FL2[I][1]
