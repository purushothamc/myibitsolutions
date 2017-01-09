class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def transpose(self, A, n, m):
        for i in xrange(n):
            for j in xrange(i, m):
                A[i][j], A[j][i] = A[j][i], A[i][j]

    def rotate(self, A):
        rows, cols = len(A), len(A[0])
        self.transpose(A, rows, cols)
        for i in xrange(rows):
            col = cols/2
            for j in xrange(col):
                A[i][j], A[i][cols-j-1] = A[i][cols-j-1], A[i][j]
        return A

P = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
print P.rotate(A)