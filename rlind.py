#!/usr/bin/env python3
# We move to python3 on this one, becuas eof its ease in handling unicodetwo cwots in here, how to slurp in a file and then a json.loads operation
# this is allows expanded use of the with statement:
import sys

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: input filename")
    sys.exit(2)

with open(sys.argv[1]) as x: slurpf = x.read()
lin=slurpf.splitlines()
lasdict= dict()
for i in lin:
    lasdict[i] = lasdict.get(i, 0) +1

for k in lasdict:
    if(lasdict[k] >1):
        print(k)
