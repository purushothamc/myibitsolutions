def repeatedNumber(A):
    numSum, squareSum = 0, 0
    for idx, elem in enumerate(A):
        numSum += elem
        numSum -= (idx + 1)
        squareSum += (elem * elem)
        squareSum -= ((idx + 1) * (idx + 1))
    squareSum /= numSum
    A = (numSum + squareSum) / 2
    B = squareSum - A
    return [A, B]
