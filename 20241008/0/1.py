import fractions
import decimal


def solution(x, y, Type):
    return Type(x) * Type(y)


print(solution('1.1', '2.2', float))
print(solution('1.1', '2.2', decimal.Decimal))
print(solution('1.1', '2.2', fractions.Fraction))
