from random import random as rd

def mergelist(l1, l2):
    out = list()
    while len(l1) != 0 and len(l2) != 0:
        if len(l1) == 0 or l1[0] > l2[0]:
            out.append(l2.pop(0))
        else:
            out.append(l1.pop(0))
    return out + l1 + l2

a = [int(rd()*100) for i in range(10)]
b = [int(rd()*100) for i in range(10)]

a.sort()
b.sort()

print(mergelist(a, b))
