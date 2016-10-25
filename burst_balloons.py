class Solution(object):
	def maxCoins(self, nums):
		return self.max_burst(nums, 0, len(nums)-1)

	def max_burst(self, nums, left, right):
		max_val = 0
		rem = -1
		if left == right:
			return 1, nums[left]
		if left > right:
			return 0, 1
		for i in range(left, right + 1):
			l_maxval, l_rem = self.max_burst(nums, left, i - 1)
			r_maxval, r_rem = self.max_burst(nums, i + 1, right)
			current_value = l_maxval + r_maxval + l_rem * nums[i] * r_rem + l_rem * r_rem
			if current_value > max_val:
				max_val = current_value
				rem = max(l_rem, r_rem)
		return max_val, rem

a = [3, 1, 5, 8]
s = Solution()
print s.maxCoins(a)