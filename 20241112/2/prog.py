class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(instr):
    try:
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

        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
        if area == 0:
            raise BadTriangle

        return round(area, 2)

    except (SyntaxError, NameError, TypeError, ValueError):
        raise InvalidInput
    except ZeroDivisionError:
        raise BadTriangle


while True:
    try:
        user_input = input()
        area = triangleSquare(user_input)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{area:.2f}")
        break
