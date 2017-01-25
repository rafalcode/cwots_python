#!/usr/bin/env python2
from Bio.Emboss.Applications import NeedleCommandline
from Bio.Emboss.Applications import FNeighborCommandline

needle_cline = NeedleCommandline(asequence="a0.fa", bsequence="b0.fa", gapopen=10, gapextend=0.5, outfile="needle.txt")
print type(needle_cline)
# print(needle_cline)
# needle -outfile=needle.txt -asequence=alpha.faa -bsequence=beta.faa -gapopen=10 -gapextend=0.5
print dir(needle_cline)
# so how to execute? simple
# sin,ser=needle_cline()
# here we capture stdin and sterr which can be checked for longer programs.

# Try the fnei
neicmdl=FNeighborCommandline(datafile="neighbor.dat", outfile="fneiout.txt")
print dir(neicmdl)
sin,ser=neicmdl()
print sin
print ser
