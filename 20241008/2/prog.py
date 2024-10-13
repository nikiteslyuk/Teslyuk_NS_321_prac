from math import *


def f(x):
    return eval(formula)


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


W, H, A, B, formula = input().split()
W, H, A, B = int(W), int(H), float(A), float(B)
sc = 1000
x_values = [scale(0, sc - 1, A, B, i) for i in range(sc)]
y_values = [f(x) for x in x_values]

y_min = min(y_values)
y_max = max(y_values)
p = 0

screen = [[' ' for _ in range(W)] for _ in range(H)]

for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = round(scale(y_min, y_max, 0, H - 1, f(x)))
    if 0 <= y < H:
        screen[y][i] = '*'
        if i != 0:
            for j in range(min(y, p) + 1, max(y, p)):
                screen[j][i - 1] = '*'
    p = y

for row in screen[::-1]:
    print(''.join(row))
