#!/usr/bin/env python2.7
# How to deal with dictionaries that get defined inside fucntions.
import os, regex, sys


def dais(strng):
	d={}
	d['today']="Wed"
	d['yest']="Tues"
	d['morrow']="Thurs"
	d['2morrow']=""
	d['goodmorrow']=None
	# note: d['amarach'] is not even None, it doesn't exist at all.
	
	try:
		val=d[strng]
	except KeyError:
		print "Warning: Value for " +strng+ " doesn't exist (not even None) returning a placeholder."
		val="A_place_holder"
	return val

L = [ "yest", "amarach", "goodmorrow"]
for I in L:
	print dais(I)
