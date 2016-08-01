#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

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
PYRGX=regex.compile(r'.+\.py')

for (cwdletl, subdl, fnl) in os.walk(sys.argv[1]):
    rdp="".join(cwdletl) # real dp.
    DLL[rdp]=[]
    DLL[rdp].append([i for i in subdl])
    DLL[rdp].append([i for i in fnl])

for k in DLL:
    print "%s: " %k,
    # for j in k:
        # print j,

        # for i in j:
        #     if PYRGX.match(i):
        #         print i,
        # print
