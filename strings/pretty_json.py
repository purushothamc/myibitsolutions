# Problem description can be found at here.
# https://www.interviewbit.com/problems/pretty-json/
def convert_list_to_str(l):
    return "".join(l)

def prettyJSON(string):
    result = []
    tab_length, default_tab_len = 0, 4
    temp_list_string = []
    for char in string:
        if not temp_list_string:
            temp_list_string = ["\t" for x in xrange(tab_length/4)]
        if char == "{" or char == "[":
            if temp_list_string:
                converted_str = convert_list_to_str(temp_list_string)
                if not converted_str.isspace():
                    result.append(converted_str)
            temp_list_string = ["\t" for x in xrange(tab_length/4)]
            temp_list_string.append(char)
            result.append(convert_list_to_str(temp_list_string))
            tab_length += default_tab_len
            temp_list_string = []
        elif char == "}" or char == "]":
            if temp_list_string:
                converted_str = convert_list_to_str(temp_list_string)
                if not converted_str.isspace():
                    result.append(converted_str)
            tab_length -= default_tab_len
            temp_list_string = ["\t" for x in xrange(tab_length/4)]
            temp_list_string.append(char)
            result.append(convert_list_to_str(temp_list_string))
            temp_list_string = []
        else:
            temp_list_string.append(char)
            if char == ",":
                lastchar = result[-1][-1]
                if lastchar == "]" or lastchar == "}":
                    result[-1] = result[-1] + char
                else:
                    result.append(convert_list_to_str(temp_list_string))
                temp_list_string = []
    for line in result:
        print line


string = "['foo', {'bar':['baz',null,1.0,2]}]"
string = "{'A':'B','C':{'D':'E','F':{'G':'H','I':'J'},'K':'L'}}"
prettyJSON(string)