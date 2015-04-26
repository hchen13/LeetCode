class Solution:
	def majorityElement(self, nums):
		nums.sort()
		current = nums[0]
		cnt = 0
		for i, val in enumerate(nums):
			if val == current:
				cnt += 1
			else:
				cnt = 1
				current = val
			if cnt >= len(nums) / 2:
				break
		return current


s = Solution()
print s.majorityElement([])