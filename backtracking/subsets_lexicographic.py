def subsets(A, r, t, s, e):
    if(s >= e): return r
    r.append(t)
    print s, e
    for i in xrange(s, e):
        t.append(A[i])
        r = subsets(A, r, t, s+1, e)
        i += 1
    return r

def printSubsets(A):
    s, e = 0, len(A)
    result = []
    temp = []
    result.append(temp)
    temp.append(A[0])
    result = subsets(A, result, temp, s+1, e)
    return result

A = [3,4,5]
print printSubsets(A)