def rSort(arr, nDigits):
    b = [None for in in range(10)]
    for i in range(len(b)):
        b[i] = list()

    column = 1
    for d in range(nDigits):
        for key in arr:
            digit = (key//column) % 10
            b[digit].append(key)
        i = 0
        for q in b:
            while len(q) > 0:
                arr[i] = q.pop(0)
                i += 1
        column *= 10

if __name__ == "__main__":
