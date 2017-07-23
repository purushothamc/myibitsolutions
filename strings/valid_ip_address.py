class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, ip_string):
        result = list()
        if len(ip_string) <= 3:
            return result
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    #print ip_string[:i], ip_string[i:j], ip_string[j:k], ip_string[k:]
                    if 1 <= len(ip_string[k:]) <=3 \
                        and 0 <= int(ip_string[:i]) <= 255 and 0 <= int(ip_string[i:j]) <= 255\
                            and 0 <= int(ip_string[j:k]) <= 255 and 0 <= int(ip_string[k:]) <= 255:
                        if not (len(ip_string[j:k]) > 1 and ip_string[j:k].startswith('0')) and \
                            not (len(ip_string[:i]) > 1 and ip_string[:i].startswith('0')) and \
                            not (len(ip_string[i:j]) > 1 and ip_string[i:j].startswith('0')) and \
                            not (len(ip_string[k:]) > 1 and ip_string[k:].startswith('0')):
                            result.append(".".join([ip_string[:i], ip_string[i:j], ip_string[j:k], ip_string[k:]]))
        return result