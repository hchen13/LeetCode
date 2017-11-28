from math import sqrt


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n == 0 or n == 1:
            return 0
        isPrime = [True for i in range(n)]
        isPrime[1] = False
        a = int(sqrt(n))
        for i in range(2, a + 1):
            if isPrime[i] is not False:
                for j in range(i + i, n, i):
                    isPrime[j] = False

        primes = 0
        for i, val in enumerate(isPrime):
            if i == 0:
                continue
            if val is not False:
                primes += 1
        return primes


s = Solution()
print s.countPrimes(1)
