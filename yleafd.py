#!/usr/bin/env python
# keep pressing down on browser to generate a listing of all the videos int he videos section of a channel.
# Just a lazy way to do it.
from pyautogui import press
import sys, os, time

argquan=len(sys.argv)
if argquan != 2:
    print("This script requires one argument: the number of sequential downs to press")
    sys.exit(2)

for i in range(int(sys.argv[1])):
    time.sleep(1)
    press("pgdn")
