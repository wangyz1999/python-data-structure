from random import random as rd

def qSort(arr):
    n = (int) (rd()*len(arr))
    swap(arr, n, len(arr)-1)
    qSort_rec(arr, 0, len(arr)-1)

def qSort_rec(arr, l, h):
    if l >= h:
        return
    p = partition(arr, l, h)
    qSort_rec(arr, l, p-1)
    qSort_rec(arr, p+1, h)

def partition(arr, l, h):
    pivot = arr[h]
    i = l
    j = h - 1
    while i <= j:
        while i < h and arr[i] <= pivot:
            i += 1
        while j >= l and arr[j] > pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
        if i > j:
            swap(arr, i, h)
            break
    return i

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [(int)(rd()*90+10) for i in range(10)]
    print(arr)
    qSort(arr)
    print(arr)
