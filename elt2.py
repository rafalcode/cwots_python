#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires at least one argument: the name of the XML file.")
    sys.exit(2)

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for els in root:
    # print(els[0].text, end=': ')
    len1=len(els)
    for i in range(0, len1, 2):
        print(els[i].text, end=":")
        len2 = len(els[i+1])
        # print(len2)
        for j in range(0, len2, 2):
            # print(els[i+1][j].text, end =" ")
            # print(els[i+1][j].text, end =" ")
            # print(els[i+1][j][0].text+",", end=" ")
            print(els[i+1][j][0].text+","+els[i+1][j][1].text, end = " ")
            print(els[i+1][j+1][0].text+","+els[i+1][j+1][1].text)


# there's actually three different authors, though each article only has two.
# the total number of different authors must be caluclated before a table can be built.
