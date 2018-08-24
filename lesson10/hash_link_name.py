from LinkList import LinkList

class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, key):
        return self.key == key

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class HashMap:
    def __init__(self, max_size):
        self.table = [LinkList() for i in range(max_size)]
        self.size = 0

    def __str__(self):
        outstr = ""
        for e in self.table:
            outstr += str(list(e)) + "\n"
        return outstr

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.find(key) is not None

    def add(self, key, value):
        slot = self.hash(key)
        node = self.table[slot].find(key)
        if node is not None:
            node.data.value = value
        else:
            self.table[slot].add(MapEntry(key, value))
            self.size += 1

    def find(self, key):
        slot = self.hash(key)
        if self.table[slot].find(key) is not None:
            return slot

    def remove(self, key):
        slot = self.find(key)
        if slot is not None:
            self.table[slot].remove(key)
            self.size -= 1

    def hash(self, key):
        M = len(self.table)
        encrypt_key = 0
        for letter in key:
            encrypt_key += ord(letter)
        return encrypt_key % M

if __name__ == '__main__':
    h = HashMap(7)
    h.add("John", "a")
    h.add("Mary", "b")
    h.add("Bill", "c")
    h.add("Mike", "d")
    h.add("Kelly", "e")
    print(h)
    h.remove("Kelly")
    print(h)
    h.add("Bill", 'nn')
    print(h)
