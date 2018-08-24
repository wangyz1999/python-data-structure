def zero(f):
    """Return church numeral 0"""
    return lambda x: x

def f(x):
    return 2*x

def one(f):
    """Return church numeral 1"""
    return lambda x: f(x)

def successor(n):
    """Return a successor of the given church numeral n"""
    return lambda f: lambda x: f(n(f)(x))

def church_to_int(n):
    """Return the church numeral n as a Python integer"""
    return n(lambda x: x + 1)(0)

def int_to_church(i):
    """Return the church numeral for integer i"""
    if i == 0:
        return zero
    else:
        return successor(int_to_church(i - 1))

def add(m, n):
    """Return the church numeral for m + n, for church numerals m and n."""
    return lambda f: lambda x: m(f)(n(f)(x))

def mul(m, n):
    """Return the church numeral for m * n, for church numerals m and n."""
    return lambda f: m(n(f))

def pow(m, n):
    """Return the church numeral for m ** n, for church numerals m and n."""
    return n(m)
