class Bag:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def __iter__(self):
        return BagIT(self.items)

class BagIT:
    def __init__(self, theList):
        self.bagList = theList
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.bagList):
            self.index += 1
            return self.bagList[self.index-1]
        else:
            raise StopIteration
