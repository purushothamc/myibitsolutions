class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        i = 0
        while i+1 < n:
            A[i], A[i+1] = A[i+1], A[i]
            i += 2
        return A

P = Solution()
print P.wave([1,2,3,4,5,6,7,8])