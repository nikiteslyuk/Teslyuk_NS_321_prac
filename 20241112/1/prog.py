import collections


class DivStr(collections.UserString):
    def __init__(self, st=""):
        self.data = st

    def __floordiv__(self, n):
        ln = len(self.data)
        for i in range(0, ln - ln % n, ln // n):
            yield self.data[i : i + ln // n]

    def __mod__(self, n):
        ln = len(self.data)
        return DivStr(self.data[-(ln % n) :])


a = DivStr("XcDfQWEasdERTdfgRTY")
print(*a // 4)
print(a % 4)
print(*a % 10 // 3)
print(a.lower() % 3)
print(*a[1:7] // 3)
print(a % 5 + DivStr() + a % 6)
