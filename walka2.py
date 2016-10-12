#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

L= [dirp, subdz, flz for dirp, subdz, flz in os.walk(sys.argv[1])]
print len(L)
