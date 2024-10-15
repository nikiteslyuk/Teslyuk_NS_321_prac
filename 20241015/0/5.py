from collections import defaultdict

text = input().split()

d = {word: 0 for word in text}
for i in text:
    d[i] += 1
print(d)
