#!/usr/bin/env python2.7
# read a job script file and pull out the relevant options
from __future__ import with_statement
import sys, regex

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: input filename"
    sys.exit(2)

OL=[] # option list
RGX=regex.compile(r'^#\$ (.+)') # this is the separator
# RGX=regex.compile(r'^(.+)') # this is the separator
with open(sys.argv[1]) as fp:
    for everyline in fp:
        m=RGX.match(everyline)
        if m is not None:
            print "a match"
            OL.append(m.group(1))

print len(OL)
print OL
