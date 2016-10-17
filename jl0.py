#!/usr/bin/env python2.7
# Demonstrates using joblib on a self-written function
import os, regex, sys
from math import sqrt
from joblib import Parallel, delayed

def dosqrt(num):
	sqn=sqrt(num)
	print "custom function for sqrt gives " +str(sqn)
	return sqn

LoN=[i for i in range(10)]
Parallel(n_jobs=2)(delayed(dosqrt)(i) for i in LoN)  # NB: If using Python 3.x, use list(range(10)).
