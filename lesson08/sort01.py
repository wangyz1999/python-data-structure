from random import random as rd

def sort01(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        while l < r and arr[l] == 0:
            l += 1
        while l < r and arr[r] == 1:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    return arr

if __name__ == '__main__':
    arr = [(int)(rd()*2) for i in range(10)]
    print(arr)
    print(sort01(arr))
