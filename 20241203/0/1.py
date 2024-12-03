class final(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError(f"Нельзя иметь более одного родителя")
        return super().__new__(metacls, name, parents, namespace)


class E(metaclass=final):
    pass


class C:
    pass


# должно возвращать ошибку
class A(C, E):
    pass
