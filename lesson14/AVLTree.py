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

	def insert(self, key):
		self.root, taller = self.recInsert(self.root, key)

	def recInsert(self, subtree, key):
		taller = False
		if(subtree is None):
			subtree = AVLTreeNode(key)
			taller = True
		elif(key < subtree.key):
			subtree.left, taller = self.recInsert(subtree.left, key)
			if(taller):
				if(subtree.bf == 1):
					subtree.bf = 0
					taller = False
				elif(subtree.bf == 0):
					subtree.bf = -1
					taller = True
				else:
					taller = False
					subtree = self.leftBalance(subtree)
		elif(key > subtree.key):
			subtree.right, taller = self.recInsert(subtree.right, key)
			if(taller):
				if(subtree.bf == -1):
					subtree.bf = 0
					taller = False
				elif(subtree.bf == 0):
					subtree.bf = 1
					taller = True
				else:
					taller = False
					subtree = self.rightBalance(subtree)
		return subtree, taller

	def leftBalance(self, P):
		C = P.left
		if(C.bf == -1):    # case 1
			P.bf = 0
			C.bf = 0
			P = self.rotateRight(P)
		elif(C.bf == 1):    # case 2
			G = C.right
			# update b-factors
			if(G.bf == 1):
				P.bf = 0
				C.bf = -1
			elif(G.bf == -1):
				P.bf = 1
				C.bf = 0
			else:
				P.bf = 0
				C.bf = 0
			G.bf = 0
			P.left = self.rotateLeft(C)
			P = self.rotateRight(P)
		return P

	def rightBalance(self, P):
		C = P.right
		if(C.bf == 1):    # case 1
			P.bf = 0
			C.bf = 0
			P = self.rotateLeft(P)
		elif(C.bf == -1):    # case 2
			G = C.left
			# update b-factors
			if(G.bf == 1):
				P.bf = -1
				C.bf = 0
			elif(G.bf == -1):
				P.bf = 0
				C.bf = 1
			else:
				P.bf = 0
				C.bf = 0
			G.bf = 0
			P.right = self.rotateRight(C)
			P = self.rotateLeft(P)
		return P

	def printTree(self):
		q = []
		q.append(self.root)
		self.recPrintTree(q)

	def recPrintTree(self, q):
		q2 = []
		for node in q:
			if(node is None):
				print('N', end=' ')
			else:
				q2.append(node.left)
				q2.append(node.right)
				print(node.key, end=' ')
		print()

		if(len(q2) > 0):
			self.recPrintTree(q2)

if __name__ == '__main__':
	from random import random as rd
	L = [60, 25, 35, 100, 17, 80]
#	L = [(int)(rd()*90+10) for i in range(80)]
	t = AVLTree()
	for x in L:
		t.insert(x)
		t.printTree()
		print('---------------')
