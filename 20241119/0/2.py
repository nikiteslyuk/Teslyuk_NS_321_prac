def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]

        return newfun

    return decorator


def istype(typ):
    def decor(fun):
        def wrapper(*args):
            for elem in args:
                if not isinstance(elem, typ):
                    raise TypeError
            return fun(*args)

        return wrapper

    return decor


@istype(int)
@multicall(5)
def simplefun(N):
    return N * 2 + 1


print(*simplefun(4))
