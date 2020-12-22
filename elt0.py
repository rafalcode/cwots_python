#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires at least one argument: the name of the XML file.")
    sys.exit(2)

tree = ET.parse(sys.argv[1])
root = tree.getroot()
# print(root)

for child in root:
    lc = len(child)
    for i in range(lc):
        print(child[i].attrib)
    # print(child.attrib['name'])
    # print(child.tag, child.attrib)
