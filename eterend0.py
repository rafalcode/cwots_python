#!/usr/bin/env python2.7
# Experiments with ETE2 render engine.
import sys, re
from ete2 import Tree, TreeStyle

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: input filename")
    sys.exit(2)

with open(sys.argv[1]) as x: slurpf = x.read()
# so we have slurpf, a file read in as a complete string.
# it may have newlines, but the last newline is usually excess to requirements.
# somewhat forgetting about memory issues, here we create a new string with the final newline deleted or stripped.
# onestr=slurpf.rstrip('\n');
onestr=slurpf.translate(None,'\n') # delete all newlines and replace with nothing.
# print "File "+ sys.argv[1] +" read in as string, of length "+ str(len(onestr))
t=Tree(onestr)
ts = TreeStyle()
# ts.show_leaf_name = True
ts.show_branch_length = True
ts.scale = 10
# ts.show_branch_support = True
# t.render("mabst.png", tree_style=ts, "px", 780, 780)
t.render("mabst.png", tree_style=ts)
