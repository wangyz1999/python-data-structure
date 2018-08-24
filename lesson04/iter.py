class Iter:
    def __init__(self, arr):
        self.a = arr
        self.size = len(arr)

    def __next__(self):
        if self.size == 0:
            raise StopIteration
        else:
            self.size -= 1
            return self.a[self.size]

    def __iter__(self):
        return self


class Test:
    def __init__(self):
        self.elements = [1,2,3,4]

    def __iter__(self):
        return Iter(self.elements)
