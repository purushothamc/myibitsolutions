def maxUnsort(A):
    ln = len(A)
    lIdx = 0
    while lIdx < ln - 1:
        if A[lIdx] > A[lIdx+1]:
            break
        lIdx += 1
    if lIdx+1 == ln:
        return [-1]
    for rIdx in xrange(ln - 1, 0, -1):
        if A[rIdx - 1] > A[rIdx]:
            break
    uMax, uMin = A[lIdx], A[lIdx]
    for idx in xrange(lIdx + 1, rIdx + 1):
        if A[idx] < uMin:
            uMin = A[idx]
        if A[idx] > uMax:
            uMax = A[idx]
    for idx in xrange(0, lIdx):
        if A[idx] > uMin:
            lIdx = idx
            break
    for idx in xrange(ln-1, rIdx, -1):
        if A[idx] < uMax:
            rIdx = idx
            break
    return [lIdx, rIdx]

A = [5,6,7,8]
print maxUnsort(A)