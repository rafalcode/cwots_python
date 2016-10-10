#!/usr/bin/env python2
# this is an exercise in treating python in a c-centric sort of way.
# I say sort of way, because the effect is pretty much visual
# we hope to emulate a c struct so that print L2[1].f2
# will work, where L2 can be seen as a c struct with a struct member called f2.

import sys
argquan=len(sys.argv)
if argquan != 1:
    print "This script requires no args"
    sys.exit(2)

# here's our class, pretty bare. Note how kwd (keywords) allows arbitrarily defined members to be me
class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# see here guileless attempt to do the same thing but as a list.
# this will be less fun because end effect will be similar to a list of lists
# class B0:
#     def __init__(self, *args):
#         self.__list__.update(args)

# Note how the following will not work ... it throws errors.
# L=[]
# for i in xrange(3):
#     L.append(Bunch(f1=i,f2=i*2)
# the reason would seem to stem fromt he fact that the class is not instantiated in python's real sense
    
# b0=Bunch(f1=4,f2=19)
# print 2*b0.f2
# L3=[B0(i+2,i*2) for i in xrange(3,5)]
# print L3[1][1]

#OK, so what works here? This! (note the lack of quoting).
L2=[Bunch(f1=i+2,f2=i*2) for i in xrange(3,5)]
print L2[1].f2
# So what you have there is bunch which will accept any keywords (member names) to be memebers of its class
# so it's a struct, sort of.

