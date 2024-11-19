class Dumper:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args, kwargs, end=" → ")
        res = self.function(*args, **kwargs)
        print(res)
        return res


@Dumper
def add(x, y, z):
    return x + y + z


print(add(1, 2, 3))
