def req(n=5, res='1'):
    if len(res) == n:
        print(res)
    else:
        req(n, res + '0')
        req(n, res + '1')


req(3)
