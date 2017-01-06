class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        import math
        if A <= 1: return 0
        if A is 2: return 1
        n = int(math.sqrt(A))+1
        isPrime = True
        for k in xrange(2, n):
            if A%k == 0:
                isPrime = False
                break
        if isPrime: return 1
        else: return 0

P = Solution()
print P.isPrime(4)