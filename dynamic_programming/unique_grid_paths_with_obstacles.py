def uniquePathsWithObstacles(A):
    n, m = len(A), len(A[0])
    if not A:
        return 0
    if A[0][0] == 1:
        return 0
    if n == 1 and m == 1 and A[0][0] == 0:
        return 1
    matrix = [[0 for i in xrange(m)] for j in xrange(n)]

    # Initialize matrix.
    for i in xrange(n):
        if not A[i][0]:
            matrix[i][0] = 1
        else:
            break
    for j in xrange(i + 1, n):
        matrix[i][0] = 0

    for i in xrange(m):
        if not A[0][i]:
            matrix[0][i] = 1
        else:
            break
    for j in xrange(i + 1, m):
        matrix[0][i] = 0

    # Solve for solution.
    for i in xrange(1, n):
        for j in xrange(1, m):
            if not A[i][j]:
                if matrix[i - 1][j] and not A[i - 1][j]:
                    matrix[i][j] += matrix[i - 1][j]
                if matrix[i][j - 1] and not A[i][j - 1]:
                    matrix[i][j] += matrix[i][j - 1]
    return matrix[n - 1][m - 1]

A = [[0, 0]]
print uniquePathsWithObstacles(A)