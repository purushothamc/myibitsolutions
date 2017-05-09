def anagrams(A):
    mapper = dict()
    for index, string in enumerate(A):
        string = "".join(sorted(string))
        print mapper
        if not mapper.get(string, 0):
            mapper[string] = [index + 1]
        else:
            mapper[string].append(index + 1)
    result = []
    for key, val in mapper.iteritems():
        result.append(val)
    return result

A = [ "cat", "dog", "god", "tca" ]
print anagrams(A)