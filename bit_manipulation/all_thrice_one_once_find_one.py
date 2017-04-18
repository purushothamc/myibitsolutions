"""
This problem specifies that all elements in the array are appeared
thrice except one number.
Solution 1) We can use counting array, but this takes extra space.
Solution 2)
    Since all elements appears thrice, there are 3x bits and each ith
    position contains 3 same bits, so XOR is not possible using this method.

    We can 32 bit array, to get the count of ith position bits.
    If we can find the count, we can easily find remainder to get the required number.
"""
def singleNumber(A):
    bitArray = [0 for x in xrange(32)]
    result = 0
    for i in xrange(32):
        for x in A:
            if (x >> i) & 1:
                bitArray[i] += 1
        result |= ((bitArray[i]%3) << i)
    return result

A = [1,1,1,2,2,2,3,4,4,4]
print singleNumber(A)