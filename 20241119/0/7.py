class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """description"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


class Age:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        """description"""
        if self._age == 42:
            print("secret value")
            return -1
        return self._age

    @age.setter
    def age(self, value):
        if value > 128:
            raise ValueError
        self._age = value


c = C()
c.age = 127
c.age = 42
