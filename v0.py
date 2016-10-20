#!/usr/bin/env python2.7
# exercise in us PyVCF which is fact loaded via "import vcf"
import sys, os ,vcf
argquan=len(sys.argv)
if argquan != 2:
	print "This script requires one argument: a vcf file"
	sys.exit(2)

vcfrdr = vcf.Reader(open(sys.argv[1], 'r'))
# the following won't work
# print "No. of records in vcf is %d" % len(vcfrdr)
# generally reader is a streamer, it won't really know the length
# you need to work it out on your first cycle through the entries.
# for rec in vcfrdr:
# 	print rec
