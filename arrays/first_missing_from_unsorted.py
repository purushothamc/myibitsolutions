def firstMissingPositive(A):
    maximum, minimum = -1, -1
    if not A: return 1
    ln = len(A)
    if ln == 1:
        if A[0] <= 0:
            return 1
        else:
            return A[0] + 1
    B = [0 for i in xrange(ln + 1)]
    for elem in A:
        if elem <= 0:
            continue
        else:
            B[elem] += 1
    for i in xrange(1, ln + 1):
        if B[i] == 0:
            return i
    return i+1

A = [-1,-2,-3]
print firstMissingPositive(A)