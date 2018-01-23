#!/usr/bin/env python2.7
# get a file with supposed timings on each line and then prints out mplayer style Mins:secs.centisec
# lines with no number will be ignored.
import sys, regex

# we're going to accept a first argument with a test file in tsv-separated tabular format and then a series of integers representing the columns to include
# when no columns are included, they are all outputted.
argquan=len(sys.argv)
if argquan != 2:
    print "This script requires at least one argument: the name of the text file. Then the later arguments should be integers: the column numbers to be _included_"
    sys.exit(2)

with open(sys.argv[1]) as f: fl=f.read().splitlines()
timergx=regex.compile(r'\d+')
for l in fl:
    fa=timergx.findall(l)
    fasz=len(fa)
    if fasz == 1:
        tstr="%s.0" % fa[0]
    elif fasz == 2:
        tstr="%s:%s.0" % (fa[0], fa[1])
    elif fasz == 3:
        tstr="%i:%s.0" % (int(fa[0])*60+int(fa[1]), fa[2])
    else:
        continue
    print tstr
