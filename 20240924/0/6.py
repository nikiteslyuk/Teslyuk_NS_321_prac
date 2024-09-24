m = []
flag = 1
while n := input():
    newline = eval(n)
    ln = len(newline)
    if flag:
        for i in range(ln):
            m.append([])
        flag = 0
    for i in range(ln):
        m[i].append(newline[i])

print(m)
