class A:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.__class__(self.val + other.val)


class B(A):
    def __sub__(self, other):
        return self.__class__(self.val - other.val)


b = B(5)
c = A(4)
print(b + B(43) - c)
