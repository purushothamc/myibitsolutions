def generateHelper(output, left, rigt, temp):
    if left > rigt:
        return
    if left == 0 and rigt == 0:
        output.append(temp)
        return
    if left > 0:
        generateHelper(output, left - 1, rigt, temp + "(")
    if rigt > 0:
        generateHelper(output, left, rigt - 1, temp + ")")
    return

def solution2Helper(output, open, close, current, total):
    if open == close and open == total:
        output.append(current)
        return
    if open > total or close > total or close > open:
        return
    if open < total:
        solution2Helper(output, open + 1, close, current + "(", total)
    if close < total:
        solution2Helper(output, open, close + 1, current + ")", total)


def generate(pLen):
    output, result = [], []
    temp = ""
    generateHelper(output, pLen, pLen, temp)
    solution2Helper(result, 0, 0, temp, pLen)
    print output
    return result

print generate(4)