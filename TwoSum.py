class Solution:
    def binSearch(self, array, p, r, target):
        if p >= r:
            if p == r and array[p] == target:
                return True
            return False
        m = (p + r) / 2;
        if array[m] == target:
            return True
        if target < array[m]:
            return self.binSearch(array, p, m - 1, target)
        else:
            return self.binSearch(array, m + 1, r, target)
        
    def twoSum(self, num, target):
        sortedNum = list(num)
        sortedNum.sort()
        size = len(sortedNum)
        start = 0
        for i in range(size):
            first = sortedNum[i]
            second = target - first
            if self.binSearch(sortedNum, i+1, size-1, second) == True:
                break
        print first, second
        
        for i, val in enumerate(num):
            if val == first:
                pos1 = i
                break
        for i, val in enumerate(num):
            if i == pos1:
                continue
            if val == second:
                pos2 = i
                break
        if (pos1 < pos2):
            return (pos1+1, pos2+1)
        else:
            return (pos2+1, pos1+1)
        
        


s = Solution()
num = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
tmp = list(num)
tmp.sort()

# print s.binSearch(tmp, 0, 3, 0)
print s.twoSum(num, 542)


