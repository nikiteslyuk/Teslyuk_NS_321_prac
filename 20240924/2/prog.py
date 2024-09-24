def key(x):
    return x * x % 100


lis = list(eval(input()))

for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        if key(lis[i]) > key(lis[j]):
            lis[i], lis[j] = lis[j], lis[i]
print(lis)
