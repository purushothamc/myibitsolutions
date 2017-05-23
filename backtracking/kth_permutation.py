# This is 1 accepted solution..... using recursion.
# it exceeds time limit since we're calculating permutations upto k.
# if k is n!, it is equal to worst case complexity.
def permutationHelper(start, temp, result, original, kthp, B):
    if len(temp) == len(original):
        kthp[0] += 1
        if kthp[0] == B:
            x = [y for y in temp]
            result.append(x)
            return True
        if kthp[0] > B:
            return False
    for index in xrange(len(original)):
        if original[index] not in temp:
            temp.append(original[index])
            if permutationHelper(index+1, temp, result, original, kthp, B):
                return True
            temp.pop()

def permutations(n, k):
    if n == 0:
        return ""
    A = [x+1 for x in xrange(n)]
    result, temp, kthp = [], [], 0
    permutationHelper(0, temp, result, A, [kthp], k)
    if not result:
        return ""
    return "".join([str(x) for x in result[0]])


def generateFactoradic(k, factoradic, n):
    f = 1
    while k:
        factoradic.append(k % f)
        k = k / f
        f = f + 1
    lenf = len(factoradic)
    for k in xrange(n - lenf):
        factoradic.append(0)
    factoradic = factoradic.reverse()

# this solution uses factoradic system as base for generating kth permutation.
def factoradicPermutation(n, k):
    if n == 0:
        return ""
    A = [x+1 for x in xrange(n)]
    factoradic, result = [], []
    generateFactoradic(k, factoradic, n)
    for x in factoradic:
        result.append(A[x])
        del A[x]
    return "".join([str(x) for x in result])

#print permutations(10, 58)
print factoradicPermutation(3, 0)