#!/usr/bin/env python3
# reads in a csv a tabulates for latex.
import sys, csv,tabulate

if __name__ == "__main__":
    argquan=len(sys.argv)
    if argquan != 2:
       print("This script requires one argument")
       sys.exit(2)
    
with open(sys.argv[1], newline='') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
