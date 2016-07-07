#!/usr/bin/env python2
# takes text as STDIN and writes it out: that simple
from sys import stdin, stdout
 
for line in stdin:
    stdout.write(line)
