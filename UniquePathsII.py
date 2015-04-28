class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
	    n = len(obstacleGrid)
	    m = len(obstacleGrid[0])
	    f = [[0 for i in range(m)] for j in range(n)]
	    
	    # initializing status
	    for i in range(n):
	    	if obstacleGrid[i][0] == 1:
	    		break
	    	f[i][0] = 1
	    for i in range(m):
	    	if obstacleGrid[0][i] == 1:
	    		break
	    	f[0][i] = 1

	    for i in range(1, n):
	    	for j in range(1, m):
	    		if obstacleGrid[i][j] == 1:
	    			continue
	    		f[i][j] = f[i-1][j] + f[i][j-1]
	    return f[n-1][m-1]


s = Solution()
print s.uniquePathsWithObstacles([[0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])