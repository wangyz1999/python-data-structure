class ExpTreeNode:
	def __init__(self, data):
		self.element = data
		self.left = None
		self.right = None

class ExpressionTree:
	def __init__(self, expStr):
		self.root = None
		self.buildTree(expStr)

	def buildTree(self, expStr):
		expQ = list(expStr)

		self.root = ExpTreeNode(None)
		self.recBuildTree(self.root, expQ)

	def recBuildTree(self, node, expQ):
		token = expQ.pop(0)

		if token == '(':
			node.left = ExpTreeNode(None)
			self.recBuildTree(node.left, expQ)

			node.element = expQ.pop(0)

			node.right = ExpTreeNode(None)
			self.recBuildTree(node.right, expQ)

			expQ.pop(0)
		else:
			node.element = token

	def __str__(self):
		return self.buildString(self.root)

	def buildString(self, node):
		if node.left is None and node.right is None:
			return str(node.element)

		expStr = '('
		expStr += self.buildString(node.left)
		expStr += str(node.element)
		expStr += self.buildString(node.right)
		expStr += ')'

		return expStr

	def evaluate(self, varMap):
		return self.evalTree(self.root, varMap)

	def evalTree(self, node, varMap):
		if node.left is None:
			if node.element.isalpha():
				assert node.element in varMap, "invalid variable"
				return varMap[node.element]
			else:
				return int(node.element)
		else:
			l = self.evalTree(node.left, varMap)
			r = self.evalTree(node.right, varMap)
			return self.computeOp(l, node.element, r)

	def computeOp(self, x, op, y):
		if op == '+':
			return x + y
		if op == '-':
			return x - y
		if op == '*':
			return x * y
		if op == '/':
			return x / y
		if op == '%':
			return x % y


if __name__ == '__main__':
	vars = {'a':5,'b':12}

	expTree = ExpressionTree("(a/(b-3))")
	print("The result = ", expTree.evaluate(vars))

	vars['a'] = 22
	print("The result = ", expTree.evaluate(vars))
