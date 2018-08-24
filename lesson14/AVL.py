class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.bf = 0
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def rotateRight(self, P):
        C = P.left
        P.left = C.right
        C.right = P
        return C

    def rotateLeft(self, P):
        C = P.right
        P.right = C.left
        C.left = P
        return C

    def min(self, subtree):
        if subtree is None:
            return None
        if subtree.left is None:
            return subtree
        return self.min(subtree.left)

    def insert(self, key):
        def recInsert(subtree, key):
            taller = False
            if subtree is None:
                subtree = AVLTreeNode(key)
                taller = True
            elif key < subtree.key:
                subtree.left, taller = recInsert(subtree.left, key)
                if taller:
                    if subtree.bf == 1:
                        subtree.bf = 0
                        taller = False
                    elif subtree.bf == 0:
                        subtree.bf = -1
                        taller = True
                    else:
                        taller = False
                        subtree = self.leftBalance(subtree)
            elif key > subtree.key:
                subtree.right, taller = recInsert(subtree.right, key)
                if taller:
                    if subtree.bf == -1:
                        subtree.bf = 0
                        taller = False
                    elif subtree.bf == 0:
                        subtree.bf = 1
                        taller = True
                    else:
                        taller = False
                        subtree = self.rightBalance(subtree)
            return subtree, taller
        self.root, taller = recInsert(self.root, key)

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

    def leftBalance(self, P):
        C = P.left
        if C.bf == -1:          # case 1
            P.bf = 0
            C.bf = 0
            P = self.rotateRight(P)
        elif C.bf == 1:         # case 2
            G = C.right
            # update b-factors
            if G.bf == 1:
                P.bf = 0
                C.bf = -1
            elif G.bf == -1:
                P.bf = 1
                C.bf = 0
            else:
                C.bf = 0
                P.bf = 0
            G.bf = 0
            P.left = self.rotateLeft(C)
            P = self.rotateRight(P)
        return P


    def rightBalance(self, P):
        C = P.right
        if C.bf == 1:          # case 1
            P.bf = 0
            C.bf = 0
            P = self.rotateLeft(P)
        elif C.bf == -1:         # case 2
            G = C.left
            if G.bf == 1:
                P.bf = -1
                C.bf = 0
            elif G.bf == -1:
                P.bf = 0
                C.bf = 1
            else:
                C.bf = 0
                P.bf = 0
            G.bf = 0
            P.right = self.rotateRight(C)
            P = self.rotateLeft(P)
        return P

    def printTree(self):
        def recPrintTree(q):
            q2 = []
            for node in q:
                if node is None:
                    print('N', end=' ')
                else:
                    q2.append(node.left)
                    q2.append(node.right)
                    print(node.key, end=' ')
            print()
            if len(q2) > 0:
                recPrintTree(q2)
        q = []
        q.append(self.root)
        recPrintTree(q)


if __name__ == '__main__':
    L = [60, 25, 35, 100, 17, 80]
    t = AVLTree()
    for x in L:
        t.insert(x)
        t.printTree()
        print()
