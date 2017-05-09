def firstMissingPositive(self, A):
    maximum, minimum = -1, -1
    if not A: return 1
    ln = len(A)
    if ln == 1:
        if A[0] <= 0:
            return 1
        else:
            return A[0] + 1
    maxint = max(A)
    B = [0 for i in xrange(maxint + 1)]
    for elem in A:
        if elem <= 0:
            continue
        else:
            B[elem] += 1
    for i in xrange(1, maxint + 1):
        if B[i] == 0:
            return i
    return i + 1