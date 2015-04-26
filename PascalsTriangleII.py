class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
    	buf = [1]
    	if rowIndex == 0:
    		return buf
    	for i in range(1, rowIndex + 1):
    		current = [1]
    		for j in range(1, len(buf)):
    			current.append(buf[j-1] + buf[j])
    		current.append(1)
    		buf = current
    	return buf

s = Solution()
print s.getRow(3)
