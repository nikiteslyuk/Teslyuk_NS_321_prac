# Так делать не надо См лекции


class A:
    pass


class B(A):
    pass


class X(A, B):
    pass


# А вот так делать надо


class A:
    pass


class B(A):
    pass


class X(B, A):
    pass
