class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.f = [0] * len(nums)
        for i, x in enumerate(nums):
            self.f[i] = self.f[i-1] + x

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            prefix = self.f[i-1]
        else:
            prefix = 0
        return self.f[j] - prefix

if __name__ == '__main__':
    left, right = 0, 3
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    result = obj.sumRange(left, right)
    print(result)

