#!/usr/bin/env python2.7
# Searching a list of tuples
import os, regex, sys


def dais():
	LoT=[('Wed', False), ('Thurs', True), ('Fri', True), ('Sat', False)]
	day=('Thurs', True)
	if day in LoT:
		print "yes"
	else:
		print "nope"

dais()
