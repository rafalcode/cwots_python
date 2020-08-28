#!/usr/bin/env python2
# experiments with pyPDF2
# particularly splitting a page.
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

argquan=len(sys.argv)
if argquan != 5:
    print "This script will insert a single page PDF after the specififilter out a certain page from a pdf"
    print "This script requires three arguments: 1) page index (i.e. zero indexed) to extract 2) input pdf name and 3) output pdf name"
    sys.exit(2)

with open(sys.argv[1], 'rb') as infile:
    reader0 = PdfFileReader(infile)
    np0 = reader.getNumPages()
    if(np0 != 1):
        print "Error. The first pdf must have only one page"
    p0 = reader0.getPage(0)

pno = int(sys.argv[2])

with open(sys.argv[3], 'rb') as infile:

    reader = PdfFileReader(infile)
    np = reader.getNumPages()
    writer = PdfFileWriter()

    for i in range(pno):
        writer.addPage(reader.getPage(pno))
    writer.addPage(p0)
    for i in range(pno+1,np):
        writer.addPage(reader.getPage(pno))

    with open(sys.argv[3], 'wb') as outfile:
        writer.write(outfile)

# Gen. notes
# d1=reader.getDocumentInfo()
# d2=reader.getNumPages()
# print(d1) will give
# {'/ModDate': u"D:20200407144402+01'00'", '/CreationDate': u'D:20190226134535Z', '/Trapped': '/False', '/Producer': u'Adobe PDF Library 15.0', '/Creator': u'Adobe InDesign CC 14.0 (Macintosh)', '/Title': u''}
# while d2 will give a simple integer
