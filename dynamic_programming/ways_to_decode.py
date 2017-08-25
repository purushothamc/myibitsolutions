def decodeWays(n):
    n = str(n)
    if n.endswith("00") or n.startswith("0"):
        return 0
    temp = [0 for i in range(len(n))]
    if len(n) == 1:
        return 1
    temp[0] = 1
    if len(n) >= 2:
        if 11 <= int(n[:2]) <= 26:
            temp[1] = 2
        else:
            temp[1] = 1
    for i in range(2, len(n)):
        if 10 <= int(n[i - 1: i + 1]) <= 26:
            temp[i] += temp[i - 2]
        if int(n[i]) != 0:
            temp[i] += temp[i - 1]
    #print temp, A
    return temp[len(n) - 1]

A = "51634903944990932211994018980202705458593263575206189535802" \
    "3716882669696553778956506242967696287703878170838557587631287" \
    "794136755741010138368419405740501886123439466090571223842867" \
    "5120866930196204792703765204322329401298924190"
A = 101
print decodeWays(A)