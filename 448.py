class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		n = len(nums)
		table = {}
		ret = []
		for i in nums:
			if i not in table:
				table[i] = 1
			else:
				table[i] += 1
		for i in range(1, n+1):
			if i not in table:
				ret.append(i)
		return ret

arr = [4,3,2,7,8,2,3,1]
s = Solution()
res = s.findDisappearedNumbers(arr)
print res