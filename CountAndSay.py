class Solution:
	def read(self, seq):
		ret = ""
		current = seq[0]
		cnt = 1
		for i in range(1, len(seq)):
			if seq[i] == current:
				cnt += 1
			else:
				ret += str(cnt) + str(current)
				current = seq[i]
				cnt = 1
		ret += str(cnt) + str(current)
		return ret

	def countAndSay(self, n):
		if n == 1:
			return str(1)
		return self.read(self.countAndSay(n - 1))

s = Solution()
# print Solution().countAndSay(3)
print s.countAndSay(5)