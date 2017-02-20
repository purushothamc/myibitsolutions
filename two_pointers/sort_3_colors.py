def sortColors(A):
    lnA = len(A)
    idxA, idxB = 0, lnA-1
    while idxA < idxB:
        while idxB >= 0 and (A[idxB] != 0 and A[idxB] != 1):
            idxB -= 1
        while idxA < lnA and A[idxA] != 2:
            idxA += 1
        if idxA < idxB and idxA < lnA and idxB >= 0:
            A[idxA] = A[idxB]
            A[idxB] = 2
            idxA += 1
            idxB -= 1
    idxA, idxB = 0, idxB
    while idxA <= idxB:
        while idxA <= idxB and A[idxA] != 1:
            idxA += 1
        while idxB >= 0 and A[idxB] != 0:
            idxB -= 1
        if idxA < idxB:
            A[idxA] = 0
            A[idxB] = 1
            idxA += 1
            idxB -= 1
    print A

A = [2,2,2,2,1]
sortColors(A)