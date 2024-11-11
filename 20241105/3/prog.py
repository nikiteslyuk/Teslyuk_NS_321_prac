class Maze:
    def __init__(self, N):
        self.N = N
        self.grid = [
            ["█" if i % 2 == 0 or j % 2 == 0 else "·" for j in range(2 * N + 1)]
            for i in range(2 * N + 1)
        ]

    def __repr__(self):
        return "\n".join("".join(row) for row in self.grid)

    def _coords(self, x, y):
        return 2 * x + 1, 2 * y + 1

    def __setitem__(self, key, value):
        y0, tmp, x1 = key
        x0, y1 = tmp.start, tmp.stop

        if x0 == x1 and y0 == y1:
            gx, gy = self._coords(x0, y0)
            self.grid[gx][gy] = value
            return

        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1)):
                gx, gy = self._coords(x0, y)
                self.grid[gx][gy + 1] = value
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1)):
                gx, gy = self._coords(x, y0)
                self.grid[gx + 1][gy] = value

    def __getitem__(self, key):
        y0, tmp, x1 = key
        x0, y1 = tmp.start, tmp.stop
        sx, sy = self._coords(x0, y0)
        ex, ey = self._coords(x1, y1)
        return self._bfs((sx, sy), (ex, ey))

    def _bfs(self, start, end):
        from collections import deque

        queue = deque([start])
        visited = set()
        visited.add(start)

        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and self.grid[nx][ny] == "·":
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False


import sys

exec(sys.stdin.read())
