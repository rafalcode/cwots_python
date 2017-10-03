#!/usr/bin/env python2.7
# chkinp.py "check input data"
# this script tells you if you have the same number of columns on all rows of 
# a tab-separated file
import csv
import sys

def prt0(nrows, nc, ar):
    print "Now for a NULL value check"
    for i in xrange(nrows):
        for j in xrange(nc[i]):
            if ar[i][j]=='':
                print "N",
            else:
                print ar[i][j],
        print

def prtn(nrows, nc, ar):
    print "Now for a NULL value check"
    for i in xrange(nrows):
        for j in xrange(nc[i]):
            if ar[i][j]=='':
                print "N@(" +str(i)+ "," +str(j)+ ")",
        print

def prtn2(nrows, nc, ar):
    print "Now for a NULL value check"
    for i in xrange(nrows):
        nn=0
        for j in xrange(nc[i]):
            if ar[i][j]=='':
                nn+=1
                print "N@c" +str(j),
        if i== 0:
            cann=nn
            print
        elif cann != nn:
            print ">>> Warning, this row " +str(i+1)+ " has " +str(nn)+ " null values when the first row has " +str(cann)+ "."
        else:
            print

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument: the name of the text file."
    sys.exit(2)

with open(sys.argv[1],'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    nrows=0
    nc=[]
    ar=[] # all rows
    for row in tsvin:
        nrows+=1
        nc.append(len(row))
        ar.append(row)

print "Numrows=" +str(nrows)
cannc=nc[0] # we decide that the first column holds the canonical number of columns that all other columns should conform to
nocans=0
for i in xrange(nrows):
    if nc[i] != cannc:
        nocans+=1
        print "Row #" +i+ "has " +nc[i]+ "number of columns, not the canonical " +cannc+ "."

if nocans ==0:
     print "All fine: all columns have the canonical " +str(cannc)+ " number of tab-separated columns."

prtn2(nrows, nc, ar)
