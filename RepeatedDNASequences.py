class Solution:

	"""
	getHash and the first solution exceeded the time limit, can't figure out why yet
	"""
	def getHash(self, s):
		seq = ""
		for i in s:
			if i == 'A' or i == 'a':
				seq += "1"
			if i == 'C' or i == 'c':
				seq += "2"
			if i == 'G' or i == "g":
				seq += "3"
			if i == 'T' or i == 't':
				seq += "4"
		num = 0
		for i, val in enumerate(seq):
			num += (int(val) - 1) * (4 ** (10 - i - 1))
		return num

	# def findRepeatedDnaSequences(self, s):
	# 	vis = [False for i in range(1048586)]
	# 	repSeqs = []
	# 	size = len(s)
	# 	for i in range(size - 9):
	# 		seq = s[i: i + 10]
	# 		h = self.getHash(seq)
	# 		if vis[h]:
	# 			repSeqs.append(seq)
	# 		else:
	# 			vis[h] = True
	# 	return repSeqs

	def findRepeatedDnaSequences(self, s):
		if s is None:
			return []
		if len(s) < 10:
			return []
		table = {}
		repSeqs = []
		for i in range(len(s) - 9):
			seq = s[i: i + 10]
			if table.get(seq) == None:
				table[seq] = 1
			elif table[seq] == 1:
				repSeqs.append(seq)
				table[seq] += 1

		return repSeqs


s = Solution()
print s.findRepeatedDnaSequences("GAGAGAGAGAGAG")
# print s.getHash("TTTTTTTTTT")