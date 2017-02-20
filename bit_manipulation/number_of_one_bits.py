def numOneBits(A):
    if not A:
        return 0
    cnt = 0
    while A:
        cnt += 1
        A &= A-1
    return cnt

A = 11
print numOneBits(A)