def to_roman(number):
    lookup_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1]
    lookup_romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", \
                     "X", "IX", "V", "IV", "III", "II", "I"]
    if number <= 0:
        return
    i, result = 0, []
    while number:
        while number / lookup_values[i]:
            result.append(lookup_romans[i])
            number = number - lookup_values[i]
        else:
            i += 1
    return "".join(result)

print to_roman(999)