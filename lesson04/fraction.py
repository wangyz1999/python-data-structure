class Fraction:
    def __init__(self, num, den=1):
        self.n = num
        assert den != 0, "denominator cannot be zero"
        self.d = den
        self.yuefen()

    def __str__(self):
        return str(self.n) + '/' + str(self.d)

    def __mul__(self, f):
        return Fraction(self.n * f.n, self.d * f.d)

    def __add__(self, f):
        return Fraction(self.n * f.d + self.d + f.n, self.d * f.d)

    def __eq__(self, f):
        return self.n == f.n and self.d == f.d

    def yuefen(self):
        if self.d % self.n == 0:
            self.d = self.d // self.n
            self.n = self.n // self.d
