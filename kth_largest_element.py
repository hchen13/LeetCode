from random import randint


class Solution(object):
	def findKthLargest(self, nums, k):
		pos = randint(0, len(nums) - 1)
		# pos = 0
		pivot_pos = partition(nums, pos)
		if pivot_pos + 1 == k:
			return nums[pivot_pos]
		if pivot_pos + 1 > k:
			return self.findKthLargest(nums[0:pivot_pos], k)
		else:
			return self.findKthLargest(nums[pivot_pos + 1:], k - pivot_pos - 1)

def swap(array, i, j):
	t = array[i]
	array[i] = array[j]
	array[j] = t

def partition(array, pivot_pos):
	swap(array, 0, pivot_pos)
	pivot = array[0]
	j = 0
	for i in range(1, len(array)):
		current = array[i]
		if current > pivot:
			j += 1
			swap(array, j, i)
	swap(array, 0, j)
	return j

# s = Solution()
# array = [3, 2, 1, 5, 6, 4, 7]
# print s.findKthLargest(array, 1)