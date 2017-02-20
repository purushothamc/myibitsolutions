def fullJustify(strings_list, number):
    result = []
    if not strings_list or number <= 0:
        return result
    current_length, idx, firstWord = 0, 0, True
    for word in strings_list:
        if firstWord:
            result.append(word)
            current_length += len(result[-1])
            firstWord = False
        else:
            next_word = " " + word
            current_length += len(next_word)
            if current_length <= number:
                result[-1] += next_word
            else:
                current_length = len(word)
                result.append(word)

    result_len = len(result)
    for idx in xrange(result_len):
        string = result[idx]
        space_count = string.count(" ")
        string_len = len(string)
        difference = number - string_len

        if (difference > 0 and space_count == 0) or idx == result_len - 1:
            string += " "*difference
            result[idx] = string
        else:
            extra_left = difference % space_count
            to_pad = difference / space_count
            temp_list = []
            for char in string:
                if char != " ":
                    temp_list.append(char)
                else:
                    spaced_char = ""
                    if extra_left:
                        spaced_char = " "
                        extra_left -= 1
                    spaced_char += " " + to_pad*" "
                    temp_list.append(spaced_char)
            result[idx] = "".join(temp_list)

    print result

A = ["This", "is", "an", "example", "of", "text", "justification."]
A = [ "What", "must", "be", "shall", "be." ]
B = 12
fullJustify(A, B)