from collections import Counter
import timeit

text = 'abc def abc qwert def'.split()

def dd(text):
    d = {word: 0 for word in text}
    for i in text:
        d[i] += 1
    return d

def cc(text):
    return Counter(text)

print(dd(text))
print(cc(text))

t1 = timeit.Timer("dd(text)", globals=globals())
t2 = timeit.Timer("cc(text)", globals=globals())
print(t1.autorange())
print(t2.autorange())
