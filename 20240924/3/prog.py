n = list(eval(input()))
ln = len(n)
m1 = []
m2 = []

m1.append(n)
for i in range(ln - 1):
    m1.append(list(eval(input())))

for i in range(ln):
    m2.append(list(eval(input())))

res = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]

for i in range(len(res)):
    for j in range(len(res[0])):
        for k in range(len(res)):
            res[i][j] += m1[i][k] * m2[k][j]

for elem in res:
    print(*elem, sep=',')
