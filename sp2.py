#!/usr/bin/env python2.7
# splitting file names, we use lookahead grouping here which is similar to perl
# whereby the splitting token is captured
import sys,regex

# some typical names
# L=['SRR4054281_2.fastq.gz', '316292K_S9_L001_R1_001.fastq.gz', 'BS546900_trimmoed/BS546900_reverse_paired.fastq.gz', 'Undetermined_trimmoed/Undetermined_forward_paired.fastq.gz', '/etc/usr/bin/SRR4054281_1.fastq.gz']
L=['SRR4054281_2.fastq.gz', '316292K_S9_L001_R1_001.fastq.gz', 'BS546900_trimmoed/_/BS546900_reverse_paired.fastq.gz', 'Undetermined_trimmoed/Undetermined_forward_paired.fastq.gz', '/etc/usr/bin/SRR4054281_1.fastq.gz']

r=regex.compile(r'(?:([/._])+)')
L0=r.split(L[2])
print len(L0)
print "|".join(L0)
