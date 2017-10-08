#!/usr/bin/env python2.7
# from mertz's book

class Klass2:
    def __init__(self, *args, **kw):
        self.listargs = args
        for key, val in kw.items():
            setattr(self, key, val)

# obj = Klass2(1, 2, 3, foo='F00', bar=Klass2(baz='BAZ'))
# with this
obj = Klass2(1, 2, 3, foo='F00', 4, 5, bar=Klass2(baz='BAZ'))
# you will get
# SyntaxError: non-keyword arg after keyword arg
# because of the order of the the __init__ func args ... I think that should be self-evident.
obj.bar.blam = 'BLAM'

# 
ob=obj.listargs, obj.foo, obj.bar.baz, obj.bar.blam

# here we let ob2 equal a list
# can be via implicit parens
# ob2=obj.listargs, obj.foo, obj.bar.baz, obj.bar.blam
# or explicit parens
ob2=(obj.listargs, obj.foo, obj.bar.baz, obj.bar.blam)
#                 ((1, 2, 3), 'F00', 'BAZ', 'BLAM')
sobj=str(obj)
print ob2
#
# But what's this? ... I have Klass2 a series of fields


# Notes:
# This example show how much manipulation can take place
