from math import sin, cos, tan, atan, pi


def F(*functions):

    def minim(x):
        return min([elem(x) for elem in functions])

    return minim


res = F(sin, cos, tan, atan)

print(res(pi / 4))
