import timeit

# python3 -m timeit "code"

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

print(timeit.timeit('char in text', setup='text = "abcd"; char = "c"'))
