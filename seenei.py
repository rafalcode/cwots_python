#!/usr/bin/env python2.7
import os, sys, re, subprocess
# from multiprocessing import Process, Queue
# from Queue import Empty

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires 1 arg: a distance matrix file"
    sys.exit(2)

dstfile=sys.argv[1]

# load right module
execfile('/usr/local/Modules/3.2.10/init/python.py')
module('load','phylip')
# CMDANDARGS=['which', 'neighbor']
CMDANDARGS=['neighbor', dstfile]
fqc_cmd=subprocess.check_output(CMDANDARGS)
# print type(fqc_cmd)
print fqc_cmd
