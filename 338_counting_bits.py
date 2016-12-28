from math import log

def adjacent(x):
	exp = int(log(x, 2))
	return 2 ** exp

class Solution(object):
	def countBits(self, num):
		count = [0] * (num+1)
		count[0] = 0
		for i in range(1, num + 1):
			count[i] = count[i - adjacent(i)] + 1
		return count

s = Solution()
result = s.countBits(4)
print result
