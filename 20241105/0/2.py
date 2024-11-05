class Rectangle:
    rectcnt = 0

    def __init__(self, x1=0, y1=0, x2=1, y2=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f'rect_{self.__class__.rectcnt}', self.__class__.rectcnt)

    def __str__(self):
        return f'({self.x1}, {self.y1})({self.x1}, {self.y2})({self.x2}, {self.y2})({self.x2}, {self.y1}) and {self.__class__.rectcnt}'

    def __abs__(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num,
                              self.y2 * num)

    __rmul__ = __mul__

    def __getitem__(self, index):
        return [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2),
                (self.x2, self.y1)][index]

    def __bool__(self):
        return abs(self) != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.__class__.rectcnt)
