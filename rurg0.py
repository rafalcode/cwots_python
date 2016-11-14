#!/usr/bin/env python3
# capturing Russian
# this is allows expanded use of the with statement:
import sys, re

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: input filename")
    sys.exit(2)

# RGX=regex.compile(r'^ {5}rus\n(?P<exp>.+)')
# RGX=regex.compile(ur'( {5}rus\n((?u) *\w+))+')
RGX=re.compile('ru: (.+)')
with open(sys.argv[1]) as x: slurpf = x.read()
print(slurpf)
fall=RGX.findall(slurpf)
print(len(fall))
print(fall[2])
