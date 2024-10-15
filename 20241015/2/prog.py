from math import *

funcs = 0
calls = 0
defuns = dict()

while s := input():
    if 'quit' in s:
        eval('print(' + s[4:] + f'.format({funcs + 1}, {calls + 1})' + ')')
        break
    elif s.startswith(':'):
        fun = s[1:].split()
        defuns[fun[0]] = eval(f'lambda {', '.join(fun[1:-1])}: {fun[-1]}')
        funcs += 1
    else:
        fun = s.split()
        print(eval(f'defuns[fun[0]]({', '.join(fun[1:])})'))
    calls += 1
