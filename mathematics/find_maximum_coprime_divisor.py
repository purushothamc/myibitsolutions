def gcd(A, B):
    if A < B:
        A, B = B, A
    while B:
        C = A % B
        A = B
        B = C
    return A

def cpFact(A, B):
    while gcd(A, B) != 1:
        A = A / gcd(A, B)
    return A

    # Solution 1 .....
    """
    maxDiv = 0
    for k in xrange(sq, 0, -1):
        if A % k == 0:
            i = k
            j = A/k
            print i, j, B
            if gcd(B, i) == 1:
                if i > maxDiv:
                    maxDiv = i
            if gcd(B, j) == 1:
                if j > maxDiv:
                    maxDiv = j
    return maxDiv
    """

print cpFact(10, 1)

