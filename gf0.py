#!/usr/bin/env python2.7
# valuable usage of list comprehension here
# this script does what? converts a table into a html table
import sys
from tabulate import tabulate

# we're going to accept a first argument with a test file in tsv-separated tabular format and then a series of integers representing the columns to include
# when no columns are included, they are all outputted.
argquan=len(sys.argv)
if argquan == 1:
    print "This script requires at least one argument: the name of the text file. Then the later arguments should be integers: the column numbers to be _included_"
    sys.exit(2)

la=len(sys.argv)
print "extra args: " +str(la-2)
if la > 2:
    cls=[int(c) for c in sys.argv[2:la]]
    # do we want to see the selected column indices?
    # print " ".join(['%i' % x for x in cls])

with open(sys.argv[1]) as f: fl=f.read().splitlines()
# the followin gwill create a list of lists because split returns a list
cells=[ x.split("\t") for x in fl]
csz=len(cells)

if la > 2:
    # cells2=[[cells[x][y] for y in cls] for x in xrange(0, la)] for y in cls]
    cells2=[[cells[x][y] for y in cls] for x in xrange(0, csz)]    # print " ".join(['%s' % x for x in cells2])
    print tabulate(cells2, headers="firstrow", tablefmt="html")
else:
    print tabulate(cells, headers="firstrow", tablefmt="html")
