def nextPermutation(self, A):
    isSorted = True
    foundPerm = False
    ln = len(A)
    minIdx = A[ln - 1], ln - 1
    for idx in xrange(ln - 1, 0, -1):
        if A[idx] > A[idx - 1]:
            isSorted = False
            foundPerm = True
            break
    if isSorted:
        return sorted(A)
    for k in xrange(ln - 1, 0, -1):
        if A[k] > A[idx - 1]:
            A[k], A[idx - 1] = A[idx - 1], A[k]
            break
    return A[:idx] + sorted(A[idx:])