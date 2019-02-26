#!/usr/bin/env python2.7
# pandas! yes!
# fltimespd.py
# File list times as pandas data frame
# this specific for using on (more or less) ftp long file listings.
from __future__ import with_statement
import sys
from datetime import datetime
import pandas as pd # practially all pandas programs have a line like that.
from tabulate import tabulate

argquan=len(sys.argv)
if argquan != 2:
    print "This script requires one argument a time file (geneseek times)"
    sys.exit(2)

with open(sys.argv[1]) as f: fl=f.read().splitlines()
nlines=len(fl)

lol=[] # an empty list of lists.
for lni in xrange(nlines):
    lsp= fl[lni].split()
    lstr= "%s %s-%s-2018" % (lsp[2], lsp[1], lsp[0])
    dtobj = datetime.strptime(lstr, '%H:%M %d-%b-%Y')
    # print dtobj.strftime("'%H:%M %d-%b-%Y")
    lol.append( [dtobj.strftime("%H:%M %d/%m/%Y"), ' '.join(lsp[3:])])

# Note that this geneseek is quite similar to a normal filelisting, and the filename comes at the end
# but may easily have spaces, that is why the join command and the open-slice to end is required.

# once you have a decently structured list of list 
df = pd.DataFrame(lol, columns=['timendate', 'foldname'])
# df['timendate'] = pd.to_datetime(df['timendate'], format='%H:%M %d/%m/%Y')
df['timendate'] = pd.to_datetime(df.timendate) # was surprised a dot-column name syntx here, maybe pandas isn't such a big hack?

# to dump out what pandas sees as the type of the df:
print df.dtypes
df.sort_values(by='timendate', ascending=True)
print tabulate(df, headers='keys', tablefmt='psql')
# note above the raw presentation of keys which must be waht pandas internally labels its column headers
