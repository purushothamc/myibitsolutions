class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        result = []
        for i in xrange(1, A+1):
            intermediate = []
            if i is 1:
                intermediate.append(1)
            else:
                intermediate.append(1)
                for j in xrange(0, len(result[i-2])-1):
                    intermediate.append(result[i-2][j] + result[i-2][j+1])
                intermediate.append(1)
            result.append(intermediate)
        return result

P = Solution()
print P.generate(4)