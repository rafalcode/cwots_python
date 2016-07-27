#!/usr/bin/env python2.7
import os, sys, re, subprocess
from multiprocessing import Process, Queue
from Queue import Empty

argquan=len(sys.argv)
if argquan != 4:
    print "This script requires three arguments: 1) directory in which to find fastq files and 2) output directory name of your choosing 3) requested number of parallel processes"
    sys.exit(2)

# From the Queue module, we're using the Empty attribute
def do_work(q):
    while True:
        try:
            x = q.get(block=False)
            subprocess.call(x, shell=True)
        except Empty:
            break

# the root directory of the 
PATH=sys.argv[1]
if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
le=os.listdir(PATH)

# DIRSUF=re.compile(r'(.\+)_(trimmoed2)')
DIRSUF=re.compile(r'(.+)_(trimmoed)')

lotu=[] # list of tuples
for l in le:
    m=DIRSUF.search(l)
    if os.path.isdir(l) and m:
        lotu.append( (m.group(1), m.group(2)) ) # root and suffix separated.

execfile('/usr/local/Modules/3.2.10/init/python.py')
module('load','FASTQC')
# module('list')
CMDANDARGS=['which', 'fastqc']
fqc_cmd=subprocess.check_output(CMDANDARGS)
fqc_cmdstr=fqc_cmd.rstrip() +" -o "+ sys.argv[2]

work_queue = Queue()
for l in lotu:
    fqc_cmd_args=[fqc_cmdstr, "./"+ l[0] +"_"+ l[1] +"/"+ l[0] +"_forward_paired.fastq.gz", "./"+ l[0] +"_"+ l[1] +"/"+ l[0] +"_reverse_paired.fastq.gz", "> fqstndout.txt"]
    cmdstr="%s %s %s" % (fqc_cmd_args[0], fqc_cmd_args[1], fqc_cmd_args[2])
    # print cmdstr
    work_queue.put(cmdstr);

# listcompre coming up
processes = [ Process(target=do_work, args=(work_queue,)) for i in range(int(sys.argv[3])) ]
for p in processes:
    p.start()
for p in processes:
    p.join()
