from datetime import datetime


# class Person:
# 	def __init__(self, x):
# 		self.org = x
# 		self.h = x[0]
# 		self.k = x[1]
#
# 	def __cmp__(self, other):
# 		if self.h < other.h:
# 			return -1
# 		elif self.h > other.h:
# 			return 1
# 		else:
# 			return self.k - other.k


class Solution(object):

	'''My original solution'''
	# def reconstructQueue(self, people):
	# 	"""
     #    :type people: List[List[int]]
     #    :rtype: List[List[int]]
     #    """
	# 	n = len(people)
	# 	result = []
	# 	used = [False] * n
	# 	people = [Person(i) for i in people]
	# 	people.sort()
	# 	for _ in range(n):
	# 		for i, p in enumerate(people):
	# 			if used[i]:
	# 				continue
	# 			if p.k == 0:
	# 				result.append(p.org)
	# 				used[i] = True
	# 				for j, q in enumerate(people):
	# 					if used[j]:
	# 						continue
	# 					if q.k > 0 and q.h <= p.h:
	# 						q.k -= 1
	# 				break
	# 	return result
	'''a super fast neat solution from discussion'''
	def reconstructQueue(self, people):
		people.sort(key=lambda (h, k): (-h, k))
		result = []
		for i in people:
			result.insert(i[1], i)
		return result


p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
before = datetime.now()
result = s.reconstructQueue(p)
print "time used:", datetime.now() - before
print result