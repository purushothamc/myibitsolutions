class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def preprocess_needle(self, needle):
        temp = [0 for i in range(len(needle))]
        j, i = 0, 1
        while i < len(needle):
            if needle[j] == needle[i]:
                temp[i] = temp[i-1] + 1
                i += 1
                j += 1
            else:
                j = temp[j-1]
                if j > 0 and needle[i] != needle[j]:
                    j = temp[j]
                if needle[i] == needle[j]:
                    temp[i] = temp[j] + 1
                else:
                    temp[i] = 0
                i += 1
        return temp

    def strStr(self, haystack, needle):
        if not haystack or not needle:
            return -1
        processed = self.preprocess_needle(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif i < len(haystack) and needle[j] != haystack[i]:
                if j > 0:
                    j = processed[j-1]
                else: i+= 1
        return -1