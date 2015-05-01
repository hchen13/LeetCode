class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		# @m, number of rows
		# @n, number of columns
		m = len(grid)
		n = len(grid[0])

		f = [[-1 for i in range(n)] for j in range(m)]

		f[0][0] = grid[0][0]
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					continue
				if i - 1 < 0:
					f[i][j] = f[i][j-1] + grid[i][j]
				elif j - 1 < 0:
					f[i][j] = f[i-1][j] + grid[i][j]
				else:
					f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]

		return f[m-1][n-1]

g = [[1, 2, 3], [6, 5, 4], [8, 7, 9]]
s = Solution()
print s.minPathSum(g)