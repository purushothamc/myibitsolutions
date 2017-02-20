def convert(string, number):
    string_len = len(string)
    if number == 0 or number >= string_len or number == 1:
        return string
    row = 0
    temp_list = []
    while row < number:
        if row == 0 or row == number - 1:
            steps = 2*(number - 2) + 1
            for x in xrange(row, string_len, steps+1):
                temp_list.append(string[x])
        else:
            up = False
            idx = row
            downIndex = 2*(number - row-1)
            upIndex = 2*row
            print row, number, downIndex, upIndex
            temp_list.append(string[row])
            while idx < string_len:
                index = downIndex if not up else upIndex
                if idx + index < string_len:
                    temp_list.append(string[idx + index])
                idx += index
                up = not up
        steps -= 1
        row += 1
    return "".join(temp_list)

def convert_v2(string, number):
    """
    This solution works by maintaining list of rows and what elements must be there in each row.
    """
    string_len = len(string)
    if number == 0 or number >= string_len or number == 1:
        return string
    row, step = 0, 1
    result = [[] for x in xrange(number)]
    for idx in xrange(string_len):
        result[row].append(string[idx])
        if row == 0:
            step = 1
        if row == number - 1:
            step = -1
        row += step

    result = "".join([value for sublist in result for value in sublist])
    return result

A = "ABCD"
B = 3
print convert_v2(A, B)