#!/usr/bin/env python2.7
# two cwots in here, how to slurp in a file and then a json.loads operation
# this is allows expanded use of the with statement:
from __future__ import with_statement
import sys, json

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: input filename"
    sys.exit(2)

with open(sys.argv[1]) as x: slurpf = x.read()

# slurpf now hold our json.
# print slurpf,

pardict = json.loads(slurpf)
# if you have seevral records remember his will be list of dicts.
# let's see how many elements the dict has:
pdl=len(pardict)
# print "%s %d" % ("length of dict'ed json file is", pdl)
for i in range(pdl):
    print i
# for k, v in pardict.iteritems:
#    print "%s:%s" % (k,v)

