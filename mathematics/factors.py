class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        import math
        n = int(math.sqrt(A)) + 1
        result = []
        for i in xrange(1, n):
            if A % i is 0:
                if A / i != i:
                    result.append(i)
                    result.append(A / i)
                else:
                    result.append(i)
        result.sort()
        return result

P = Solution()
print P.allFactors(0)