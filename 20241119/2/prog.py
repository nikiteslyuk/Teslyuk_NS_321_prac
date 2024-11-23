class Num:
    def __init__(self):
        self.default = 0
        self.data = {}

    def __get__(self, key, value):
        return self.data.get(key, self.default)

    def __set__(self, key, value):
        if hasattr(value, "real"):
            self.data[key] = value.real
        elif hasattr(value, "__len__"):
            self.data[key] = value.__len__()


import sys

exec(sys.stdin.read())
