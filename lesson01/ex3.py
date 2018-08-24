from decimal import Decimal as de
from decimal import getcontext as gc

gc().prec = 50

f = 1
e = de(2)

for i in range(2, 50):
    f *= i
    e += de(1)/de(f)
#    print(f)
    print(e)
