import timeit

snip = input()
T = timeit.Timer(snip)
res = T.autorange()
print(res)
