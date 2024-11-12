class A:
    v = 1


class B(A):
    v = 2


a = A()
b = B()
b.v = 3
print(b.v, a.v)
del b.v
print(b.v, a.v)
del B.v
print(b.v, a.v)
