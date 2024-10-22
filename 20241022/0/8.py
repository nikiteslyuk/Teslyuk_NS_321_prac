from itertools import *


def ffn(n, seq):
    return filterfalse(lambda x: x % n, seq)


print(list(ffn(7, range(1, 10))))


def repeater(seq, n):
    yield from chain.from_iterable(map(lambda x: repeat(x, n), seq))


print(list(repeater('1234', 2)))
