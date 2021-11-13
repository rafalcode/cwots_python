#!/usr/bin/env python3
# this script does what?
import sys 

argquan=len(sys.argv)
if argquan != 1:
   print("This script requires one argument")
   sys.exit(2)

# refer to arguments with sys.argv[1] etc.

# this was in the realpython artcile about lambdas
# but it's not great
import functools # reduce is now in this lib
# pairs = [(9, 'a'), (12, 'b'), (4, 'c')]
# a=functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
# the problem is the naming.
# give it a go this way:
tlist = [(9, 'a'), (12, 'b'), (4, 'c')] # so you know it's a list and most probably, a list of tuples, therefore the t.
b=functools.reduce(lambda acc, tup: acc + tup[0], tlist, 0)
print(b)

# so it's clear that the lambda second arg is a tuple of which the first element is used.
# so the first elemtn of each of tuples in tlist is progressively added to acc so that's how the sum is produced.
