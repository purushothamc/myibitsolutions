def removeDuplicates(A):
    if not A:
        return A
    lenA = len(A)
    k, count = 0, 1
    A[k] = A[0]
    for idx in xrange(lenA):
        if idx+1 < lenA and A[k] == A[idx+1]:
            count += 1
            if count <= 2:
                k += 1
                if idx + 1 < lenA:
                    A[k] = A[idx+1]
            else:
                continue
        else:
            k += 1
            if idx + 1 < lenA:
                A[k] = A[idx+1]
            count = 1
    print A[:k]

A = [1,1,1,1,1,2,2,3,4,4,4,4,5]
removeDuplicates(A)