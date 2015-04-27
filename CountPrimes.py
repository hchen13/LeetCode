from math import sqrt


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n == 0:
            return 0
        isPrime = [True] * (n + 1)
        isPrime[1] = False
        a = int(sqrt(n))
        for i in range(2, a + 1):
            if isPrime[i] != False:
                for j in range(i + i, n + 1, i):
                    isPrime[j] = False
                    
        primes = 0
        for i, val in enumerate(isPrime):
            if i == 0:
                continue
            if val != False:
                primes += 1
        return primes


s = Solution()
print s.countPrimes(1000000)