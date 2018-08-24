import numpy as np

isPrime = np.ones((100,),dtype=bool)
isPrime[:2] = 0
N = int(np.sqrt(len(isPrime)-1))
for j in range(2, N+1):
    isPrime[2*j::j] = 0
print(isPrime.nonzero())
