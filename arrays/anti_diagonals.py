def diagonal(a):
    if not a:
        return [[]]
    rows = len(a)
    cols = rows
    result = []
    for j in xrange(cols):
        temp = []
        x, y = j, 0
        while x >= 0 and y <= j:
            temp.append(a[y][x])
            x -= 1
            y += 1
        result.append(temp)
    for i in xrange(1, rows):
        temp = []
        x, y = i, j
        while x <= rows and y >= i:
            temp.append(a[x][y])
            x += 1
            y -= 1
        result.append(temp)
    return result