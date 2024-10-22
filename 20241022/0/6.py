def travel(n):
    yield from ["по кочкам"] * n
    return 'и в яму'


def travelwrap(n):
    res = yield from n
    yield res


g = travel(5)
print(list(g))
g = travel(5)
k = travelwrap(g)
print(list(k))
