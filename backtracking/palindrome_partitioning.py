def isPalin(S):
    if not S:
        return False
    start, end = 0, len(S) - 1
    while start < end:
        if S[start] != S[end]:
            return False
        start += 1
        end -= 1
    return True

def partitionHelper(start, string, temp, result):
    if start == len(string):
        x = [y for y in temp]
        result.append(x)
        return
    for index in xrange(start, len(string)):
        if isPalin(string[start : index + 1]):
            temp.append(string[start : index + 1])
            partitionHelper(index + 1, string, temp, result)
            temp.pop()

def partition(A):
    # base case, length 0 or string None.
    result = []
    if not A or len(A) is 0:
        return result
    temp = []

    # run backtracking
    partitionHelper(0, A, temp, result)
    return result

A = "aab"
print partition(A)