#!/usr/bin/env python2.7
# splitting file names, we use lookahead grouping here which is similar to perl
# whereby the splitting token is captured
import sys,regex

# some typical names
# L=['SRR4054281_2.fastq.gz', '316292K_S9_L001_R1_001.fastq.gz', 'BS546900_trimmoed/BS546900_reverse_paired.fastq.gz', 'Undetermined_trimmoed/Undetermined_forward_paired.fastq.gz', '/etc/usr/bin/SRR4054281_1.fastq.gz']
L=['roar.txt', 'SRR4054281_2.fastq.gz', '316292K_S9_L001_R1_001.fastq.gz', 'BS546900_trimmoed/_/BS546900_reverse_paired.fastq.gz', 'Undetermined_trimmoed/Undetermined_forward_paired.fastq.gz', '/etc/usr/bin/SRR4054281_1.fastq.gz','/etc/usr/bin/SRR9999999.fastq.gz', '/on/theball_R']

# r=regex.compile(r'(?:([/_])+)')
# L0=r.split(L[0])
# print len(L0)
# print "|".join(L0)
# note how the split command will split on multicharacter. Notice how it does not return False if the token did not exist.
# the only way it would seem to make sure the toekn existed is to check for 1.
# not eedge case ... if split mataches it will still be a 2.
for i in L:
	print len(i.split('_R'))
