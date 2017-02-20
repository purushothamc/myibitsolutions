def merge(A, B):
    lenB = len(B)
    lenA = len(A) + lenB
    for x in xrange(lenB):
        A.append(0)
    idxA, idxB = lenA - 1, lenA - lenB - 1
    while idxB >= 0:
        A[idxA] = A[idxB]
        idxA -= 1
        idxB -= 1
    print A
    idxA, idxB, k = lenB, 0, 0
    while idxB < lenB and idxA < lenA:
        print A[idxA], B[idxB]
        if A[idxA] < B[idxB]:
            A[k] = A[idxA]
            k += 1
            idxA += 1
        elif A[idxA] > B[idxB]:
            A[k] = B[idxB]
            k += 1
            idxB += 1
        else:
            A[k] = A[idxA]
            k += 1
            A[k] = A[idxA]
            k += 1
            idxA += 1
            idxB += 1
    print idxA, lenA, idxB, lenB
    while idxB < lenB and idxA -1 < lenA:
        A[idxA-1] = B[idxB]
        idxA += 1
        idxB += 1

A = [2,2,2]
B = [2]
merge(A, B)
print A