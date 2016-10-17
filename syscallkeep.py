#!/usr/bin/env python2.7
# Procedures to get output from command in python
from subprocess import check_output
outp=check_output(["ls", "-l"])
print "here is your ls -l output:"
print outp
