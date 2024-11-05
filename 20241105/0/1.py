class C:
    pass


def fun(a, b):
    print(a, b)


C.a = 123
e = C()
e.qer = 23e4
C.foo = fun
e.foo = fun
print(e.foo(1, 2))
