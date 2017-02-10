def roman_to_integer(roman_string):
    if not roman_string:
        return 0
    idx, strlen = 0, len(roman_string)
    result = 0
    while idx < strlen:
        if idx + 1 < strlen and roman_string[idx] == "I" and roman_string[idx+1] == "V":
                result += 4
                idx += 2
        elif idx + 1 < strlen and roman_string[idx] == "I" and roman_string[idx+1] == "X":
                result += 9
                idx += 2
        elif idx + 1 < strlen and roman_string[idx] == "X" and roman_string[idx+1] == "L":
                result += 40
                idx += 2
        elif idx + 1 < strlen and roman_string[idx] == "X" and roman_string[idx+1] == "C":
                result += 90
                idx += 2
        elif idx + 1 < strlen and roman_string[idx] == "C" and roman_string[idx+1] == "D":
                result += 400
                idx += 2
        elif idx + 1 < strlen and roman_string[idx] == "C" and  roman_string[idx+1] == "M":
                result += 900
                idx += 2
        else:
            if roman_string[idx] == "M":
                result += 1000
            elif roman_string[idx] == "D":
                result += 500
            elif roman_string[idx] == "C":
                result += 100
            elif roman_string[idx] == "L":
                result += 50
            elif roman_string[idx] == "X":
                result += 10
            elif roman_string[idx] == "V":
                result += 5
            elif roman_string[idx] == "I":
                result += 1
            idx += 1
    return result

def roman_to_integer_v2(roman_string):
    if not roman_string:
        return 0
    lookup_table = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000
                   }
    idx, strlen = 0, len(roman_string)
    result = 0
    while idx < strlen:
        if idx + 1 < strlen and \
                lookup_table[roman_string[idx]] < lookup_table[roman_string[idx + 1]]:
            result -= lookup_table[roman_string[idx]]
        else:
            result += lookup_table[roman_string[idx]]
        idx += 1
    return result

A = "XIV"
print roman_to_integer_v2(A)