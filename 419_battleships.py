def leftmost(i, j, board):
	if i == 0 and j == 0:
		return True
	if i == 0 and board[i][j-1] != 'X':
		return True
	if j == 0 and board[i-1][j] != 'X':
		return True
	return board[i-1][j] != 'X' and board[i][j-1] != 'X'

class Solution(object):
	def countBattleships(self, board):
		"""
		:type board: List[List[str]]
		:rtype: int
		"""
		count = 0
		for i, row in enumerate(board):
			for j, cell in enumerate(row):
				if cell == 'X':
					if leftmost(i, j, board):
						count += 1
		return count


board = [
	['X', '.', '.', 'X'],
	['.', '.', '.', 'X'],
	['.', '.', '.', 'X']
]
s = Solution()
result = s.countBattleships(board)
print result