def fib(m, n):
    a, b = 1, 1
    for _ in range(m):
        a, b = b, b + a
    for _ in range(m, n + m):
        yield a
        a, b = b, b + a


import sys

exec(sys.stdin.read())
