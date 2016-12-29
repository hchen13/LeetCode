def countAS(length):
	return (length ** 2 - 3 * length + 2) / 2

class Solution(object):
	def numberOfArithmeticSlices(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		count = 0
		current_length = 1
		current_diff = None
		for i, num in enumerate(A):
			if i == 0:
				continue
			diff = num - A[i-1]
			if current_diff is None:
				current_diff = diff
			if current_diff == diff:
				current_length += 1
			else:
				if current_length > 2:
					count += countAS(current_length)

				current_length = 2
				current_diff = num - A[i-1]

		if current_length > 2:
			count += countAS(current_length)
		return count


arr = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
s = Solution()
result = s.numberOfArithmeticSlices(arr)
print result