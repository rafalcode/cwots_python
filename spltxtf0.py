#!/usr/bin/env python2
# splits a text file in a series of smaller ones of size splitLen
import sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: input filename"
    sys.exit(2)

splitLen = 8         # 20 lines per file
outputBase = 'output' # output.1.txt, output.2.txt, etc.

# This is shorthand and not friendly with memory
# on very large files (Sean Cavanagh), but it works.
input = open(sys.argv[0], 'r').read().split('\n')
nlines=len(input)

at = 1
for lines in range(0, nlines, splitLen):
    # First, get the list slice
    outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    output = open(outputBase + str(at) + '.txt', 'w')
    output.write('\n'.join(outputData))
    output.close()

    # Increment the counter
    at += 1
