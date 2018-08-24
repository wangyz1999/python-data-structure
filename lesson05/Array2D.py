from Array1D import *

class Array2D:
    def __init__(self, nr, nc):
        self.rows = Array1D(nr)
        for r in range(nr):
            self.rows[r] = Array1D(nc)
        self.clear(None)

    def numRows(self):
        return len(self.rows)

    def numCols(self):
        return len(self.rows[0])

    def clear(self, value):
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, idx):
        r, c = idx
        row = self.rows[r]
        return row[c]

    def __setitem__(self, idx, value):
        r, c = idx
        row = self.rows[r]
        row[c] = value
