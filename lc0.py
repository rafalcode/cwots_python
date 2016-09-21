#!/usr/bin/env python2.7
# List comprehension of lines in a file which obey a certain regex.
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target file"
    sys.exit(2)

# RGX=regex.compile(r'(([^_]+_)+(\w+))\.fastq\.gz') # could be sample repeating pattern
RGX=regex.compile(r'^Mon .+')
fname = sys.argv[1]
with open(fname) as file:
    lines = [line.rstrip('\n') for line in file if RGX.match(line) is not None]
file.closed

LSSZ=len(lines)
print "Num regexed lines %d" % LSSZ
