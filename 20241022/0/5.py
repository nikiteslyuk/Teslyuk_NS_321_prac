def f(x):
    yield ">"
    yield from x
    yield "<"
    return len(x)


def run(gen):
    s = yield from gen
    print(f'/{s}/')


g = f('qw')
lst = list(run(g))
print(lst)
