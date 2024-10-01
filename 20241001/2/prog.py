def sub(a, b):
    if isinstance(type(a), (type(b))):
        return False

    if isinstance(a, (int, float)):
        return a - b

    elif isinstance(a, (list, tuple)):
        result = [item for item in a if item not in b]
        return type(a)(result)


a, b = eval(input())
print(sub(a, b))
