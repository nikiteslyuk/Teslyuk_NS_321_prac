def parse(st):
    st = st.lower()
    s = set()
    for i in range(len(st) - 1):
        tmp = st[i:i + 2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            s.add(tmp)
    return len(s)


s = input()
print(parse(s))
