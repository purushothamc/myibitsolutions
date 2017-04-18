def prettyPrint(number):
    size = 2*(number - 1) + 1
    result = [[] for x in xrange(size)]
    for x in result:
        for y in xrange(size):
            x.append(0)
    for x in xrange(number):
        sz = 2*(number-1) + 1
        ud = number - x
        for idx in xrange(x, sz-x):
            result[x][idx] = ud
        for idx in xrange(x, sz-x):
            result[idx][sz-x-1] = ud
        for idx in xrange(x, sz-x):
            result[sz - x - 1][idx] = ud
        for idx in xrange(x, sz-x):
            result[idx][x] = ud

    for x in result:
        print x

prettyPrint(4)