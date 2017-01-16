#!/usr/bin/env python3
# capturing Russian
# this is allows expanded use of the with statement:
# note python3 !
import sys, re

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: input filename")
    sys.exit(2)

# RGX=regex.compile(r'^ {5}rus\n(?P<exp>.+)')
# RGX=regex.compile(ur'( {5}rus\n((?u) *\w+))+')
RGX0=re.compile('   \[\d+\]L y r')
# rus0='Назв'.decode('utf-8') # that's P2
rus0=u'Назв'
RGX2=re.compile(rus0)
with open(sys.argv[1]) as x: flines = x.read().splitlines()
print(len(flines))
indic=0
for l in flines:
    if indic==0:
        m=RGX2.match(l)
        if m is not None:
            indic=1
    else:
        m=RGX2.match(l)
        if m is not None:
            indic=0

print(indic)
