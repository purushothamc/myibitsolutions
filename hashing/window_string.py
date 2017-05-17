def check(m):
    return all([v == 0 for k, v in m.items()])

def minWindow(S, T):
    from collections import deque
    count, minCount, left = 0, len(S) + 1, 0
    result, output, mapper = dict(), "", dict()
    for each in T:
        mapper[each] = mapper.get(each, 0) + 1

    for index, each in enumerate(S):
        if mapper.has_key(each):
            if result.has_key(each):
                if result[each] < mapper[each]:
                    count += 1
                result[each] += 1
            else:
                result[each] = 1
                count += 1
        if count == len(T):
            sc = S[left]
            while not result.has_key(sc) or result[sc] > mapper[sc]:
                if result.has_key(sc) and result[sc] > mapper[sc]:
                    result[sc] -= 1
                left += 1
                sc = S[left]
            if index - left + 1 < minCount:
                minCount = index - left + 1
                output = S[left: index + 1]
    return output

A = "ADOBECODEBANC"
B = "ABC"
A = "xiEjBOGeHIMIlslpQIZ6jERaAVoHUc9Hrjlv7pQpUSY8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0B" \
    "rmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9Bbk" \
    "NsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5u" \
    "q1IxhAYZvRQVHtuHae0xxwCbRh6S7fCLKfXeSFITfKHnLdT65K36vGC7qOEyyT0Sm3Gwl2iXYSN2ELIoITfGW888G" \
    "XaUNebAr3fnkuR6VwjcsPTldQSiohMkkps0MH1cBedtaKNoFm5HbH15kKok6aYEVsb6wOH2w096OwEyvtDBTQwoLN" \
    "87JriLwgCBBavbOAiLwkGGySk8nO8dLHuUhk9q7f0rIjXCsQeAZ1dfFHvVLupPYekXzxtWHd84dARvv4Z5L1Z6j8ur" \
    "2IXWWbum8lCi7aErEcq41WTo8dRlRykyLRSQxVH70rUTz81oJS3OuZwpI1ifBAmNXoTfznG2MXkLtFu4SMYC0bPHN" \
    "ctW7g5kZRwjSBKnGihTY6BQYItRwLUINApd1qZ8W4yVG9tnjx4WyKcDhK7Ieih7yNl68Qb4nXoQl079Vza3SZoKeWp" \
    "hKef1PedfQ6Hw2rv3DpfmtSkulxpSkd9ee8uTyTvyFlh9G1Xh8tNF8viKgsiuCZgLKva32fNfkvW7TJC654Wmz7tPM" \
    "Iske3RXgBdpPJd5BPpMpPGymdfIw53hnYBNg8NdWAImY3otYHjbl1rqiNQSHVPMbDDvDpwy01sKpEkcZ7R4SLCazPC" \
    "lvrx5oDyYolubdYKcvqtlcyks3UWm2z7kh4SHeiCPKerh83bX0m5xevbTqM2cXC9WxJLrS8q7XF1nh"
B = "dO4BRDaT1wd0YBhH88Afu7CI4fwAyXM8pGoGNsO1n8MFMRB7qugS9EPhCauVzj7h"
print minWindow(A, B)