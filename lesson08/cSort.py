def cSort(arr):
    c = [0 for i in range(10)]
    for n in arr:
        c[n] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    b = [0 for i in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        c[arr[i]] -= 1
        b[c[arr[i]]] = arr[i]
    return b

if __name__ == "__main__":
    arr = [8, 3, 5, 1, 8, 2, 9, 5, 3, 1, 6]
    print(cSort(arr))
