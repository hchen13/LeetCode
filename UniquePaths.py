class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePaths(self, m, n):
		f = [[1 for i in range(n)] for j in range(m)]
		for i in range(1, m):
			for j in range(1, n):
				f[i][j] = f[i-1][j] + f[i][j-1]
		return f[m-1][n-1]

s = Solution()
print s.uniquePaths(4, 3)