def check(s, w, n1, c1, n2, c2):
    res1 = 0
    res2 = 0
    for i in range(n1 + 1):
        res1 += c1[i] * s**(n1 - 1 - i)
    for i in range(n2 + 1):
        res2 += c2[i] * s**(n2 - 1 - i)
    if res2 == 0:
        return False
    return res1 / res2 == w


def parse(inp):
    s = inp[0]
    w = inp[1]
    n1 = inp[2]
    coeffs1 = inp[3:3 + n1 + 1]
    n2 = inp[3 + n1 + 1]
    coeffs2 = inp[3 + n1 + 2:]
    return s, w, n1, coeffs1, n2, coeffs2


data = eval(input())
print(check(*parse(data)))
