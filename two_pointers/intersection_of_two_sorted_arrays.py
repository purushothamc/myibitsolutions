def intersection(A, B):
    result = []
    if not A:
        return B
    elif not B:
        return A
    lenA, lenB = len(A), len(B)
    idxA, idxB = 0, 0
    while idxA < lenA and idxB < lenB:
        if A[idxA] < B[idxB]:
            idxA += 1
        elif A[idxA] > B[idxB]:
            idxB += 1
        else:
            result.append(A[idxA])
            idxA += 1
            idxB += 1
    return result

A = [1,2,3,3,4,5,6]
B = [3,3,5]
print intersection(A, B)