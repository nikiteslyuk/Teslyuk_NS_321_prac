def objcount(cls):
    cls.counter = 0
    init = cls.__init__ if hasattr(cls, "__init__") else None
    dell = cls.__del__ if hasattr(cls, "__del__") else None

    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if init:
            init(self, *args, **kwargs)

    def new_del(self, *args, **kwargs):
        cls.counter -= 1
        if dell:
            dell(self, *args, **kwargs)

    cls.__init__ = new_init
    cls.__del__ = new_del

    return cls


import sys

exec(sys.stdin.read())
