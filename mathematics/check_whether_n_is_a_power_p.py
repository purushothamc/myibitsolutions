class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        import math
        n = int(math.sqrt(A))+1
        if A <= 3 and A is not 1:
            return False
        if A is 1: return True
        for i in xrange(2, n):
            B = A
            while B%i == 0:
                B = B/i
            if B is 1:
                return True
        return False

P = Solution()
print P.isPower(4)