from math import sin, cos, pi


def s(f, g):

    def fun(x):
        return f(x) + g(x)

    return fun


res = s(sin, cos)
print(res(pi / 4))
