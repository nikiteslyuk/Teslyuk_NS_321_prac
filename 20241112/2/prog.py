class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(instr):
    coordinates = eval(instr)

    if not (isinstance(coordinates, tuple) and len(coordinates) == 3):
        raise InvalidInput

    (x1, y1), (x2, y2), (x3, y3) = coordinates

    if not (
        isinstance(x1, (int, float))
        and isinstance(y1, (int, float))
        and isinstance(x2, (int, float))
        and isinstance(y2, (int, float))
        and isinstance(x3, (int, float))
        and isinstance(y3, (int, float))
    ):
        raise InvalidInput

    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5
    if area == 0:
        raise BadTriangle
    return area


while True:
    try:
        inp = input()
        area = triangleSquare(inp)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(area)
        break
