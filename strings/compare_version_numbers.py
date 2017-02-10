# ---- Problem statement ca be found here
# https://www.interviewbit.com/problems/compare-version-numbers/

def compareVersion(a, b):
    def compare_numbers(a, b):
        print a, " puru ", b
        len1, len2 = len(a), len(b)
        i, j = 0, 0
        while i < len1 and a[i] == "0":
            i += 1
        while j < len2 and b[j] == "0":
            j += 1
        if len1-i < len2-j:
            return -1
        elif len1-i > len2-j:
            return 1
        while i < len1 and j < len2:
            if a[i] > b[j]:
                return 1
            elif a[i] < b[j]:
                return -1
            i += 1
            j += 1
        if i == len1 and j < len2:
            return -1
        if j == len2 and i < len1:
            return 1
        return 0

    len1, len2 = len(a), len(b)
    i, j = 0, 0
    while i < len1 or j < len2:
        temp1, temp2 = [], []
        while i < len1 and a[i] != ".":
            temp1.append(a[i])
            i += 1
        while j < len2 and b[j] != ".":
            temp2.append(b[j])
            j += 1
        return_value = compare_numbers(temp1, temp2)
        if not return_value:
            i += 1
            j += 1
        else:
            return return_value
    return 0

A = "324"
B = "4.13"
print compareVersion(A, B)