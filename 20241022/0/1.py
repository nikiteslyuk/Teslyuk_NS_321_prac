from itertools import count


def summ():
    res = 0
    for i in count(1):
        res += 1 / (i * i)
        yield res


k = summ()
for i in range(200):
    print(next(k), i)
