def isSafe(row, col, result):

    # check column rows
    for x in xrange(row):
        if result[x][col] == "Q":
            return False
    for x in xrange(row, len(result)):
        if result[x][col] == "Q":
            return False

    # check left up cross
    i, j = row, col
    while i >= 0 and j >= 0:
        if result[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # check right up cross
    i, j = row, col
    while i >= 0 and j < len(result):
        if result[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solveHelper(queen, row, cols, result, output):
    if queen == cols:
        x = ""
        for idx, y in enumerate(result):
            x += "".join(y)
            if idx != len(result) - 1:
                x += " "
        output.append(x)
        return True
    for col in xrange(cols):
        if isSafe(row, col, result):
            result[row][col] = "Q"
            solveHelper(queen + 1, row + 1, cols, result, output)
            result[row][col] = "."
    return False

def solveNQueens(n):
    result = [["."]*n for i in xrange(n)]
    output = []
    solveHelper(0, 0, n, result, output)
    return output


x = solveNQueens(4)
print x