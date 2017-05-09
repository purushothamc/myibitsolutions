def equal(A):
    if not A or len(A) <= 3:
        return list()
    mapper = {}
    result = []
    for outer in xrange(len(A)-1):
        for inner in xrange(outer+1, len(A)):
            s = A[outer] + A[inner]
            if mapper.get(s, 0):
                res = mapper.get(s)
                if res[0] < res[1] and res[0] < outer and res[1] != outer and res[1] != inner and outer < inner:
                    while result:
                        if result[-1][0] > res[0]:
                            result.pop()
                        elif result[-1][1] > res[1]:
                            result.pop()
                        elif result[-1][2] > outer:
                            result.pop()
                        elif result[-1][2] > inner:
                            result.pop()
                        else:
                            break
                    result.append([res[0], res[1], outer, inner])
                else:
                    continue
            else:
                mapper[s] = [outer, inner]
    if not result:
        return result
    return result[0]

A = [3, 4, 7, 1, 2, 9, 8]
#A = [3, 5, 2, 6]
#A = [1, 3, 3, 3, 3, 2, 2]
#A = [0, 0, 1, 0, 2, 1]
print equal(A)