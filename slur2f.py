#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# combines two vtt files: one usually russian, the other english
# this is allows expanded use of the with statement:
from __future__ import with_statement
import sys, codecs

argquan=len(sys.argv)
if argquan != 3:
    print "This script combines to two subtitle files and thereforet wo args"
    print "reuires two arguments: 1) the russian tetx and then the english"
    sys.exit(2)

with codecs.open(sys.argv[1], "r", "utf-8") as x: ruf = x.read()
with codecs.open(sys.argv[2], "r", "utf-8") as x: enf = x.read()
# with codecs.open(sys.argv[1], "r", "utf-16") as x: slurpf = x.read()
# with codecs.open(sys.argv[1]) as x: slurpf = x.read()

# two lists now.
rul=ruf.split("\n\n")
enl=enf.split("\n\n")
ruln=len(rul)
enln=len(enl)
print "ruln len=%i, enln len=%i" % (ruln,enln)

for i in xrange(ruln):
    print rul[i].encode("utf-8")
    print enl[i].encode("utf-8")
    print


# this is ht eway to print out
# print i.encode("utf-8")
# if you're consolde is UTF-8
# which you can find out by printing out
# sys.stdin.encoding
