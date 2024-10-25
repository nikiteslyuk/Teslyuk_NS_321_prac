from itertools import *
print(*sorted(filter(lambda x: x.count('TOR') == 2, list(map(''.join, product('TOR', repeat=int(input())))))), sep=', ')
