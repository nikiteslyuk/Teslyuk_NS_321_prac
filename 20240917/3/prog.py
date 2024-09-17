n = eval(input())
k = n
i = 0
while i < 3: 
    j = 0
    while j < 3: 
        mul = (n + i) * (n + j)
        sm = sum(map(int, list(str(mul))))
        if sm == 6: 
            print('{} * {} = {} '.format(n + i, n + j, ":=)"), end = '')
        else: 
            print('{} * {} = {} '.format(n + i, n + j, mul), end = '')
        j += 1
    print()
    i += 1
