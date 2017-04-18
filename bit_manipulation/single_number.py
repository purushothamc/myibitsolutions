def singleNumber(A):
    """
    This is default solution using counting array.
    """
    d = {}
    for x in A:
        if not d.get(x, None):
            d[x] = 1
        else:
            d[x] += 1
    for x in d.keys():
        if d[x] == 1:
            return x

def singleNumberXOR(A):
    """
    XOR solution can be used when all elements appear twice except 1 number.
    In this case, all bits at position i, will appear odd number of times.
    With XOR, even number of occurrences of bits cancel out, and number remains
    """
    result = 0
    for x in A:
        result ^= x
    return result

A = [1,2,2,3,1]
print singleNumber(A)