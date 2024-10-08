import fractions
import decimal


def esum(N, one):
    res = one
    n = one
    for i in range(1, N):
        n *= i
        res += one / n
    return res


print(esum(100000, decimal.Decimal(1)))
