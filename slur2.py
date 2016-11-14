#!/usr/bin/env python3
# We move to python3 on this one, becuas eof its ease in handling unicodetwo cwots in here, how to slurp in a file and then a json.loads operation
# this is allows expanded use of the with statement:
import sys, re

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: input filename")
    sys.exit(2)

# OK, compile the regex, we include an option for . to include newlines. We us the ungreedy quantifier *? on our dot.
RGX=re.compile('\nSentence #([0-9]+).*?rus\n *([^\n]+).*?deu\n *([^\n]+).*?eng\n *([^\n]+)', re.DOTALL)
# RGX=re.compile('\nSentence #([0-9]+).*?rus\n *([^.]+).*?deu\n *([^.]+).*?eng\n *([^.]+)', re.DOTALL)
with open(sys.argv[1]) as x: slurpf = x.read()
fall=RGX.findall(slurpf)
print(len(fall))
for j in fall:
    print("%s\n%s\n%s\n%s\n" % (j[0], j[1], j[2], j[3])),
