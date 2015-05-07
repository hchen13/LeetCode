class Solution:
	# @param {string} s
	# @return {integer}
	def longestValidParentheses(self, s):
		n = len(s)
		stack = []
		ret = 0
		dp = [i for i in range(n)]
		for i, val in enumerate(s):
			if val == '(':
				stack.append(i)
			elif stack:
				matchingPos = stack.pop()
				dp[i] = matchingPos
				if matchingPos > 0 and dp[matchingPos - 1] != matchingPos - 1:
					dp[i] = dp[matchingPos - 1]
			if dp[i] != i:
				ret = max(ret, i - dp[i] + 1)
		return ret



s = Solution()
print s.longestValidParentheses("()((())()")