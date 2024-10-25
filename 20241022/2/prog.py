from itertools import islice, tee
import itertools


def slide(seq, n):
    it1, = itertools.tee(seq, 1)
    length = sum(1 for _ in it1)
    for i in range(length):
        it2, = itertools.tee(seq, 1)
        yield from itertools.islice(it2, i, i + n)


import sys

exec(sys.stdin.read())
