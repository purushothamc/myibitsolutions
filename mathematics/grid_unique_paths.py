class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        result = 0
        if A is 1 or B is 1: return 1
        matrix = [[0 for i in xrange(B)] for j in xrange(A)]
        for i in xrange(A): matrix[i][0] = 1
        for i in xrange(B): matrix[0][i] = 1
        for i in xrange(1, A):
            for j in xrange(1, B):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[A-1][B-1]

P = Solution()
print P.uniquePaths(3,4)