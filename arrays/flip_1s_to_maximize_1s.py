def flip(A):
    ln = len(A)
    count, maxCount, maxStart = 0, 0, 0
    start, end = 0, 0
    for idx in xrange(ln):  # looping over all elements
        if A[idx] == "0":  # if I encounter zero, I increment count.
            count += 1
            # if number of 0s which are seen till now are greater,
            # I'll update max Sum value and also the indices.
            if count > maxCount:
                maxCount = count
                end = idx + 1
                start = maxStart + 1
        # if 1 is seen, I'll decrement count since on flipping 1 becomes zero.
        elif A[idx] == "1":
            count -= 1
            if count < 0:
                count = 0
                maxStart = idx + 1
    if end == 0 and start == 0:
        return []
    if start == 0:
        start += 1
    return [start, end]

#A = "0111000100010"
#A = "01100"
#A = "110100111101101"
#A = "01"
#A = "01010111010100010010"
A = "111"
print flip(A)