def reverseBits(A):
    result, i = 0, 0
    while i < 32:
        bit = A & 1
        result = result * 2 + bit
        A >>= 1
        i += 1
    return result

def swapBits(i, j, x):
    lo = (x >> i) & 1
    hi = (x >> j) & 1
    if lo ^ hi:
        x ^= (1 << i) | (1 << j)
    return x

def reverseBitsV2(x):
    import sys
    size = sys.getsizeof(x)*8
    idx = 0
    while idx < size / 2:
        x = swapBits(idx, size-idx-1, x)
        idx += 1
    return x

x = 3
print reverseBitsV2(x)