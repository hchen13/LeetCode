class Solution(object):
	def searchMatrix(self, matrix, target):
		m, n = len(matrix), len(matrix[0])
		found = False
		for i in matrix:
			lower_bound, upper_bound = i[0], i[n-1]
			if lower_bound <= target <= upper_bound:
				found |= self.binary_search(i, 0, n-1, target)
		return found

	def binary_search(self, list, left, right, target):
		mid = (left + right) / 2
		if list[mid] == target:
			return True
		if left >= right:
			return False
		if target < list[mid]:
			return self.binary_search(list, left, mid-1, target)
		else:
			return self.binary_search(list, mid+1, right, target)

m = [
	[1,   4,  7, 11, 15],
	[2,   5,  8, 12, 19],
	[3,   6,  9, 16, 22],
	[10, 13, 14, 17, 24],
	[18, 21, 23, 26, 30]
]

s = Solution()
print s.searchMatrix(m, 20)