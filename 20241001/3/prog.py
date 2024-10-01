from math import *


def Calc(s, t, u):

    def func(a):
        x = a
        y1 = eval(s)
        y2 = eval(t)
        x = y1
        y = y2
        return eval(u)

    return func


s, t, u = eval(input())
x = eval(input())
f = Calc(s, t, u)
print(f(x))
