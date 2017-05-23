def grayCodeHelper(temp, output, t):
    #-------------------------- ---- #
    #------ This will not work ----- #
    if t < 0:
        return
    sum, i = 0, 0
    for bit in reversed(temp):
        sum += 2 ** (i) * bit
        i += 1
    output.append("".join([str(x) for x in temp]))
    print temp, t
    for index in xrange(t-1, -1, -1):
        temp[index] = 1
        grayCodeHelper(temp, output, index)
        temp[index] = 0


def grayCode(A):
    result = []
    if A == 0:
        result.append(0)
        return result
    result = grayCode(A-1)
    numToAdd = 1 << (A-1)
    for x in xrange(len(result)-1, -1, -1):
        result.append(numToAdd + result[x])
    return result

print grayCode(3)