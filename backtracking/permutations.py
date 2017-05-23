def permutationHelper(start, temp, result, original):
    if len(temp) == len(original):
        x = [y for y in temp]
        result.append(x)
        return
    for index in xrange(len(original)):
        if original[index] not in temp:
            temp.append(original[index])
            permutationHelper(index+1, temp, result, original)
            temp.pop()

def permutations(A):
    if not A:
        return []
    result, temp = [], []
    permutationHelper(0, temp, result, A)
    print result

A = [1,2,3]
permutations(A)