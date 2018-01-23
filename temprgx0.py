#!/usr/bin/env python2.7
# kind of a template for regex based on r2.py .. fairly arbitrary name.
import sys, regex

def main():
    argquan=len(sys.argv)
    if argquan != 2:
        print "This script requires one argument: a file listing of the mash re sults files"
        sys.exit(2)

    # regex
    # Target range: 138 -> 222
    RGX0=regex.compile(r' +Target range: (\d+) -> (\d+)$')
    with open(sys.argv[1]) as x: fl = x.read().splitlines()
    L=[]
    for i in fl:
        m=RGX0.match(i)
        if(m):
            pd0= int(m.groups(1)[0]) # come out as strings of course ... pd, pair distance ... this we can convert to integer.
            pd2= int(m.groups(1)[1]) # come out as strings of course ... pd, pair distance ... this we can convert to integer.
            L.append( (pd0, pd2) )

    LSZ=len(L)
    cou=0
    for i in xrange(LSZ):
        if L[i][1]>L[i][0]:
            d=L[i][1]-L[i][0]
        else:
            d=-1*(L[i][1]-L[i][0])
        if d> 38:
            cou = cou+1
    print "%s: allals=%i / num38als=%i" % (sys.argv[1], LSZ,cou)

if __name__=='__main__':
    main()
