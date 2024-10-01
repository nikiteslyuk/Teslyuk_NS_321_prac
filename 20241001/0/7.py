def F():

    def fun():
        return x

    x = 3

    return fun


res = F()
print(res())
