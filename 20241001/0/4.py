def req(x):
    if x <= 0:
        return 0
    req(x - 1)


req(4)
