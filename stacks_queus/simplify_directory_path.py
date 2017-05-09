def simplifyPath(self, A):
    strings = A.split("/")
    lst = []
    for string in strings:
        if string == "..":
            if not lst:
                continue
            else:
                lst.pop()
        elif not string or string == ".":
            continue
        else:
            lst.append(string)
    if not lst:
        return "/"
    else:
        return "/" + "/".join(lst)