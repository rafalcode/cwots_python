#!/usr/bin/env python2.7

import regex, subprocess

poav="/home/nutria/po.t"
with open(poav) as x: FSLURP = x.read()

RGX=regex.compile(r'\n +\d+\n +\d+\n +\[\d+\](.+)\n +\[\d+\].+\n +(\d+):(\d+)\n')
m=RGX.findall(FSLURP)
print len(m)
t=[]
z=0
for i in m:
    print"Title: %s, time: %s:%s" % (i[0], i[1], i[2])
    z += 60*int(i[1]) + int(i[2])
    t.append(z)

ltd2=len(t)/2
for i in xrange(ltd2):
    print "%4.2f %4.2f 1" % (t[2*i], t[2*i+1])
