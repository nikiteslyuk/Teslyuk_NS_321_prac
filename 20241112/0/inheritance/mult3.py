class A:
    def __str__(self):
        return "A"


class B(A):
    def __str__(self):
        st = super().__str__()
        return st + ":" + "B"


class C(B):
    def __str__(self):
        st = super().__str__()
        return st + ":" + "C"
