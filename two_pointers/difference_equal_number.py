def difference(A, B):
    if not A:
        return 0
    i, j, lenA = 0, 1, len(A)
    while i < lenA and j < lenA:
        if i != j and A[j] - A[i] == B:
            return True
        if A[j] - A[i] < B:
            j += 1
        else:
            i += 1
    return False

A = [1,3,4]
B = 4
print difference(A, B)