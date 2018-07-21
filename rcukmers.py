#!/usr/bin/env python2.7
# Recursion is a function calling itself
# it's a very important and clever effect
# which is hard to explain really, but is widely used
import sys

def recurseit(k, symbols, arr, y):
    if k>0:
        for m in symbols:
            recurseit(k - 1, symbols, arr, m + y)
    else:
        arr.append(y)
    return arr

if __name__ == "__main__":
    argquan=len(sys.argv)
    if argquan != 2:
        print "Give the number of loops you want done"
        sys.exit(2)
    symbols = ['A', 'C', 'T', 'G']
    arr = []
    y=''
    kms=recurseit(int(sys.argv[1]), symbols, arr, y)

    print kms
    print "Length of kmer list = %i" % len(kms)
