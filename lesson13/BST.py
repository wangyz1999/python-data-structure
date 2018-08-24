class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSTIT:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def __next__(self):
        if self.index < len(self.elements):
            self.index += 1
            return self.elements[self.index-1]
        raise StopIteration

    def __iter__(self):
        return self

class BST:
    def __init__(self):
        self.root = None

    def __iter__(self):
        def preOrd(subtree, items):
            if subtree is not None:
                preOrd(subtree.left, items)
                items.append(subtree.key)
                preOrd(subtree.right, items)
        elements = list()
        preOrd(self.root, elements)
        return BSTIT(elements)

    def search(self, key):
        def recSearch(subtree, key):
            if subtree is None:
                return None
            if subtree.key == key:
                return subtree
            if key > subtree.key:
                return recSearch(subtree.right, key)
            return recSearch(subtree.left, key)
        return recSearch(self.root, key)

    def insert(self, key):
        def recInsert(subtree, key):
            if subtree is None:
                subtree = BSTNode(key)
            elif key > subtree.key:
                subtree.right = recInsert(subtree.right, key)
            elif key < subtree.key:
                subtree.left = recInsert(subtree.left, key)
            return subtree
        self.root = recInsert(self.root, key)

    def min(self, subtree):
        if subtree is None:
            return None
        if subtree.left is None:
            return subtree
        return self.min(subtree.left)

    def printTree(self):
        def recPrintTree(q):
            q2 = []
            stop = True
            for e in q:
                if e is None:
                    print('N', end=' ')
                else:
                    stop = False
                    print(e.key, end=' ')
                    q2.append(e.left)
                    q2.append(e.right)
            print()
            if not stop:
                recPrintTree(q2)
        q = []
        q.append(self.root)
        recPrintTree(q)

    def remove(self, key):
        def recRemove(subtree, key):
            if subtree is None:
                return None
            if key > subtree.key:
                subtree.right = recRemove(subtree.right, key)
            elif key < subtree.key:
                subtree.left = recRemove(subtree.left, key)
            else:
                if subtree.left is None and subtree.right is None:
                    subtree = None
                elif subtree.left is None:
                    subtree = subtree.right
                elif subtree.right is None:
                    subtree = subtree.left
                else:
                    successor = self.min(subtree.right)
                    subtree.key = successor.key
                    subtree.right = recRemove(subtree.right, successor.key)
            return subtree
        self.root = recRemove(self.root, key)

from random import random as rd

if __name__ == '__main__':
    L = [(int)(rd()*90 + 10) for i in range(10)]
    print(L)
    t = BST()
    for x in L:
        t.insert(x)
    t.printTree()
