def walk2d(x=0, y=0):
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy


w = walk2d()
print(next(w))
for dx, dy in zip(range(1, 10), range(-20, -10, 1)):
    print(dx, dy, w.send((dx, dy)))
