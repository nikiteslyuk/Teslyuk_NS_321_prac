import sys


data = sys.stdin.buffer.read()
N = data[0]
tail = data[1:]
L = len(tail)

parts = [tail[round(i * L / N) : round((i + 1) * L / N)] for i in range(N)]

parts.sort()
result = bytes([N]) + b"".join(parts)
sys.stdout.buffer.write(result)
