class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def DFS(self, node, depth):
		if node is None:
			return 
		if depth + 1 > len(self.v):
			self.v.append(node.val)
		else:
			self.v[depth] = node.val
		self.DFS(node.left, depth + 1)
		self.DFS(node.right, depth + 1)

	def rightSideView(self, root):
		self.v = []
		self.DFS(root, 0)
		return self.v
		
	