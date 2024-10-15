import string
import timeit

s = "aabABbcD123"

def alph(s):
    vovels = set("aeyuio")
    mn = set(string.ascii_lowercase)
    s = set(s)
    s1 = (s & mn) & vovels
    s2 = (s & mn) - vovels
    print(f"vovels = {len(s1)}, consonats = {len(s2)}")

t= timeit.Timer("alph(s)", globals=globals())
print(t.autorange())
