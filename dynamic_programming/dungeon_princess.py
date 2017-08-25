def findPrincess(dungeon):
    if not dungeon:
        return 0
    m, n = len(dungeon), len(dungeon[0])

    matrix = [[dungeon[i][j] for j in range(n)] for i in range(m)]

    for i in xrange(m - 2, -1, -1):
        matrix[m - 1][i] += matrix[m - 1][i + 1]
    for i in xrange(n - 2, -1, -1):
        matrix[i][n - 1] += matrix[i + 1][n - 1]

    print matrix

    for i in xrange(m - 2, -1, -1):
        for j in xrange(n - 2, -1, -1):
            matrix[i][j] += max(matrix[i + 1][j], matrix[i][j + 1])

    print matrix

    if matrix[0][0] >= 0:
        return abs(matrix[0][0]) + 1
    else:
        return abs(matrix[0][0])

A = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print findPrincess(A)