class Vowel:
    __slots__ = ["a", "o", "u", "i", "e", "y", "_answer"]

    def __init__(self, a=None, o=None, u=None, i=None, e=None, y=None):
        self.a = a
        self.o = o
        self.u = u
        self.i = i
        self.e = e
        self.y = y
        self._answer = 42

    def __str__(self):
        fields = [
            f"{k}: {getattr(self, k)}" for k in "aouiey" if getattr(self, k) is not None
        ]
        return ", ".join(sorted(fields)) if fields else ""

    @property
    def answer(self):
        raise AttributeError("answer is read-only")

    @property
    def full(self):
        return all(getattr(self, k) is not None for k in "aouiey")


import sys

exec(sys.stdin.read())
