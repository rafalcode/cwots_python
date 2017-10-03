#!/usr/bin/env python2.7
import sys
from itertools import repeat
import csv

with open(sys.argv[1],'rb') as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)

    for row in tsvin:
        print len(row)




        # count = int(row[4])
        # if count > 0:
        #     csvout.writerows(repeat(row[2:4], count))
