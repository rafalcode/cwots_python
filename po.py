#!/usr/bin/env python2.7

import regex, subprocess

def hilite(string, bold):
    attr = []
    lo=ord(string[0])
    if lo < 97:
        lo+=32 
    fli=lo%5
    if fli==0:
        # green
        attr.append('32')
    elif fli ==1:
        # other color (31 is red BTW)
        attr.append('33')
    elif fli ==2:
        attr.append('35')
    elif fli ==3:
        attr.append('36')
    elif fli ==4:
        attr.append('37')
    if bold:
        attr.append('1')
    str='\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
    return str.ljust(50)


moav="/usr/local/Modules/3.2.10/modulefiles/moduleav.asof"
with open(moav) as x: FSLURP = x.read()

RGX=regex.compile(r'\n([A-Za-z].+)')
m=RGX.findall(FSLURP)
msz4=len(m)/4
hdr='\n\x1b[33;1mColorized, faster listing of modules available for loading on marvin:\x1b[0m\n'
hdr+='\x1b[33;1m--------------------------------------------------------------------\x1b[0m'
print hdr
for i in xrange(msz4):
    print "%s\t%s\t%s\t%s" % (hilite(m[i], 0), hilite(m[i+msz4], 0), hilite(m[i+2*msz4], 0), hilite(m[i+3*msz4], 0))
print
