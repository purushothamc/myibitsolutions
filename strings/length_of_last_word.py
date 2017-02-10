def lengthOfLastWord(S):
    result = 0
    i, j = 0, len(S) - 1
    while j >= 0:
        while j >= 0 and S[j] == " ":
            j -= 1
        i = j
        while i >= 0 and S[i] != " ":
            result += 1
            i -= 1
        j = i
        break
    return result

A = "q"
print lengthOfLastWord(A)