def maxPoints(A, B):
    if not A or not B: return 0
    maxLen = 1
    for fp in xrange(len(A)-1):
        dup = 1
        already_seen = {}
        for sp in xrange(fp+1, len(A)):
            if A[fp] == A[sp] and B[fp] == B[sp] and fp != sp:
                dup += 1
            elif fp != sp:
                if A[fp] == A[sp]:
                    already_seen['v'] = already_seen.get('v', 0) + 1
                elif B[fp] == B[sp]:
                    already_seen['h'] = already_seen.get('h', 0) + 1
                else:
                    slope = (1.0*(B[sp] - B[fp])) / (A[sp] - A[fp])
                    already_seen[slope] = already_seen.get(slope, 0) + 1
        if len(already_seen) > 0:
            maxLen = max(maxLen, max(already_seen.values()) + dup)
        else:
            maxLen = max(maxLen, dup)
    return maxLen


A = [6, 5, 18, 2, 5, 2]
B = [17, 16, 17, 4, 13, 20]
"""A = [14, 17, 2, 13, 18, 9, 15, 2, 3, 7, 10, 14, 2, 18, 7, 12, 1, 9, 16, 4, 11, 4, 16, 17, 5, 8, 16,
     8, 5, 4, 16, 14, 12, 13, 2, 14, 9, 20, 5, 19, 16, 19, 3, 3, 1, 18, 19, 11, 16, 10, 12, 5, 1, 5,
     17, 20, 18, 15, 3, 5, 17, 14, 0, 0, 3, 10, 13, 10, 15, 2, 19, 14, 17, 4, 6, 1, 12]
B = [2, 3, 3, 5, 6, 10, 5, 11, 18, 1, 13, 6, 13, 14, 1, 19, 13, 2, 6, 3, 2, 2, 11, 5, 13, 18, 15,
     12, 5, 14, 2, 8, 4, 20, 1, 1, 16, 20, 9, 2, 0, 1, 4, 1, 20, 2, 9, 2, 10, 12, 4, 12, 3, 2, 3, 4,
     1, 10, 19, 17, 14, 7, 17, 5, 9, 13, 6, 18, 1, 2, 4, 6, 6, 3, 7, 18, 18]"""
#A = [20]
#B = [13]
print maxPoints(A, B)