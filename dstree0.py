#!/usr/bin/env python2
# this pulled from http://biopython.org/wiki/Phylo

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

# the alignmnet is pretty much the elementary structure
aln = AlignIO.read('./msa.phy', 'phylip')
# print aln
# SingleLetterAlphabet() alignment with 5 rows and 13 columns
# AACGTGGCCACAT Alpha
# AAGGTCGCCACAC Beta
# GAGATTTCCGCCT Delta
# GAGATCTCCGCCC Epsilon
# CAGTTCGCCACAA Gamma

# Several thigns can be done witht he alignment: get a distance matrix from it:
dstcalc = DistanceCalculator('identity')
dm = dstcalc.get_distance(aln)
# DistanceMatrix(names=['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'], matrix=[[0], [0.23076923076923073, 0], [0.3846153846153846, 0.23076923076923073, 0], [0.5384615384615384, 0.5384615384615384, 0.5384615384615384, 0], [0.6153846153846154, 0.3846153846153846, 0.46153846153846156, 0.15384615384615385, 0]])
print "What's the get_distance(aln) from DistanceCalculator('identity') object?"
print type(dm)
print dm
# Alpha   0
# Beta    0.230769230769  0
# Gamma   0.384615384615  0.230769230769  0
# Delta   0.538461538462  0.538461538462  0.538461538462  0
# Epsilon 0.615384615385  0.384615384615  0.461538461538  0.153846153846  0

# build a tree from it.
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

construc0 = DistanceTreeConstructor(dstcalc, 'nj')
tre0 = construc0.build_tree(aln)
print type(tre0)
# as you can see from abovedstcalc is needed for te constructor and then
# to build the tree the alignment is needed. That's two things which need to originae fromt he same thing.
# A bit of a tall order
# You can build the tree from a distance matrix only, by leaving out the aln argument
# by not using the build_tree method on the constructor, but rather the .nj method

construc2 = DistanceTreeConstructor()
tre2 = construc2.nj(dm)
print type(tre2)
