#!/usr/bin/env python2.7
# script showing how to invoke a module within a python script
# and output the location of the executable to be used.
# harded coded for fastqc but any module will do.
import subprocess

execfile('/usr/local/Modules/3.2.10/init/python.py')
module('load','FASTQC')
CMDANDARGS=['which', 'fastqc']
fqc_cmd=subprocess.check_output(CMDANDARGS)
print "Using \"%s\" as FASTQC executable!" % fqc_cmd.rstrip('\n')
