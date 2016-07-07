#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex

for (dp, dn, fn) in os.walk('.'):
    # prob "dp" means Dir Present, "dn" Dir Names (subdirectories)and "fn" File Name
    print "len(dp)=%i, len(dn)=%i, len(fn)=%i" % (len(dp), len(dn), len(fn)),
    # weirdly, dp gets split into letters
    for i in (dp):
        print "%s" % (i)
    print "---"
    for i in (dn):
        print i
    print "---"    
    for i in (fn):
        print i
    print "==="    

