#!/bin/env python2.7
# playing around with difflib
# but it also turned into an exercise in precise formatting of strings
import sys
from difflib import SequenceMatcher as SQMA

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: a file listing file"
    sys.exit(2)

with open(sys.argv[1]) as f: fl=f.read().splitlines()
flsz=len(fl)

f0sz=len(fl[0])
ssz=f0sz
for i in xrange(1,flsz):
    fisz=len(fl[i])
    s = SQMA(None, fl[0], fl[i])
    (ast, bst, csz)=s.find_longest_match(0, f0sz, 0, fisz)
    # print "*.s" % (fl[0], 3)
    # print ":.*".format(2, fl[0])
    if fisz > f0sz:
        ssz=fisz
        print '{:>{width}.{prec}}'.format(fl[0][ast:], width=ssz,prec=csz)
        # the > right aligns
        # print '{:>{width}.{prec}}'.format(fl[i][ast:], width=ssz,prec=csz)
        print "{}".format(fl[i])
    else:
        print '{:>{width}.{prec}}'.format(fl[0][ast:], width=ssz,prec=csz)
        print '{:>{width}.{prec}}'.format(fl[i][ast:], width=ssz,prec=csz)

# s = SQMA(None, " abcd", "abcd abcd")
# res=s.find_longest_match(0, 5, 0, 9)
# print res
# Match(a=0, b=4, size=5)
