s = []
while True:
    try:
        n = list(eval(input()))
        if not n:
            break
        s.append(n)
    except EOFError:
        break

m1 = s[:len(s) // 2]
m2 = s[len(s) // 2:]
res = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]

for i in range(len(res)):
    for j in range(len(res[0])):
        for k in range(len(res)):
            res[i][j] += m1[i][k] * m2[k][j]

for elem in res:
    print(*elem, sep=',')
