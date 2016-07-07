#!/usr/bin/env python2
# basic class exercises
# from the phrasebook

class testClass(object):
# class testClass():
    print "Creating New Class\n=================="
    number=5
    def __init__(self, string):
        self.string = string
    def printClass(self):
        print "Number = %d"% self.number
        print "String = %s"% self.string

tc = testClass("Five")
# tc = testClass()
tc.printClass()
tc.number = 10
tc.string = "Ten"
tc.printClass()

# Above I tried to leave out the argument in the call and I got
# Traceback (most recent call last):
#   File "./bcla0.py", line 15, in <module>
#     tc = testClass()
# TypeError: __init__() takes exactly 2 arguments (1 given)

# omitting the argument (i.e. object) inn the Class definition 
# does not cause an error.
