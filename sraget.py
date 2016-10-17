#!/usr/bin/env python2.7
# A partially automated way of retrieving an SRA file from the Short Read Archive
import sys
from subprocess import call

argquan=len(sys.argv)
if argquan != 3:
    print "This script requires two arguments: the SRX##etc and the SR##etc"
    sys.exit(2)

U=r'ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByExp/sra/SRX/'
U +=sys.argv[1][0:6] +'/'
U +=sys.argv[1] +'/'
U +=sys.argv[2] +'/'
U +=sys.argv[2] +'.sra'
cmd=['wget', U]
# wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByExp/sra/SRX/SRX339/SRX339603/SRR961865/SRR961865.sra
print "%s" % " ".join(cmd)
call(cmd)
