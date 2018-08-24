class PolyTerm:
    def __init__(self, degree, coefficient):
        self.deg = degree
        self.coef = coefficient
        self.nextTerm = None


class Polynomial:
    def __init__(self, *coefficients):
        self.head = None
        if len(coefficients) != 0:
            for d in range(len(coefficients)):
                self.append(len(coefficients) -1 - d, coefficients[d])

    def degree(self):
        if self.head is None:
            return -1
        return self.head.deg

    def __str__(self):
        term = self.head
        polystr = ""
        if term is not None:
            polystr += "{}x^{}".format(term.coef, term.deg)
            term = term.nextTerm
        while term is not None:
            if term.coef is not None:
                polystr += " + {}x^{}".format(term.coef, term.deg)
                term = term.nextTerm
        return polystr

    def __getitem__(self, degree):
        term = self.head
        while term is not None and term.deg != degree:
            term = term.nextTerm
        if term is None:
            return 0
        else:
            return term.coef

    def __setitem__(self, degree, coefficient):
        if coefficient != 0:
            term = self.head
            preTerm = None
            while term is not None and term.deg > degree:
                preTerm = term
                term = term.nextTerm
            if term is None:
                self.append(degree, coefficient)
            elif term.deg == degree:
                term.coef = coefficient
            elif preTerm is None:
                newTerm = PolyTerm(degree, coefficient)
                newTerm.nextTerm = self.head
                self.head = newTerm
            else:
                newTerm = PolyTerm(degree, coefficient)
                preTerm.nextTerm = newTerm
                newTerm.nextTerm = term

    def evaluate(self, scalar):
        sum = 0.0
        term = self.head
        while term is not None:
            sum += term.coef * (scalar ** term.deg)
            term = term.nextTerm
        return sum

    def __add__(self, rhs):
        p = Polynomial()
        maxDeg = max(self.degree(), rhs.degree())
        for deg in range(maxDeg, -1, -1):
            p[deg] = self[deg] + rhs[deg]
        return p

    def __mul__(self, rhs):
        p = Polynomial()
        selfTerm = self.head
        while selfTerm is not None:
            rhsTerm = rhs.head
            while rhsTerm is not None:
                p[selfTerm.deg + rhsTerm.deg] += selfTerm.coef * rhsTerm.coef
                rhsTerm = rhsTerm.nextTerm
            selfTerm = selfTerm.nextTerm
        return p

    def append(self, deg, coef):
        if coef != 0:
            newTerm = PolyTerm(deg, coef)
            if self.head is None:
                self.head = newTerm
            else:
                self.tail.nextTerm = newTerm
            self.tail = newTerm

if __name__ == '__main__':
    p = Polynomial(1, 2, 2, 0)
    q = Polynomial(2, 4, 0, 3, 0)
    print(p)
    print(q)
    print(p+q)
    print(p*q)
