#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys
from collections import deque

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed"
    sys.exit(2)

# Following variable names mean to precisely say what walk is returning
# cwdletl: list of current working directory letters .. because that is what you get (weirdly enough)
# subdl: list of subdirectories in CWD
# fnl: list of filenames in CWD
COU=0
DLL={}
# PYRGX=regex.compile(r'.+\.py')
FQRGX=regex.compile(r'(([^_]+_)+(\w+))\.fastq\.gz')

for (cwdletl, subdl, fnl) in os.walk(sys.argv[1]):
    rdp="".join(cwdletl) # real dp.
    DLL[rdp]=[]
    DLL[rdp].append([i for i in subdl])
    DLL[rdp].append([i for i in fnl])

for k in DLL:
    print "%s: " %k,
    # the second list hold the files in CWD
    cou=0
    for j in DLL[k][1]:
        m=FQRGX.match(j)
        if m:
            cou+=1
            # mg=m.groups()
            # for i in mg:
            #     print "%s " % i,
            lg=m.captures(2)
            for i in lg:
                print "%s " % i,
            print
print cou
        # for i in j:
        #     if PYRGX.match(i):
        #         print i,
        # print
