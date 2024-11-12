def devisior(a, b, eps=1e-9):
    if abs(b) < eps:
        raise ZeroDivisionError
    return a / b


a, b = eval(input())
try:
    print(devisior(a, b))
except Exception:
    print("(")
