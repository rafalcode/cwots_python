#!/usr/bin/env python2
# raison-d-etre: precisionon the calculation of the exp of 0.00001
# number precisions

from math import exp, expm1
print exp(1e-5) - 1
# 1.0000050000069649e-05
print expm1(1e-5)    # result accurate to full precision
# 1.0000050000166668e-05
