class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
	    n = len(triangle)
	    if n == 0:
	    	return 0
	    m = n
	    f = [[0 for i in range(m)] for j in range(n)]
	    f[0][0] = triangle[0][0]
	    for i in range(1, n):
	    	for j in range(i + 1):
	    		if j < 1:
	    			f[i][j] = f[i-1][j] + triangle[i][j]
	    		elif j == i:
	    			f[i][j] = f[i-1][j-1] + triangle[i][j]
	    		else:
	    			f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]

	    return min(f[n-1])

s = Solution()
tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print s.minimumTotal(tri)