import sys
from random import randrange

n = int(sys.argv[1])

res = [[randrange(10) for i in range(n)] for j in range(n)]
for i in range(2, len(sys.argv), 2):
    res[int(sys.argv[i])] = [randrange(10) for i in range(int(sys.argv[i + 1]))]
print(*res, sep='\n', end='\n\n')
