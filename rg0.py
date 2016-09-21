#!/usr/bin/env python2.7
# ATtempt at repeated regex group idiom
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target file"
    sys.exit(2)

RGX=regex.compile(r'(([^_]+_)+(\w+))\.fastq\.gz')
fname = sys.argv[1]
with open(fname) as file:
    lines = [line.rstrip('\n') for line in file]
file.closed


