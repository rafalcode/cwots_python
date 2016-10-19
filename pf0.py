#!/usr/bin/env python2.7
# Prinnintg to a file and appending too!
import os, regex, sys

F="hi I'm Roger Mellie,\nThe Man on the Telly"
fh=open("of.txt", "w")
print >>fh, "%s" % F
print >>fh, "%s" % F
fh.close()

