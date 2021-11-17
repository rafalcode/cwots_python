#!/usr/bin/env python3
# rglod.py Mnemonic Regex to list of dictionaries.
import sys, re

argquan=len(sys.argv)
if argquan != 1 and argquan !=2:
    print("rglod.py: takes in an entire file and cycles a (newline-spanned) regex through a text file")
    print("WIth no argument an internal hardcoded string will be used. With one argument, input filename")
    sys.exit(2)

if(argquan==2): 
    with open(sys.argv[1]) as x: slurpf = x.read()
else:
    slurpf='''
1:25:15
Now playing
Сашка (военная драма, реж. Александр Сурин, 1981)
685K views11 days ago
1:29:53
Now playing
«Неизвестные страницы из жизни разведчика» (приключения, военный, реж. Владимир Чеботарев, 1990)
18K views13 days ago
1:38:03
Now playing
Пять вечеров (мелодрама, реж. Никита Михалков, 1978)
296K views2 weeks ago
1:23:38
Now playing
По прозвищу «Зверь» (боевик, реж. Александр Муратов, 1990)
2.9M views3 weeks ago
'''

# Following just so hap
RGX=re.compile('(?P<LN>.+)\nNow playing\n(?P<TX>.+)\n(?P<VI>\d+\w) v.+')

# many re functions look for one match ... to cycle through them all, you need finditer()
outs= [m.groupdict() for m in re.finditer(RGX, slurpf)]

#print out
print("%12s %8s     %20s" % ("Duration", "Views", "Titles and comments"))
for o in outs:
    print("%12s %8s     %20s" % (o['LN'], o['VI'], o['TX']))
