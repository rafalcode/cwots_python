#!/usr/bin/env python2
# simple stdin to stdout direction
# Samuel Lampa's short piper.
from sys import stdin as i
from sys import stdout as o
for l in i:
    o.write(l)
