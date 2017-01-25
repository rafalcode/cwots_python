#!/usr/bin/env python2.7
# Using a list comprehension to initialise a 2D matrix
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: n, the size of the 2D matrix"
    sys.exit(2)

n=int(sys.argv[1])
MA=[ [0 for i in xrange(n)] for j in xrange(n)]

for i in xrange(n):
    for j in xrange(n):
        print MA[i][j],
    print
