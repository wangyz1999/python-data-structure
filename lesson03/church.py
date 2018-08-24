def zero(f):    # f is a function
    return lambda x : x     # returns a function

def f(x):
    return 2*x

def successor(n):
    return lambda y : lambda x : y(n(y)(x))     # nested lambda

def one(f):
    return successor(zero)(f)

def two(f):
    return successor(one)(f)

def three(f):
    return successor(two)(f)

def church_to_int(n):
    return n(lambda x : x+1)(0)

def many(n, f):
    def rec(n, f):
        if n == 0:
            return zero
        return successor(rec(n-1, f))
    return rec(n,f)(f)
