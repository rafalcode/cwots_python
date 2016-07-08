#!/usr/bin/env python2.7
import os, sys, re

# the root directory of the 
PATH="/storage/home/users/ml228/Genomics/NEA_first_lane/BGI_raw_data"

# what follows is a list comprehension of a loop over the files in a subdirectory
# and a loop over the subdirectories of the path, with the path and filename finally being joined together
# the code follows the engish in reverse: i.e. looping over files comes last.
fqz = [os.path.join(dp, f) for dp, dn, fnz in os.walk(PATH) for f in fnz ]

lfqz=len(fqz) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# we now want to pair the fastq's up
LL=[] # create empty list of pairs


# Going to use regex, although apparently module fnmatch (filename match) might also do a similar thing.
GZRGX=re.compile(r'.+gz')
DNRGX=re.compile(r'.+[IS]R*[0-9]+:')

# loop through fastq list two by two.
for i in xrange(1,lfqz/2):
    LF=[]
#     LL.append( [ fqz[2*i], fqz[2*i+1] ] ) # fill up LL with the paired-up fastq files
    if GZRGX.match(fqz[2*i]) is not None:
        LF.append(fqz[2*i])
        LF.append(fqz[2*i+1])
    LL.append(LF)

# for i in LL:
#     print "%s | %s" % (i[0], i[1])

TJAR="/usr/local/Modules/modulefiles/tools/trimmomatic/0.32/bin/trimmomatic-0.32.jar"
OPTS1="PE -threads 6 -phred33"
P1="/shelf/scratch/ml228/dolphins/NEA/raw_data_BGI_clean/cdts-wh.genomics.cn/F16FTSEUHT0289_DOLajnR/Clean/IR23/FCHVMHNCCXX_L1_wHAXPI030603-63_1.fq.gz"
P2="/shelf/scratch/ml228/dolphins/NEA/raw_data_BGI_clean/cdts-wh.genomics.cn/F16FTSEUHT0289_DOLajnR/Clean/IR23/FCHVMHNCCXX_L1_wHAXPI030603-63_2.fq.gz"
OFL=["IR23_forward_paired.fq", "IR23_forward_unpaired.fq", "IR23_reverse_paired.fq", "IR23_reverse_unpaired.fq"] # output file list

ENDSTR="ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:50"

CMDSTR="java -jar "+ TJAR +" "+ OPTS1 +" "+ P1 +" "+ P2 +" "+ OFL[0] +" "+ OFL[1] +" "+ OFL[2] +" "+ OFL[3] +" "+ ENDSTR # checked yes.
# for checking
# print "java -jar /usr/local/Modules/modulefiles/tools/trimmomatic/0.32/bin/trimmomatic-0.32.jar PE -threads 6 -phred33 /shelf/scratch/ml228/dolphins/NEA/raw_data_BGI_clean/cdts-wh.genomics.cn/F16FTSEUHT0289_DOLajnR/Clean/IR23/FCHVMHNCCXX_L1_wHAXPI030603-63_1.fq.gz /shelf/scratch/ml228/dolphins/NEA/raw_data_BGI_clean/cdts-wh.genomics.cn/F16FTSEUHT0289_DOLajnR/Clean/IR23/FCHVMHNCCXX_L1_wHAXPI030603-63_2.fq.gz IR23_forward_paired.fq IR23_forward_unpaired.fq IR23_reverse_paired.fq IR23_reverse_unpaired.fq ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:5 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:50"
for i in LL:
    CMDSTR="java -jar "+ TJAR +" "+ OPTS1 +" "+ i[0] +" "+ i[1] +" "+ OFL[0] +" "+ OFL[1] +" "+ OFL[2] +" "+ OFL[3] +" "+ ENDSTR # checked yes.
    print CMDSTR
