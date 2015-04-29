class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        n = len(nums)
        minVal = nums[0]
        maxVal = nums[0]
        ret = nums[0]
        for i in range(1, n):
            bufMinVal = minVal
            bufMaxVal = maxVal
            minVal = min(nums[i], bufMinVal * nums[i], bufMaxVal * nums[i])
            maxVal = max(nums[i], bufMinVal * nums[i], bufMaxVal * nums[i])
            if maxVal > ret:
                ret = maxVal
        return ret

s = Solution()
print s.maxProduct([2, 3, -2, 4])
