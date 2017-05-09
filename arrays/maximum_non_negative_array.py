def maxset(A):
    if not A: return A
    start, end, ln, s = 0, 0, 0, 0
    old_start, old_end, old_ln, old_sum = 0, 0, 0, 0
    for idx, x in enumerate(A):
        if x >= 0:
            if not end and not ln:
                start, end = idx, idx
            else:
                end += 1
            ln += 1
            s += x
            if s > old_sum or (s == old_sum and ln > old_ln):
                old_start, old_end, old_ln, old_sum = start, end, ln, s
        else:
            end, ln, s = 0, 0, 0
    if not s and not old_sum and not ln:
        return []
    if s < old_sum:
        return A[old_start:old_end + 1]
    elif s == old_sum:
        if ln > old_ln:
            return A[start: end + 1]
        elif ln < old_ln:
            return A[old_start:old_end + 1]
        else:
            if start < old_start:
                return A[start: end + 1]
            else:
                return A[old_start:old_end + 1]
    else:
        return A[start:end + 1]