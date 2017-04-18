def sequenceSumRangeV1(A, B, C):
    cnt = 0
    if not B or not C:
        cnt += 1
    for ix in xrange(len(A)-1):
        ls = 0
        for jx in xrange(ix, len(A)):
            ls += A[jx]
            if B <= ls <= C:
                cnt += 1
            elif ls > C:
                break
    print cnt

def subSequenceSumRangeV2(A, B, C):
    cnt = 0
    cb, cc = 0, 0
    j, k = 0, 0
    for x in xrange(len(A)):
        while j < len(A) and cb + A[j] < B:
            cb += A[j]
            j += 1
        while k < len(A) and cc + A[k] <= C:
            cc += A[k]
            k += 1
        #print x, j, k, cb, cc, " before"
        for i in xrange(j, k):
            if x <= i:
                #print A[x:i+1], x, i
                cnt += 1
        cb -= A[x]
        if cb < 0:
            cb = 0
            j += 1
        cc -= A[x]
        #print x, j, k, cb, cc, " after"
    print cnt

A = [2, 5, 1, 1, 2, 2, 3, 4, 8, 2]
#A = [3,4]
#A = [0, 0, 0, 5]
A = [3]
B = 0
C = 0

#sequenceSumRangeV1(A, B, C)
subSequenceSumRangeV2(A, B, C)