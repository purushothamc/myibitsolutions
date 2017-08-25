def minPathSum(A):
    if not A:
        return 0
    m, n = len(A), len(A[0])
    matrix = [[0 for i in xrange(n)] for j in xrange(m)]
    matrix[0][0] = A[0][0]

    for i in xrange(1, m):
        matrix[i][0] = matrix[i-1][0] + A[i][0]
    for i in xrange(1, n):
        matrix[0][i] = matrix[0][i-1] + A[0][i]

    for i in xrange(1, m):
        for j in xrange(1, n):
            matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j]) + A[i][j]

    return matrix[m-1][n-1]

A = [[1, 3, 2], [4, 3, 1], [5, 6, 1]]
print minPathSum(A)