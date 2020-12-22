#!/usr/bin/env python3
# A CSV table preparation of sorts.
# we take a list and break it into tupes.
# if anything because that's fundamentally what they're for
# and then we make a csv oout of them

a = ["ab", "cd", "ef", "gh", "ij", "kl"]
la=len(a)

lot=[]
for i in range(0,la,3):
    lot.append((a[i], a[i+1], a[i+2]))

llot=len(lot)
for i in range(llot):
    print(lot[i][0] +","+ lot[i][1] +","+ lot[i][2])

ofn = "output.csv"

with open(ofn, "w") as f:
    for i in range(llot):
        f.write(lot[i][0] +","+ lot[i][1] +","+ lot[i][2]+"\n")
    f.close()
