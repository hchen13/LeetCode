class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		rep = [""] * (n)
		for i in range(1, n + 1):
			if not i % 3:
				rep[i-1] = "Fizz"
			if not i % 5:
				rep[i-1] += "Buzz"
			if not len(rep[i-1]):
				rep[i-1] = str(i)
		return rep

s = Solution()
r = s.fizzBuzz(15)
print r
