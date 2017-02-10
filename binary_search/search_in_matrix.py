def searchMatrix(A, B):
    rows = len(A)
    cols = len(A[0])
    if not A:
        return 0
    r, c = rows-1, 0
    while r >= 0 and c <= cols-1:
        print r, c
        if A[r][c] == B:
            return 1, r, c
        if B > A[r][c]:
            c += 1
        elif B < A[r][c]:
            r -= 1
    return 0

A = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
B = 12

print searchMatrix(A, B)