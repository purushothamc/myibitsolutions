def print_rangoli(size):
    result = []
    for idx in range(size, 0, -1):
        count = (4*idx - 3) / 2
        temp_str = []
        ord_val = ord('a') + size - 1

        for i in range(count):
            temp_str.append("-")
        for j in range(size, idx-1, -1):
            temp_str.append(chr(ord('a') + j - 1))
        if j != idx:
                temp_str.append("-")

        	
        for j in range(idx, size):
            if size != idx:
                temp_str.append("-")
            temp_str.append(chr(ord('a') + j))
        for i in range(count):
            temp_str.append("-")
	
        result.append("".join(temp_str))
	
    for x in result:
        print x
    for x in range(len(result)-2, -1, -1):
        print result[x]

print_rangoli(10)
