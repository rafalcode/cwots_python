#!/usr/bin/env python2
# These are examples of using the collections module
# which do some very cool things whihc can take the headache of some things.
from collections import defaultdict

# first up, default dict ... you have a list of 2-tuples where the first element appears seveal times which different values.
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('blue', 2)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    
print d.items()

# WHat this does is combine the second member of the two-tuples (the values essentially)
# into a list. They key is unchanged and is only mentioned once.
# Even if there are no values to combine, the result is still a list, though only of one member.
