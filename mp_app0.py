#!/usr/bin/env python2
# multiprocessing approach
import sys, subprocess, re
from multiprocessing import Process, Queue
from Queue import Empty

def do_work(q):
    while True:
        try:
            x = q.get(block=False)
            subprocess.call(x, shell=True)
        except Empty:
            break

# we accept one argument, which is a file listing. BEware that, if you use "find" the first entry will be the directory
fname = sys.argv[1]

# we read our file listing into a list.
with open(fname) as file:
    lines = [line.rstrip('\n') for line in file]
file.closed
# we close the file, its lines are in memory, it's not required anymore.

LASZ=len(lines)
BSZ=2 # batch size

j=0
lol=[]
for i in xrange(BSZ,LASZ,BSZ):
    print j,i
    lol.append(list(lines[j:i]))
    j=i
lol.append(list(lines[i:])) # catches the final left over ones.

lolsz=len(lol)
for i in xrange(0,lolsz):
    for j in xrange(0,len(lol[i])):
        print lol[i][j],
    print
