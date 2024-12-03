class Doubeleton(type):
    _instance = 1
    _classes = []

    def __call__(cls, *args, **kw):
        if cls._instance < 2:
            cls._classes.append(super().__call__(*args, **kw))
        cls._instance += 1
        return cls._classes[cls._instance % len(cls._classes)]


class C(metaclass=Doubeleton):
    pass


print(*(C() for i in range(7)), sep="\n")
