class Solution:
	def reverseBits(self, n):
		seq = "{0:b}".format(n)
		if (len(seq) < 32):
			zeros = ""
			for i in range(32-len(seq)):
				zeros += "0"
			seq = zeros + seq
		revSeq = seq[::-1]
		return int(revSeq, 2)

s = Solution()
print s.reverseBits(43261596)

