def sortstring(st):
    s = ''
    for elem in st:
        if elem.isalpha():
            s += elem
        else:
            s += ' '
    return s


n = int(input())
anls = dict()

while s := input():
    s = sortstring(s)
    s = list(s.lower().split())
    for elem in s:
        if len(elem) == n:
            anls[elem] = anls.get(elem, 0) + 1

if anls:
    mx = max(anls.values())
    result = [elem for elem, i in anls.items() if i == mx]
    print(*result)
