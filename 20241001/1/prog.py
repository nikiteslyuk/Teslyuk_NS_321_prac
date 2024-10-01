def is_dominate(x, y, a, b):
    if x <= a and y <= b and (x < a or y < b):
        return True
    return False


def Pareto(*args):
    res = []
    for i in range(len(args)):
        cool = True
        for j in range(len(args)):
            if i != j:
                if (is_dominate(*args[i], *args[j])):
                    cool = False
                    break
        if cool:
            res.append(args[i])

    return tuple(res)


arr = eval(input())
print(Pareto(*arr))
