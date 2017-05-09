def trailingZeroes(self, A):
    import math
    if A <= 0:
        return 0
    count = 0
    factor = 5
    while factor <= A:
        count += int(math.floor(A / factor))
        factor *= 5
    return count
