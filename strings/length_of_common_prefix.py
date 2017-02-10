def common_prefix_length(A):
    """
    :param A: list of strings
    :return: length of common prefix of all strings
    """
    resultPrefix = ""
    ln = len(A)
    if not A:
        return resultPrefix
    resultPrefix = A[0]
    for k in xrange(1, ln):
        i, j = 0, 0
        tempPrefix = ""
        while k < ln and i < len(resultPrefix) and j < len(A[k]) and resultPrefix[i] == A[k][j]:
            tempPrefix += resultPrefix[i]
            i += 1
            j += 1
        resultPrefix = tempPrefix
        if not resultPrefix:
            break
    return resultPrefix

def common_prefix_length_v2(A):
    resultPrefix = ""
    if not A:
        return resultPrefix
    for k in xrange(len(A[0])):
        foundChar = True
        for j in xrange(1, len(A)):
            if A[j][k] != A[0][k] or k >= len(A[j]):
                foundChar = False
                break
        if not foundChar:
            break
        resultPrefix += A[0][k]
    return resultPrefix

A = ["abcd", "abcef", "abcfg"]
A = ["abcdefgh","aefghijk","abcefgh"]

print common_prefix_length(A)
print common_prefix_length_v2(A)