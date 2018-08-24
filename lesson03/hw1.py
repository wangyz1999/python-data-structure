def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[mid:]
        right = arr[:mid]
        arr.clear()

        mergesort(left)
        mergesort(right)

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
        arr += left + right
    return arr

print(mergesort([2,1,4,2,5,31,22,6,3]))
