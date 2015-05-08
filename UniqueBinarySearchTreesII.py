'''
TO DO..
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param {integer} n
	# @return {TreeNode[]}
	def generateTrees(self, n):
		return self.root(1, n)

	def root(self, start, end):
		ret = []
		if start > end:
			ret.append(None)
			return ret

		for i in xrange(start, end + 1):
			leftChildren = self.root(start, i - 1)
			rightChildren = self.root(i + 1, end)
			for l in (leftChildren):
				for r in (rightChildren):
					node = TreeNode(i)
					node.left = l
					node.right = r
					ret.append(node)
		return ret

s = Solution()
print len(s.generateTrees(3))