class Solution:
    # @param A : integer
    # @return an integer
    def sieve(self, A):
        import math
        n = int(math.sqrt(A)) + 1
        result = []
        intermediate = [True for i in xrange(0, A+1)]
        for k in xrange(2, n):
            if intermediate[k]:
                for j in xrange(k*k, A+1, k):
                    intermediate[j] = False
        for k in xrange(2, A+1):
            if intermediate[k]:
                result.append(k)
        return result

P = Solution()
print P.sieve(15)