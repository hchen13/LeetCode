class Solution:
	def rotate(self, nums, k):
		size = len(nums)
		k %= size
		if k != 0:
			tmp = nums[-k: ] + nums[0: size - k]
			for i, val in enumerate(tmp):
				nums[i] = val

s = Solution()
nums = [1, 2]
s.rotate(nums, 0)
print nums