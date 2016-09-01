#!/usr/bin/env python2
# a python way of doing strtok?
# http://stackoverflow.com/questions/456084/how-do-i-do-what-strtok-does-in-c-in-python

# awkward string
A = '1, 2,,3,4  '
B = [int(x) for x in A.split(',') if x.strip()]
# B = [int(x) for x in A.split(',')]

lB=len(B)
print "%d" % lB
for i in xrange(lB):
    print "%1d|" % B[i],
print

# What's happening is that there's leading space ... don't know what it is
print "%d" % (B[0] + B[3])
