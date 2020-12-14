#!/usr/bin/env python3
import os, regex, sys

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: the target file")
    sys.exit(2)

# RGX=regex.compile(r'(([^_]+_)+(\w+))\.fastq\.gz') # could be sample repeating pattern
# RGX=regex.compile(r'^Mon (\d\d:\d\d:\d\d) \.+')
# RGX=regex.compile(r'^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t.+')
# RGX=regex.compile(r'(([^\t]+)\t)+')

# for the days thing
# RGX=regex.compile(r'^(?P<day>[a-zA-Z]+) (?P<time>[^\t]+)\t(?P<lat>[^\t]+)\t(?P<lng>[^\t]+)')
RGX=regex.compile(r'^(?P<f3>[^ ]{,3})[^ ]* +(?P<s2>[^ ]{,2}).+')
RGX2=regex.compile(r'^(?P<f3>[^ ]{,3})[^ ]* +[^ ]+ +(?P<s2>[^ ]{,2}).+')
# RGX=regex.compile(r'^(?P<f3>[^ ]+) (?P<s2>[^ ]*).\+')
# RGX=regex.compile(r'(?P<f3>[^ ]+) .+')
name0 = sys.argv[1]
c=name0.count(" ")
print("space-count: "+str(c))
name=name0.replace("'", "")

if c == 1:
    m=RGX.match(name)
elif c == 2:
    m=RGX2.match(name)

if m is not None:
    gd = m.groupdict()
    outs = gd['f3']+gd['s2']
    print(outs.upper())
else:
    print("No frig match")

