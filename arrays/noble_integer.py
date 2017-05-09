def solve(A):
    A = sorted(A)
    c = 0
    for idx in xrange(len(A)):
        if idx < len(A) - 1 and A[idx] == A[idx + 1]:
            continue
        else:
            greater = len(A) - idx - 1
            if A[idx] == greater:
                return 1
    return -1