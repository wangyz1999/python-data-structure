class BinTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinTree:
	def __init__(self):
		self.root = None

	def q_buildTree(self, treeStr):
		q = list()
		self.root = BinTreeNode(treeStr.pop(0))
		q.append(self.root)
		while len(treeStr) > 0:
			node = q.pop(0)
			node.left = BinTreeNode(treeStr.pop(0))
			q.append(node.left)
			if len(treeStr) > 0:
				node.right = BinTreeNode(treeStr.pop(0))
				q.append(node.right)

	def buildTree(self, treeStr):
		nodes = []
		for c in treeStr:
			nodes.append(BinTreeNode(c))

		for i in range(len(treeStr)//2):
			nodes[i].left = nodes[2*i+1]
			nodes[i].right = nodes[2*i+2]

		self.root = nodes[0]

	def preOrderTrav(self):
		self.preOrder(self.root)

	def preOrder(self, tree):
		if(tree is None):
			return
		print(tree.data)
		self.preOrder(tree.left)
		self.preOrder(tree.right)

	def breadthFirstTrav(self):
		q = [self.root]
		while(len(q) > 0):
			node = q.pop(0)
			print(node.data)
			if(node.left is not None):
				q.append(node.left)
			if(node.right is not None):
				q.append(node.right)

	def rightSideView(self, root):
		ans = list()
		def DFS_RL(node, depth):
			if node is not None:
				if depth == len(ans):
					ans.append(node.data)
				DFS_RL(node.right, depth+1)
				DFS_RL(node.left, depth+1)
		DFS_RL(root, 0)
		return ans

if __name__ == "__main__":
	# t = BinTree()
	# t.buildTree("ABCDEFG");
	# t.preOrderTrav()
	# print("-----------------")
	# t.breadthFirstTrav()

	t = BinTree()
	Input = ['A','B','C','D',None,None,'E',None,'F']
	t.buildTree(Input)
	print(t.rightSideView(t.root))
