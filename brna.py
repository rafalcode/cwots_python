#!/usr/bin/env python2.7
# using biopython to render DNA into RNA forward and reverse.
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

sq="AGTACACTGGT"
dn = Seq(sq, generic_dna)
print "we convert " +dn
rn = dn.transcribe()
print "to " +rn
# rn2=rn.back_transcribe().reverse_complement()
rn2=rn.reverse_complement()
rn3=rn2.complement()
print "and then reverse complement the transcription to " +rn2
print
print "in a more visual friendly form:"
print dn+ " ->"
print "       " +rn
print "rev:   " +rn3
print "comp:  " +rn2
