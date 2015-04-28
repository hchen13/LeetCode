class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        f = [0 for i in range(n+1)]
        f[0] = 1
        for i in range(1, n+1):
            f[i] = f[i-1]
            if i - 2 >= 0:
                f[i] += f[i-2]
        return f[n]

s = Solution()
print s.climbStairs(3)