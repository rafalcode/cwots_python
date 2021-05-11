#!/usr/bin/env python
# objects into dict! from https://www.kite.com/python/answers/how-to-use-a-custom-object-as-a-key-in-a-dictionary-in-python
# the example itself is a little thwarted because two objects witht he exact same attributes are put in
# that is not a good idea, because we are choosing dictionary because we want to enforce uniqueness of some sort
# i.e. we're confident there is uniqueness and we wanted it tracked.
# so the example is thwarted. 

class C:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    # essentia for the dict: how is the hash calculated?
    def __hash__(self):
        return hash((self.a1, self.a2)) # Ans: two variables, packed together in a tuple.
    def __eq__(self, other):
        # may not look necessary, but best to be explicit, hashes invariably need this.
        return (self.a1, self.a2) == (other.a1, other.a2)

ath = C("a", 1)
bth = C("a", 1)
cth = C("b", 2)

odict = {ath: 3, bth: 4, cth: 5}

print(odict[ath])
print(odict[bth])
print(odict[cth])
print(len(odict))
