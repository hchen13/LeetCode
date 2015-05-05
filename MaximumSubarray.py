class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def maxSubArray(self, nums):
	    n = len(nums)
	    f = [0 for i in range(n)]
	    f[0] = nums[0]
	    for i in range(1, n):
	    	if f[i-1] < 0:
	    		f[i] = nums[i]
	    	else:
	    		f[i] = f[i-1] + nums[i]
	    return max(f)

s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-2, -3, -1]
print s.maxSubArray(arr)