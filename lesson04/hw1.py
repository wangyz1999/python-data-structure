class ArrayIT:
    def __init__(self, array):
        self.array = array
        self.index = 0

    def __next__(self):
        self.index += 1
        if self.index < len(self.array):
            return self.array[self.index]
        else:
            raise StopIteration

    def __iter__(self):
        return self
