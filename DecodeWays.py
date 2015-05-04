class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s == '0':
        	return 0
        f = [0 for i in range(n + 1)]
        f[0] = 1
        f[1] = 1
        for i in range(1, n+1):
            if int(s[i-1]) != 0:
                f[i] = f[i-1]
            else:
                f[i] = 0

            if i > 1 and int(s[i-2:i]) in range(10, 27):
                f[i] += f[i-2]

        return f[n]


s = Solution()
print s.numDecodings("1012")