# Problem statement can be found here
def countAndSay(A):
    if not A:
        return ""
    result, temp = "1", ""
    i = 2
    while i <= A:
        j = 0
        temp = ""
        while j < len(result):
            count = 1
            while j+1 < len(result) and result[j] == result[j+1]:
                count += 1
                j += 1
            else:
                temp += str(count) + result[j]
                j += 1
        result = temp
        i += 1
    return result

print countAndSay(6)