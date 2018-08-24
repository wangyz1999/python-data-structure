from Array1D import *

class MaxHeap:
    def __init__(self, maxSize):
        self.elements = Array1D(maxSize)
        self.size = 0

    def __len__(self):
        return self.size

    def capacity(self):
        return len(self.elements)

    def add(self, element):
        assert self.size < self.capacity(), "Heap Full"
        self.elements[self.size] = element
        self.siftUp(self.size)
        self.size += 1

    def extract(self):
        assert self.size > 0, "Heap Empty"
        self.size -= 1
        self.swap(0, self.size)
        self.siftDown(0)
        return self.elements[self.size]

    def siftUp(self, idx):
        if idx > 0:
            parent = (idx-1)//2
            if self.elements[idx] > self.elements[parent]:
                self.swap(idx, parent)
                self.siftUp(parent)

    def siftDown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2

        largest = self.max(idx, left)
        largest = self.max(largest, right)

        if largest != idx:
            self.swap(largest, idx)
            self.siftDown(largest)

    def max(self, i, j):
        if j < len(self) and self.elements[j] > self.elements[i]:
            return j
        return i

    def swap(self, i, j):
        self.elements[i], self.elements[j] = \
        self.elements[j], self.elements[i]

    def display(self):
        for i in self.elements:
            print(i, end=' ')
        print()

    def heapify(self):
        for i in range(len(self)//2 - 1, -1, -1):
            self.siftDown(i)

if __name__ == "__main__":
    h = MaxHeap(10)
    h.add(7)
    h.add(4)
    h.add(6)
    h.add(1)
    h.add(3)
    h.add(8)
    h.display()
