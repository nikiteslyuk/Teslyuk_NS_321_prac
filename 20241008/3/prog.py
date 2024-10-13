import math


def read():
    n = 2
    gas = 0
    liquid = 0
    firtsline = input()
    m = len(firtsline)
    other = input()
    while other != firtsline:
        if '.' in other:
            gas += (m - 2)
        elif '~' in other:
            liquid += (m - 2)
        n += 1
        other = input()
    return n, m, gas, liquid


def format_fraction(numerator, denominator, width):
    return f"{numerator}/{denominator}".rjust(width)


def out(n, m, gas, liquid, stat=False):
    if n == m == 2:
        print('##')
        print('##')
        return
    liquid_lines = math.ceil(liquid / (n - 2))
    gas_lines = m - 2 - liquid_lines
    print('#' * n)
    for i in range(gas_lines):
        print('#' + '.' * (n - 2) + '#')
    for i in range(liquid_lines):
        print('#' + '~' * (n - 2) + '#')
    print('#' * n)

    if stat:
        total_volume = (n - 2) * (m - 2)
        gas_ratio = f"{gas}/{total_volume}"
        liquid_ratio = f"{liquid}/{total_volume}"

        gas_str, liquid_str = "", ""

        if gas < liquid:
            gas_ratio = " " * (len(str(liquid)) - len(str(gas))) + gas_ratio
            gas_str = ('.' * round(gas / liquid * 20)).ljust(20)
            liquid_str = '~' * 20
        else:
            liquid_ratio = " " * (len(str(gas)) -
                                  len(str(liquid))) + liquid_ratio
            gas_str = '.' * 20
            liquid_str = ('~' * round(liquid / gas * 20)).ljust(20)
        print(gas_str, gas_ratio)
        print(liquid_str, liquid_ratio)


out(*read(), True)
