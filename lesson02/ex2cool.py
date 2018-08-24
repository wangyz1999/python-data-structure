from random import random as rd

a = [int(rd()*100) for i in range(10)]
b = [int(rd()*100) for i in range(10)]

a.sort()
b.sort()

c = []

while(len(a) > 0 and len(b) > 0):
    if a[0] < b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))

c = c + a + b
