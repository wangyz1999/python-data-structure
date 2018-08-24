def binSearch(arr, key):
    def recBinSearch(arr, key, l, h):
        if l > h:
            return -1
        m = (l+h)//2
        if arr[m] == key:
            return m
        if key > arr[m]:
            return recBinSearch(arr, key, m+1, h)
        return recBinSearch(arr, key, l, m-1)
    return recBinSearch(arr, key, 0, len(arr)-1)

from random import random as rd
arr = [(int)(rd()*30 + 10) for i in range(15)]
arr.sort()
print(arr)
print(binSearch(arr, 23))
