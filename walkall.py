#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target directory on which you'd like the walk performed 2) target filename ending (inc. extension}"
    sys.exit(2)

# Following variable names mean to precisely say what walk is returning
# cwdletl: list of current working directory letters .. because that is what you get (weirdly enough)
# subdl: list of subdirectories in CWD
# fnl: list of filenames in CWD
COU=0
# incredible the CWD is returned as a list of letters!
for dirp, subdz, flz in os.walk(sys.argv[1]):
    print "CWD: %s |" % dirp,
    print "SUBDIRS: " + " ".join(["%s " % i for i in subdz]),
    print"| FILES: " + " ".join(["%s " % i for i in flz])

# note use of mnemonic postfix "z" to denote multiple. Implication is that a list is required for it.
