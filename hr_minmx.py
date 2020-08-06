#!/usr/bin/env python

import math
import os
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr2= sorted(arr)
    la = len(arr)
    bsum=sum(arr2[1:la-1])
    mn=arr2[0]+bsum
    mx=arr2[la-1]+bsum
    return mn, mx

if __name__ == '__main__':
    argquan=len(sys.argv)
    if argquan != 1:
        print("Follow hackerrank conventions for easy scripts, there are no argument, but atfer execution numbers of the array must be input.")
        sys.exit(2)
    arr = list(map(int, input().rstrip().split()))
    mn, mx= miniMaxSum(arr)
    # print("Min is "+str(mn)+" and max is "+str(mx))
    # above was wrong ... well, for the automated answer any how, only the two numbers were required.
    # following is correc (passed all the tests)
    print(mn, mx)

