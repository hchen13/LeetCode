class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        size = len(s)
        f = [False for i in range(size + 1)]
        f[0] = True
        stack = []
        for i in range(size+1):
            for j in range(i):
                if f[j] is True and s[j: i] in wordDict:
                    f[i] = True
                    stack.append(s[j: i])
        return f[size]

s = Solution()
print s.wordBreak("leetcodeleet", ["lee", "t", "code"])
        