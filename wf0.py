#!/usr/bin/env python3
# count word frequencies
# more or less from https://programminghistorian.org/en/lessons/counting-frequencies
# heavy lifting function is the count. it's a method on the list.
# now this generates

wstr = 'it was the best of times it was the worst of times '
wstr += 'it was the age of wisdom it was the age of foolishness'

wlst = wstr.split()

# wf = []
# for w in wlst:
#         wf.append(wlst.count(w))
# list comprehension for this is:
wf = [wlst.count(w) for w in wlst] 
# easy enough because the loop is easy.
# how to list comprehend more difficult loops is different

print("Subject string is:\n" + wstr +"\n")
print("Split string results:\n" + str(wlst) + "\n")
print("Frequencies\n" + str(wf) + "\n")
pa = list(zip(wlst, wf))
pa = dict(pa)
print("Pairs\n" + str(pa))
