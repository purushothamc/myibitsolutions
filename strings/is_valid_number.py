def atoi(A):
    maxint = 2147483647
    result, current_sum = 0, 0
    seenDigitBefore, founde = False
    lenStr, idx = len(A), 0
    while idx < lenStr:
        if A[idx] != " ": break
        idx += 1
    negative = True if A[idx] == "-" else False
    positive = True if A[idx] == "+" else False
    if negative or positive: idx += 1
    while idx < lenStr:
        digit = A[idx]
        if digit.isdigit() and not seenDigitBefore:
            seenDigitBefore = True
        elif not digit.isdigit() and seenDigitBefore:
            break
        elif not digit.isdigit() and not seenDigitBefore:
            return 0
        if digit.isalpha() and digit == "e" and seenDigitBefore:
            founde = True
        if not founde:
            digit_int = int(digit)
            if (result == maxint / 10 and digit_int > maxint % 10) or \
                (result > maxint / 10):
                return maxint if not negative else -1*(maxint+1)
            result = result*10 + int(digit)
            idx += 1
    if negative:
        return result*(-1)
    return result