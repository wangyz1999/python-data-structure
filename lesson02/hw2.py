from random import random

arr = [int(random()*100) for i in range(10)]
print(arr)

l = list()
length = len(arr)

for i in range(length):
    min = 101
    index = 0
    for j in range(i,length):
        if arr[j] < min:
            min = arr[j]
            index = j
    arr[i],arr[index] = arr[index],arr[i]

print(arr)
