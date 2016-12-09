#!/usr/bin/env python2.7
# read a file into memory, only if its lines conform to a certain regex.
from __future__ import with_statement
import sys, regex

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: input filename"
    sys.exit(2)

OL=[] # option list
RGX=regex.compile(r'^$# (.+)') # this is the separator
with open(sys.argv[1]) as fp:
    for everyline in fp:
        m=RGX.match(everyline)
        if m is not None:
            OL.append(m.capture(1))

print len(OL)
