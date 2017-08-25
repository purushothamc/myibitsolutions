def stairs(n):
    temp = [1 for i in xrange(n+1)]
    temp[0] = 0
    temp[1] = 1
    temp[2] = 2
    if n <= 2:
        return n
    for i in xrange(3, n+1):
        temp[i] = temp[i-1] + temp[i-2]
    return temp[n]

n = 3
print stairs(n)