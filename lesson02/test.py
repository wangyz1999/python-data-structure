import numpy as np
import scipy.stats as stats
import pylab as pl
from random import random

out = list()
#total = {j for j in range(10000)}
for hah in range(3000):
    arr = {int(random()*100000) for i in range(100000)}
    #diff = total - set
    size = 100000 - len(arr)
    out.append(size)
out.sort()
#print(out)

fit = stats.norm.pdf(out, np.mean(out), np.std(out))

print("mean: {}\nmedian: {}\nstd: {}".format(np.mean(out),np.median(out),np.std(out)))

pl.plot(out, fit, '-o')

pl.hist(out, density=True)

pl.show()
