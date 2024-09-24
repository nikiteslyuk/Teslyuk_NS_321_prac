lis = []
while n := input():
    newline = list(eval(n))
    lis.append(newline)

# проверка равенства длины подсписков
if not all([len(e) == len(lis) for e in lis]):
    print("wat")
    exit(100500)

for i in range(len(lis)):
    for j in range(i + 1, len(lis[0])):
        lis[i][j], lis[j][i] = lis[j][i], lis[i][j]

print(lis)
