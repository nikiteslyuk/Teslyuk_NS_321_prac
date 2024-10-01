def F(a, b):

    def linear(x):
        return a * x + b

    return linear


res = F(5, 5)
print(res(-5))
