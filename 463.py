
class Solution(object):
	def enlarge_grid(self, grid):
		n, m = len(grid), len(grid[0])
		large = [[0 for j in range(m + 2)] for i in range(n + 2)]
		for i, row in enumerate(grid):
			for j, cell in enumerate(row):
				large[i + 1][j + 1] = grid[i][j]
		return large


	def count_perimeter(self, grid, i, j):
		steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		count = 0
		for dx, dy in steps:
			x = i + dx
			y = j + dy
			if grid[x][y] == 0:
				count += 1
		return count


	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		grid = self.enlarge_grid(grid)
		n, m = len(grid), len(grid[0])
		perimeter = 0
		for i in range(1, n-1):
			for j in range(1, m-1):
				if grid[i][j] == 1:
					perimeter += self.count_perimeter(grid, i, j)
		return perimeter


grid = [[0,1,0,0],
		[1,1,1,0],
		[0,1,0,0],
		[1,1,0,0]]

s = Solution()
result = s.islandPerimeter(grid)
print result
