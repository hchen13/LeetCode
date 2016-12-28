class Solution(object):
	def hammingDistance(self, x, y):
		bits = '{0:b}'.format(x ^ y)
		return bits.count('1')


if __name__ == '__main__':
	a = 2; b = 4
	s = Solution()
	c = s.hammingDistance(a, b)
	print c, type(c)