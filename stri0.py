#!/usr/bin/env python2.7
# equivalent of ${N%/*} in python

S="/storage/home/users/ramon/rafbb/callsnpphylo2"
print "/".join(S.split("/")[:-1])
print '/'+ "/".join(S.split("/")[2:])
