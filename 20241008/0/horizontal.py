from math import sin


def show(scr):
    print('\n'.join(''.join(s) for s in scr))


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


def gra(a, b, w, h):
    screen = [[' '] * w for i in range(h)]
    for i in range(w):
        x = scale(0, w - 1, a, b, i)
        y = sin(x)
        shift = scale(-1, 1, 0, h - 1, y)
        screen[round(shift)][i] = '*'
    return screen


res = gra(-4, 4, 60, 20)
show(res)
