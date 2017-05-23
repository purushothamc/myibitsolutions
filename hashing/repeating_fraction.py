def fractionToDecimal(numerator, denominator):
    result = []
    mapper, index, before, negative = dict(), 0, 0, False
    if numerator == 0: return "0"

    # for negative numbers
    if (numerator < 0) ^ (denominator < 0): result.append("-")

    # take absolute values
    numerator, denominator = abs(numerator), abs(denominator)

    # append integral part to output
    result.append(numerator/denominator)
    if numerator % denominator == 0: return "".join([str(x) for x in result])

    # now try the fractional part until its remainder is 0
    # or remainder is not seen in a map.
    result.append(".")
    remainder = numerator % denominator

    while remainder != 0:
        # if a remainder is already seen in the map, insert a '(' in its 1st screen location.
        # insert ')' at end.
        if mapper.has_key(remainder):
            result.insert(mapper[remainder], "(")
            result.append(")")
            break

        mapper[remainder] = len(result)
        remainder *= 10
        quoint = remainder / denominator
        remainder = remainder % denominator
        result.append(quoint)

    return "".join([str(x) for x in result])

#print fractionToDecimal(1, 1111)
#print fractionToDecimal(1, 2147483648)
#print fractionToDecimal(123, 23452454)
#print fractionToDecimal(123, 234524)
print fractionToDecimal(1, 2)
print fractionToDecimal(-1, 2)
#print fractionToDecimal(12, 99009)