def palindrome(A):
    if not A:
        return True
    ln = len(A)
    i, j = 0, ln-1
    while i <= j:
        while i < j and not A[i].isalnum():
            i += 1
        while i < j and not A[j].isalnum():
            j -= 1
        if A[i].lower() != A[j].lower():
            return False
        i += 1
        j -= 1
    return True

A = "race a car"
print palindrome(A)