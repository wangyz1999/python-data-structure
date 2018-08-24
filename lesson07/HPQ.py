class PQE:
    def __init__(self, item, p):
        self.item = item
        self.priority = p

    def __str__(self):
        return '{}:{}'.format(self.item, self.priority)

class HeapPQ:
    def __init__(self):
        self.qList = list()

    def __len__(self):
        return len(self.qList)

    def enqueue(self, i, p):
        entry = PQE(i, p)
        self.qList.append(entry)
        self.siftUp(len(self)-1)

    def dequeue(self):
        assert len(self) > 0, "Queue Empty"
        self.swap(0, -1)
        temp = self.qList.pop()
        self.siftDown(0)
        return temp

    def siftUp(self, idx):
        if idx > 0:
            parent = (idx-1)//2
            if self.qList[idx].priority > \
               self.qList[parent].priority:
                self.swap(idx, parent)
                self.siftUp(parent)

    def siftDown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = self.max(self.max(idx, left), right)
        if largest != idx:
            self.swap(largest, idx)
            self.siftDown(largest)

    def max(self, i, j):
        if j < len(self) and self.qList[j].priority > \
                             self.qList[i].priority:
            return j
        return i

    def swap(self, i, j):
        self.qList[i], self.qList[j] = \
        self.qList[j], self.qList[i]

    def display(self):
        for i in self.qList:
            print(i, end=' ')
        print()

if __name__ == "__main__":
    a = HeapPQ()
    a.enqueue('a',1)
    a.enqueue('b',69)
    a.enqueue('c',520)
    a.enqueue('d',80)
    a.enqueue('e',7)
    a.enqueue('f',8848)
    a.enqueue('g',13)
    a.enqueue('h',44944)
    a.display()
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
    print(str(a.dequeue()))
