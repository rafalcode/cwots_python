#!/usr/bin/env python2.7
# script showing how to invoke a module within a python script
# and output the location of the executable to be used.
# harded coded for fastqc but any module will do.

# Very difficult trying to get output of module available.
import subprocess

# execfile('/usr/local/Modules/3.2.10/init/python.py')
# module('load','FASTQC')
# module('list', '>uit')
# CMDANDARGS=['which', 'fastqc']
# fqc_cmd=subprocess.check_output(CMDANDARGS)
# print "Using \"%s\" as FASTQC executable!" % fqc_cmd.rstrip('\n')

# CMDANDARGS=['module', 'list']
# CMDANDARGS=['ls', '-tr']
# execcmd=subprocess.check_output(CMDANDARGS)
# print "%s" % execcmd,
# out=subprocess.check_output(['/usr/local/Modules/3.2.10/bin/modulecmd', 'python', 'list'])
# out=subprocess.check_output(['echo', 'this mule'])
echo_for_cmd = ['/usr/local/Modules/3.2.10/bin/modulecmd', 'python', 'list']
echocmdproc = subprocess.Popen(echo_for_cmd, stderr=subprocess.PIPE)
o=subprocess.check_output("cat", stdin=echocmdproc.stderr)
echocmdproc.wait()
print type(o)
print len(o)
