def diffPossible(A, B):
    mapper = dict()
    if len(A) == 1:
        return []
    for index, each in enumerate(A):
        if not mapper.get(each, 0):
            mapper[each] = [index+1]
        else:
            mapper[each].append(index+1)
    for index, each in enumerate(A):
        if mapper.get(B + each, 0):
            lst = mapper.get(B + each, 0)
            for elem in lst:
                if index+1 != elem:
                    return 1
                else:
                    continue
    return 0


A = [1, 1, 1]
B = 1
print diffPossible(A, B)