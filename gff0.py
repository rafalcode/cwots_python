#!/usr/bin/env python2.7
import os, sys, re, subprocess
from gff3 import Gff3

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires 1 arg: a gff file"
    sys.exit(2)

gff = Gff3(sys.argv[1])
type_map = {'exon': 'pseudogenic_exon', 'transcript': 'pseudogenic_transcript'}
pseudogenes = [line for line in gff.lines if line['line_type'] == 'feature' and line['type'] == 'pseudogene']
for pseudogene in pseudogenes:
    # convert types
    for line in gff.descendants(pseudogene):
        if line['type'] in type_map:
            line['type'] = type_map[line['type']]
    # find overlapping gene
    overlapping_genes = [line for line in gff.lines if line['line_type'] == 'feature' and line['type'] == 'gene' and gff.overlap(line, pseudogene)]
    if overlapping_genes:
        # move pseudogene children to overlapping gene
        gff.adopt(pseudogene, overlapping_genes[0])
        # remove pseudogene
        gff.remove(pseudogene)
gff.write('annotations_fixed.gff')
