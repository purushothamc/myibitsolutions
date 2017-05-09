def findPerm(self, A, B):
    ln = len(A)
    result = []
    incr, decr = 1, B
    for letter in A:
        if letter == "D":
            if decr <= 0:
                decr = B
            result.append(decr)
            decr -= 1
        elif letter == "I":
            if incr > B:
                incr = 1
            result.append(incr)
            incr += 1
    if A[-1] == "D":
        result.append(decr)
    else:
        result.append(incr)
    return result