#!/usr/bin/env python2.7
from Bio.Emboss.Applications import NeedleCommandline

needle_cline = NeedleCommandline(asequence="a0.fa", bsequence="b0.fa", gapopen=10, gapextend=0.5, outfile="needle.txt")
print type(needle_cline)
# print(needle_cline)
# needle -outfile=needle.txt -asequence=alpha.faa -bsequence=beta.faa -gapopen=10 -gapextend=0.5
print dir(needle_cline)
# so how to execute? simple
# sin,ser=needle_cline()
# here we capture stdin and sterr which can be checked for longer programs.

# Tryng the fneighbor program is thorny because it's not actually in EMBOSS proper.
# It's in its sister package EMBASSY, and inside that, in the PHYLIP subpackage.
from Bio.Emboss.Applications import FNeighborCommandline
# neicmdl=FNeighborCommandline(datafile="neighbor.dat", outfile="fneiout.txt")

# OK with a foreign matrix this finally works
# it's forward slash type of square matrix, but it accepts it great .. because all examples show backwards
neicmdl=FNeighborCommandline(datafile="dma0.dat", outfile="mabsdm.out", outtreefile="mabsdm.tree", matrixtype="square")
# however the labels must be left justified. No small matter. Actually in python %-7s did it.
# 

# what does thsi object igve you?
# negold the output of print dir(neicmdl)
# ['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_value', '_clear_parameter', '_get_parameter', '_validate', 'auto', 'datafile', 'debug', 'die', 'error', 'filter', 'help', 'jumble', 'matrixtype', 'options', 'outfile', 'outgrno', 'outtreefile', 'parameters', 'program_name', 'progress', 'seed', 'set_parameter', 'stdout', 'treeprint', 'treetype', 'trout', 'verbose', 'warning']

# no output tree file defined. the default is neighbor.treefile
sin,ser=neicmdl()
print sin
print ser
