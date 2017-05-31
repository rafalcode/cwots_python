#!/usr/bin/env python2.7
# wiki tabulate a file .. an abandoned attempt
import sys
from tabulate import tabulate

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the name of the text file."
    sys.exit(2)

with open(sys.argv[1]) as f: fl=f.read().splitlines()
flsz
print tabulate(cells, headers="firstrow", tablefmt="html")
