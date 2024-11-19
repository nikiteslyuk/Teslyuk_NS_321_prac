def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]

        return newfun

    return decorator


class istype:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def wrapper(*args):
            for elem in args:
                if not isinstance(elem, self.typ):
                    raise TypeError
            return fun(*args)

        return wrapper


@istype(int)
@multicall(5)
def simplefun(N):
    return N * 2 + 1


print(*simplefun(4))
