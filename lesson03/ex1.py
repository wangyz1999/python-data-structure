def fibrec(n):
    assert n >= 0, "n can't be negative"
    if n == 0 or n == 1:
        return n
    return fibrec(n-1) + fibrec(n-2)
