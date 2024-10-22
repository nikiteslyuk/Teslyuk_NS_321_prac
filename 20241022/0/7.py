from itertools import dropwhile, islice, count


def summ():
    res = 0
    for i in count(1):
        res += 1 / (i * i)
        yield res


def prog():
    s = 0
    print(
        list(
            islice(
                dropwhile(lambda x: x <= 1.6,
                          (s := s + 1 / (i * i) for i in count(1))), 10)))


prog()
