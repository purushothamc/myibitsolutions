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

def swapPermutation(left, right, result, A, mapper):
    if left == right:
        temp = [y for y in A]
        if not mapper.has_key(tuple(temp)):
            result.append(temp)
        mapper[tuple(temp)] = True

        return

    for index in xrange(left, right+1):
        A[left], A[index] = A[index], A[left]
        swapPermutation(left+1, right, result, A, mapper)
        A[left], A[index] = A[index], A[left]

def permutations(A):
    if not A:
        return []
    result, temp, _mapper = [], [], {}
    swapPermutation(0, len(A)-1, result, A, _mapper)
    return result

A = [ 0, 0, 1, 9 ]
A = [1,2,3]
print permutations(A)