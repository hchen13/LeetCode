class Solution(object):
	def findComplement(self, num):
		import math
		length = int(math.log(num, 2)) + 1
		ceil = 2 ** length - 1
		return num ^ ceil


if __name__ == '__main__':
	x = 5
	s = Solution()
	ans = s.findComplement(x)