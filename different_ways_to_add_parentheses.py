class Solution(object):
	def diffWaysToCompute(self, input):
		try:
			number = int(input)
			return [number]
		except:
			pass
		return_list = []
		for i, char in enumerate(input):
			if char in ['+', '-', '*']:
				left_list = self.diffWaysToCompute(input[0:i])
				right_list = self.diffWaysToCompute(input[i+1:])
				list = []
				for a in left_list:
					for b in right_list:
						if char == '+':
							list.append(a + b)
						elif char == '-':
							list.append(a - b)
						elif char == '*':
							list.append(a * b)
				return_list += list
		return return_list



