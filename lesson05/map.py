class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)


class MapIT:
    def __init__(self, entries):
        self.entries = entries
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.entries):
            self.index += 1
            return self.entries[self.index-1]
        else:
            raise StopIteration


class Map:
    def __init__(self):
        self.entries = list()

    def __len__(self):
        return len(self.entries)

    def __contains__(self, key):
        idx = self.find(key)
        return idx is not None

    def add(self, key, value):
        entry = MapEntry(key, value)
        if key in self.entries:
            self.entries[key] = MapEntry
            return False
        else:
            self.entries.append(entry)
            return True

    def valueOf(self, key):
        idx = self.find(key)
        assert idx is not None, "Invalid map key"
        return self.entries[idx].value

    def remove(self, key):
        idx = self.find(key)
        assert idx is not None, "Invalid map key"
        self.entries.pop(idx)

    def __iter__(self):
        return MapIT(self.entries)

    def find(self, key):
        for i in range(len(self)):
            if self.entries[i].key == key:
                return i
        return None
