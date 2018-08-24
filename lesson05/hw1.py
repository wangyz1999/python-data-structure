class Set:
    def __init__(self):
        self.elements = list()

    def __len__(self):
        return len(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def __str__(self):
        return str(self.elements)

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def remove(self, element):
        assert element in self, "The element must be in the set"
        self.elements.remove(element)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        for element in self:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        tmp = Set()
        for element in self:
            tmp.add(element)
        for element in setB:
            if element not in self:
                tmp.add(element)
        return tmp

    def intersect(self, setB):
        tmp = Set()
        for element in self:
            if element in setB:
                tmp.(element)
        return tmp

    def difference(self, setB):
        tmp = Set()
        for element in self:
            if element not in setB:
                tmp.add(element)
        return tmp

    def __iter__(self):
        return SetIT(self.elements)

class SetIT:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def __next__(self):
        if self.index < len(self.elements):
            self.index += 1
            return self.elements[self.index-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    s1 = Set()
    s2 = Set()
    s3 = Set()
    for i in range(5):
        s1.add(i)
        s2.add(i)
    for j in range(3,9):
        s3.add(j)
    print(s1)
    print(s2)
    print(s3)
    print(s1 == s2)
    print(s1 == s3)
    print(s1.union(s3))
    print(s1.intersect(s3))
    print(s1.difference(s3))
    print(s3.difference(s1))
    s3.remove(5)
    print(s3)
    s3.remove(88)
