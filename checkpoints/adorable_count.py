import re
regex = re.compile("^[a-z][a-z0-9:]*\/[a-z0-9]+\\\[a-z]+$")
def adorableCount(words):
    from collections import deque
    import re
    #regex = re.compile("[a-z][a-z0-9:]*/[0-9a-z]+\\[a-z]+")
    regex = re.compile("^[a-z][a-z0-9:]*\/[a-z0-9]+\\\[a-z]+$")
    second_regex = re.compile("^[a-z]")
    result = list()

    for word in words:
        count, temp = 0, deque()
        index, matchFound = 0, False
        while index < len(word):
            while index < len(word) and not regex.match("".join(temp)):
                temp.append(word[index])
                index += 1
            else:
                count += 1
                while index < len(word):
                    temp.append(word[index])
                    if regex.match("".join(temp)):
                        count += 1
                        index += 1
                    else:
                        break
                print "".join(temp)
                temp.popleft()
                while not second_regex.match("".join(temp)):
                    temp.popleft()

        result.append(count)
    return result

def adorableWordCount(words):
    result = list()
    for word in words:
        count = 0
        for outer in xrange(len(word)-1):
            for inner in xrange(outer+1, len(word)):
                if regex.match(word[outer:inner+1]):
                    count += 1
        result.append(count)
    return result


words = ["w\//a/b", "w\//a\\y", "w\/a\\y", "w:://a\\b", "w::/a\\y", "w:/a\\yc::/12\hyz"]
#words = ["w:/a\\yc::/12\hyz"]
#print adorableCount(words)
print adorableWordCount(words)