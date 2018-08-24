class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.a > 100000:
            raise StopIteration
        else:
            self.a, self.b = self.b, self.a + self.b
            return self.a

    def __iter__(self):
        return self

class Test:
    def __iter__(self):
        return Fibs()
