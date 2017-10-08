#!/usr/bin/env python2.7
# from mertz's book

class Klass2:
    def __init__(self, *args, **kw):
        self.listargs = args
        for key, val in kw.items():
            setattr(self, key, val)

    def seeme(self):
        for i in self.listargs:
            print "%s " % i,
        print
        for key, val in self.__dict__:
            if key == "listargs":
                continue
            print "%s:%s " % (key, val)
        print

# obj = Klass2(1, 2, 3, foo='F00', bar=Klass2(baz='BAZ'))
obj = Klass2(1, 2, 3, foo='F00')
obj.seeme()
# print obj.__dict__
