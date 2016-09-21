#!/usr/bin/env python2.7
# implement named groups in the regex module
# and use groupdict() to capture all of them in a dict
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the target file"
    sys.exit(2)

# RGX=regex.compile(r'(([^_]+_)+(\w+))\.fastq\.gz') # could be sample repeating pattern
# RGX=regex.compile(r'^Mon (\d\d:\d\d:\d\d) \.+')
RGX=regex.compile(r'^(?P<day>[a-zA-Z]+) (?P<time>[^\t]+)\t(?P<lat>[^\t]+)\t(?P<lng>[^\t]+)')
# RGX=regex.compile(r'^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t.+')
# RGX=regex.compile(r'(([^\t]+)\t)+')
L2=[]
fname = sys.argv[1]
with open(fname) as file:
    for line in file:
        m=RGX.match(line)
        if m is not None:
            L2.append(m.groupdict())
file.closed

for i in L2:
    print "%s %s %s %s" % (i['day'], i['time'], i['lat'], i['lng'])
