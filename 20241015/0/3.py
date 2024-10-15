s = set(range(1, 8))
t = {i * 2 + 1 for i in range(8)}
print("s:", s, "t:", t)
print(f"{s | t =}")
print(f"{s ^ t =}")
print(f"{s - t =}")
print(f"{s & t =}")
