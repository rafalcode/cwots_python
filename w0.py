#!/usr/bin/env python2.7
# Getting to know os.walk
import os, sys
argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

from os.path import join, getsize
for root, dirs, files in os.walk(sys.argv[1]):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
