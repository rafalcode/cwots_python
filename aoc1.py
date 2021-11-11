#!/usr/bin/env python3
# AOC 2020 day 1
# take a list of numbers, find the single pair that adds to 2020 and return their product.
# the cahllenge itself is massively wordy.
# Joel is very succint here ... I think he's seen it before.
import sys 

argquan=len(sys.argv)
if argquan != 1:
   print("This script requires one argument")
   sys.exit(2)

# refer to arguments with sys.argv[1] etc.
from typing import List

INPUTS = [
        1721,
        979,
        366,
        299,
        675,
        1456,
]

def fiprod(inputs: List[int]) -> int:
    # (NOT) a dict comp where the key is the value subtracted from 2020.
    needs = {2020 - i for i in inputs} # sorry not a dict comp
    # print(needs)
    for i in inputs:
        # travel through the inputs ...
        if i in needs:
            # if they appear as a key then the corresponding value must be its partner in crime
            print(f"{2020-i} and {i}")
            return (2020-i) * i

assert fiprod(INPUTS) == 514579
