def removeElement(A, B):
    if not A:
        return 0
    lenA = len(A)
    k = 0
    for idx in xrange(lenA):
        if A[idx] == B:
            continue
        else:
            A[k] = A[idx]
            k += 1
    return A[:k], k

A = [1,2,3]
print removeElement(A, 1)