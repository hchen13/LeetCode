class Solution(object):
	def getSum(self, a, b):
		get_bin = lambda x: format(x, 'b')
		seq_a = get_bin(a)
		seq_b = get_bin(b)
		length = max(len(seq_a), len(seq_b))
		seq_a = seq_a.zfill(length)
		seq_b = seq_b.zfill(length)
		result = ""

		carry_in = 0
		for i in range(length-1, -1, -1):
			A, B = int(seq_a[i]), int(seq_b[i])
			sum = self.s(A, B, carry_in)
			carry_out = self.carry(A, B, carry_in)
			result = str(sum) + result
			carry_in = carry_out
		sum = self.s(0, 0, carry_in)
		result = str(sum) + result

		return int(result, 2)


	def s(self, a, b, c):
		return int((not a) and ((not b and c) or (b and not c)) or (a and ((not b and not c) or b and c)))

	def carry(self, a, b, c):
		result = (a and (b or (not b and c))) or (not a and b and c)
		return int(result)

sol = Solution()
print sol.getSum(1, -3)