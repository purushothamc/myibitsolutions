def twoSum(A, B):
    mapper = dict()
    if len(A) == 1:
        return []
    for index, each in enumerate(A):
        if not mapper.get(each, 0):
            mapper[each] = [index + 1]
        else:
            mapper[each].append(index+1)
    result = []
    for index, each in enumerate(A):
        if mapper.get(B - each, 0):
            for each in mapper.get(B - each, 0):
                if(index+1 < each):
                    while result and result[-1][1] > each:
                        result.pop()
                    result.append([index+1, each])
    if not result:
        return result
    return result[0]

A = [2, 7, 11, 15]
#print twoSum(A, 9)
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
print twoSum(A, -3)
#A = [1, 1, 1]
#print twoSum(A, 2)
A = [ 0, 8, -3, -1, 7, 9, -1, 8, -2, 2, -8, -6, -7, -4, -6, -1, -6, 6, 8, -10, -6, 4,
      -8, 7, 6, -4, -4, -10, -6, 5, -8, -1, 10, 6, 6, -3, -3, -7, -8, -7, 4, -7, 1, -10, 5 ]
#A = [1,1,1,3]
print twoSum(A, 2)