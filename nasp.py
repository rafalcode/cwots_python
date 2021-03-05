#!/usr/bin/env python
# name splitQ
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


n1="Jose Ramon Ibarra"
n2="Joyce Edith WIlkin"

RGX=regex.compile(r'([A-Za-z]+)')
m=RGX.findall(n1)
if m:
    print(m)
    print("there was a match")
else:
    print("No match")
