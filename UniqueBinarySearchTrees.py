class Solution:
    # @param {integer} n
    # @return {integer}
    def root(self, i, start, end):
        if i == end:
            return self.calc(start, i-1) * self.calc(i, end)
        return self.calc(start, i-1) * self.calc(i+1, end)
    
    def calc(self, start, end):
        if self.tree[start][end] != -1:
            return self.tree[start][end]
        sum = 0
        for i in range(start, end + 1):
            sum += self.root(i, start, end)
        self.tree[start][end] = sum
        return sum
    
    def numTrees(self, n):
        self.n = n
        self.tree = [[-1 for i in range(n+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(0, i+1):
                self.tree[i][j] = 1
        return self.calc(1, n)

s = Solution()
print s.numTrees(3)