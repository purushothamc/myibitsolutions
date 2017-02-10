def add_2_binary_strings(string1, string2):
    len1, len2 = len(string1), len(string2)
    i, j = len1 - 1, len2 - 1
    result = []
    carry = 0
    while i >= 0 or j >= 0 or carry:
        binsum = 0
        if i >= 0: binsum += int(string1[i])
        if j >= 0: binsum += int(string2[j])
        if carry >= 0: binsum += carry
        result.append(binsum % 2)
        carry = binsum / 2
        i -= 1
        j -= 1
    return "".join([str(x) for x in reversed(result)])

A = "1"
B = "11"
print add_2_binary_strings(A, B)