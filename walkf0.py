#!/usr/bin/env python2.7
import os, sys, re

# the root directory of the 
PATH="/storage/home/users/ml228/Genomics/NEA_first_lane/BGI_raw_data"
PATH="./"

# what follows is a list comprehension of a loop over the files in a subdirectory
# and a loop over the subdirectories of the path, with the path and filename finally being joined together
# the code follows the engish in reverse: i.e. looping over files comes last.
fqz = [os.path.join(dp, f) for dp, dn, fnz in os.walk(PATH) for f in fnz ]

lfqz=len(fqz) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# we now want to pair the fastq's up
LL=[] # create empty list of pairs

# Going to use regex, although apparently module fnmatch (filename match) might also do a similar thing.
GZRGX=re.compile(r'.+gz')
FGZRGX=re.compile(r'.+\.fastq\.gz')
DNRGX=re.compile(r'.+[IS]R*[0-9]+:')

# loop through fastq list two by two.
for i in xrange(1,lfqz):
    if FGZRGX.match(fqz[i]) is not None:
        LL.append(fqz[i])

for i in LL:
    print "%s " % (i[0], i[1]),
print
