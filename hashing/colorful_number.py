def colorful(A):
    mapper = {}
    strA = str(A)
    for start in xrange(len(strA)):
        mul = int(strA[start])
        if mapper.get(int(strA[start]), 0):
            return 0
        mapper[int(strA[start])] = True
        for end in xrange(start + 1, len(strA)):
            mul *= int(strA[end])
            if mapper.get(mul, 0):
                return 0
            mapper[mul] = True
    return 1

A = 23
print colorful(A)