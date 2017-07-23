class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, string):
        start, end, result = 0, 0, 0
        for i in range(0, len(string)):
            j, k = i - 1, i + 1
            cnt = 1
            while j >= 0 and k < len(string):
                if string[j] == string[k]:
                    cnt += 2
                    if cnt > result:
                        start, end = j, k
                        result = cnt
                else:
                    break
                k += 1
                j -= 1
            j, k = i - 1, i
            cnt = 0
            while j >= 0 and k < len(string):
                if string[j] == string[k]:
                    cnt += 2
                    if cnt > result:
                        start, end = j, k
                        result = cnt
                else:
                    break
                k += 1
                j -= 1

        return string[start:end + 1]