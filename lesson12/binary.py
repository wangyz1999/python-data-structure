def toChar(d):
    b = 0
    for c in d:
        b = b*2 + int(c)
    return chr(b)

def toDigit(c):
    n = ord(c)
    d = ''
    for i in range(8):
        d = str(n%2) + d
        n = n//2
    return d

d = '1110010110010'
c = toChar(d)
print(c)
print(ord(c))
d2 = toDigit(c)
print(d2)
