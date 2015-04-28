class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        f = [[0 for i in range(2)] for j in range(n)]
        
        f[0][0] = 0
        f[0][1] = nums[0]
        
        for i in range(1, n):
            for j in range(2):
                maxVal = 0
                if j == 0:
                    for k in range(i):
                        if f[k][0] > maxVal:
                            maxVal = f[k][0]
                        if f[k][1] > maxVal:
                            maxVal = f[k][1]
                if j == 1:
                    for k in range(i-1):
                        if f[k][1] + nums[i] > maxVal:
                            maxVal = f[k][1] + nums[i]
                    for k in range(i):
                        if f[k][0] + nums[i] > maxVal:
                            maxVal = f[k][0] + nums[i]
                f[i][j] = maxVal
                
        return max(f[n-1])
                
s = Solution()
nums = [1, 2, 3, 6]
print s.rob(nums)