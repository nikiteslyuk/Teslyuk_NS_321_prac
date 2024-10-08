from math import sin


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


w = 80
h = 25
a, b = -4, 4
for i in range(h):
    # x = (b - a) / (h - 1) * i + a
    x = scale(0, h - 1, a, b, i)
    y = sin(x)
    # shift = round((y + 1) / 2 * w)
    shift = scale(-1, 1, 0, w - 1, y)
    print(' ' * round(shift), '*')
