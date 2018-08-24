class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class HashMap:
    def __init__(self, max_size):
        self.table = [None] * max_size
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.find(key) is not None

    def add(sel, key, value):
        slot = self.find_next_slot(key)
        self.table[slot] = MapEntry(key, value)
        self.size += 1

    def find_next_slot(self, key):
        assert len(self) < len(self.table), 'table full'
        assert key not in self.table, 'duplicated keys'
        slot = self.hash(key)
        M = len(self.table)
        while self.table[slot] is not None and \
              self.table[slot].key is not None:
            slot = (slot+1) % M
        return slot

    def find(self, key):
        slot = self.hash(key)
        M = len(self.table)
        while self.table[slot] is not None and \
              self.table[slot].key != key:
            slot = (slot+1) % M
        if self.table[slot] is not None:
            return slot

    def remove(self, key):
        slot = self.find(key)
        if slot is not None:
            self.table[slot].key = None
            self.size -= 1

    def hash(self, key):
        M = len(self.table)
        return key % M

if __name__ == '__main__':
    h = HashMap(13)
    h.add(765, "a")
    h.add(431, "b")
    h.add(96, "c")
    h.add(142, "d")
    h.add(579, "e")
    h.add(226, "f")

    for e in h.table:
        print(e)
