def string_power_of_2(string):
    string_len = len(string)
    if not string_len or (string_len == 1 and int(string[0]) <= 1):
        return 0
    temp_string = string
    while temp_string != "1":
        idx, carry, sum, temp = 0, 0, 0, []
        string_len = len(temp_string)
        while idx < string_len:
            digit = int(temp_string[idx])
            sum = digit + carry*10
            temp.append(sum / 2)
            carry = sum % 2
            idx += 1
        for i in xrange(len(temp)):
            if temp[i] != 0:
                break
        temp = "".join([str(x) for x in temp[i:]])
        if temp != "1" and carry != 0:
            return 0
        temp_string = temp
    if temp_string == "1" and carry == 0:
        return 1
    return 0

A = "34315486476536324"
print string_power_of_2(A)
