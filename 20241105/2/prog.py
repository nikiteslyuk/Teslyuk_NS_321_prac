class Triangle:
    def __init__(self, d1, d2, d3):
        self.d1 = tuple(d1)
        self.d2 = tuple(d2)
        self.d3 = tuple(d3)

    def __abs__(self):
        x1, y1 = self.d1
        x2, y2 = self.d2
        x3, y3 = self.d3
        return 0.5 * abs((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3))

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def _sign(self, p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    def _is_in_dot(self, dot):
        d1 = self._sign(dot, self.d1, self.d2)
        d2 = self._sign(dot, self.d2, self.d3)
        d3 = self._sign(dot, self.d3, self.d1)

        return not (
            ((d1 < 0) or (d2 < 0) or (d3 < 0)) and ((d1 > 0) or (d2 > 0) or (d3 > 0))
        )

    def __contains__(self, other):
        if not other:
            return True
        return (
            self._is_in_dot(other.d1)
            and self._is_in_dot(other.d2)
            and self._is_in_dot(other.d3)
        )

    def __and__(self, other):
        if not self or not other:
            return False

        if (
            other._is_in_dot(self.d1)
            or other._is_in_dot(self.d2)
            or other._is_in_dot(self.d3)
        ):
            return True

        if (
            self._is_in_dot(other.d1)
            or self._is_in_dot(other.d2)
            or self._is_in_dot(other.d3)
        ):
            return True

        return False


import sys

exec(sys.stdin.read())
