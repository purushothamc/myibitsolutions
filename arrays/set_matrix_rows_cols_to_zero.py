class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        rows = len(A)
        cols = len(A[0])
        firstRow = False
        firstCol = False
        for i in xrange(rows):
            if A[i][0] is 0:
                firstCol = True
                break
        for i in xrange(cols):
            if A[0][i] is 0:
                firstRow = True
                break
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                if A[i][j] is 0:
                    A[i][0] = 0
                    A[0][j] = 0
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                if A[i][0] is 0 or A[0][j] is 0:
                    A[i][j] = 0
        if firstRow:
            for i in xrange(cols):
                A[0][i] = 0
        if firstCol:
            for i in xrange(rows):
                A[i][0] = 0
        return A

P = Solution()
A = [[1,0,1],[1,1,1],[1,1,1]]
print P.setZeroes(A)