#!/usr/bin/env python2
# experiment in using dendropy ... dendropy seems to be more manipulation. Viewing uses no graphics, merely ASCII.
import dendropy
tree = dendropy.Tree.get( path='mabsdm.tree', schema='newick')
# print type(tree)
# print dir(tree)
tree.print_plot()
