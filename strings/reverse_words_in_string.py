def reverse_helper(S):
    i, j = 0, len(S) - 1
    result = list(S)
    while i <= j:
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
    return "".join(result)

def reverse_words(A):
    """
    This solution uses 2 passes over string,
    1st pass to reverse entire string
    2nd pass to reverse individual words of string.
    :param A:
    :return:
    """
    if not A:
        return A
    i = 0
    ln = len(A)
    result = []
    A = reverse_helper(A)
    while i < ln:
        while i < ln and A[i] == " ":
            i += 1
        j = i
        while j < ln and A[j] != " ":
            j += 1
        if i < ln and A[i] != " ":
            rev_word = reverse_helper(A[i:j])
            result.append(rev_word)
        i = j
    return " ".join(result)

def reverse_words_v2(S):
    """
    This solution uses only 1 pass over string to reverse words in it.
    This works by starting from end char to find beginning
    of word and append the word to result
    """
    string_len = len(S)
    j, i = string_len - 1, 0
    result = []
    while j >= 0 and i >= 0:
        while j >= 0 and S[j] == " ":
            j -= 1
        i = j
        while i >= 0 and S[i] != " ":
            i -= 1
        if i+1 >= 0 and S[i+1] != " ":
            result.append(S[i+1:j+1])
        j = i
    return " ".join(result)

A = " j "
print reverse_words_v2(A), len(reverse_words_v2(A))
