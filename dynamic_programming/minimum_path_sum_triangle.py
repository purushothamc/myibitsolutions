def minPathSumTriangle(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0][0]

    for index in xrange(len(A)-2, -1, -1):
        for elem in A[index]:
            A[index] += min(A[index+1][index], A[index+1][index+1])
    return A[index]