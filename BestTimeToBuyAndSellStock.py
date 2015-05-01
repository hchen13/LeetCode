'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

f(i, j) = max{f(i-1, j), f(i-1, j-1) - a[i], f(i-1, j+1) + a[i]} this is totally wrong!!!!
'''
class Solution:
    # @param {integer[]} prices
    # @return {integer}

    # def maxProfit(self, prices):
    # 	n = len(prices)
    # 	if n == 0:
    # 		return 0
    #     f = [[-2147483647 for i in range(n+1)] for j in range(n)]
    #     f[0][0] = 0
    #     f[0][1] = -prices[0]

    #     for i in range(1, n):
    #     	for j in range(i+2):
    #     		cmpList = [f[i-1][j]]
    #     		if f[i][j] != -1:
    #     			cmpList.append(f[i][j])
    #     		if j - 1 >= 0:
    #     			cmpList.append(f[i-1][j-1] - prices[i])
    #     		if j + 1 <= i:
    #     			cmpList.append(f[i-1][j+1] + prices[i])
    #     		f[i][j] = max(cmpList)

    #     ret = f[n-1][0]
    #     for val in f[n-1]:
    #     	if val > ret:
    #     		ret = val
    #     return ret
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        lowestPrice = prices[0]
        highestProfit = 0
        for i, val in enumerate(prices):
            if val < lowestPrice:
                lowestPrice = val
            if val - lowestPrice > highestProfit:
                highestProfit = val - lowestPrice
        return highestProfit

s = Solution()
a = [1, 2, 4, 3, 5]
print s.maxProfit(a)
