from ctypes import *

class Array1D:
    def __init__(self, size):
        self.size = size
        array = py_object * size
        self.elements = array()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def clear(self, value):
        for i in range(self.size):
            self.elements[i] = value

    def __iter__(self):
        return ArrayIT(self.elements)


class ArrayIT:
    def __init__(self, array):
        self.array = array
        self.index = 0

    def __next__(self):
        self.index += 1
        if self.index < len(self.array):
            return self.array[self.index-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self
