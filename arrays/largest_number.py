def largestNumber(A):
    if not A: return ""

    def comparator(x, y):
        x, y = str(x), str(y)
        return int(x + y) - int(y + x)

    """import math
    rlist = [[] for i in xrange(10)]
    for elem in A:
        if elem:
            digits = int(math.log10(elem))
            rlist[elem/(10**digits)].append(elem)
    for elem in xrange(len(rlist)):
        rlist[elem] = sorted(rlist[elem], cmp=comparator, reverse=True)
    """
    A = sorted(A, cmp=comparator)
    result = []
    for elem in xrange(len(A) - 1, -1, -1):
        if A[elem]:
            result.append(A[elem])
    if not result: return "0"
    return "".join([str(x) for x in result])