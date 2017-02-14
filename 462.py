def dist(num, tar):
	return abs(num - tar)


def moves(arr, tar):
	res = 0
	for i in arr:
		res += dist(i, tar)
	return res


class Solution(object):
	def minMoves2(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		pass


arr = [1, 2, 3]
s = Solution()
result = s.minMoves2(arr)
