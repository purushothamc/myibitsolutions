def removeDuplicates(A):
    if not A:
        return A
    lenA = len(A)
    k = 0
    A[k] = A[0]
    for idx in xrange(lenA):
        if idx+1 < lenA and A[k] == A[idx+1]:
            continue
        else:
            k += 1
            if idx + 1 < lenA:
                A[k] = A[idx+1]
    print k

A = [1,2,3]
removeDuplicates(A)