class Solution:
    def __init__(self):
        pass
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        result = []
        if not A: return [1]
        for i in xrange(A+1):
            intermediate = []
            if i is not 0:
                intermediate.append(1)
                for j in xrange(len(result)-1):
                    intermediate.append(result[j] + result[j+1])
                intermediate.append(1)
            result = intermediate
        return result

P = Solution()
print P.getRow(3)