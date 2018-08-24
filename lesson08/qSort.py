from random import random as rd

def qSort(arr):
    n = (int) (rd()*len(arr))
    swap(arr, n, len(arr)-1)
    qSort_rec(arr, 0, len(arr)-1)

def qSort_rec(arr, l, h):
    if(l >= h):
        return
    p = partition(arr, l, h)
    qSort_rec(arr, l, p-1)
    qSort_rec(arr, p+1, h)

def partition(arr, l, h):
    pivot = arr[h]
    i = l
    for j in range(l, h):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, h)
    return i

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [(int)(rd()*90+10) for i in range(10)]
    print(arr)
    qSort(arr)
    print(arr)
